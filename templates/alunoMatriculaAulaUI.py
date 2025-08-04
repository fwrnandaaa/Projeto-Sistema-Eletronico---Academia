import streamlit as st
from datetime import datetime
from models.esporte import Esportes
from models.matricula import Matricula, Matriculas
from models.turma import Turmas
from models.professor import Professores

class AlunoMatriculaAulaUI:
    @staticmethod
    def main():
        st.header("Matricule-se em uma Aula")

        nome_aluno = st.session_state.get("aluno_nome", "Aluno")
        id_aluno = st.session_state.get("id_aluno", None)

        if id_aluno is None:
            st.error("Erro: ID do aluno não encontrado.")
            return

        st.markdown(f"**Olá, {nome_aluno}! Aqui estão as turmas disponíveis:**")

        turmas = Turmas.listar_obj()
        esportes = Esportes.listar_obj()
        professores = Professores.listar_obj()
        Matriculas.abrir()  # garante dados atualizados

        if not turmas:
            st.warning("Nenhuma turma disponível no momento para matrícula.")
            return

        opcoes = []
        mapa_turmas = {}

        for turma in turmas:
            esporte = next((e for e in esportes if e.getId() == turma.get_id_esporte()), None)
            professor = next((p for p in professores if p.get_id() == turma.get_id_prof()), None)

            if esporte and professor:
                # calcula matrículas ativas para essa turma
                matriculas_ativas = sum(
                    1 for m in Matriculas.objetos
                    if m.getIdTurma() == turma.get_id() and m.getStatus() == "Ativa"
                )
                vagas_disponiveis = turma.get_vagas() - matriculas_ativas

                desc = f"{turma.get_id()} - {esporte.getNome()} com {professor.get_nome()} às {turma.get_horario()} | Vagas disponíveis: {vagas_disponiveis}"
                opcoes.append(desc)
                mapa_turmas[desc] = (turma, vagas_disponiveis)

        escolhido = st.selectbox("Escolha a turma:", opcoes)

        if st.button("Matricular-se"):
            turma_escolhida, vagas_disponiveis = mapa_turmas[escolhido]

            if vagas_disponiveis <= 0:
                st.error("Essa turma não possui vagas disponíveis.")
                return

            ja_matriculado = any(
                m.getIdAluno() == id_aluno and m.getIdTurma() == turma_escolhida.get_id() and m.getStatus() == "Ativa"
                for m in Matriculas.objetos
            )

            if ja_matriculado:
                st.warning("Você já está matriculado nesta turma.")
                return

            nova_matricula = Matricula(
                id=0,
                idAluno=id_aluno,
                idTurma=turma_escolhida.get_id(),
                dataMatricula=datetime.now().strftime("%d-%m-%Y %H:%M"),
                status="Ativa"
            )

            Matriculas.inserir(nova_matricula)
            st.success(f"Você se matriculou na turma de {escolhido}")

