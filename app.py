import streamlit as st
import pickle
import sklearn
import pandas as pd



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
        input_values.append(st.number_input(labels[i], step=1.0, format='%.f'))
        

    if st.button('Calcule Preço'):
        # transforma os dados em um df
        df = pd.DataFrame([input_values], columns=labels)
        # reescala os dados com a transformação original dos dados
        scaled_cols = scaler.transform(df[labels])
        scaled_cols = pd.DataFrame(scaled_cols, columns=labels)
        # Calcular a saída com base nas entradas
        output = pickled_model.predict(scaled_cols)
        # Exibir a saída
        st.header("Saída:")
        st.success(f'O preço da residência é de: ${output[0]:,.2f} USD')

if __name__ == "__main__":

    main()
