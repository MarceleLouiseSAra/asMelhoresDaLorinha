import sqlite3

print("\nOlha nós outra vez no ar!")

def main():

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        print("\nentrei na main!")

        while True:

            teste = int(input("insira 1 ou 2"))

            if (teste==1):
                print("\noutra iteração do loop")
                continue
            
            else: 
                print("\nloop exited")
                break

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()