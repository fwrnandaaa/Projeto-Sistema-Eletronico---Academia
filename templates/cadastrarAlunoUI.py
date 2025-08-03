import streamlit as st
from views import View

class CadastrarAlunoUI:
    @staticmethod
    def main():
        st.header("Cadastrar Novo Aluno")
        
        with st.form(key="cadastro_aluno"):
            nome = st.text_input("Nome completo")
            cpf = st.text_input("CPF (apenas números)", max_chars=11)
            senha = st.text_input("Senha", type="password")
            confirmar_senha = st.text_input("Confirmar senha", type="password")
            
            if st.form_submit_button("Cadastrar"):
                try:
                    # Validações
                    if len(cpf) != 11 or not cpf.isdigit():
                        st.error("CPF deve conter exatamente 11 dígitos numéricos")
                        return
                    
                    if senha != confirmar_senha:
                        st.error("As senhas não coincidem")
                        return
                    
                    if len(senha) < 4:
                        st.error("A senha deve ter pelo menos 4 caracteres")
                        return
                    
                    # Verifica se CPF já existe (usando View.aluno_autenticar)
                    if View.aluno_autenticar(cpf, "qualquer_senha") is not None:
                        st.error("CPF já cadastrado")
                        return
                    
                    # Cadastra via View
                    View.aluno_inserir(nome, cpf, senha)
                    st.success("Aluno cadastrado com sucesso!")
                    
                except ValueError as e:
                    st.error(f"Dados inválidos: {e}")
                except Exception as e:
                    st.error(f"Erro: {e}")