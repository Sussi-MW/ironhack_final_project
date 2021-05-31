import pandas as pd
import streamlit as st
from PIL import Image
from h2o import models
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import Ridge, Lasso
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
import pickle

imagen = Image.open("images/mexico.jpg")
st.image(imagen)


st.write("""
# Real State Predictor MEXICO CITY
""")


def user_input_features():
    property_type = st.selectbox('Select type of property', ('house', 'apartment', 'store', 'PH'))
    state_name = st.selectbox('Select state', ('Colima', 'Puebla', 'Hidalgo', 'Jalisco', 'Sinaloa', 'Tabasco',
           'Guerrero', 'Tlaxcala', 'Chihuahua', 'Querétaro', 'Tamaulipas',
           'Nuevo León', 'Durango', 'Morelos', 'Nayarit', 'Sonora', 'Yucatán',
           'Campeche', 'Chiapas', 'Guanajuato', 'San Luis Potosí',
           'Ciudad de México', 'Estado de México', 'Zacatecas', 'Oaxaca',
           'Quintana Roo', 'Baja California Sur', 'Baja California',
           'Aguascalientes', 'Distrito Federal', 'Coahuila de Zaragoza',
           'Veracruz de Ignacio de la Llave'))
    surface_total_in_m2 = st.slider('Display property surface total', 1, 200000, 200000)
    surface_covered_in_m2 = st.slider('Display property surface covered', 1, 200000, 200000)
    price_per_m2 = st.slider('Display price per square meter', 1, 35000, 35000)
    data = {'property_type': property_type,
            'state_name': state_name,
            'surface_total_in_m2': surface_total_in_m2,
            'surface_covered_in_m2': surface_covered_in_m2,
            'price_per_m2': price_per_m2}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('Summary of your data')
st.write(df)


# Dataset with categorical variables
df_str = df[['property_type', 'state_name']]

with open("models/encoder", "rb") as f:
    enc = pickle.load(f)
coded = enc.transform(df_str[['property_type', 'state_name']]).toarray()
df_str = pd.DataFrame(coded)


# Prepare data for normalization
df_num = df[['surface_total_in_m2', 'surface_covered_in_m2', 'price_per_m2']]


# train the normalization
with open("models/scaler", "rb") as f:
    scaler = pickle.load(f)


# normalize the dataset and print the first 5 rows
print(df_num)
try:
    normalized = scaler.transform(df_num)
except Exception as e:
    print(e)

column_names = ['surface_total_in_m2', 'surface_covered_in_m2', 'price_per_m2']
df_num_norma = pd.DataFrame(normalized, columns=column_names)

new_df = pd.concat([df_num_norma, df_str], axis=1)

model_names = ['ridge', 'lasso', 'sgd', 'gradient', 'DecisionTree', 'MLP']


def display_prediction():
    try:

        predictions = {}
        for name in model_names:
            print(name + '...')
            model = pickle.load(open('models/' + name + '.pkl', 'rb'))
            prediction = model.predict(new_df.to_numpy())
            predictions[name] = prediction
            print(name, prediction)

    except Exception as e:
        print(e)

    preds = pd.DataFrame(predictions, index=[0])
    return preds


df_pred = display_prediction()


st.subheader('Price predictions')
df_pred *= 69000000.0
st.write(df_pred)

st.subheader('Recommended price value')
st.write(df_pred['gradient'])
