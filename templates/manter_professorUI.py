import streamlit as st
import pandas as pd
from views import View
import time

class ManterProfessorUI:
    @staticmethod
    def main():
        st.header("Cadastro de Professores")
        tab1, tab2, tab3 = st.tabs(["Listar", "Inserir", "Excluir"])

        with tab1:
            ManterProfessorUI.professor_listar()
        with tab2:
            ManterProfessorUI.professor_inserir()
        with tab3:
            ManterProfessorUI.professor_excluir()

    @classmethod 
    def professor_inserir(cls):
        nome = st.text_input("Nome completo do professor")
        cpf = st.text_input("CPF (apenas números)", max_chars=11)
        senha = st.text_input("Senha", type="password")
        confirmar_senha = st.text_input("Confirmar senha", type="password")

        if st.button("Inserir"):
            try:
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError("CPF deve ter 11 dígitos numéricos")
                if senha != confirmar_senha:
                    raise ValueError("As senhas não coincidem")
                if len(senha) < 4:
                    raise ValueError("Senha deve ter pelo menos 4 caracteres")
                
                View.professor_inserir(nome, cpf, senha)
                st.success("Professor cadastrado com sucesso!")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(f"Erro: {str(erro)}")

    @classmethod 
    def professor_listar(cls):
        professores = View.listar_professores()
        if len(professores) == 0:
            st.write("Nenhum professor cadastrado")
        else:
            dic = []
            for obj in professores: 
                dic.append({
                    "ID": obj.get_id(),
                    "Nome": obj.get_nome(),
                    "CPF": f"{obj.get_cpf()[:3]}.{obj.get_cpf()[3:6]}.{obj.get_cpf()[6:9]}-{obj.get_cpf()[9:]}"
                })
            
            df = pd.DataFrame(dic)
            
            st.dataframe(
                df,
                hide_index=True,
                column_config={
                    "ID": st.column_config.NumberColumn(width="small"),
                    "Nome": st.column_config.TextColumn(width="medium"),
                    "CPF": st.column_config.TextColumn(width="medium")
                },
                use_container_width=True
            )

    @classmethod 
    def professor_excluir(cls):
        professores = View.listar_professores()
        if len(professores) == 0:
            st.write("Nenhum professor cadastrado")
        else:
            professor_selecionado = st.selectbox(
                "Selecione o professor para excluir",
                professores,
                format_func=lambda x: f"{x.get_id()} - {x.get_nome()}"
            )
       
            if st.button("Excluir"):
                try:
                    # Precisamos adicionar este método na View
                    View.professor_excluir(professor_selecionado.get_id())
                    st.success("Professor excluído com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(f"Erro: {str(erro)}")