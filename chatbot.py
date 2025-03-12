from flask import Flask, request, jsonify
import chatbot_cosmos  # Ensure this file is in the same directory

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json
    name = user_input.get('name')
    company = user_input.get('company')
    email = user_input.get('email')
    phone = user_input.get('phone')

    # Store user data in Cosmos DB
    chatbot_cosmos.handle_user_input(name, company, email, phone)

    response = {
        "message": "Thank you! Your information has been saved."
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)