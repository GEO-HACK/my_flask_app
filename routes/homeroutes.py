from flask import render_template, Blueprint

main_bp = Blueprint('main',__name__)

@main_bp.route('/')
def home():
    return  render_template('index.html')

@main_bp.route('/dailytask')
def dailytask():
    # This function renders the dailytask.html template
    return render_template('dailytask.html')