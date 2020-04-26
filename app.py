from flask import Flask, render_template, request
from nepali_stemmer.stemmer import NepStemmer
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    errors = []
    value = request.form['input']
    nepstem = NepStemmer()
    results = nepstem.stem(value)
    return render_template('index.html', errors=errors, results=results)


if __name__ == "__main__":
    app.run()
