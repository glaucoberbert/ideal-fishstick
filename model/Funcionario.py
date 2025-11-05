from model.Pessoas import Pessoas
from Dao import Banco_de_Dados

class Funcionarios(Pessoas):
    def __init__(self,CPF,Nome,Email,Salario,Cargo):
        super().__init__(CPF,Nome,Email)
        self.__Salario = Salario
        self.__Cargo = Cargo
        
    def get_Salario(self):
        return self.__Salario
    
    def get_Cargo(self):
        return self.__Cargo
    
    def salvar_funcionario(self):
        conn = None
        cursor = None
        try:  
            conn = Banco_de_Dados.mysql.connector.connect(**Banco_de_Dados.db_config)
            if conn.is_connected():
                
                sql = "INSERT INTO Pessoas (CPF, Nome, Email) VALUES (%s, %s, %s)"
                val = (self.get_cpf(), self.get_nome(), self.get_Email())
                cursor.execute(sql, val)
                conn.commit()
                
                sql = "INSERT INTO Funcionarios (CPF, Salario, Cargo) VALUES (%s, %s, %s)"
                val = (self.get_CPF(), self.__Salario, self.__Cargo)
                cursor.execute(sql, val)
                conn.commit()
                print(f"Funcionario {self.get_nome()} salvo com sucesso.")
        except Banco_de_Dados.mysql.connector.Error as e:
            print(f"Erro ao salvar Funcionario: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()
    
    @staticmethod
    def buscar_por_nome(nome):
      conn = None
      cursor = None
      try:
         conn = Banco_de_Dados.mysql.connector.connect(**Banco_de_Dados.db_config)
         if conn.is_connected():
            cursor = conn.cursor()
            sql = "SELECT CPF, Nome, Email, Salario, Cargo FROM Pessoas as p, Funcionarios as f WHERE p.CPF = f.Pessoas_CPF and Nome = %s"  
            val = (nome,)
            cursor.execute(sql, val)
            resultado = cursor.fetchone()
            if resultado:
               return Pessoas(resultado[0], resultado[1], resultado[2]) + Funcionarios(resultado[3], resultado[4])
            else:
               return None
      except Banco_de_Dados.mysql.connector.Error as e:
         print(f"Erro ao buscar funcionario por nome: {e}")
         return None
      finally:
         if cursor is not None:
            cursor.close()
         if conn is not None and conn.is_connected():
            conn.close()