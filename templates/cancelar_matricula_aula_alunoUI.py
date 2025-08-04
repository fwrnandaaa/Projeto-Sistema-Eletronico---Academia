import streamlit as st
from datetime import datetime
from models.matricula import Matriculas
from models.esporte import Esportes 

class CancelarMatriculaAulaUI:
    @staticmethod
    def main():
        st.header("Cancelar presença na Aula")

        id_aluno = st.session_state.get("id_aluno")

        matriculas = Matriculas.listar_obj()

        matriculas_ativas = [
            m for m in matriculas
            if m.getIdAluno() == id_aluno and m.getStatus().lower() == "ativa"
        ]

        if not matriculas_ativas:
            st.info("Você não possui nenhuma matrícula ativa.")
            return

        esportes = {e.getId(): e.getNome() for e in Esportes.listar_obj()}

        opcoes = [
            f"{m.getId()} - {esportes.get(m.getIdTurma(), 'Esporte desconhecido')} ({m.getDataMatricula().strftime('%d/%m/%Y %H:%M')})"
            for m in matriculas_ativas
        ]

        opcao_selecionada = st.selectbox("Selecione a matrícula para cancelar:", opcoes)

        if st.button("Cancelar matrícula"):
            id_matricula = int(opcao_selecionada.split(" - ")[0])
            matricula = Matriculas.listar_id(id_matricula)

            if matricula:
                matricula._Matricula__setStatus("Cancelada")
                sucesso = Matriculas.atualizar(matricula)

                if sucesso:
                    st.success("Matrícula cancelada com sucesso.")
                else:
                    st.error("Erro ao cancelar a matrícula. Tente novamente.")
            else:
                st.error("Matrícula não encontrada.")
