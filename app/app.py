from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    classroom = "A101"
    people_count = 12
    status = "普通"

    return render_template(
        "index.html",
        classroom=classroom,
        people_count=people_count,
        status=status
    )

if __name__ == "__main__":
    app.run(debug=True)