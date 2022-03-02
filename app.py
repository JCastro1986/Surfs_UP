#mport the Flask dependency
#from flask import Flask

#Create a New Flask App Instance
#app = Flask(__name__)

#Create Flask Routes
#@app.route('/')
#def hello_world():
#    return 'Hello world'

#Run a Flask App
#export FLASK_APP=app.py

#flask run

# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user goes to the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user goes to the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)



