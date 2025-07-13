import streamlit as st


def generarMenu(param):
    pass


def generarLogin():
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario'])
    else:
        with st.form('frmLogin', clear_on_submit= True):
            user= st.text_input('User')
            pasw= st.text_input('User', type='password')
            btLogin= st.form_submit_button('Ingresar')

            if btLogin:
                if user=='fredy' and pasw=='1526':
                    st.info('logueado')
                else:
                    st.error('usuario o clave invalido', icon=":material/error:")


generarLogin()