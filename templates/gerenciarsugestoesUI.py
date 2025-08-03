import streamlit as st
from views import View
from datetime import datetime

class GerenciarSolicitacoesUI:
    @staticmethod
    def main():
        st.header("Solicitações de Aula Pendentes")
        
        solicitacoes = View.listar_solicitacoes_pendentes()
        esportes = {e.getId(): e.getNome() for e in View.listar_esportes()}
        professores = {p.get_id(): p.get_nome() for p in View.listar_professores()}

        if not solicitacoes:
            st.write("Nenhuma solicitação pendente")
            return

        for sol in solicitacoes:
            with st.expander(f"Solicitação #{sol.get_id()}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Professor:** {professores.get(sol.get_id_professor(), 'Desconhecido')}")
                    st.write(f"**Esporte:** {esportes.get(sol.get_id_esporte(), 'Desconhecido')}")
                    st.write(f"**Data/Hora:** {sol.get_data_hora()}")
                    st.write(f"**Vagas sugeridas:** {sol.get_vagas()}")
                with col2:
                    st.write(f"**Motivo:**")
                    st.write(sol.get_motivo())
                
                col1, col2, _ = st.columns(3)
                with col1:
                    if st.button("Aprovar", key=f"aprovar_{sol.get_id()}"):
                        View.aprovar_solicitacao(sol.get_id())
                        st.rerun()
                with col2:
                    if st.button("Rejeitar", key=f"rejeitar_{sol.get_id()}"):
                        View.rejeitar_solicitacao(sol.get_id())
                        st.rerun()