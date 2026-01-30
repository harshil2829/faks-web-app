from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# Create Database
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()


# Home Page
@app.route("/")
def index():

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM students")
    data = c.fetchall()

    conn.close()

    return render_template("index.html", students=data)


# Add Student
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO students(name,age,course) VALUES (?,?,?)",
            (name, age, course)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")


if __name__ == "__main__":

    init_db()
    app.run(debug=True)
