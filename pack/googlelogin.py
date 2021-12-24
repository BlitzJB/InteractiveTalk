"""
All logic pertaining to loggin in with a google account.

""" 

from flask import redirect, request, url_for, Request, session
from hashlib import pbkdf2_hmac
from io import TextIOWrapper
import requests
import json

from pip._vendor import cachecontrol
import google.auth.transport.requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow

from .secret_config import config
from .db import client


class GoogleClientConfig():
  def __init__(self, f: TextIOWrapper) -> None:
    """
    :param f: file object of the client_secret json file
    """
    self.contents = json.load(f)
    self.file_path = f.name
    self.scope = None
    
    for k, v in self.contents.get('web').items(): 
      setattr(self, k, v)
      
  def set_scope(self, scope):
    setattr(self, 'scope', scope)    
  
  def to_dict(self):
    return self.contents
    

class GoogleLogin():
  def __init__(self, config_file: GoogleClientConfig) -> None:
    self.config = config_file
    self.flow = Flow.from_client_secrets_file(
      client_secrets_file=self.config.file_path,
      scopes=self.config.scope,
      redirect_uri=self.config.redirect_uris[0]
    )
  
  def login(self):
    auth_url, state = self.flow.authorization_url()
    return (auth_url, state)
  
  def handle_callback(self, request: Request):
    self.flow.fetch_token(authorization_response=request.url)
    
    credentials = self.flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    
    id_info = id_token.verify_oauth2_token(
      id_token=credentials._id_token,
      request=token_request,
      audience=self.config.client_id
    )
    
    session['google_id'] = id_info['sub']
    return id_info
  
  @staticmethod
  def protected(f):
    def wrapper(*args, **kwargs):
      if config.SECURITY_TOKEN_NAME in request.cookies:
        current_user = User().find_user(request.cookies[config.SECURITY_TOKEN_NAME])
        return f(current_user, *args, **kwargs)
      else:
        return redirect(url_for('login'))
    return wrapper
    
class User(object):
  def __init__(self) -> None:
    self.users = client.get_collection('users')
    pass
    
  def create_user(self, user_info: dict) -> str:
    """
    Create a new user in the database.
    """
    _exists = self.find_user(user_info['sub'])
    if not _exists:
      payload = {
        config.SECURITY_TOKEN_NAME: user_info['sub'],
        'name': user_info['name'],
        'email': user_info['email'],
        'picture': user_info['picture'],
        'given_name': user_info['given_name']
      }
      self.users.insert(payload)
      return user_info['sub']
    else:
      return _exists[config.SECURITY_TOKEN_NAME]
      
  def find_user(self, google_id: str) -> dict:
    """
    Find a user in the database.
    """
    user = self.users.find({config.SECURITY_TOKEN_NAME: google_id})
    user = user[0] if user else None
    return user

  def get_google_id(self, google_id: str) -> str:
    """
    Get a user's google_id.
    """
    user = self.find_user(google_id)
    return user[config.SECURITY_TOKEN_NAME] if user else None