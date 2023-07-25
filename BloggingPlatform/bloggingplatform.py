import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "blog.db"

# Database helper functions
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def create_tables():
    db = get_db()
    with app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()

# Routes
@app.route("/")
def index():
    db = get_db()
    cur = db.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = cur.fetchall()
    return render_template("index.html", posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Simplified user authentication
    if request.method == "POST":
        if request.form["username"] == "user" and request.form["password"] == "password":
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        category = request.form["category"]

        db = get_db()
        db.execute("INSERT INTO posts (title, content, category) VALUES (?, ?, ?)", (title, content, category))
        db.commit()

        return redirect(url_for("index"))

    return render_template("create.html")

@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    if request.method == "POST":
        comment = request.form["comment"]
        db = get_db()
        db.execute("INSERT INTO comments (post_id, comment) VALUES (?, ?)", (post_id, comment))
        db.commit()

    db = get_db()
    cur = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    post = cur.fetchone()

    cur = db.execute("SELECT * FROM comments WHERE post_id = ?", (post_id,))
    comments = cur.fetchall()

    return render_template("post.html", post=post, comments=comments)

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        create_tables()
    app.run(debug=True)
