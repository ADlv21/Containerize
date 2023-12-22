from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"Server Status" : 200}

@app.route('/hi')
def hi():
    return {"Server HI" : 200}


@app.route('/hell')
def hell():
    return {"Server hell" : 300}

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')