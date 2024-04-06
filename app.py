import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Charger le modèle et le scaler sauvegardés
model = joblib.load('C:\\Users\\ababa\\Desktop\\SCALA\\BIGDATA\\Exam\\model_rf.pkl')
scaler = joblib.load('C:\\Users\\ababa\\Desktop\\SCALA\\BIGDATA\\Exam\\scaler.pkl')

st.title('Détection de Fraude Bancaire en Temps Réel')
st.write('Entrez les caractéristiques de la transaction pour prédire si elle est frauduleuse ou non.')

features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V9', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V18', 'V21']
user_input = []
for feature in features:
    user_input.append(st.number_input(feature))

if st.button('Prédire'):
    data = scaler.transform([user_input])  # Mise à l'échelle des données
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.write('La transaction est prédite comme frauduleuse.')
    else:
        st.write('La transaction est prédite comme normale.')

