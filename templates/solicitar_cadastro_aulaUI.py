import streamlit as st
from views import View
from datetime import datetime
import time

class SolicitarAulaUI:
    @staticmethod
    def main():
        st.header("Solicitar Nova Aula")
        
        if "professor_id" not in st.session_state:
            st.error("Você precisa estar logado como professor")
            return

        esportes = View.listar_esportes()
        professor_id = st.session_state["professor_id"]

        with st.form(key="solicitar_aula"):
            # Campos que estavam faltando
            motivo = st.text_area("Motivo da Solicitação*", 
                                placeholder="Descreva o propósito desta aula",
                                help="Explique por que esta aula é necessária")
            
            esporte = st.selectbox("Esporte*", 
                                 esportes, 
                                 format_func=lambda e: e.getNome(),
                                 help="Selecione o esporte para esta aula")
            
            # Campos existentes
            col1, col2 = st.columns(2)
            with col1:
                data = st.date_input("Data*", 
                                   min_value=datetime.now().date(),
                                   help="Data prevista para a aula")
            with col2:
                hora = st.time_input("Hora*", 
                                   value=datetime.strptime("14:00", "%H:%M").time(),
                                   help="Horário de início")
            
            vagas = st.number_input("Vagas Sugeridas*", 
                                  min_value=1, 
                                  max_value=50, 
                                  value=10,
                                  help="Número estimado de participantes")
            
            st.markdown("* Campos obrigatórios")
            
            if st.form_submit_button("Enviar Solicitação"):
                try:
                    # Formata a data e hora separadamente
                    data_str = data.strftime("%Y-%m-%d")
                    hora_str = hora.strftime("%H:%M")
                    
                    View.solicitar_aula(
                        motivo=motivo.strip(),
                        id_esporte=esporte.getId(),
                        data=data_str,  # Passa data como string
                        hora=hora_str,  # Passa hora como string
                        vagas=vagas,
                        id_professor=professor_id
                    )
                    st.success("Solicitação enviada com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except ValueError as ve:
                    st.error(str(ve))
                except Exception as e:
                    st.error(f"Erro ao enviar solicitação: {str(e)}")