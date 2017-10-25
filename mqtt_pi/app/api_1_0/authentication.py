from flask_httpauth import HTTPBasicAuth
from flask import g, jsonify
from ..models import User
from .errors import unauthorized, forbidden
from . import api

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account_or_token, password):
    if account_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(account_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(account=account_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.route('/token')
@auth.login_required
def get_token():
    if g.token_used:
        return unauthorized('Invalid credentials')
    # two days
    return jsonify({"token": g.current_user.generate_auth_token(expiration=172800), 'expiration': 172800})


# @api.before_request
# @auth.login_required
# def before_request():
#     if not g.current_user.confirmed:
#         return forbidden('Unconfirmed account')
