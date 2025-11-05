from Dao import Banco_de_Dados

class Pessoas:
    def __init__(self,CPF,Nome,Email):
        self.__CPF = CPF
        self.__Nome = Nome
        self.__Email = Email

    def get_CPF(self):
        return self.__CPF
    
    def get_Nome(self):
        return self.__Nome
    
    def get_Email(self):
        return self.__Email
    
    def to_String(self):
        print('CPF: ',self.__CPF)
        print('Nome: ',self.__Nome)
        print('Email: ',self.__Email)
        