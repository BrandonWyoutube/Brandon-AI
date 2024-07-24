from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if user_input:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        return jsonify({
            'response': response.choices[0].text.strip()
        })
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
