from . import db, datetime


class TransactionModel(db.Model):

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime, default=datetime.now())
    transaction_value = db.Column(db.Float, nullable=False)
    
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    company = db.relationship('CompanyModel', back_populates='transactions')
