import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
# title
st.title('Credit Card Detection Project')
st.subheader('A Journey into Fraudulent Card Detection')
st.write('Fraudulent card activities pose a significant threat to individuals and financial institutions alike. Detecting and preventing such activities is crucial to safeguarding financial transactions and maintaining trust in the banking system. In this case study, we dive into a dataset of fraudulent card transactions to uncover insights, patterns, and indicators that can help strengthen fraud detection systems.')

# def load_model(file_path):
#     with open(file_path, 'rb') as f:
#         model = pickle.load(f)
#         model.__class__ = DecisionTreeClassifier
#     return model

# dt_model = load_model('dt_model.pkl')

# pickle_in = open("dt_model.pkl","rb")
# dt_model = pickle.load(pickle_in)
# dt_model = joblib.load('dt_model.jl')
lg_model = joblib.load('lg_model.jl')


def predict_credit_card(distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order):
   
    prediction=lg_model.predict([[distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order]])
    print(prediction)
    return prediction



def main():
    # st.title("Credit Card Detection Project")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card Detection Project ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    distance_from_home = st.number_input("distance_from_home", min_value = 0.0, value=None, placeholder ="Type Here")
    distance_from_last_transaction = st.number_input("distance_from_last_transaction",min_value = 0.0, value=None, placeholder="Type Here")
    ratio_to_median_purchase_price = st.number_input("ratio_to_median_purchase_price",min_value = 0.0, value=None, placeholder="Type Here")
    repeat_retailer = st.number_input("repeat_retailer",min_value = 0, value=None, placeholder="Type Here")
    used_chip = st.number_input("used_chip",min_value = 0, value=None, placeholder="Type Here")
    used_pin_number = st.number_input("used_pin_number",min_value = 0, value=None, placeholder="Type Here")
    online_order = st.number_input("online_order",min_value = 0, value=None, placeholder="Type Here")
    if st.button("Predict"):
        result=predict_credit_card(distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order)
        st.success('The transaction is {}.'.format('not fradulent' if result[0] else 'fradulent'))
    

if __name__=='__main__':
    main()
# print(predict_credit_card(2,3,4,1,16,5,1))
