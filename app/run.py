from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:secret@localhost:5432/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

app = create_app()

from flask import request, jsonify
import google.generativeai as genai

@app.route('/ask', methods=['POST'])
def ask():
    from models import Question
    try:
        content = request.json
        question = content.get('question')
        if not question:
            return jsonify({"error": "No question provided"}), 400

        genai.configure(api_key='AIzaSyDHkXtRUPElLZ7IDV3y5ahdtwpuL314zdA')
        # Use Google Generative AI to generate the response
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f'Answer the following question: {question}')
        answer = response.text

        new_entry = Question(query=question, answer=answer)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify(question=question, answer=answer), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
