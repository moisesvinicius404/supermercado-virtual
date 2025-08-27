# supermercado-virtual 👨‍💻🛒💻


# SuperMercado: Seu Simulador de Caixa de Supermercado em Python!
# O que é o SuperMercado?

O SuperMercado é um programa Python que simula o processo de compra em um supermercado. Ele permite que você:

# Crie um catálogo de produtos com seus preços.
# Adicione produtos ao carrinho, digitando a quantidade desejada.
# Escolha a forma de pagamento: cartão, Pix ou dinheiro.
# Realize o pagamento, informando o valor e validando a forma de pagamento.
# Receba o troco, se necessário.
# Opcionalmente, inclua o CPF na compra.
# Como Funciona:

# Importe as bibliotecas: time e os.
# Crie a classe SuperMercado:
# Construtor (__init__):
Inicializa o catálogo de produtos com preços.
Inicializa o carrinho vazio.
Define o total da compra como 0.
# Método comprar:
Exibe o catálogo de produtos.
Permite ao usuário escolher um produto e digitar a quantidade desejada.
Adiciona o produto ao carrinho e atualiza o total da compra.
Finaliza a compra quando o usuário digita "sair".
# Método pagar:
Permite ao usuário escolher a forma de pagamento: cartão, Pix ou dinheiro.
Para cada forma de pagamento:
Obtém o valor pago do usuário.
Valida o valor pago e a forma de pagamento (chave Pix, dinheiro suficiente).
Simula o processamento do pagamento.
Exibe mensagem de sucesso ou erro.
Opcionalmente, pede o CPF do usuário e valida o formato.
Agradece a compra e finaliza o programa.
