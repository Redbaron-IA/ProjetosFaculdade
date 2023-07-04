#Carregando as classes
from Heranca.PessoaClass import Pessoa
from Heranca.ContaClass import Conta
from Heranca.ContaCorrenteClass import ContaCorent
from Heranca.ContaPupancaClass import ContaPoupanca

#criando objeto Vandelson

vandelson = Pessoa("Vandelson", 1.75, 42, '14/09/1980', 'Ensino Superior', 1.320)

print('Manipulando o objeto {}:'.format(vandelson))

#criando objetos contas Vandelson

conta1 = ContaCorent(6677, 'CC.1234.56', '10/07/2002', vandelson, 9876, 500.00, 200.00)
conta2 = ContaPoupanca(6678, 'PP.1234.56', vandelson, 9876, 500.00, '10/07')

for row in conta1:
    conta1 = contap[row]