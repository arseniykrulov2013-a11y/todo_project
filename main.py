from flask import Flask, session, redirect, render_template, request
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

todo_data =[]


@app.route("/")
def index():
    if len(todo_data) > 0:
        return render_template("index.html", data=todo_data)
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template("index.html")

@app.route("/add_item", methods=["POST", "GET"])
def add_item():
    text = request.form.get("text")
    if text:
        todo_dict = {
            "name": text,
            "id": index
        }
        todo_data.append(todo_dict)
        print(todo_dict)
        return redirect("/")
    else:
        return redirect("/")

@app.route("/didit/<id>")
def didit(id):
    todo_data.remove(todo_data[int(id)])
    return redirect("/")

@app.errorhandler(500)
def internal_server_error(error):
    return redirect("/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))