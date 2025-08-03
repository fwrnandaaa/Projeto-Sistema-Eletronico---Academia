import streamlit as st
from views import View
from templates.loginUI import LoginUI
from templates.manter_alunosUI import ManterAlunoUI
from templates.manter_professorUI import ManterProfessorUI
from templates.manter_aulasUI import ManterAulaUI
from templates.manter_esporteUI import ManterEsporteUI
from templates.historicoAulasUI import HistoricoAulasUI
from templates.solicitar_cadastro_aulaUI import SolicitarAulaUI
from templates.gerenciarsugestoesUI import GerenciarSolicitacoesUI
from templates.visualizar_historico_aulasUI import HistoricoAulasUI
from templates.visualizar_sugestao_aulaUI import VisualizarSugestaoAulaUI


class IndexUI:
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema"])
        if op == "Entrar no Sistema":
            LoginUI.main()
    @staticmethod
    def menu_professor():
        op = st.sidebar.selectbox("Menu",["Solicitar cadastro de aula", "Visualizar histórico de aulas", "Visualizar sugestões de aula", "Sair"])
        if op == "Visualizar histórico de aulas":
           HistoricoAulasUI.main()
        if op == "Solicitar cadastro de aula":
           SolicitarAulaUI.main()
        if op == "Visualizar sugestões de aula": 
            VisualizarSugestaoAulaUI.main() 
        if op == "Sair":
            for key in list(st.session_state.keys()):
                del st.session_state[key]  
            st.rerun() 
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
            "Manter professor",
            "Manter alunos",
            "Manter aulas",
            "Manter esportes",
            "Sugestões de aula",
            "Visualizar histórico de aulas",
            "Sair"
        ])
        if op == "Sugestões de aula":
             GerenciarSolicitacoesUI.main()
        if op == "Visualizar histórico de aulas":
            HistoricoAulasUI.main()
        if op == "Manter esportes":
            ManterEsporteUI.main()
        if op == "Manter aulas":
            ManterAulaUI.main()
        if op == "Manter professor":
            ManterProfessorUI.main()
        if op == "Manter alunos":
            ManterAlunoUI.main()
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
            elif tipo == "professor":
                IndexUI.menu_professor()


View.cadastrar_admin()
IndexUI.main()