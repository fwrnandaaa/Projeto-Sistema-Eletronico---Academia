import streamlit as st
import pandas as pd
from views import View
import time

class ManterAlunoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Alunos")
        tab1, tab2, tab3 = st.tabs(["Listar", "Inserir", "Excluir"])

        with tab1:
            ManterAlunoUI.aluno_listar()
        with tab2:
            ManterAlunoUI.aluno_inserir()
        with tab3:
            ManterAlunoUI.aluno_excluir()

    @classmethod 
    def aluno_inserir(cls):
        nome = st.text_input("Nome completo do aluno")
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
                
                View.aluno_inserir(nome, cpf, senha)
                st.success("Aluno cadastrado com sucesso!")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(f"Erro: {str(erro)}")

    @classmethod 
    def aluno_listar(cls):
        alunos = View.listar_alunos()
        if len(alunos) == 0:
            st.write("Nenhum aluno cadastrado")
        else:
            dic = []
            for obj in alunos: 
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
    def aluno_excluir(cls):
        alunos = View.listar_alunos()
        if len(alunos) == 0:
            st.write("Nenhum aluno cadastrado")
        else:
            aluno_selecionado = st.selectbox(
                "Selecione o aluno para excluir",
                alunos,
                format_func=lambda x: f"{x.get_id()} - {x.get_nome()}"
            )
       
            if st.button("Excluir"):
                try:
                    View.aluno_excluir(aluno_selecionado.get_id())
                    st.success("Aluno excluído com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(f"Erro: {str(erro)}")