from .secret_config import config
from hashlib import pbkdf2_hmac

def return_hash(_str):
  """
  :param _str: String to be hashed.\n
  Returns\n
  Hashed String.
  """
  return pbkdf2_hmac('sha256', _str.encode('utf-8'), config.SALT, 100000).hex()