import streamlit as st
import pickle
import sklearn

st.header("Insurance cost prediction")

col1, col2, col3 = st.columns(3)

diabetic = col1.selectbox("Diabetes", ("Yes","No"))
bp = col2.selectbox("BP", ("Yes","No"))
transplants = col3.selectbox("Transplants", ("Yes","No"))
chronic_disease = col1.selectbox("Chronic disease", ("Yes","No"))
history_of_cancer_in_family = col2.selectbox("History of cancer in family", ("Yes","No"))
number_of_major_surgeries = col3.selectbox("Number of major surgeries", (0,1,2,3))

age = col1.slider("Age", 18,66,1)
weight = col2.slider("Weight", 50,132,1)

encode_dict = { 'diabetic': {'Yes':1, 'No':0}, 
               'bp': {'Yes':1, 'No':0}, 
               'transplants': {'Yes':1, 'No':0},
               'chronic_disease': {'Yes':1, 'No':0},
               'history_of_cancer_in_family':{'Yes':1, 'No':0} }



def model_pred(age,diabetic,bp,transplants,chronic_disease,
               weight,history_of_cancer_in_family,number_of_major_surgeries):

    with open('model.pkl', 'rb') as file:
        final_model = pickle.load(file)
        input_features = [[age,diabetic,bp,transplants,chronic_disease,
                           weight,history_of_cancer_in_family,number_of_major_surgeries]]
        return final_model.predict(input_features)
    


if(st.button("Predict price")):
    diabetic = encode_dict['diabetic'][diabetic]
    bp = encode_dict['bp'][bp]
    transplants = encode_dict['transplants'][transplants]
    chronic_disease = encode_dict['chronic_disease'][chronic_disease]
    history_of_cancer_in_family = encode_dict['history_of_cancer_in_family'][history_of_cancer_in_family] 

    price = model_pred(age,diabetic,bp,transplants,chronic_disease,
                weight,history_of_cancer_in_family,number_of_major_surgeries)

    st.text(f"Insurance cost is {price[0].round(0)}") 