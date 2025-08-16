def verificaEntradaNumérica():
    
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

def verificaEntradaAlfabetica():
    
    while True:
        
        entradaAlfabetica = input()

        if not(entradaAlfabetica.isalpha()):
            
            for caractere in range(len(entradaAlfabetica)):
                if entradaAlfabetica[caractere].isalpha() or entradaAlfabetica[caractere].isspace() or entradaAlfabetica[caractere].isdigit():
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