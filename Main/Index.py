
from Main.Menus import menu_principal
from Main.Menus import Gestao_Funcionarios
from model.Funcionario import Funcionarios

def menu():
    op = menu_principal()
    if op == 1:
        opf = Gestao_Funcionarios()
        if opf == 1:
            Funcionarios.salvar_funcionario()
    