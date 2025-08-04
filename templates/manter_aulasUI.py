import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterAulaUI:
    @staticmethod
    def main():
        st.header("Cadastro de Aulas")
        tab1, tab2, tab3 = st.tabs(["Listar", "Inserir", "Excluir"])

        with tab1:
            ManterAulaUI.aula_listar()
        with tab2:
            ManterAulaUI.aula_inserir()
        with tab3:
            ManterAulaUI.aula_excluir()

    @classmethod 
    def aula_inserir(cls):
        esportes = View.listar_esportes()
        professores = View.listar_professores()

        if not esportes or not professores:
            st.error("Cadastre esportes e professores primeiro!")
            return

        # Seleção de esporte (usando getId())
        esporte_nomes = [f"{e.getId()} - {e.getNome()}" for e in esportes]
        esporte_selecionado = st.selectbox("Esporte", esporte_nomes)
        id_esporte = int(esporte_selecionado.split(" - ")[0])

        # Seleção de professor (usando get_id())
        professor_nomes = [f"{p.get_id()} - {p.get_nome()}" for p in professores]
        professor_selecionado = st.selectbox("Professor", professor_nomes)
        id_professor = int(professor_selecionado.split(" - ")[0])

        # Demais campos
        vagas = st.number_input("Vagas disponíveis", min_value=1, max_value=50, value=10)
        horario = st.text_input("Horário (DD-MM-YYYY HH:MM)")

        if st.button("Inserir"):
                try:
                    # Validação deve usar o MESMO formato que você pede ao usuário
                    datetime.strptime(horario, "%d-%m-%Y %H:%M")  # Corrigido para DD-MM-YYYY
                    View.aula_inserir(vagas, horario, id_esporte, id_professor)
                    st.success("Aula cadastrada com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError:
                    st.error("Formato de horário inválido. Use 'DD-MM-YYYY HH:MM'")  # Mensagem corrigida
                except Exception as e:
                    st.error(f"Erro: {str(e)}")
    @classmethod 
    def aula_listar(cls):
        aulas = View.listar_aulas()
        if len(aulas) == 0:
            st.write("Nenhuma aula cadastrada")
        else:
            esportes = {e.getId(): e.getNome() for e in View.listar_esportes()}
            professores = {p.get_id(): p.get_nome() for p in View.listar_professores()}
            
            dados = []
            for aula in aulas:
                dados.append({
                    "ID": aula.get_id(),
                    "Esporte": esportes.get(aula.get_id_esporte(), "?"),
                    "Professor": professores.get(aula.get_id_prof(), "?"),
                    "Vagas": aula.get_vagas(),
                    "Horário": aula.get_horario()
                })
            
            df = pd.DataFrame(dados)
            st.dataframe(
                df,
                hide_index=True,
                column_config={
                    "ID": st.column_config.NumberColumn(width="small"),
                    "Esporte": st.column_config.TextColumn(width="medium"),
                    "Professor": st.column_config.TextColumn(width="medium"),
                    "Vagas": st.column_config.NumberColumn(width="small"),
                    "Horário": st.column_config.TextColumn(width="medium")
                },
                use_container_width=True
            )

    @classmethod 
    def aula_excluir(cls):
        aulas = View.listar_aulas()
        if len(aulas) == 0:
            st.write("Nenhuma aula cadastrada")
        else:
            esportes = {e.getId(): e.getNome() for e in View.listar_esportes()}
            professores = {p.get_id(): p.get_nome() for p in View.listar_professores()}
            
            aula_selecionada = st.selectbox(
                "Selecione a aula para excluir",
                aulas,
                format_func=lambda x: f"{x.get_id()} - {esportes.get(x.get_id_esporte(), '?')} ({x.get_horario()})"
            )
       
            if st.button("Excluir"):
                try:
                    View.aula_excluir(aula_selecionada.get_id())
                    st.success("Aula excluída com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(f"Erro: {str(erro)}")