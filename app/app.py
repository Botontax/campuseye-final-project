from flask import Flask, render_template
from database.db import read_data

app = Flask(__name__)

@app.route("/")
def home():
    data = read_data()

    return render_template(
        "index.html",
        classroom=data["classroom"],
        people_count=data["people_count"],
        status=data["status"],
        reason=data.get("reason", "尚無資料")
    )

if __name__ == "__main__":
    app.run(debug=True)