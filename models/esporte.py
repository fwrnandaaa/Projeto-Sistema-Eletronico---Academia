import json
class Esporte:
    def __init__(self, id, nome):
        self.setId(id)
        self.setNome(nome)

    def getId(self):
        return self.__id
    def setId(self, value):
        if value < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = value

    def getNome(self):
        return self.__nome

    def setNome(self, value):
        self.__nome = value

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome
        }

    def __str__(self):
        return f"Esporte(id={self.__id}, nome='{self.__nome}')"
    
class Esportes:
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("esportes.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    esporte = Esporte(
                        id=dic["id"],
                        nome=dic["nome"]
                    )
                    cls.objetos.append(esporte)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda e: e.getId())
        with open("esportes.json", mode="w") as arquivo:
            lista_dicts = [e.to_dict() for e in cls.objetos]
            json.dump(lista_dicts, arquivo, indent=4)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        t = 0
        if len(cls.objetos) > 0:
            t = max(cls.objetos, key=lambda e: e.getId()).getId()
        obj.setId(t + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return [str(e) for e in cls.objetos]

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
        for obj in cls.objetos:
            if obj.getId() == obj_atualizado.getId():
                obj.setNome(obj_atualizado.getNome())
                cls.salvar()
                return True
        return False

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        x = cls.listar_id(obj.getId())
        if x is not None:
            cls.objetos.remove(x)
            cls.salvar()
