from flask import render_template, Blueprint,request, redirect,url_for, jsonify
from services.json_handler import TaskManager


main_bp = Blueprint('main',__name__)
task_manager = TaskManager()

@main_bp.route('/')
def home():
    return  render_template('index.html')

@main_bp.route('/dailytask', methods=['GET', 'POST'])
def dailytask():

    if request.method == 'POST':
        task_text= request.form.get('task')

        if task_text:
            task_manager.add_task(task_text, "daily")

            #handle form resubmission
        return redirect(url_for('main.dailytask')) 

    tasks = task_manager.get_tasks("daily")
    return render_template('dailytask.html', tasks=tasks)

@main_bp.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    """Delete task from array"""
    task_manager.delete_task(task_id, 'daily')
    return redirect(url_for('main.dailytask'))

@main_bp.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    
    task_manager.complete_task(task_id, 'daily')
    return redirect(url_for('main.dailytask'))