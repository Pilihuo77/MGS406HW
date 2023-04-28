from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
  return " Welcome to my Flask app!"

@app.route('/greetings/<occasion>')

def greeting(occasion):
  if occasion == 'christmas':
     return 'Merry Christmas!'

  elif occasion == 'newyear':
    return 'Happy New Year!'
  else:
    return 'Hello!'


if __name__== "__main__":
  app.run()
