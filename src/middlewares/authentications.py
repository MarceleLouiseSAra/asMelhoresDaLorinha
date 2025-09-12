from datetime import datetime

def verificaEntradaNumérica() -> int:
    
    while True:

        try:
            entradaNumerica = int(input())

        except (ValueError, TypeError):
            print("\nO tipo da entrada dada é inesperado: forneça uma entrada válida.")

        except Exception as erro:
            print(f"\nFoi encontrado um {erro.__class__}. Forneça uma entrada válida.")

        else:
            if entradaNumerica < 0:
                print("\nEntrada negativa: forneça uma entrada válida.")
            else:
                return entradaNumerica 

def verificaEntradaAlfabetica() -> str:
    
    while True:
        
        entradaAlfabetica = input()

        if not(entradaAlfabetica.isalpha()):
            
            for caractere in range(len(entradaAlfabetica)):
                if entradaAlfabetica[caractere].isalpha() or entradaAlfabetica[caractere].isspace():
                    controle = 1
                    continue
                else: 
                    controle = 0
                    print("\nEntrada inválida: forneça uma nova entrada.")
                    break

        else:
            return entradaAlfabetica
        
        if controle:
            return entradaAlfabetica
        else:
            continue

def verificaData() -> str:

    while True:
    
        data = input("Insira a data no formato 'DD-MM-YYYY': ")

        # if (data):
        #     continue

        try:
            dataFormatada = datetime.strptime(data, '%d-%m-%Y').strftime('%Y-%m-%d')

            if (dataFormatada > datetime.now.strftime('%Y-%m-%d')):
                print("\nSó são aceitas datas iguais ou anteriores à data de hoje.")
                continue

            return dataFormatada
        
        except (ValueError, TypeError):
            print("\nO formato da entrada dada não é o adequado:  Use 'DD-MM-YYYY'.")

        except Exception as erro:
            print(f"\nFoi encontrado um {erro.__class__}. Forneça uma entrada válida.")