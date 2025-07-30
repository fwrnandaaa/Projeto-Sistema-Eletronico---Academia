import json
from datetime import datetime, date

class Matricula:
    def __init__(self, id, idAluno, idTurma, dataMatricula, status):
        self.__setId(id)
        self.__setIdAluno(idAluno)
        self.__setIdTurma(idTurma)
        self.__setDataMatricula(dataMatricula)
        self.__setStatus(status)

    def getId(self):
        return self.__id

    def __setId(self, id):
        if id < 0:
            raise ValueError("Id não pode ser negativo")
        self.__id = id

    def getIdAluno(self):
        return self.__idAluno

    def __setIdAluno(self, idAluno):
        if idAluno < 0:
            raise ValueError("Id do aluno não pode ser negativo")
        self.__idAluno = idAluno
    
    def getIdTurma(self):
        return self.__idTurma

    def __setIdTurma(self, idTurma):
        if idTurma < 0:
            raise ValueError("Id da turma não pode ser negativo")
        self.__idTurma = idTurma
    def getDataMatricula(self):
        return self.__dataMatricula

    def __setDataMatricula(self, dataMatricula):
        if dataMatricula == "":
            raise ValueError("Horário não pode ser vazio")
        else:
            try:
                
                horario_datetime = datetime.strptime(dataMatricula, "%Y-%m-%d %H:%M")
                self.__dataMatricula = horario_datetime
            except ValueError:
                raise ValueError("Formato de horário inválido. Use 'YYYY-MM-DD HH:MM'")
            
    def getStatus(self):
        return self.__status

    def __setStatus(self, status):
        self.__status = status

 
    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "idAluno": self.__idAluno,
            "idTurma": self.__idTurma,
            "dataMatricula": self.__dataMatricula.isoformat(),
            "status": self.__status
        }


    def __str__(self) -> str:
        return (
            f"Matricula(id={self.__id}, idAluno={self.__idAluno}, idTurma={self.__idTurma}, "
            f"dataMatricula={self.__dataMatricula}, status='{self.__status}')"
        )