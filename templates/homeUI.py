import streamlit as st

class HomeUI:
    @staticmethod
    def main():
        tipo = st.session_state.get("tipo_usuario", "visitante")
        nome = (
            st.session_state.get("aluno_nome")
            or st.session_state.get("professor_nome")
            or "Usuário"
        )
        
        st.title("🏋️‍♂️ Bem-vindo(a) à Academia!")
        st.markdown(f"### Olá, **{nome}**! 👋")
        
        if tipo == "aluno":
            st.markdown(
                "Aqui está seu painel de aluno, onde você pode se matricular em aulas, "
                "cancelar matrículas e acompanhar seu histórico."
            )
            st.markdown("---")
            st.subheader("Ações disponíveis")
            st.write("- Matricular-se em aulas")
            st.write("- Cancelar matrícula")
            st.write("- Visualizar histórico")
            
        elif tipo == "professor":
            st.markdown(
                "Bem-vindo ao painel do professor! Aqui você pode solicitar o cadastro de aulas, "
                "visualizar o histórico das suas aulas e conferir as sugestões feitas para você."
            )
            st.markdown("---")
            st.subheader("Ações disponíveis")
            st.write("- Solicitar cadastro de aula")
            st.write("- Visualizar histórico de aulas")
            st.write("- Visualizar sugestões de aula")
        
        else:
            st.markdown(
                "Para acessar os recursos da academia, faça login com sua conta de aluno ou professor."
            )
        
        st.markdown("---")
        st.subheader("Fale conosco")
        st.markdown(
            "Se tiver dúvidas, sugestões ou quiser entrar em contato, "
            "escreva sua mensagem abaixo. Responderemos o mais rápido possível!"
        )
        mensagem = st.text_area("Digite sua mensagem aqui:", height=150)
        if st.button("Enviar mensagem"):
            if mensagem.strip():
                st.success("Mensagem enviada com sucesso! Obrigado pelo seu contato.")
            else:
                st.warning("Por favor, digite uma mensagem antes de enviar.")
        
        st.markdown("---")
        st.markdown(
            "Aproveite tudo que nossa academia tem a oferecer. 💪"
        )
