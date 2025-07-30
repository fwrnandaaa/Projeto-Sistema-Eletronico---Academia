from models.aluno import Aluno, Alunos
from models.professor import Professor, Professores
from models.esporte import Esporte, Esportes
from models.turma import Turma, Turmas
from models.matricula import Matricula, Matriculas



#aluno = Aluno(nome="João Silva", cpf="12345678901", senha="senha123")
#print("Teste da classe aluno: ")
#Alunos.inserir(aluno)
#print(aluno)

#professor = Professor(nome="Maria Oliveira", cpf="09876543210", senha="senha456")
#print("Teste da classe professor: ")
#Professores.inserir(professor)
#print(professor)

#esporte = Esporte(id=0, nome="Futebol")
#print("Teste da classe esporte: ")
#print(esporte)
#Esportes.inserir(esporte)
#print("Esportes salvos:", Esportes.listar())



#turma = Turma(
#   vagas=30,
#    horario="2025-08-01 14:00",
#    IdEsporte=1,
#    IdProfessor=1,
#    id=0
#)

#print("Teste da classe turmas: ")
#print(turma)
#Turmas.inserir(turma)
#print("Turmas salvas:", Turmas.listar())



matricula = Matricula(
    id=0,
    idAluno=1,
    idTurma=1,
    dataMatricula="2025-08-01 14:00",
    status="Ativa"
)
print("Teste da classe matricula: ")
print(matricula)
Matriculas.inserir(matricula)
print("Matriculas salvas:", Matriculas.listar())
