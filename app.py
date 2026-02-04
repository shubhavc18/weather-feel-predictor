from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Reference data
data = {
    10: "Very Cold ",
    15: "Cold ",
    20: "Pleasant ",
    25: "Comfortable ",
    30: "Warm ",
    35: "Hot",
    40: "Very Hot"
}

# Function to predict feeling
def predict_label(temp):
    closest = min(data.keys(), key=lambda x: abs(x - temp))
    return data[closest]

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    temp = float(request.form.get("temperature"))
    feeling = predict_label(temp)
    return jsonify({"feeling": feeling})

if __name__ == "__main__":
    app.run(debug=True)
