from pack import app

# TODO: Downgrade to requests-oauthlib==1.1.0

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)