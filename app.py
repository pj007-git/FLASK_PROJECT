from flask import Flask,render_template,request,flash,redirect,session,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "PREMBHAV007"   #used For protecting the User with Session
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)



class User(db.Model):
    u_id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20),nullable = False)
    email = db.Column(db.String(30),nullable = False)
    number = db.Column(db.Integer,nullable = False)
    password = db.Column(db.String(50),nullable = False)

    def __repr__(self) -> str:
        return f"{self.name} , {self.email}"

@app.route("/")
def starting_url():
    return redirect("/OA/Registration/")

@app.route('/OA/Registration/', methods=['GET', 'POST'])
def Registration():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        number = request.form['number']
        password = request.form['password']


        existing_user = User.query.filter_by(name = username).first()
        if existing_user:
            flash("user is already registerd")
            return render_template('OA/index.html')

        user = User(name = username, email = email, number = number, password = password)
        db.session.add(user)
        db.session.commit()
        flash('user is registered')
        return redirect('/OA/Login/')
    else:
        return render_template('OA/index.html')


@app.route('/OA/Login/', methods = ['GET', 'POST'])
def Login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #f = User.query.filter_by(name=username)    
        find_user = User.query.filter_by(name=username).first()
        #print(type(find_user), User)
        if find_user:
            #print(find_user.password)
            if password == find_user.password:
                session["user"] = find_user.name
                return redirect(url_for('Home'))
                #return redirect('/OA/Home/')   
        flash('Invalid Credentials')
        return render_template('OA/login.html')
    else:
        return render_template('OA/login.html')


@app.route('/OA/Home/', methods = ['GET'])
def Home():
    try:
        if session["user"]:
            try:
                if session["user_list"]:
                    page = request.args.get('page',1,type=int)
                    users = User.query.paginate(page = page, per_page = 3)
                    return render_template('OA/home.html',users = users, user_name =session["user"] )
            except:
                flash("User is Succefully Loggedin")
                return render_template('OA/home.html',user_name = session["user"])
    except:
        flash("Please Login First")
        return redirect('/OA/Registration/')

@app.route('/OA/Users/', methods = ['GET'])
def Users():
    if session["user"]:
        session["user_list"] = "get"
        return redirect('/OA/Home/')

@app.route('/OA/Logout/', methods = ['GET', 'POST'])
def Logout():
    session.pop("user")
    try:
        session.pop("user_list")
    except:
        pass
    flash('User Successfully LoggedOut')
    return redirect('/OA/Login/')


if __name__ == "__main__":
    app.run(debug = True)
