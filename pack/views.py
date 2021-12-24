import json
from flask import render_template, url_for, redirect, request, jsonify
from flask.helpers import make_response

from .secret_config import config
from .googlelogin import GoogleClientConfig, GoogleLogin, User
from secrets import token_hex

from .app import app

import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

googleconfig = GoogleClientConfig(open('./pack/client_secret.json', 'r'))
googleconfig.set_scope(
  ["https://www.googleapis.com/auth/userinfo.profile", 
   "https://www.googleapis.com/auth/userinfo.email", 
   "openid"]
)
googlelogin = GoogleLogin(googleconfig)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/oauth2callback')
def oauth2callback():
  info = googlelogin.handle_callback(request)
  User().create_user(info)
  resp = make_response(render_template('redirect.html', action = 'Logged In', extras = f'as {info["name"]}', url = url_for('index')))
  resp.set_cookie(config.SECURITY_TOKEN_NAME, info['sub'])
  resp.set_cookie(config.PROFILE_PICTURE_TOKEN_NAME, info['picture'])
  resp.set_cookie(config.NAME_TOKEN_NAME, info['given_name'])
  return resp

@app.route('/login')
def login():
  auth_url, _state = googlelogin.login()
  return redirect(auth_url)

@app.route('/logout')
def logout():
  resp = redirect(url_for('index'))
  resp.set_cookie(config.SECURITY_TOKEN_NAME, '', expires=0)
  resp.set_cookie(config.PROFILE_PICTURE_TOKEN_NAME, '', expires=0)
  resp.set_cookie(config.NAME_TOKEN_NAME, '', expires=0)
  return resp

@app.route('/profile')
@googlelogin.protected
def profile(current_user):
  return render_template('profile.html', user=current_user)

@app.route('/get_user')
def get_user():
  return jsonify(User().find_user(request.args.get(config.SECURITY_TOKEN_NAME)))