from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Shall we just go Insane?</h1><p>#人類は廣井きくりになる必要がある</p>"