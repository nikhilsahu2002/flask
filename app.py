from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'Missing "text" key in request body'}), 400
        
        english_text = data['text']
        translated_text = translator.translate(english_text, dest='fr').text
        
        return jsonify({'translation': translated_text}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
