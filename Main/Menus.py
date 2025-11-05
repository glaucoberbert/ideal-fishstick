

@staticmethod
def menu_principal():
    print('\n--- Menu Principal ---')
    print('1-Gestão de Funcionarios')
    print('2-Gestão de Filmes')
    print('3-Gestão de Produtos')
    print('4-Gestão de Salas')
    print('5-Gestão de Planos')
    print('6-Gestão de Sessão')
    print('0-Sair do Programa')
    op = int(input('Digite uma opção acima: '))
    return op

@staticmethod
def Gestao_Funcionarios():
    print('1-Adicionar Funcionario')
    print('2-Listar Funcionarios')
    print('0-Voltar ao Menu Principal')
    opf = int(input('Digite uma opção acima: '))
    return opf

@staticmethod 
def Gestao_Filmes():
    print('1-Adicionar Filme')
    print('2-Listar Filmes')
    print('0-Voltar ao Menu Principal')    
    op = int(input('Digite uma opção acima: '))
    return op

def adicionar_funcionario():
    cpf = input('Digite o CPF do funcionario: ')
    nome = input('Digite o nome do funcionario: ')
    email = input('Digite o email do funcionario: ')
    salario = input('Digite o salario do funcionario: ')
    cargo = input('Digite o cargo do funcionario: ')
    funcionario = Funcionarios(cpf, nome, email, salario, cargo)
    funcionario.salvar()
    print('Funcionario adicionado com sucesso.')