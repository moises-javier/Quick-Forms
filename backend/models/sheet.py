from utils.db import db
from datetime import datetime

class Sheet(db.Model):
    __tablename__ = "sheet"

    id = db.Column(db.Integer, primary_key=True)
    id_template_question = db.Column(db.Integer, db.ForeignKey("template_question.id"))
    user_answer = db.Column(db.String(400))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_all(self, data):
        db.session.add_all(data)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
