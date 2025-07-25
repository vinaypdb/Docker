from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Crafted with purpose by vinaypdb — 'Don't just deploy apps, deploy your passion.' 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
