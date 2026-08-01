import streamlit as st
from sympy import symbols, factor
from sympy.ntheory import primefactors

# මෙය අනිවාර්යයෙන්ම කේතයේ මුලින්ම තිබිය යුතුය
st.set_page_config(page_title="Math Factor Tool", page_icon="🧮")

st.title("🧮 Mathematical Factorization AI Tool")
st.write("අංකයක හෝ වීජීය ප්‍රකාශනයක (Algebraic Expression) සාධක සොයා ගන්න.")

# Input Type Selection
option = st.selectbox("තෝරන්න:", ["Algebraic Expression (e.g., x^2 - 9)", "Number Prime Factors (e.g., 60)"])

if option == "Algebraic Expression (e.g., x^2 - 9)":
    user_input = st.text_input("ප්‍රකාශනය ඇතුළත් කරන්න (උදා: x**2 + 5*x + 6):")
    
    if st.button("සාධක සොයන්න"):
        try:
            x, y, z = symbols('x y z')
            expression = sympify(user_input)
            factored_result = factor(expression)
            st.success(f"**පිළිතුර:** {factored_result}")
        except Exception as e:
            st.error("දෝෂයකි: කරුණාකර නිවැරදි ආදානයක් ලබා දෙන්න.")

elif option == "Number Prime Factors (e.g., 60)":
    num_input = st.number_input("අංකයක් ඇතුළත් කරන්න:", min_value=1, step=1)
    
    if st.button("ප්‍රථමක සාධක සොයන්න"):
        factors = primefactors(int(num_input))
        st.success(f"**{num_input} හි ප්‍රථමක සාධක:** {factors}")
