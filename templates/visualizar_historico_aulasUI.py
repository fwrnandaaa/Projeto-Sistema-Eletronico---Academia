import streamlit as st
from views import View
from datetime import datetime

class HistoricoAulasUI:
    @staticmethod
    def main():
        st.header("Histórico de Aulas")


        if "professor_id" not in st.session_state:
            st.error("Você precisa estar logado como professor")
            return

        professor_id = st.session_state["professor_id"]
        

        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.date_input("Data de início", value=datetime.now().replace(day=1))
        with col2:
            data_fim = st.date_input("Data de fim", value=datetime.now())


        aulas = View.listar_aulas_por_professor(professor_id)
        
        if not aulas:
            st.info("Nenhuma aula encontrada no período selecionado")
            return

        aulas_filtradas = []
        for aula in aulas:
            data_aula = datetime.strptime(aula.get_horario(), "%Y-%m-%d %H:%M").date()
            if data_inicio <= data_aula <= data_fim:
                aulas_filtradas.append(aula)

        aulas_filtradas.sort(key=lambda x: datetime.strptime(x.get_horario(), "%Y-%m-%d %H:%M"), reverse=True)


        for aula in aulas_filtradas:
            with st.expander(f"Aula {aula.get_id()} - {aula.get_horario()}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Esporte:** {View.listar_esportes()[aula.get_id_esporte()-1].getNome()}")
                    st.write(f"**Vagas:** {aula.get_vagas()}")
                with col2:
                    professor = View.listar_professores()[aula.get_id_prof()-1]
                    st.write(f"**Professor:** {professor.get_nome()}")
                    st.write(f"**Horário:** {aula.get_horario()}")
                

                matriculas = View.listar_matriculas()
                alunos_matriculados = [m for m in matriculas if m.getIdTurma() == aula.get_id()]
                if alunos_matriculados:
                    st.write("**Alunos matriculados:**")
                    for matricula in alunos_matriculados:
                        aluno = View.listar_alunos()[matricula.get_id_aluno()-1]
                        st.write(f"- {aluno.get_nome()}")