import streamlit as st


def generarMenu(param):
    pass


def validarUsuario(user, pasw):
    if user == 'fredy' and pasw == '1526':
        st.info(f'Usuario {user} logueado')
        return
    elif user:
        st.warning('Debes completar los campos')
    elif pasw:
        st.error('Debes ingresar la costraseña')
    else:
        st.toast('Usuario o constraseña invalida', icon=":material/error:")


def generarLogin():
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario'])
    else:
        with st.form('frmLogin', clear_on_submit=True):
            user = st.text_input('User')
            pasw = st.text_input('User', type='password')
            btLogin = st.form_submit_button('Ingresar')

            if btLogin:
                if validarUsuario(user, pasw):
                    st.session_state['usuario'] = user




generarLogin()
