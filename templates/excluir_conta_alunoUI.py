import streamlit as st
import altair as alt
import pandas as pd
from models.aluno import Alunos

class ExcluirContaAlunoUI:
    @staticmethod
    def main():
        st.header("Perfil")

        id_aluno = st.session_state.get("id_aluno")

        if id_aluno is None:
            st.error("Você precisa estar logado para acessar esta página.")
            return

        st.subheader("Deletar Conta")

        confirma = st.checkbox("Eu entendo que esta ação é irreversível e desejo continuar.")

        if confirma:
            data = pd.DataFrame({'Aviso': ['Essa opção deletará sua conta para sempre e não poderá ser recuperada.']})
            chart = alt.Chart(data).mark_text(size=16, color='red').encode(
                text='Aviso'
            )
            st.altair_chart(chart)

            if st.button("Confirmar Exclusão"):
                aluno = Alunos.listar_id(id_aluno)
                if aluno:
                    sucesso = Alunos.excluir(aluno)
                    if sucesso:
                        st.success("Conta deletada com sucesso.")
                        st.session_state.clear()
                        st.rerun()  # ← volta para tela de login (visitante)
                    else:
                        st.error("Erro ao tentar deletar a conta.")
                else:
                    st.error("Aluno não encontrado.")
        else:
            st.info("Marque a caixa de confirmação para continuar.")
