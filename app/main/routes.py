from app.main import bp


@bp.route('/')
@bp.route('/index')
def table_tennis():
    return "<i>Works</i>"
