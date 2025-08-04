import streamlit as st
from views import View
from datetime import datetime

class VisualizarSugestaoAulaUI:
    @staticmethod
    def main():
        st.header("Minhas Sugestões de Aula")

        if "professor_id" not in st.session_state:
            st.error("Você precisa estar logado como professor")
            return

        professor_id = st.session_state["professor_id"]
        

        col1, col2 = st.columns(2)
        with col1:
            filtro_status = st.selectbox("Filtrar por status", ["Todos", "Pendente", "Aprovada", "Rejeitada"])
        with col2:
            ordenar_por = st.selectbox("Ordenar por", ["Data mais recente", "Data mais antiga"])


        sugestoes = View.listar_solicitacoes_por_professor(professor_id)
        
        if not sugestoes:
            st.info("Você ainda não enviou nenhuma sugestão de aula")
            return


        if filtro_status != "Todos":
            sugestoes = [s for s in sugestoes if s.get_status().lower() == filtro_status.lower()]

        reverse_order = (ordenar_por == "Data mais recente")
        sugestoes.sort(
            key=lambda x: datetime.strptime(x.get_data_hora(), "%Y-%m-%d %H:%M"),  # Alterado para Y-m-d
            reverse=reverse_order
        )


        for sugestao in sugestoes:
            status_msg = f"Status: {sugestao.get_status().capitalize()}"
            
            with st.expander(f"Sugestão #{sugestao.get_id()} - {sugestao.get_data_hora()} - {status_msg}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"Esporte: {View.listar_esportes()[sugestao.get_id_esporte()-1].getNome()}")
                    st.write(f"Data/Hora: {sugestao.get_data_hora()}")
                with col2:
                    st.write(f"Vagas sugeridas: {sugestao.get_vagas()}")
                    st.write(f"Status: {sugestao.get_status().capitalize()}")
                
                st.write(f"Motivo:")
                st.text(sugestao.get_motivo())
                
                if sugestao.get_status().lower() != "pendente":
                    st.write(f"**Resposta:** Esta sugestão foi {sugestao.get_status().lower()} pela administração")