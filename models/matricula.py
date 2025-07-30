import json
from datetime import datetime

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
                pass
            
    def getStatus(self):
        return self.__status

    def __setStatus(self, status):
        self.__status = status

 
    def to_dict(self):
        return {
            "id": self.__id,
            "idAluno": self.__idAluno,
            "idTurma": self.__idTurma,
            "dataMatricula": self.__dataMatricula.strftime("%Y-%m-%d %H:%M"),
            "status": self.__status
        }


    def __str__(self):
        return (
            f"Matricula(id={self.__id}, idAluno={self.__idAluno}, idTurma={self.__idTurma}, "
            f"dataMatricula={self.__dataMatricula}, status='{self.__status}')"
        )
    
class Matriculas:
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("matriculas.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    matricula = Matricula(
                        id=dic["id"],
                        idAluno=dic["idAluno"],
                        idTurma=dic["idTurma"],
                        dataMatricula=dic["dataMatricula"],
                        status=dic["status"]
                    )
                    cls.objetos.append(matricula)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda m: m.getId())
        with open("matriculas.json", mode="w") as arquivo:
            lista_dicts = [m.to_dict() for m in cls.objetos]
            json.dump(lista_dicts, arquivo, indent=4)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        t = 0
        if len(cls.objetos) > 0:
            t = max(cls.objetos, key=lambda m: m.getId()).getId()
        obj._Matricula__setId(t + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return [str(m) for m in cls.objetos]

    @classmethod
    def listar_obj(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.getId() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj_atualizado):
        cls.abrir()
        for i, obj in enumerate(cls.objetos):
            if obj.getId() == obj_atualizado.getId():
                try:
                    obj._Matricula__setIdAluno(obj_atualizado.getIdAluno())
                    obj._Matricula__setIdTurma(obj_atualizado.getIdTurma())
                    obj._Matricula__setDataMatricula(obj_atualizado.getDataMatricula())
                    obj._Matricula__setStatus(obj_atualizado.getStatus())
                    cls.salvar()
                    return True
                except ValueError as e:
                    raise ValueError(f"Dados inválidos: {e}")
        return False

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        x = cls.listar_id(obj.getId())
        if x is not None:
            cls.objetos.remove(x)
            cls.salvar()