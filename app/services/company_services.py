from . import datetime, timedelta, HTTPStatus
from app.serializers.company_schema import CompanySchema
from app.models.company_model import CompanyModel


class CompanyServices:
    def __init__(self, session):
        self.session = session
        self.todays_datetime = datetime(
            datetime.today().year, datetime.today().month, datetime.today().day
        )

    def get(self, request):
        companies = CompanyModel.query.all()

        with self.session.no_autoflush:
            for company in companies:
                company.transactions = [
                    transaction
                    for transaction in company.transactions
                    if (self.todays_datetime - transaction.transaction_date)
                    < timedelta(hours=1) 
                ]

        # companies = [
        #    company
        #    for company in companies
        #    if all(
        #        (self.todays_datetime - transaction.transaction_date)
        #        < timedelta(days=1)
        #        for transaction in company.transacions
        #    )
        # ]

        return {"companies": CompanySchema(many=True).dump(companies)}, HTTPStatus.OK
