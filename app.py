from flask import Flask, render_template, request
from nepali_stemmer.stemmer import NepStemmer
app = Flask(__name__)             # create an app instance


@app.route('/')
def hello():
    return render_template('post.html')


@app.route('/post', methods=['POST'])
def post():
    value = request.form['input']
    nepstem = NepStemmer()
    return nepstem.stem(value)
    




if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app
