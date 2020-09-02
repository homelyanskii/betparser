from flask import Blueprint

bp = Blueprint('bets', __name__)

from app.bets import routes