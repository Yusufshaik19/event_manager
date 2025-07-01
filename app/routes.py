from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# In-memory store for demo
events = []

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/events')
def view_events():
    return render_template('events.html', events=events)

@main.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        desc = request.form['description']
        events.append({'title': title, 'date': date, 'description': desc})
        return redirect(url_for('main.view_events'))
    return render_template('add_event.html')
