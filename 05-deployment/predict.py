import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model2.bin'
dict_vectorizer_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dict_vectorizer_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('loan')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    loan = (y_pred >= 0.5)

    result = {
        'loan_probability': float(y_pred),
        'loan': bool(loan)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)