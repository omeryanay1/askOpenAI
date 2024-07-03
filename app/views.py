from flask import request, jsonify
import google.generativeai as genai


def ask_view(app):
    @app.route('/ask', methods=['POST'])
    def ask():
        try:
            content = request.json
            from .models import db, Question
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
