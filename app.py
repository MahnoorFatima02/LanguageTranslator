from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def submit():
    data = request.form['translation_text']
    print("Translation request recieved for " + data)
    translator = pipeline(task="translation", model="Helsinki-NLP/opus-mt-en-fi")
    translated_text = translator(data)
    return jsonify({"translated_text": translated_text[0]["translation_text"]})

if __name__ == '__main__':
    app.run(debug=True)
