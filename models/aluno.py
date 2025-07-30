import json


class Aluno:
    def __init__(self, nome, cpf, senha, id=0):
        self.set__id(id)
        self.set__nome(nome)
        self.set__cpf(cpf)
        self.set__senha(senha)


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
        cpf = 00000000000
        if len(cpf) != 11:
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









