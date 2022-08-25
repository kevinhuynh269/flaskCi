from flask import Flask

app = Flask(__name__)

@app.rute("/")
df hell_world():
    return "<p>Helo, World!</p>"