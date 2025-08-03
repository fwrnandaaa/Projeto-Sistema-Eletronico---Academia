import streamlit as st
from views import View
from templates.loginUI import LoginUI
from templates.cadastrarAlunoUI import CadastrarAlunoUI
from templates.cadastrarAulaUI import CadastrarAulaUI
from templates.cadastrarProfessorUI import CadastrarProfessorUI

class IndexUI:
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema"])
        if op == "Entrar no Sistema":
            LoginUI.main()

    @staticmethod
    def menu_aluno():
        op = st.sidebar.selectbox("Menu", ["Matricular-se em aula", "Cancelar matrícula", "Visualizar histórico", "Excluir conta", "Sair"])
        if op == "Sair":
            for key in list(st.session_state.keys()):
                del st.session_state[key]  
            st.rerun() 

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastrar aluno",
            "Cadastrar aula",
            "Cadastrar professor",
            "Listar alunos",
            "Listar professores",
            "Excluir aula",
            "Excluir professor",
            "Excluir aluno",
            "Sugestões de aula",
            "Visualizar histórico de aulas",
            "Sair"
        ])
        if op == "Cadastrar aluno":
            CadastrarAlunoUI.main()
        if op == "Cadastrar aula":
            CadastrarAulaUI.main()
        if op == "Cadastrar professor":
            CadastrarProfessorUI.main()
        if op == "Sair":
            for key in list(st.session_state.keys()):
                del st.session_state[key]  
            st.rerun()  
    @staticmethod
    def main():
        if "tipo_usuario" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            tipo = st.session_state["tipo_usuario"]
            if tipo == "admin":
                IndexUI.menu_admin()
            elif tipo == "aluno":
                IndexUI.menu_aluno()

View.cadastrar_admin()
IndexUI.main()