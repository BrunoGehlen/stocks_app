from . import db, datetime
from sqlalchemy.orm import backref

class CompanyModel(db.Model):

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    abreviation = db.Column(db.String, nullable=False)
    transactions = db.relationship('TransactionModel', back_populates="company")

    