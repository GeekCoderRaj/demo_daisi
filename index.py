from flask import Flask , jsonify

app = Flask(__name__)


@app.route('/',methods=['GET'])
def predict():
    response = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    return response

if __name__=='__main__':
    app.run(debug=True)