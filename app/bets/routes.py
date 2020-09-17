from app.bets import bp
from app.bets.parser import Parimatch_parser as pp
from flask import current_app

@bp.route('/table_tennis')
def table_tennis():
    current_app.table_tennis = {}

    pp.parse(current_app.pari_driver_ru)
    pp.parse(current_app.pari_driver_en)

    return "Success"
