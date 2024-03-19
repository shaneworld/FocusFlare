from flask import redirect, render_template, request, url_for
from app.blueprints.gtd import gtd
from app.models import Task
from flask_login import current_user
from app import db
from datetime import datetime

@gtd.route("/gtd")
def gtd_list():
    tasks = Task.query.filter(Task.is_completed == 0).all()
    return render_template('gtd.html', active='gtd', tasks=tasks)

@gtd.route("/save_task", methods=["GET", "POST"])
def save_task():
    if request.method == "POST":
        taskName = request.form['taskName']
        startDateTime = request.form['startDateTime']
        endDateTime = request.form['endDateTime']
        label = request.form['taskLabel']

        task_time = [startDateTime, endDateTime]
        python_datetime = list()

        for time in task_time:
            time_format = '%Y-%m-%d %H:%M'
            datetime_obj = datetime.strptime(time, time_format)
            python_datetime.append(datetime_obj)

        new_task = Task(
                name = taskName,
                start_datetime = python_datetime[0],
                end_datetime = python_datetime[1],
                user_id = current_user.get_id(),
                label = label
                )

        db.session.add(new_task)
        db.session.commit()
        
    return redirect(url_for('gtd.gtd_list'))

@gtd.route('/update-task', methods=['POST'])
def update_task():
    task_id = request.form.get('task_id')
    is_completed = 'is_completed' in request.form

    task = Task.query.get(task_id)
    if task:
        task.is_completed = is_completed
        db.session.commit()
        return redirect(url_for('gtd.gtd_list'))  # 假设有一个名为 'get_tasks' 的视图函数
    return 'Task not found', 404
