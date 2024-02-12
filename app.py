import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'studytracker'

db = 'save.db'

with sqlite3.connect(db) as conn:
        # Create a cursor
        cursor = conn.cursor()

        # Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

with sqlite3.connect(db) as conn:
        # Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users_saves (
                id INTEGER,
                time TEXT NOT NULL,
                day DATE NOT NULL
            )
        ''')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('time') != '00:00:00':
            with sqlite3.connect(db) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users_saves (id, time, day) VALUES (?, ?, date('now'))",
                               (session['user_id'], request.form.get('time')))
                conn.commit()
                cursor.execute("SELECT * FROM users_saves WHERE id = ?", (session['user_id'],))
                rows = cursor.fetchall()

        with sqlite3.connect(db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users_saves WHERE id = ?", (session['user_id'],))
                rows = cursor.fetchall()

        with sqlite3.connect(db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users_saves WHERE id = ? AND day = date('now')", (session['user_id'],))
                rows2 = cursor.fetchall()
                t = [0, 0, 0]

                for row in rows2:
                    t[0] += int((row[1])[:2])
                    t[1] += int((row[1])[3:5])
                    t[2] += int((row[1])[-2:])

                t[0] += int(t[1]/60)
                t[1] = int(t[1]%60)
                t[1] += int(t[2]/60)
                t[2] = int(t[2]%60)

        return render_template('index.html', data=reversed(rows), dt=t)
    else:
        if not 'user_id' in session:
            session['user_id'] = None
        if session['user_id'] == None:
            return redirect("/login")
        else:
            with sqlite3.connect(db) as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM users_saves WHERE id = ?", (session['user_id'],))
                rows = cursor.fetchall()

            with sqlite3.connect(db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users_saves WHERE id = ? AND day = date('now')", (session['user_id'],))
                rows2 = cursor.fetchall()
                t = [0, 0, 0]

                for row in rows2:
                    t[0] += int((row[1])[:2])
                    t[1] += int((row[1])[3:5])
                    t[2] += int((row[1])[-2:])

                t[0] += int(t[1]/60)
                t[1] = int(t[1]%60)
                t[1] += int(t[2]/60)
                t[2] = int(t[2]%60)

            return render_template("index.html", data=reversed(rows), dt=t)

        return redirect("/login")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            conn.commit()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            npass = "0"

            for row in rows:
                if request.form.get('username') == row[1]:
                    npass = row[2]
                    break


            hpass = check_password_hash(npass, request.form.get('password'))

            for row in rows:
                if request.form.get('username') == row[1] and hpass:
                    session['user_id'] = row[0]

            if session['user_id'] == None:
                return render_template("login.html", warning="Wrong username or password")
            else:
                return redirect("/")
    else:
        session['user_id'] = None
        return render_template("login.html", m=request.args.get('m'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if not request.form.get('username'):
            return render_template("register.html", warning="Invalid username")
        elif not request.form.get('password'):
            return render_template("register.html", warning="Invalid password")
        elif not request.form.get('verify'):
            return render_template("register.html", warning="You need to verify your password")

        if request.form.get('password') != request.form.get('verify'):
            return render_template("register.html", warning="Passwords must match")

        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()

            for row in rows:
                if request.form.get('username') == row[1]:
                    return render_template("register.html", warning="Username already taken")

            user = request.form.get('username')
            hpass = generate_password_hash(request.form.get('password'))

            cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (user, hpass))
            conn.commit()

            return redirect(url_for('login', m='Successfully registered'))
    else:
        return render_template("register.html")
