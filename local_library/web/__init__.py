# Web Module

from flask import (
  Blueprint,
  render_template
)

bp = Blueprint('web', 'web', url_prefix='/')

@bp.route('', methods=('GET', 'POST'))
def index():
  return render_template('index.html')

@bp.route('/about', methods=('GET', 'POST'))
def about():
  return render_template('pages/about.html')