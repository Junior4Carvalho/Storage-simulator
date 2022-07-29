import os
import time
import getpass
import datetime as dt

tempo = dt.datetime.now()
tempo2 = tempo.strftime("%d/%m/%Y/ %H:%M")

cod = ["storefunc", "employee0029", "JuninALenda"]
lista = ["Teclados", "Monitores", "Mouses", "Gabinetes", "Placa de Vídeos", "CPU's", "Ram's", "HD's", "SSD's", "Headsets"]

print("-*"*10)
print("      PyStore")
print("-*"*10)
first = getpass.getpass("Bem-vindo a PyStore\n ")
if first in cod:
    time.sleep(.3)
    os.system('cls')
    second = "Sistema de gerência"
    print("-*"*10)
    print(second.upper())
    print("-*"*10)

    try:
        third = int(input("Você Deseja Verificar, Retirar, Adicionar ou Substituir produtos? [1, 2, 3, 4] "))
        
        if third == 1:
            print("Os Produtos disponiveis são os seguintes:\n", lista)

        elif third == 2:
            print("Verifique a lista para retirar o produto desejado:\n", lista)
            retirar = int(input("Que produto deseja retirar ? \n"))
            
            try:
                item = lista[retirar]
                del(lista[retirar])
                print("Você removeu {} o {}º item da lista\n a lista atualizada ficou assim: \n".format(item, retirar), lista)
            
            except:
                print("item não identificado")
            
            pergunta1 = input("Deseja remover mais algum item? [S/N]\n ")
            if pergunta1 == "S" or "s":
                print("Verifique a lista para retirar o produto desejado:\n", lista)
                retirar2 = int(input("Que produto deseja retirar ? \n"))
                
                try:
                    item = lista[retirar2]
                    del(lista[retirar])
                    print("Você removeu {} o {}º item da lista\n a lista atualizada ficou assim: \n".format(item, retirar2), lista)

                
                except:
                    print("ñ rolou")
            
            else:
                pass    

        elif third == 3:
            print("Verifique a lista para adicionar o produto :\n", lista)
            adicionar =  input("Adicione o produto desejado: ")
            lista.append("{}".format(adicionar))
            lista2 = lista
            print(lista)
            
            for add in range(0,5):
                pergunta2 = input("Deseja adicionar mais algum item? [S/N]\n ")
                if pergunta2 == "S" or "s":
                    
                    print("Verifique a lista antes de adicionar um produto:\n", lista)
                    adicionar =  input("Adicione o produto desejado: ")
                    try:
                        lista.append("{}".format(adicionar))
                        print(lista)
                    
                    except:
                        print("ñ rolou")
                
                if pergunta2 == "N" or "n":
                 break

        elif third == 4:
            print("Verifique a Lista de produtos para os substituir")
            print(lista)
            produto1 = input("Que produto deseja susbtituir?\n ")

            if produto1 in lista:
                produto2 = input("Adicione o novo produto: \n")
                getnumber = lista.count(produto1)
                print(getnumber)

                lista[getnumber] = produto2
                print("Lista atualizada com sucesso:\n", lista)
            else:
                print("Algo deu errado!")
            
        print("Código gerado em: ", tempo2 )
                        
    except:
        print("Lamentamos, ocorreu algum erro\n Tente mais tarde!")

else:
    print("system error!")
            
 #Copyright-Junior_Carvalho06

