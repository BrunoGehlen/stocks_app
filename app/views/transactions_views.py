from flask import Blueprint, current_app, request
from app.services.transaction_services import TransactionServices
from app.services.company_services import CompanyServices
from app.models.company_model import CompanyModel


bp_trasactions = Blueprint("bp_trasactions", __name__, url_prefix="")


@bp_trasactions.route("/", methods=["GET"])
def get_trasactions():
    session = current_app.db.session
    return TransactionServices(session).get(request)


@bp_trasactions.route("/companies", methods=["GET"])
def get_companies():
    session = current_app.db.session
    return CompanyServices(session).get(request)
