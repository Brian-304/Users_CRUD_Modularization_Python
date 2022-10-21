print("running controller file")
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/read')
def read():
    return render_template('read.html')

@app.route('/') #read.html
def index():
    names = User.get_all()
    return render_template('read.html', names=names)

@app.route('/add_new') #create.html
def add ():
    return render_template('/create.html')
    
@app.route('/process', methods=['POST']) #read_one.html
def process():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }        
    id = User.save(data)
    return redirect(f'/show/{id}')

@app.route('/show/<int:id>') #read_one
def show(id):
    data = {
        "id": id
    }
    print(id)
    return render_template('read_one.html', user=User.show(data))

@app.route('/create_user', methods=['POST'])
def create():
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')
    
@app.route('/edit') #edit.html
def edit():
    return render_template('edit.html')



