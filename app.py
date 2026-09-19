from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load models
breast_model = joblib.load(
    "model/breast_cancer_model.pkl"
)

lung_model = joblib.load(
    "model/lung_cancer_model.pkl"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction")
def prediction_page():
    return render_template("prediction.html")

@app.route("/cancer_info")
def cancer_info():
    return render_template("cancer_info.html")

@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")

@app.route("/treatments")
def treatments():
    return render_template("treatments.html")

@app.route("/hospitals")
def hospitals():
    return render_template("hospitals.html")

@app.route("/patient_resources")
def patient_resources():
    return render_template("patient_resources.html")

@app.route("/predict", methods=["POST"])
def predict():

    cancer_type = request.form["cancer_type"]

    value1 = float(request.form["radius_mean"])
    value2 = float(request.form["texture_mean"])
    value3 = float(request.form["perimeter_mean"])

    features = [[
        value1,
        value2,
        value3
    ]]

    # BREAST CANCER
    if cancer_type == "breast":

        prediction = breast_model.predict(features)

        probability = breast_model.predict_proba(features)

        confidence = round(
            max(probability[0]) * 100,
            2
        )

        if prediction[0] == 1:
            result = "Breast Cancer Detected"
            color = "red"
        else:
            result = "No Breast Cancer"
            color = "green"

    # LUNG CANCER
    else:

        prediction = lung_model.predict(features)

        probability = lung_model.predict_proba(features)

        confidence = round(
            max(probability[0]) * 100,
            2
        )

        if prediction[0] == 1:
            result = "Lung Cancer Detected"
            color = "red"
        else:
            result = "No Lung Cancer"
            color = "green"

    return render_template(
        "prediction.html",
        prediction_text=result,
        color=color,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)