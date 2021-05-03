from . import Flask, SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.company_model import CompanyModel
    from app.models.transaction_model import TransactionModel
