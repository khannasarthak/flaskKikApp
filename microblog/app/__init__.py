#keep this in a folder named app

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from app import views # this app is not the one on line 2, this import is at end
# to avoid circular call backs
