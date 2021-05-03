from flask import Flask, Blueprint


def init_app(app: Flask):

    from app.views.transactions_views import bp_trasactions

    app.register_blueprint(bp_trasactions)
