from flask import Flask
app = Flask(__name__)  # always needed


@app.route('/') # home page , @app.route(‘/hello’) : localhost/hello
def main():
    return 'Welcome!'

app.run() # app.run(host, port, debug, options) ; Finally the run() method of
    # Flask class runs the application on the local development server.
