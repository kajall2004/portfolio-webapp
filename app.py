from flask import Flask, render_template, request, redirect, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Load project data from JSON
def load_projects():
    with open("data/projects.json", "r") as f:
        return json.load(f)

@app.route("/")
def index():
    projects = load_projects()
    return render_template("index.html", projects=projects)

@app.route("/project/<slug>")
def project_detail(slug):
    projects = load_projects()
    for project in projects:
        if project["slug"] == slug:
            return render_template("project_detail.html", project=project)
    return "Project not found", 404

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    if name and email and message:
        flash("Message received! Thank you.")
        # You can write to file or send email here
        with open("data/messages.txt", "a") as f:
            f.write(f"{name} - {email} - {message}\n")
    else:
        flash("Please fill all fields.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
