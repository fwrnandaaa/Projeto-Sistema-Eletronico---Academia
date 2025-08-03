import streamlit as st
from views import View

class CadastrarProfessorUI:
    @staticmethod
    def main():
        st.header("Cadastrar Novo Professor")
        
        with st.form(key="cadastro_professor"):
            nome = st.text_input("Nome completo")
            cpf = st.text_input("CPF (apenas números)", max_chars=11, help="11 dígitos sem pontuação")
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
                    
                    # Verifica se CPF já existe
                    professores = View.listar_professores()
                    for prof in professores:
                        if prof.get_cpf() == cpf:
                            st.error("CPF já cadastrado")
                            return
                    
                    # Cadastra o professor
                    View.professor_inserir(nome, cpf, senha)
                    st.success("Professor cadastrado com sucesso!")
                    
                except ValueError as e:
                    st.error(f"Dados inválidos: {str(e)}")
                except Exception as e:
                    st.error(f"Erro ao cadastrar: {str(e)}")