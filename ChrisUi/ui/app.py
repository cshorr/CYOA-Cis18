from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("template1.html")

@app.get("/next")
def next_screen():
    return render_template("next.html")

if __name__ == "__main__":
    app.run(debug=True)
server = Server(app.wsgi_app)
server.serve(debug=True, port=5000)









