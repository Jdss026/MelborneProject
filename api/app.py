from flask import Flask, jsonify, request, make_response, render_template
import pickle
import pandas as pd
import numpy as np

# cria o app flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#importa modelo e scaler como objetos
model = pickle.load(open('./model/model.pkl', 'rb'))
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
    return render_template('./index.html')

# decorator do flask para rotear caminho a função
@app.route('/predict_json',methods=['POST'])
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

    return make_response(
        jsonify(mensagem = "Previsao feita com sucesso",
                dado = prediction[0]))


@app.route('/predict', methods=['POST'])
def predict_index():
    try:
        rooms = float(request.form.get('Rooms'))
    except (ValueError, TypeError):
        rooms = 0

    try:
        distance = float(request.form.get('Distance'))
    except (ValueError, TypeError):
        distance = 0

    try:
        bathroom = float(request.form.get('Bathroom'))
    except (ValueError, TypeError):
        bathroom = 0

    try:
        car = float(request.form.get('Car'))
    except (ValueError, TypeError):
        car = 0

    try:
        landsize = float(request.form.get('Landsize'))
    except (ValueError, TypeError):
        landsize = 0

    try:
        lattitude = float(request.form.get('Lattitude'))
    except (ValueError, TypeError):
        lattitude = 0

    try:
        longtitude = float(request.form.get('Longtitude'))
    except (ValueError, TypeError):
        longtitude = 0

    try:
        propertycount = float(request.form.get('Propertycount'))
    except (ValueError, TypeError):
        propertycount = 0

    try:
        month = float(request.form.get('Month'))
    except (ValueError, TypeError):
        month = 0

    # rooms         = float(request.form.get('Rooms'))
    # distance      = float(request.form.get('Distance'))
    # bathroom      = float(request.form.get('Bathroom'))
    # car           = float(request.form.get('Car'))
    # landsize      = float(request.form.get('Landsize'))
    # lattitude     = float(request.form.get('Lattitude'))
    # longtitude    = float(request.form.get('Longtitude'))
    # propertycount = float(request.form.get('Propertycount'))
    # month         = float(request.form.get('Month'))

    features = pd.DataFrame(np.array([rooms,
        distance,
        bathroom,
        car,
        landsize,
        lattitude,
        longtitude,
        propertycount, 
        month]).reshape(1,9), columns=labels)
    
    df_scalar = []

    for cols in features.keys():
        z_prod = (features[cols]-scaler[cols][0])/scaler[cols][1]
        df_scalar.append(z_prod)

    df_scalar = pd.DataFrame([df_scalar], columns=labels)
    prediction = model.predict(df_scalar)[0]
    
    return render_template('index.html', result=prediction)

if __name__ == '__main__':
    app.run(debug=True)