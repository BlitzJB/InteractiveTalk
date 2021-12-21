from flask import Flask

app = Flask(
  __name__,
  static_folder='./src',
  template_folder='./src/html'
)