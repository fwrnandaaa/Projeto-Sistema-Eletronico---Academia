import json


class Aluno:
    def __init__(self, nome, cpf, senha, id=0):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_senha(senha)


    def set_id(self, id):
        id = int(id)
        if id < 0:
            raise ValueError("ID não pode ser negativo!")
        else:
            self.__id = id
   
    def get_id(self):
        return self.__id


    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio!")
        else:
            self.__nome = nome
   
    def get_nome(self):
        return self.__nome


    def set_cpf(self, cpf):
        if len(str(cpf)) != 11:
            raise ValueError  ("CPF inválido!")
        else:
            self.__cpf = cpf


    def get_cpf(self):
        return self.__cpf


    def set_senha(self, senha):
        if senha == "":
            raise ValueError("Senha não pode ser vazio!")
        else:
            self.__senha = senha


    def get_senha(self):
        return self.__senha


    def __str__(self):
        return f"ID: {self.__id} \n Nome: {self.__nome} \n CPF: {self.__cpf} \n Senha: {self.__senha}"
   
    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "cpf": self.__cpf,
            "senha": self.__senha
        }
    
class Alunos:
    objetos = []
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("alunos.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    aluno = Aluno(
                        id=dic["id"],
                        nome=dic["nome"],
                        cpf=dic["cpf"],
                        senha=dic["senha"]
                    )
                    cls.objetos.append(aluno)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda a: a.get_id())
        with open("alunos.json", mode="w") as arquivo:
            lista_dicts = [a.to_dict() for a in cls.objetos]
            json.dump(lista_dicts, arquivo, indent=4)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        t = 0
        if len(cls.objetos) > 0:
            t = max(cls.objetos, key=lambda a: a.get_id()).get_id()
        obj.set_id(t + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return [str(a) for a in cls.objetos]

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
        for obj in cls.objetos:
            if obj.get_id() == obj_atualizado.get_id():
                try:
                    obj.set_nome(obj_atualizado.get_nome())
                    obj.set_cpf(obj_atualizado.get_cpf())
                    obj.set_senha(obj_atualizado.get_senha())
                    cls.salvar()
                    return True
                except ValueError as e:
                    raise ValueError(f"Dados inválidos: {e}")
        return False

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cls.objetos = [aluno for aluno in cls.objetos if aluno.get_id() != obj.get_id()]
        cls.salvar()
        return True










