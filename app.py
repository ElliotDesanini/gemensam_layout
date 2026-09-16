from flask import Flask, render_template, request
import json

app = Flask( __name__ )

@app.route("/")
def home():

    with open("content.json", "r") as file:
        contents = json.load(file)

    return render_template("subpage.html", heading=contents["main"]["heading"], content=contents["main"]["content"])

@app.route("/about")
def about():

    with open("content.json", "r") as file:
        contents = json.load(file)

    return render_template("subpage.html", heading=contents["about"]["heading"], content=contents["about"]["content"])

@app.route("/contacts")
def contacts():

    with open("content.json", "r") as file:
        contents = json.load(file)

    return render_template("subpage.html", heading=contents["contacts"]["heading"], content=contents["contacts"]["content"])



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')