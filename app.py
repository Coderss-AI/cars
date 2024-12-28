import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
encoder = LabelEncoder()
with open('carsprice.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("AVTO NARX")

st.write("Bu dastur sizning kiritgan ma'lumotlaringizga asoslanib avtomobilingizning taxminiy narxini bashorat qiladi!")

mm = st.text_input("Mashina modeli")
year = st.text_input("Ishlab chiqarilgan yili")
sp = st.text_input("Sotib olingan narxi")
dk = st.text_input("Yurgan yo'li probeg")
ftt = st.selectbox("Yoqilg'i turi", ["Benzin", "Dizel", "Gaz"])

if ftt=="Benzin":
    ft=2
elif ftt=="Dizel":
    ft=1
elif ftt=="Gaz":
    ft=0

# Bashorat tugmasi
if st.button("Bashorat qilish"):
    df =pd.DataFrame([{
        'Year': year,
        'Selling_Price': sp,
        'Driven_kms': dk,
        'Fuel_Type': ft
    }]) 
    df['Year'] = encoder.fit_transform(df['Year'].values)
    df['Selling_Price'] = encoder.fit_transform(df['Selling_Price'].values)
    df['Driven_kms'] = encoder.fit_transform(df['Driven_kms'].values)
    prediction = model.predict(df)[0]
    st.success(f"{mm} mashinangizning taxminiy narxi: ${prediction:.2f}$ {"$"}")