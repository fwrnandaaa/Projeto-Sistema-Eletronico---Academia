from models.aluno import Aluno, Alunos
from models.esporte import Esporte, Esportes
from models.matricula import Matricula, Matriculas
from models.professor import Professor, Professores
from models.turma import Turma, Turmas

class View:

    #aluno
    @staticmethod
    def aluno_autenticar(cpf, senha):
        try:
            aluno = Alunos.listar_obj()
            for obj in aluno:
                if obj.get_cpf() == cpf and obj.get_senha() == senha:
                    return{
                        "id": obj.get_id(),
                        "nome": obj.get_nome(),
                        "admin": (obj.get_cpf() == "12345678912")
                    }
   
        except Exception as e:
            print(f"Erro ao autenticar: {str(e)}")
            return None
    @staticmethod
    def aluno_inserir(nome, cpf, senha):
        c = Aluno(nome, cpf, senha, 0)
        Alunos.inserir(c)
        
        
    #professor
    @staticmethod
    def professor_autenticar(cpf, senha):
        try:
            professor = Professores.listar_obj()
            for obj in professor:
                if obj.get_cpf() == cpf and obj.get_senha() == senha:
                    return{
                        "id": obj.get_id(),
                        "nome": obj.get_nome(),
                        "admin": (obj.get_cpf() == "12345678912")
                    }
   
        except Exception as e:
            print(f"Erro ao autenticar: {str(e)}")
            return None
        # ADMIN
    @staticmethod
    def cadastrar_admin():
        for aluno in Alunos.listar_obj():
            if aluno.get_cpf() == "12345678912" and aluno.get_senha() == "admin":
                return
        return  View.aluno_inserir("admin", "12345678912", "admin")
