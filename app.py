from flask import Flask, render_template, request

app = Flask(__name__)

def check_password(password):
    if len(password) < 8:
        return "Weak Password ❌"
    elif any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return "Strong Password ✅"
    else:
        return "Medium Password ⚠️"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    strength = ""

    if request.method == "POST":
        password = request.form["password"]
        result = check_password(password)

        if "Strong" in result:
            strength = "strong"
        elif "Medium" in result:
            strength = "medium"
        else:
            strength = "weak"

    return render_template("index.html", result=result, strength=strength)

if __name__ == "__main__":
    app.run(debug=True)