import os
import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.getenv('NAME', 'World')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, {name}! Current time: {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
