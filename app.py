from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple rule-based responses
def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input, "Sorry, I didn't understand that.")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('input', '')
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
