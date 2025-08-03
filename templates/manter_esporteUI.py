import streamlit as st
import pandas as pd
from views import View
import time

class ManterEsporteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Esportes")
        tab1, tab2, tab3 = st.tabs(["Listar", "Inserir", "Excluir"])

        with tab1:
            ManterEsporteUI.esporte_listar()
        with tab2:
            ManterEsporteUI.esporte_inserir()
        with tab3:
            ManterEsporteUI.esporte_excluir()

    @classmethod 
    def esporte_inserir(cls):
        nome = st.text_input("Nome do esporte")

        if st.button("Inserir"):
            try:
                if nome == "":
                    raise ValueError("Nome não pode ser vazio!")
                
                View.esporte_inserir(nome)
                st.success("Esporte cadastrado com sucesso!")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(f"Erro: {str(erro)}")

    @classmethod 
    def esporte_listar(cls):
        esportes = View.listar_esportes()
        if len(esportes) == 0:
            st.write("Nenhum esporte cadastrado")
        else:
            dic = []
            for obj in esportes: 
                dic.append({
                    "ID": obj.getId(),
                    "Nome": obj.getNome()
                })
            
            df = pd.DataFrame(dic)
            
            st.dataframe(
                df,
                hide_index=True,
                column_config={
                    "ID": st.column_config.NumberColumn(width="small"),
                    "Nome": st.column_config.TextColumn(width="medium")
                },
                use_container_width=True
            )

    @classmethod 
    def esporte_excluir(cls):
        esportes = View.listar_esportes()
        if len(esportes) == 0:
            st.write("Nenhum esporte cadastrado")
        else:
            esporte_selecionado = st.selectbox(
                "Selecione o esporte para excluir",
                esportes,
                format_func=lambda x: f"{x.getId()} - {x.getNome()}"
            )
       
            if st.button("Excluir"):
                try:
                    View.esporte_excluir(esporte_selecionado.getId())
                    st.success("Esporte excluído com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(f"Erro: {str(erro)}")