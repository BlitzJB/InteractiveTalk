from flask import Flask
from .secret_config import config

app = Flask(
  __name__,
  static_folder='./src',
  template_folder='./src/html'
)

app.config.update(
  SECRET_KEY=config.SALT
)

