import streamlit as st
import pandas as pd
from views import View
from datetime import datetime

class HistoricoAulasADMINUI:
    @staticmethod
    def main():
        st.header("Histórico de Aulas")
        
        aulas = View.listar_aulas()
        professores = {p.get_id(): p.get_nome() for p in View.listar_professores()}
        esportes = {e.getId(): e.getNome() for e in View.listar_esportes()}
        matriculas = View.listar_matriculas()
        
        if not aulas:
            st.warning("Nenhuma aula cadastrada", icon="⚠️")
            return

        dados = []
        for aula in aulas:
            alunos_matriculados = sum(1 for m in matriculas if m.getIdTurma() == aula.get_id())
            
            dados.append({
                "ID": aula.get_id(),
                "Esporte": esportes.get(aula.get_id_esporte(), "Desconhecido"),
                "Professor": professores.get(aula.get_id_prof(), "Desconhecido"),
                "Vagas": f"{alunos_matriculados}/{aula.get_vagas()}",
                "Horário": aula.get_horario(),
                "Status": "Ativa" if datetime.strptime(aula.get_horario(), "%d-%m-%Y %H:%M") > datetime.now() else "Encerrada"
            })

        dados.sort(key=lambda x: datetime.strptime(x["Horário"], "%d-%m-%Y %H:%M"), reverse=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            filtro_esporte = st.selectbox("Filtrar por esporte", ["Todos"] + list(sorted({d["Esporte"] for d in dados})))
        with col2:
            filtro_professor = st.selectbox("Filtrar por professor", ["Todos"] + list(sorted({d["Professor"] for d in dados})))
        with col3:
            filtro_status = st.selectbox("Filtrar por status", ["Todos", "Ativa", "Encerrada"])

        if filtro_esporte != "Todos":
            dados = [d for d in dados if d["Esporte"] == filtro_esporte]
        if filtro_professor != "Todos":
            dados = [d for d in dados if d["Professor"] == filtro_professor]
        if filtro_status != "Todos":
            status_filter = "Ativa" if filtro_status == "Ativa" else "Encerrada"
            dados = [d for d in dados if d["Status"] == status_filter]

        df = pd.DataFrame(dados)
        
        st.dataframe(
            df,
            column_config={
                "ID": st.column_config.NumberColumn(width="small"),
                "Esporte": st.column_config.TextColumn(width="medium"),
                "Professor": st.column_config.TextColumn(width="medium"),
                "Vagas": st.column_config.TextColumn("Matrículas", width="small"),
                "Horário": st.column_config.DatetimeColumn(width="medium"),
                "Status": st.column_config.TextColumn(width="small")
            },
            hide_index=True,
            use_container_width=True
        )

        ativas = sum(1 for d in dados if d["Status"] == "Ativa")
        st.metric("Total de Aulas ativas: ", ativas)
