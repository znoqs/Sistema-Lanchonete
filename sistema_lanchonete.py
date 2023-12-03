print('Sistema de Pedidos Online!')
print('Seja bem-vindo ao sistema de pedidos da lanchonete XXX!')
print()
print('-'*50)
print('Vou te ajudar a fazer seu pedido!')


#--------------Funções e variáveis ------------------


#---------Variáveis Globais---------------
carrinho_compras = {}
total = 0 

#----------------Main Menu-----------------
def main():
    while True:
        escolha_menu = int(input("""
        Escolha alguma das opções abaixo!    

        1. Lanches
        2. Bebidas
        3. Bolos
        4. Carrinho
        5. Sair
                                 
        """))
        
        if escolha_menu == 1:
            print('-'*50)
            print('-'*50)
            print('-'*50)
            menu_lanches()
        elif escolha_menu == 2:
            menu_bebidas()
        elif escolha_menu == 3:
            print('-'*50)
            print('-'*50)
            print('-'*50)
            menu_bolos()
        elif escolha_menu == 4:
            print('-'*50)
            print('-'*50)
            print('-'*50)
            carrinho()
        elif escolha_menu == 5:
            print("\nSaindo do sistema de pedidos!")
            print('-'*50)
            print('-'*50)
            print('-'*50)
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            print('-'*50)
            print('-'*50)
            print('-'*50)
#----------------Menu de Lanches-------------------
def menu_lanches():
    
      print()
      print(""" 
    Você escolheu o menu de Lanches!
    Escolha alguma das opções abaixo:
            
    1. X-Burger -------------- R$ 10,00
    2. X-Salada -------------- R$ 12,00
    3. X-Tudo ---------------- R$ 15,00
    4. X-Bacon --------------- R$ 13,00
    5. Voltar para o Menu principal
    """)
      pedido_lanche = int(input('Digite o número do lanche desejado: '))
      if pedido_lanche == 1:
          lanche = "X-burger"
          print(f"\n{lanche} adicionado ao carrinho!")
          carrinho_compras[lanche] = 10.00
      elif pedido_lanche == 2:
          lanche = "X-salada"
          carrinho_compras[lanche] = 12.00
          print(f'\n{lanche} adicionado ao carrinho!')
      elif pedido_lanche == 3:
          lanche = "X-tudo"
          carrinho_compras[lanche] = 15.00
          print(f'\n{lanche} adicionado ao carrinho!')
      elif pedido_lanche == 4:
          lanche = "X-bacon"
          carrinho_compras[lanche] = 13.00
          print(f'\n{lanche} adicionado ao carrinho!')
      elif pedido_lanche == 5:
          print('-'*50)
          print('-'*50)
          print('-'*50)
          main()
      
  
#----------------Menu de Bebidas-------------------

def menu_bebidas():
    print()
    print("""
    Você escolheu o menu de Bebidas!
    Escolha alguma das opções abaixo:
          
    1. Suco de Laranja ------- R$ 5,00
    2. Coca Cola(500ml) ------ R$ 7,00
    3. Fanta(500ml) ---------- R$ 6,50
    4. Guaraná(500ml) -------- R$ 5,00
    5. Voltar para o Menu principal
    """)
    pedido_bebida = int(input('Digite o número da bebida desejada: '))
    if pedido_bebida == 1:
        bebida = 'Suco de Laranja'
        carrinho_compras[bebida] = 5.00
        print(f'\n{bebida} adicionada ao carrinho!')
    elif pedido_bebida == 2:
        bebida = 'Coca Cola'
        carrinho_compras[bebida] = 7.00
        print(f'\n{bebida} adicionada ao carrinho!')
    elif pedido_bebida == 3:
        bebida = 'Fanta'
        carrinho_compras[bebida] = 6.50
        print(f'\n{bebida} adicionada ao carrinho!')
    elif pedido_bebida == 4:
        bebida = 'Guarana'
        carrinho_compras[bebida] = 5.00
        print(f'\n{bebida} adicionada ao carrinho!')
    elif pedido_bebida == 5:
        print('-'*50)
        print('-'*50)
        print('-'*50)
        main()

    print('-'*50)
    print('-'*50)
    print('-'*50)
#---------------Menu de Bolos-----------------
def menu_bolos():
      print()
      print("""
    Você escolheu o menu de Bolos!
    Escolha alguma das opções abaixo:
            
    1. Bolo de Chocolate ----- R$ 10,00
    2. Bolo de Cenoura ------- R$ 10,00
    3. Bolo de Fubá ---------- R$ 10,00
    4. Bolo de Limão --------- R$ 10,00
    5. Voltar para o Menu principal
      """)
      pedido_bolo = int(input('Digite o número do bolo desejado: '))
      if pedido_bolo == 1:
          bolo = 'bolo de chocolate'
          carrinho_compras[bolo] = 10.00
          print(f'\n{bolo} adicionado ao carrinho!')
      elif pedido_bolo == 2:
          bolo = 'bolo de cenoura'
          carrinho_compras[bolo] = 10.00
          print(f'\n{bolo} adicionado ao carrinho!')
      elif pedido_bolo == 3:
          bolo = 'bolo de fuba'
          carrinho_compras[bolo] = 10.00
          print(f'\n{bolo} adicionado ao carrinho!')
      elif pedido_bolo == 4:
          bolo = 'bolo de limao'
          carrinho_compras[bolo] = 10.00
          print(f'\n{bolo} adicionado ao carrinho!')
      elif pedido_bolo == 5:
          print('-'*50)
          print('-'*50)
          print('-'*50)
          main()
  
#---------------Carrinho-------------------
def carrinho():
    print()
    print('Itens no carrinho')
    global total
    total = 0
    for item in carrinho_compras:
        print(f'{item} - R${carrinho_compras[item]}')
        total += carrinho_compras[item]
    print(f'Total a pagar: R${total}')
    finalizarPedido()
    print('-'*50)
    print('-'*50)
    print('-'*50)

#------------------------------------------------
#finalizar pedido 

def finalizarPedido():
    perguntaFimPedido = input('\nDeseja finalizar o pedido? [s/n] ')
    if perguntaFimPedido == 's':
        escolhaPagamento = input('''
        Qual a forma de pagamento?
        1. Dinheiro
        2. Cartão
        3. Pix
        ''')
        if escolhaPagamento == '1':
            escolhaTroco = input('Vai precisar de troco? [s/n] ')
            if escolhaTroco == 's':
                qtdTroco = float(input('Para quanto? '))
                totalTroco = total - qtdTroco
                print(f'''
Total do pedido: (R${total})
Seu troco: (R${totalTroco})
Pedido Finalizado! Obrigado pela preferência!
                ''')
            else:
                print(f'''
Ótimo!
Total do pedido: (R${total})
Pedido Finalizado! Obrigado pela preferência!
                ''')
        elif escolhaPagamento == '2':
            escolhaCartao = input('''
1. Débito
2. Crédito
            ''')
            if escolhaCartao == '1':
                print(f'''
Total do pedido: (R${total})
Pedido Finalizado! Obrigado pela preferência!
                ''')
            else:
                print(f'''Total do pedido: (R${total})
Pedido Finalizado! Obrigado pela preferência!
                ''')
        elif escolhaPagamento == '3':
            print(f'''Ótimo, chave do pix: 11983654110! (R${total})''')
          
        exit()
    if perguntaFimPedido == 's':
        print('Pedido Finalizado! Obrigado pela preferência!')

main()

