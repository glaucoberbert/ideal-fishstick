from Dao import Banco_de_Dados

def __init__(self,IdSalas,Capacidade):
        self.__IdSalas = IdSalas
        self.__Capacidade = Capacidade
        
def get_IdSalas(self):
    return self.__IdSalas

def get_Capacidade(self):
    return self.__Capacidade

def salvar(self):
        conn = None
        cursor = None
        try:  
            conn = Banco_de_Dados.mysql.connector.connect(**Banco_de_Dados.db_config)
            if conn.is_connected():
                
                sql = "INSERT INTO Salas (IdSalas, Capacidade) VALUES (%s, %s)"
                val = (self.get_IdSalas(), self.get_Capacidade())
                cursor.execute(sql, val)
                conn.commit()
                
                print(f"Salas {self.get_IdSalas()} salvo com sucesso.")
        except Banco_de_Dados.mysql.connector.Error as e:
            print(f"Erro ao salvar Salas: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()
    
@staticmethod
def buscar_por_IdSalas(IdSalas):
      conn = None
      cursor = None
      try:
         conn = Banco_de_Dados.mysql.connector.connect(**Banco_de_Dados.db_config)
         if conn.is_connected():
            cursor = conn.cursor()
            sql = "SELECT IdSalas, Capacidade FROM Salas WHERE IdSalas = %s"
            val = (IdSalas,)
            cursor.execute(sql, val)
            resultado = cursor.fetchone()
            if resultado:
               return Salas(resultado[0], resultado[1])
            else:
               return None
      except Banco_de_Dados.mysql.connector.Error as e:
         print(f"Erro ao buscar sala por Id: {e}")
         return None
      finally:
         if cursor is not None:
            cursor.close()
         if conn is not None and conn.is_connected():
            conn.close()