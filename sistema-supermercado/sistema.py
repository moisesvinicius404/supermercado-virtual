import time
import os

class SuperMercado:
    def __init__(self):
        self.catalago =  {
            'Arroz': 5.0,
            'Feijão': 9.0,
            'Macarrão': 4.90,
            'Cuscuz': 2.50,
            'Coca-cola': 5.0,
            'Bife': 20.0,
            'File mion': 22.0,
            'Carne de porco': 19.0,
            'Oléo': 10.90,
            'Biscoito': 2.50}
                        
        self.carrinho = {}
        self.total = 0.0
        
    def comprar(self):
        print('\nCatalago de produtos:')
        for produto, preco in self.catalago.items():
            print(f'{produto.capitalize()}: - R$ {preco:.2f}')
        while True:
                
                escolha = input('\nDigite o nome do produto que deseja comprar ou ("sair" para encerrar): ').capitalize()
                
                if escolha == 'Sair':
                    os.system('cls')
                    break
                
                
                if escolha in self.catalago:
                    quantidade = int(input(f'Quantas unidades de {escolha} você deseja compra? : '))
                    if quantidade > 0:
                        self.carrinho[escolha] = quantidade
                        self.total += self.catalago[escolha] * quantidade
                        print(f'Produto: {escolha} foi adicionado ao carrinho!')
                    else:
                        print('Quantidade inválida!')
                else:
                    print('Produto não encontrado!')
                    
    def pagar(self):
        forma_de_pagamento = str(input('Qual a forma de pagamento (cartão, pix, dinheiro)? : ')).lower()
        if forma_de_pagamento == 'cartão':
            print(f'O valor total do seu carrinho é R$ {self.total:.2f}')
            
            pagamento = float(input('Digite a quantia a ser paga: '))
            
            if pagamento < self.total:
                print('Processando pagamento...')
                time.sleep(1)
                print('Valor insuficiente!')
                while pagamento != self.total:
                    pagamento = float(input('Digite uma quantia igual o valor da compra: '))
                
            else:
                print('Processando pagamento...')
                time.sleep(1)
                print('Compra realizada com sucesso!')
                
                
        elif forma_de_pagamento == 'pix':
            print(f'O valor total do seu carrinho é R$ {self.total:.2f}')
            chave_pix = '982007590'
            print(f'Essa é nossa chave pix: {chave_pix}')
            digito_chave_pix = input('Digite nossa chave pix para efetuar o pagamento: ')
            pagamento = float(input('Digite a quantia a ser paga: '))
            if chave_pix == digito_chave_pix and pagamento == self.total:
                print('Processando pagamento...')
                time.sleep(1)
                print('Compra realizada com sucesso!')
            else:
                print('Valor ou chave pix inválidos!\n')
                print(f'Essa é nossa chave pix: {chave_pix}')
                while chave_pix != digito_chave_pix and pagamento != self.total:
                    digito_chave_pix = input('Digite uma chave pix igual a nossa: ')
                    pagamento = float(input('Digite uma quantia igual o valor da compra: '))
                
                
        elif forma_de_pagamento == 'dinheiro':
            print(f'O valor total do seu carrinho é R$ {self.total:.2f}')
            dinheiro = float(input('Digite a quantia a ser paga:  '))
            
            if dinheiro < self.total:
                print('Processando pagamento...')
                time.sleep(1)
                print('Valor insuficiente!')
                while  dinheiro != self.total:
                    pagamento = float(input('Digite uma quantia igual o valor da compra: '))
            else:
                print('Processando pagamento...')
                time.sleep(1)
                print('Compra realizada com sucesso!')
                troco = dinheiro - self.total
                print(f'O seu troco é R$ {troco:.2f}')
        else:
            print('Forma de pagamento inválida!')
            while forma_de_pagamento != 'cartão' and forma_de_pagamento != 'pix' and forma_de_pagamento != 'dinheiro':
                forma_de_pagamento = str(input('so temos essas formas de pagamento (cartão, pix, dinheiro) digite uma delas: ')).lower()
            
        # Pergunta entre coloca o CPF ou não
        per_cpf = input('Deseja coloca seu CPF (sim,não): ').lower()
        if per_cpf == 'sim':
            cpf = input('Digite o numero de seu CPF: ')
            if len(cpf) < 11:
                print('Processando...')
                time.sleep(1)
                print('CPF inválido!')
                while len(cpf) < 11:
                    cpf = input('Digite o número de CPF valido: ')
            else:
                print('Processando...')
                time.sleep(1)
                print('CPF valido!\n')
            print('CPF valido!')
            print('Obrigado por comprar conosco!')
                
                

mercado = SuperMercado() # instancia
mercado.comprar() # metodos
mercado.pagar() # metodos