from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model and sample row for input structure
MODEL_PATH = os.path.join(os.path.dirname(__file__), './linear_regression_model.joblib')
SAMPLE_PATH = os.path.join(os.path.dirname(__file__), './clean_df.csv')
model = joblib.load(MODEL_PATH)
sample_df = pd.read_csv(SAMPLE_PATH)
sample_row = sample_df.iloc[[0]].copy()
model_features = model.feature_names_in_

@app.route('/', methods=['GET', 'POST'])
def predict():
    predicted_price = None
    if request.method == 'POST':
        user_data = {
            'make': request.form['make'].lower(),
            'fuel-type': request.form['fuel_type'].lower(),
            'aspiration': request.form['aspiration'].lower(),
            'num-of-doors': request.form['num_of_doors'].lower(),
            'body-style': request.form['body_style'].lower(),
            'num-of-cylinders': request.form['num_of_cylinders'].lower(),
            'horsepower': float(request.form['horsepower'])
        }
        input_row = sample_row.copy()
        for col in user_data:
            input_row[col] = user_data[col]
        if 'price' in input_row.columns:
            input_row = input_row.drop('price', axis=1)
        input_df = pd.get_dummies(input_row)
        input_df = input_df.reindex(columns=model_features, fill_value=0)
        predicted_price = model.predict(input_df)[0]
    return render_template('predict.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)