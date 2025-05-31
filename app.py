from flask import Flask # type: ignore
import main
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is test server'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
