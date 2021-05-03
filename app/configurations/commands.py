from . import Flask, AppGroup, TransactionModel, CompanyModel, random, decimal


def init_app(app):

    cli_db_group = AppGroup('database')

    # create Compannies
    @cli_db_group.command('create_companies')
    def cli_db_create_companies():
        session = app.db.session
        company_info = (
            {'name': 'Apple Inc.', 'abreviation': 'AAPL'},
            {'name': 'Amazon.com, Inc.', 'abreviation': 'AMZN'},
            {'name': 'Twitter Inc.', 'abreviation': 'TWTR'},
            {'name': 'Century Communities, Inc.', 'abreviation': 'CCS'},
            {'name': 'Aspen Technology, Inc.', 'abreviation': 'AZPN'},
        )

        for company in company_info:
            new_company = CompanyModel(
                company_name=company['name'] ,
                abreviation=company['abreviation']
            )
            session.add(new_company)
            session.commit()

    @cli_db_group.command('trade')
    def cli_db_create_transactions():
        session = app.db.session
        companies = CompanyModel.query.all()

        def sell_value():
            return decimal.Decimal(
                '%d.%d' % (random.randint(0, 2), random.randint(0, 99))
            )
        for company in companies:
            for _ in range(random.randint(20, 100)):
                transaction = TransactionModel(
                    transaction_value=sell_value(),
                    company_id=company.id
                )

                session.add(transaction)
                session.commit()

    @cli_db_group.command('create')
    def cli_db_create_all():
        app.db.create_all()

    @cli_db_group.command('drop')
    def cli_db_drop_all():
        app.db.drop_all()

    app.cli.add_command(cli_db_group)
