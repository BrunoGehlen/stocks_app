from . import TransactionSchema, TransactionModel, datetime, timedelta, HTTPStatus


class TransactionServices:
    def __init__(self, session):
        self.session = session
        self.todays_datetime = datetime(
            datetime.today().year, datetime.today().month, datetime.today().day
        )

    def get(self, request):

        todays_transactions = TransactionModel.query

        todays_transactions = todays_transactions.filter(
            (self.todays_datetime - TransactionModel.transaction_date)
            < timedelta(days=1)
        )

        for key in request.args:
            if hasattr(TransactionModel, key):
                vals = request.args.getlist(key)
                todays_transactions = todays_transactions.filter(
                    getattr(TransactionModel, key).in_(vals)
                )

        return {
            "transactions": TransactionSchema(many=True).dump(todays_transactions.all())
        }, HTTPStatus.OK
