import streamlit as st
import pickle
import sklearn
import pandas as pd

def calculate_output(input_data):
    # Realize o processamento necessário para calcular a saída com base nas entradas
    # Neste exemplo, vamos simplesmente somar todas as entradas
    output = sum(input_data)
    return output

def main():
    st.title("Regressor Melbourne Price")

    # Criar as 9 entradas
    input_values = []

    # Importar scaler e model
    scaler = pickle.load(open('./model/scalar.pkl', 'rb'))
    pickled_model = pickle.load(open('./model/model.pkl', 'rb'))

    labels = ['Rooms',
        'Distance',
        'Bathroom',
        'Car',
        'Landsize',
        'Lattitude',
        'Longtitude',
        'Propertycount', 
        'Month']
    
    for i in range(9):
        input_values.append(st.number_input( labels[i] , value=0.0))

    if st.button('Predição'):
        df = pd.DataFrame([input_values], columns=labels)
        # reescalar os valores de input
        scaled_cols = scaler.fit_transform(df)
        # Calcular a saída com base nas entradas
        output = pickled_model.predict(scaled_cols)
        # Exibir a saída
        st.header("Saída:")
        st.write(output)

if __name__ == "__main__":
    main()
