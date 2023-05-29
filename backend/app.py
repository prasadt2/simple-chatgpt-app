import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai
from flask import Response

# read OPENAI_API_KEY from .env file and save it in environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print("key is", openai.api_key)

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()


@app.route('/ask', methods=['POST'])
@cross_origin(supports_credentials=True)
def ask_endpoint():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"error": "Question not provided"}), 400

    try:
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{question}"}]
        )

        # read the response from OpenAI API
        answer = chat_completion.choices[0].message.content.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
