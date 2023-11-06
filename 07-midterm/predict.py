import pickle
import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify
from preprocessing import feature_eng

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask('prediction')

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    feature_eng(data)

    y_pred = model.predict_proba(pd.DataFrame([data]))[0, 1]
    smoke = (y_pred >= 0.4) #let's maximize F1-score

    result = {
        'smoking_probability': float(y_pred),
        'smoking': bool(smoke)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)