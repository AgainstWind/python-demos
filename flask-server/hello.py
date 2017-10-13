from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
    dictValue = {'key1':'value1','key2':'value2'}
    return json.dumps(dictValue)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090)
