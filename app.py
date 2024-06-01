from flask import Flask , redirect , url_for , render_template ,request
from database import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    db = get_database()
    task_entry = db.execute("select * from todos")
    all_tasks = task_entry.fetchall()
    return render_template('index.html' , all_task = all_tasks)


@app.route('/inserttask', methods=['POST'])
def inserttask():
    if request.method == "POST":
        tmember = request.form['tmember']
        task = request.form['task']
        db = get_database()
        db.execute('insert into todos( todaystask, Tmember) values (?,?) ',[tmember,task])
        db.commit()
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/deletetask/<int:id>', methods=['POST', 'GET'])
def deletetask(id):
    if request.method == "GET":
        db = get_database()
        db.execute('delete from todos where id = ? ',[id])
        db.commit()
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/updatetask/<int:id>', methods=['POST', 'GET'])
def updatetask(id):
    db = get_database()
    if request.method == "POST":
        tmember = request.form['tmember']
        task = request.form['task']
        db.execute('UPDATE todos SET todaystask = ? , Tmember = ? WHERE id = ?', [task , tmember, id])
        
        db.commit()
        return redirect(url_for('index'))
    else:
        task = db.execute("select * from todos where id = ?",[id]).fetchone()
        return render_template('update.html', task = task)



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)