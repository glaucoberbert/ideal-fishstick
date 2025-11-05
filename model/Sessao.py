from Dao import Banco_de_Dados

def __init__(self,IdSessao,IdFilme,IdSalas,Horario,Data):
    self.__IdSessao = IdSessao
    self.__IdFilme = IdFilme
    self.__IdSalas = IdSalas
    self.__Horario = Horario
    self.__Data = Data

def get_IdSessao(self):
    return self.__IdSessao
    
def get_Horario(self):
    return self.__Horario

def get_Data(self):
    return self.__Data

def get_IdSalas(self):
    return self.__IdSalas

def get_IdFilme(self):
    return self.__IdFilme

def get_Data(self):
    return self.__Data

def salvar(self):
        conn = None
        cursor = None
        try:  
            conn = Banco_de_Dados.mysql.connector.connect(**Banco_de_Dados.db_config)
            if conn.is_connected():
                
                sql = "INSERT INTO Sessao (IdSessao, IdFilme, IdSalas, Horario, Data) VALUES (%s, %s, %s, %s, %s)"
                val = (self.get_IdSessao(), self.get_IdFilme(), self.get_IdSalas(), self.get_Horario(), self.get_Data())
                cursor.execute(sql, val)
                conn.commit()
                
                print(f"Sessao {self.get_IdSessao()} salvo com sucesso.")
        except Banco_de_Dados.mysql.connector.Error as e:
            print(f"Erro ao salvar Sessao: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()
    
@staticmethod
def buscar_por_IdSessao(IdSessao):
      conn = None
      cursor = None
      try:
         conn = Banco_de_Dados.mysql.connector.connect(**Banco_de_Dados.db_config)
         if conn.is_connected():
            cursor = conn.cursor()
            sql = "SELECT IdSessao, IdFilme, IdSalas, Horario, Data FROM Sessao WHERE IdSessao = %s"  
            val = (IdSessao,)
            cursor.execute(sql, val)
            resultado = cursor.fetchone()
            if resultado:
               return Sessao(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            else:
               return None
      except Banco_de_Dados.mysql.connector.Error as e:
         print(f"Erro ao buscar sessao por Id: {e}")
         return None
      finally:
         if cursor is not None:
            cursor.close()
         if conn is not None and conn.is_connected():
            conn.close()
#Fazer menu para opcao de filme e sala pra fazer sessao 