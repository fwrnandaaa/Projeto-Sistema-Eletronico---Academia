import streamlit as st
from datetime import datetime
from views import View

class CadastrarAulaUI:
    @staticmethod
    def main():
        st.header("Cadastrar Nova Aula")

        # Carrega listas de esportes e professores
        esportes = View.listar_esportes()
        professores = View.listar_professores()

        with st.form(key="cadastro_aula"):
            # Seleção de esporte
            if not esportes:
                st.error("Nenhum esporte cadastrado!")
                return
            esporte_nomes = [e.getNome() for e in esportes]
            esporte_selecionado = st.selectbox("Esporte", esporte_nomes)
            id_esporte = esportes[esporte_nomes.index(esporte_selecionado)].getId()

            # Seleção de professor
            if not professores:
                st.error("Nenhum professor cadastrado!")
                return
            professor_nomes = [f"{p.get_nome()} (ID: {p.get_id()})" for p in professores]
            professor_selecionado = st.selectbox("Professor", professor_nomes)
            id_professor = professores[professor_nomes.index(professor_selecionado)].get_id()

            # Demais campos
            vagas = st.number_input("Vagas disponíveis", min_value=1, max_value=50, value=10)
            horario = st.text_input("Horário (YYYY-MM-DD HH:MM)")

            if st.form_submit_button("Cadastrar"):
                try:
                    # Validação do horário
                    datetime.strptime(horario, "%Y-%m-%d %H:%M")  # Testa o formato
                    
                    # Insere a aula
                    View.aula_inserir(vagas, horario, id_esporte, id_professor)
                    st.success("Aula cadastrada com sucesso!")
                    
                except ValueError as e:
                    st.error(f"Erro no formato: {str(e)}")
                except Exception as e:
                    st.error(f"Erro ao cadastrar: {str(e)}")