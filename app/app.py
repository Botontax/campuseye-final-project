from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return render_template(
        "index.html",
        classroom=data["classroom"],
        people_count=data["people_count"],
        status=data["status"]
    )

if __name__ == "__main__":
    app.run(debug=True)