from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required
from .import auth
from ..models import User
from .forms import LoginForm
import paho.mqtt.publish as mqttpub
from ..main.mqttsub import actuator_dict, Conversion_table, actuator_num_list


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(account=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('main.temperature_and_humidity'))


@auth.route('/actuator')
@login_required
def actuator():
    return render_template('actuator.html')


@auth.route('/use_actuator', methods=['POST'])
@login_required
def test_post():
    print('---------------------------------------')
    print(request.form.get('topic'))
    print(request.form.get('parameter'))
    print('---------------------------------------')

    if request.form.get('topic') in actuator_num_list:
        actuator_dict[request.form.get('topic')] = request.form.get('parameter')
    else:
        actuator_dict[request.form.get('topic')] = Conversion_table[request.form.get('parameter')]
    mqttpub.single(request.form.get('topic'), request.form.get('parameter'), hostname='localhost')
    return 'success'


@auth.route('/actuator_data', methods=['GET'])
@login_required
def get_actuator():
    return jsonify(actuator_dict)
