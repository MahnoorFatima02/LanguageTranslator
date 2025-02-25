from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import os


app = Flask(__name__)

# Initialize the translation model once at startup
translator = pipeline(task="translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def submit():
    data = request.form['translation_text']
    print("Translation request recieved for " + data)
    translated_text = translator(data)
    # translator = pipeline(task="translation", model="Helsinki-NLP/opus-mt-en-fi")
    # translated_text = translator(data)
    return jsonify({"translated_text": translated_text[0]["translation_text"]})

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Get port from Render's environment
    app.run(host="0.0.0.0", port=port, debug=True)  # Bind to all network interfaces

