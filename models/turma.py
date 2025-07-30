import json
from datetime import datetime


class Turma:
    def __init__(self, vagas, horario, IdEsporte, IdProfessor, id=0):
        self.set_id(id)
        self.set_id_esporte(IdEsporte)
        self.set_id_prof(IdProfessor)
        self.set_vagas(vagas)
        self.set_horario(horario)
    def set_id(self, value):
        if value < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = value

    def set_id_esporte(self, IdEsporte):
        if IdEsporte < 0:
            raise ValueError("Id do esporte não pode ser negativo")
        self.__id_esporte = IdEsporte

    def set_id_prof(self, IdProfessor):
        if IdProfessor < 0:
            raise ValueError("ID do professor não poden ser negativo")
        self.__id_prof = IdProfessor

    def get_id(self):
        return self.__id

    def get_id_esporte(self):
        return self.__id_esporte

    def get_id_prof(self):
        return self.__id_prof

    def set_vagas(self, vagas):
        if vagas < 0:
            raise ValueError("A quantidade de vagas não pode ser negativo")
        else:
            self.__vagas = vagas


    def get_vagas(self):
        return self.__vagas


    def set_horario(self, horario):
        if horario == "":
            raise ValueError("Horário não pode ser vazio")
        else:
            try:
                
                horario_datetime = datetime.strptime(horario, "%Y-%m-%d %H:%M")
                self.__horario = horario_datetime
            except ValueError:
                raise ValueError("Formato de horário inválido. Use 'YYYY-MM-DD HH:MM'")

    def get_horario(self):
        if self.__horario is None:
            return None
        return self.__horario.strftime("%Y-%m-%d %H:%M")



    def __str__(self):
        return f"ID: {self.__id} \n ID esporte: {self.__id_esporte} \n ID professor: {self.__id_prof} \n Vagas: {self.__vagas} \n Horário: {self.__horario}"


    def to_dict(self):
            return{
                "id": self.__id,
                "id_esporte": self.__id_esporte,
                "id_prof": self.__id_prof,
                "vagas": self.__vagas,
                "horario": self.get_horario() 
            }


class Turmas:
    objetos = []


    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("turmas.json", mode="r") as arquivo:
                try:
                    a = json.load(arquivo)
                except json.JSONDecodeError:
                    a = []  # se o JSON estiver vazio/corrompido, considera lista vazia

                for dic in a:
                    turma = Turma(
                        id=dic["id"],
                        IdEsporte=dic["id_esporte"],
                        IdProfessor=dic["id_prof"],
                        vagas=dic["vagas"],
                        horario=dic["horario"]
                    )
                    cls.objetos.append(turma)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda turma: turma.get_id())
        with open("turmas.json", mode="w") as arquivo:
            lista_dicts = [turma.to_dict() for turma in cls.objetos]
            json.dump(lista_dicts, arquivo, indent=4)


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        t = 0
        if len(cls.objetos) > 0:
            t = max(cls.objetos, key=lambda c: c.get_id()).get_id()
        obj.set_id(t + 1)
        cls.objetos.append(obj)
        cls.salvar()


    @classmethod
    def listar(cls):
        cls.abrir()
        return [str(turma) for turma in cls.objetos]


    @classmethod
    def listar_obj(cls):
        cls.abrir()
        return cls.objetos


    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj_atualizado):
        cls.abrir()
        for i, obj in enumerate(cls.objetos):
            if obj.get_id == obj_atualizado.get_id():
                try:
                    obj.set_vagas(obj_atualizado.get_vagas())
                    obj.set_horario(obj_atualizado.get_horario())
                    return True
                except ValueError as e:
                    raise ValueError(f"Dados inválidos: {e}")


    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None:
            cls.objetos.remove(x)
            cls.salvar




   



