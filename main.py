from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!sss</p>"

# @app.route('/hello/')
# def hello_world2():
#     return 'Hi my name is someone'

@app.route("/")
def index():
    # This function runs when you visit http://localhost:5000/
    return render_template('index.html')