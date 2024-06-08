from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__, static_folder="../dist", static_url_path="/")
CORS(app)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ideas = db.relationship('Idea', backref='session', lazy=True, cascade="all, delete-orphan")

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)

@app.route('/', methods=['GET'])
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/sessions', methods=['GET'])
def get_sessions():
    sessions = Session.query.all()
    result = [{'id': session.id, 'title': session.title, 'ideas': [{'id': idea.id, 'text': idea.text, 'votes': idea.votes} for idea in session.ideas]} for session in sessions]
    return jsonify(result)

@app.route('/sessions', methods=['POST'])
def add_session():
    data = request.json
    new_session = Session(title=data['title'])
    db.session.add(new_session)
    db.session.commit()
    return jsonify({'id': new_session.id, 'title': new_session.title, 'ideas': []}), 201

@app.route('/sessions/<int:session_id>/ideas', methods=['POST'])
def add_idea(session_id):
    data = request.json
    session = Session.query.get_or_404(session_id)
    new_idea = Idea(text=data['text'], session_id=session.id)
    db.session.add(new_idea)
    db.session.commit()
    return jsonify({'id': new_idea.id, 'text': new_idea.text, 'votes': new_idea.votes}), 201

@app.route('/sessions/<int:session_id>/ideas/<int:idea_id>/vote', methods=['POST'])
def vote_idea(session_id, idea_id):
    idea = Idea.query.filter_by(id=idea_id, session_id=session_id).first_or_404()
    idea.votes += 1
    db.session.commit()
    session = Session.query.get(session_id)
    return jsonify({'id': session.id, 'title': session.title, 'ideas': [{'id': i.id, 'text': i.text, 'votes': i.votes} for i in session.ideas]})

@app.route('/sessions/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    session = Session.query.get_or_404(session_id)
    db.session.delete(session)
    db.session.commit()
    return '', 204

@app.route('/sessions/<int:session_id>/ideas/<int:idea_id>', methods=['DELETE'])
def delete_idea(session_id, idea_id):
    idea = Idea.query.filter_by(id=idea_id, session_id=session_id).first_or_404()
    db.session.delete(idea)
    db.session.commit()
    session = Session.query.get(session_id)
    return jsonify({'id': session.id, 'title': session.title, 'ideas': [{'id': i.id, 'text': i.text, 'votes': i.votes} for i in session.ideas]})

if __name__ == '__main__':
    app.run(debug=True)
