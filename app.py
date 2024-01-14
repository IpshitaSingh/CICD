#defining the Flask app
from flask import Flask
app = Flask(__name__)

#defining a route that returns "Hello World!"
@app.route("/")
def hello():
   return "Hello World!"

#defining the /other route 
@app.route("/other")  
def other_route():
    return "This is another route"

#to run the app when this script is executed
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
