from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    with app.app_context():

        from app.bets.parser import Parimatch_parser
        app.pari_driver_ru = Parimatch_parser.open_connection()
        app.pari_driver_ru.get(app.config['PARIMATCH_URL_RU'])

        app.pari_driver_en = Parimatch_parser.open_connection()
        app.pari_driver_en.get(app.config['PARIMATCH_URL_EN'])

    from app.bets import bp as bets_bp
    app.register_blueprint(bets_bp)

    return app