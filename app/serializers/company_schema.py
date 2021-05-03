from . import fields, TransactionModel, CompanyModel, marsh
from app.serializers.transaction_schema import TransactionSchema


class SimpleTransactionSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = TransactionModel
        fields = ("transaction_value",'transaction_date')
        ordered = True
        load_instance = True

    transaction_value = marsh.auto_field()
    transaction_date = marsh.auto_field()


class CompanySchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = CompanyModel
        fields = ('company_name', 'abreviation', 'transactions')
        ordered = True
        load_instance = True

    company_name = marsh.auto_field()
    abreviation = marsh.auto_field()
    transactions = marsh.Nested(SimpleTransactionSchema(many=True))