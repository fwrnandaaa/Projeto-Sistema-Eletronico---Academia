import streamlit as st
from models.matricula import Matriculas
from models.turma import Turmas
from models.esporte import Esportes
from models.professor import Professores

class HistoricoAulasAlunoUI:
    @staticmethod
    def main():
        st.header("Histórico de Aulas")

        id_aluno = st.session_state.get("id_aluno")
        
        matriculas = Matriculas.listar_obj()
        turmas = Turmas.listar_obj()
        esportes = Esportes.listar_obj()
        professores = Professores.listar_obj()

        esportes_dict = {e.getId(): e.getNome() for e in esportes}
        professores_dict = {p.get_id(): p.get_nome() for p in professores}
        turmas_dict = {t.get_id(): t for t in turmas}

        matriculas_ativas = [m for m in matriculas if m.getIdAluno() == id_aluno and m.getStatus().lower() == "ativa"]
        matriculas_canceladas = [m for m in matriculas if m.getIdAluno() == id_aluno and m.getStatus().lower() == "cancelada"]

        abas = st.tabs(["Aulas Ativas", "Aulas Canceladas"])

        def render_matriculas(lista, cor_status):
            if not lista:
                st.info("Nenhuma aula para mostrar.")
                return
            for m in lista:
                turma = turmas_dict.get(m.getIdTurma())
                if not turma:
                    st.warning("Turma não encontrada.")
                    continue
                
                esporte_nome = esportes_dict.get(turma.get_id_esporte(), "Desconhecido")
                professor_nome = professores_dict.get(turma.get_id_prof(), "Desconhecido")
                horario = turma.get_horario()
                status = m.getStatus().capitalize()

                st.markdown(f"### {esporte_nome}")
                st.markdown(f"**Professor:** {professor_nome}")
                st.markdown(f"**Horário:** {horario}")
                st.markdown(f"**Status:** <span style='color:{cor_status}; font-weight:bold'>{status}</span>", unsafe_allow_html=True)
                st.markdown("---")

        with abas[0]:
            st.subheader("Aulas Ativas")
            render_matriculas(matriculas_ativas, "green")

        with abas[1]:
            st.subheader("Aulas Canceladas")
            render_matriculas(matriculas_canceladas, "red")
