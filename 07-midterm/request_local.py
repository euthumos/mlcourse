import requests

url = 'http://localhost:8080/predict'


sample = {'age': 40.0,
 'height(cm)': 165.0,
 'weight(kg)': 70.0,
 'waist(cm)': 84.0,
 'eyesight(left)': 1.2,
 'eyesight(right)': 1.2,
 'hearing(left)': 1.0,
 'hearing(right)': 1.0,
 'systolic': 130.0,
 'relaxation': 89.0,
 'fasting blood sugar': 107.0,
 'Cholesterol': 200.0,
 'triglyceride': 186.0,
 'HDL': 49.0,
 'LDL': 115.0,
 'hemoglobin': 14.2,
 'Urine protein': 1.0,
 'serum creatinine': 0.9,
 'AST': 19.0,
 'ALT': 25.0,
 'Gtp': 32.0,
 'dental caries': 0.0}


response = requests.post(url, json=sample).json()
print(response)