from . import fields, TransactionModel, CompanyModel, marsh


class SimpleCompanySchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = CompanyModel
        fields = (
            'company_name',
            'abreviation'
        )
        ordered = True
        load_instance = True
    
    company_name = marsh.auto_field()
    abreviation = marsh.auto_field()


class TransactionSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = TransactionModel
        fields = (
            'company',
            'transaction_date',
            'transaction_value',
        )

        ordered = True
        load_instance = True

    company = marsh.Nested(SimpleCompanySchema())
    transaction_date = marsh.auto_field()
    transaction_value = marsh.auto_field()
