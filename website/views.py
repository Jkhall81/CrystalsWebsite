from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@views.route('/bookings', methods=['GET', 'POST'])
def booking():
    return render_template('booking.html')


@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@views.route('/gallery', methods=['GET', 'POST'])
def gallery():
    return render_template('gallery.html')
