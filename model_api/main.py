from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np

# cria o app flask
app = Flask(__name__)

#importa modelo e scaler como objetos
model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('./model/std_scalar.pkl','rb'))

#labels para colunas do df
labels = ['Rooms',
        'Distance',
        'Bathroom',
        'Car',
        'Landsize',
        'Lattitude',
        'Longtitude',
        'Propertycount', 
        'Month']

@app.route('/',methods=['GET'])
def main():
    return 'main'

# decorator do flask para rotear caminho a função
@app.route('/predict',methods=['POST'])
def predict():
    features = request.get_json()

    for key in labels:
        if key not in features:
            return jsonify({'error': f'A chave "{key}" está faltando no JSON enviado.'})

    df_scalar = []

    for cols in features.keys():
        z_prod = (features[cols]-scaler[cols][0])/scaler[cols][1]
        df_scalar.append(z_prod)

    df_scalar = pd.DataFrame([df_scalar], columns=labels)
    prediction = model.predict(df_scalar)

    return jsonify(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)