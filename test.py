from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return "hello"
@app.route('/test')
def new():
    return "Successfull deployment"

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
