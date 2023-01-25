from flask import Flask, render_template
app = Flask(__name__)
src = "PycharmProjects\GLO-2005-Project-\Frontends\index.html"
@app.route("/")
def home():
    return render_template(src)

if __name__ == "__main__":
    app.run()