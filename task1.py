from flask import Flask



app = Flask(__name__)

@app.route("/api/v1/hello-world-16")
def index():
    return 'Hello world 16'

if __name__ == '__main__':
    app.run()
