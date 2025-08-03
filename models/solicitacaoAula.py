import json
from datetime import datetime

class SolicitacaoAula:
    def __init__(self, motivo, id_esporte, data_hora, vagas, id_professor, status="pendente", id=0):
        self.set_id(id)
        self.set_motivo(motivo)
        self.set_id_esporte(id_esporte)
        self.set_data_hora(data_hora)
        self.set_vagas(vagas)
        self.set_id_professor(id_professor)
        self.set_status(status)  

    def get_id(self): 
        return self.__id
    def get_motivo(self): 
        return self.__motivo
    def get_id_esporte(self): 
        return self.__id_esporte
    def get_data_hora(self): 
        return self.__data_hora.strftime("%Y-%m-%d %H:%M")
    def get_data_hora_datetime(self):
        return self.__data_hora
    def get_vagas(self): 
        return self.__vagas
    def get_id_professor(self): 
        return self.__id_professor
    def get_status(self): 
        return self.__status
    
    def set_motivo(self, motivo):
        if not motivo or motivo.strip() == "":
            raise ValueError("O motivo não pode estar vazio")
        self.__motivo = motivo.strip()

    def set_vagas(self, vagas):
        if not isinstance(vagas, int) or vagas <= 0:
            raise ValueError("O número de vagas deve ser um inteiro positivo")
        self.__vagas = vagas

    def set_data_hora(self, data_hora):
        if data_hora == "":
            raise ValueError("Data/hora não pode ser vazia")
        try:
            if isinstance(data_hora, str):
                self.__data_hora = datetime.strptime(data_hora, "%Y-%m-%d %H:%M")
            elif isinstance(data_hora, datetime):
                self.__data_hora = data_hora
            else:
                raise ValueError("Tipo inválido para data_hora")
        except ValueError:
            raise ValueError("Formato de data/hora inválido. Use 'YYYY-MM-DD HH:MM'")

    def set_id(self, id): 
        self.__id = id
    def set_id_esporte(self, id_esporte): 
        self.__id_esporte = id_esporte
    def set_id_professor(self, id_professor): 
        self.__id_professor = id_professor
    def set_status(self, status): 
        self.__status = status

    def to_dict(self):
        return {
            "id": self.__id,
            "motivo": self.__motivo,
            "id_esporte": self.__id_esporte,
            "data_hora": self.get_data_hora(),
            "vagas": self.__vagas,
            "id_professor": self.__id_professor,
            "status": self.__status
        }

class SolicitacoesAula:
    objetos = []
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("solicitacoes_aula.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    solicitacao = SolicitacaoAula(
                        id=dic["id"],
                        motivo=dic["motivo"],
                        id_esporte=dic["id_esporte"],
                        data_hora=dic["data_hora"],
                        vagas=dic["vagas"],
                        id_professor=dic["id_professor"],
                        status=dic["status"]
                    )
                    cls.objetos.append(solicitacao)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("solicitacoes_aula.json", mode="w") as arquivo:
            lista_dicts = [s.to_dict() for s in cls.objetos]
            json.dump(lista_dicts, arquivo, indent=4)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        obj.set_id(max([s.get_id() for s in cls.objetos] or [0]) + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_obj(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_pendentes(cls):
        cls.abrir()
        return [s for s in cls.objetos if s.get_status() == "pendente"]