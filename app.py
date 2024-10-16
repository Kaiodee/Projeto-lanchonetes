import os

restaurantes = [{'nome':'Poke','categoria': 'Japonesa','ativo':True},
                {'nome':'Zé carne', 'categoria':'Baiana','ativo':True},
                {'nome':'Farto', 'categoria':'Italiana','ativo':False},
]

def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Alternar estado do restaurante') 
    print ('4. Sair\n')
    
def voltar_ao_menu_principal ():
    input('Digite uma tecla para recomeçar!: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)#coloca astericos de enfeite por meio da função len(lenght)
    print(linha)     
    print(texto)
    print(linha)

   
def finalizar_app():
   exibir_subtitulo("finalizando o sistema")


def opcao_invalida():
    print('Opção invalida!')
    voltar_ao_menu_principal ()

    
def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")

  
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'digite a categoria do restaurante {nome_do_restaurante} : ')
    dados_do_restaurante = {'nome':nome_do_restaurante ,'categoria' : categoria , 'ativo' : False  }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado!\n')
     
    voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado :')
    restaurante_encontrado = False
    
    for restaurante in restaurantes :
        if nome_restaurante == restaurante['nome']: 
            restaurante_encontrado = True#verificador booleano do if acima
            restaurante['ativo'] = not restaurante['ativo']
            #if ternario
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso ' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('o restaurante nao foi encontrado')
        
    voltar_ao_menu_principal()           
    
    


def listar_restaurantes (): 
    exibir_subtitulo("Listando restaurantes")
    
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes :
        nome_do_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado' # o mesmo que if restaurante [ativado]: print(ativado)
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    
     
    voltar_ao_menu_principal()
        
def escolher_opcao():
    try:
        opcao_escolhida = int(input('escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
           alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app( )
        else:
            opcao_invalida ()
    except:
        opcao_invalida()    
        
#def escolher_opcao_dois():  --testando o match--
    #opcao_escolhida = int(input('escolha uma opção: '))
   # match opcao_escolhida:
         
        # case 1:
             #print('primeira opção escolhida')
        # case 2:
             #print('segunda opção')
    
        
    
    
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
  
if __name__ == "__main__":
    main()


