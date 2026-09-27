import streamlit as st


st.set_page_config(page_title="Meu App Streamlit")
def main():
    nome = st.text_input("Digite seu nome:")
    idade = st.number_input("Digite sua idade:", min_value=0)
    email = st.text_input("Digite seu email:")
    
    #Validação de email
    if not "@" in email:
        st.error("Email inválido")
        return None

    return f"Nome {nome}, Idade {idade}, Email {email}"

print(main())

