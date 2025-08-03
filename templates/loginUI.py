from views import View
import streamlit as st

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        cpf = st.text_input("Informe seu CPF")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            try:
                aluno = View.aluno_autenticar(cpf, senha)
                if aluno is not None:
                    st.session_state["id_aluno"] = aluno["id"]
                    st.session_state["aluno_nome"] = aluno["nome"]
                    st.session_state["admin"] = aluno["admin"]
                    st.session_state["tipo_usuario"] = "admin" if aluno["admin"] else "aluno"  # Alterado para "aluno"
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    professor = View.professor_autenticar(cpf, senha)
                    if professor is not None:
                        st.session_state["professor_id"] = professor["id"]
                        st.session_state["professor_nome"] = professor["nome"]
                        st.session_state["tipo_usuario"] = "professor"
                        st.success("Login como professor realizado!")
                        st.rerun()
                    else:
                        st.error("CPF ou senha inválidos")
            except Exception as e:
                st.error(f"Erro ao autenticar: {str(e)}")