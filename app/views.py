from flask import request, jsonify
from app.models import db, Question
import openai

def configure_routes(app):

    @app.route('/ask', methods=['POST'])
    def ask():
        content = request.json
        question = content['question']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response['choices'][0]['message']['content']
        new_entry = Question(query=question, answer=answer)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(question=question, answer=answer)
