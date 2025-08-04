from models.aluno import Aluno, Alunos
from models.esporte import Esporte, Esportes
from models.matricula import Matricula, Matriculas
from models.professor import Professor, Professores
from models.turma import Turma, Turmas
from models.solicitacaoAula import SolicitacaoAula, SolicitacoesAula
from datetime import datetime


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

    @staticmethod
    def listar_alunos():
        return Alunos.listar_obj()

    @staticmethod
    def aluno_excluir(id_aluno):
        aluno = Alunos.listar_id(id_aluno)
        if aluno is not None:
            Alunos.excluir(aluno)
        
        # ADMIN
    @staticmethod
    def cadastrar_admin():
        for aluno in Alunos.listar_obj():
            if aluno.get_cpf() == "12345678912" and aluno.get_senha() == "admin":
                return
        return  View.aluno_inserir("admin", "12345678912", "admin")
    
    #turmas
    @staticmethod
    def aula_inserir(vagas, horario, id_esporte, id_professor):
        t = Turma(vagas, horario, id_esporte, id_professor)
        Turmas.inserir(t)
    @staticmethod
    def listar_aulas():
        return Turmas.listar_obj()

    @staticmethod
    def aula_excluir(id_aula):
        aula = Turmas.listar_id(id_aula)
        if aula is not None:
            Turmas.excluir(aula)
    @staticmethod
    def listar_matriculas():
        return Matriculas.listar_obj()

    #esportes
    @staticmethod
    def listar_esportes():
        return Esportes.listar_obj()
    @staticmethod
    def esporte_inserir(nome):
        e = Esporte(0, nome)  
        Esportes.inserir(e)

    @staticmethod
    def esporte_excluir(id_esporte):
        esporte = Esportes.listar_id(id_esporte)
        if esporte is not None:
            Esportes.excluir(esporte)

    #professores
    @staticmethod
    def listar_aulas_por_professor(id_professor):
        turmas = Turmas.listar_obj()
        return [turma for turma in turmas if turma.get_id_prof() == id_professor]
    @staticmethod
    def listar_professores():
        return Professores.listar_obj()

    @staticmethod
    def professor_inserir(nome, cpf, senha):
        p = Professor(nome, cpf, senha)
        Professores.inserir(p)

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
    @staticmethod
    def professor_excluir(id):
        p = Professor("teste", "14523678965", "teste", id)  # Cria objeto temporário apenas com o ID
        Professores.excluir(p)

    @staticmethod
    def listar_solicitacoes_por_professor(id_professor):
        solicitacoes = SolicitacoesAula.listar_obj()
        return [s for s in solicitacoes if s.get_id_professor() == id_professor]


    @staticmethod
    def solicitar_aula(motivo, id_esporte, data, hora, vagas, id_professor):
            try:

                data_str = data.strftime("%Y-%m-%d") if hasattr(data, 'strftime') else data
                hora_str = hora.strftime("%H:%M") if hasattr(hora, 'strftime') else hora
                data_hora = f"{data_str} {hora_str}"
                
                s = SolicitacaoAula(
                    motivo=motivo,
                    id_esporte=id_esporte,
                    data_hora=data_hora,
                    vagas=vagas,
                    id_professor=id_professor
                )
                SolicitacoesAula.inserir(s)
                return True
            except Exception as e:
                raise ValueError(f"Erro ao criar solicitação: {str(e)}")
    @staticmethod
    def listar_solicitacoes_pendentes():
        from models.solicitacaoAula import SolicitacoesAula
        return SolicitacoesAula.listar_pendentes()

    @staticmethod
    def aprovar_solicitacao(id_solicitacao):
        solicitacoes = SolicitacoesAula.listar_obj()
        for s in solicitacoes:
            if s.get_id() == id_solicitacao:
                try:
                    data_hora = datetime.strptime(s.get_data_hora(), "%Y-%m-%d %H:%M")
                    horario_formatado = data_hora.strftime("%d-%m-%Y %H:%M")
                    View.aula_inserir(
                        vagas=s.get_vagas(),
                        horario=horario_formatado,
                        id_esporte=s.get_id_esporte(),
                        id_professor=s.get_id_professor()
                    )
                    s.set_status("aprovada")
                    SolicitacoesAula.salvar()
                    return True
                except ValueError as e:
                    raise ValueError(f"Erro ao criar turma: {str(e)}")
        return False



    @staticmethod
    def rejeitar_solicitacao(id_solicitacao):
        from models.solicitacaoAula import SolicitacoesAula
        solicitacoes = SolicitacoesAula.listar_obj()
        for s in solicitacoes:
            if s.get_id() == id_solicitacao:
                s.set_status("rejeitada")
                SolicitacoesAula.salvar()
                return True
        return False