import streamlit as st
from PIL import Image

st.title("BMI CALCULATOR")

w = st.number_input("what is your weight in kg")
h = st.number_input("what is your height in metre")
yourname = st.text_input("what is your firstname?")


def MI_calculator(w,h,yourname):
  #w-weight in kg
  #h- height in m
  #BMI Key-
  # Bmi Categories :
  # Underweight = < 18.5
  # Normal weight = 18.5 – 24.9
  # Overweight = 25 – 29.9
  # Obesity = >= 30
  #BMI_Ranges <- c (18, 23, 25, 30)
  #BMI_Categories <- c("underwight", "normal weight", "overweight", "obesity" )
        h2 = h**0.5
        BMI = round((w /h2),0)

        if(BMI > 30):
            rating = "you are overweight"

        elif BMI>24.9:

            rating= "you are overweight"

        elif BMI > 18.4:

            rating= "and you   are normal" 
        else:
            rating = "you are underweight"

        return f"Dear {yourname}, your BMI is {BMI} and {rating}." 

if st.button("Caculate BMI"):
    st.write(MI_calculator(w,h,yourname))
          
  