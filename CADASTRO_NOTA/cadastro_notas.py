import pandas as pd
from datetime import datetime

ARQUIVO_CSV = "notas_3B1.csv"

while True:
    print("\n1. Cadastrar aluno")
    print("2. Listar notas")
    print("3. Salvar e sair")

    opcao = input("Opcao: ")

    if opcao == "1":
       nome = input("Nome do aluno: ")
       nota = float(input("Nota (0 a 10): "))
       horario = datetime.now().strftime("%d/%m/%Y %H:%M")

    nova_linha = pd.DataFrame([{
        "Aluno": nome,
        "Nota": nota,
        "Data_Cadastro": horario
    }])

    try:
            df = pd.read_csv(ARQUIVO_CSV)
            df = pd.concat([df, nova_linha], ignore_index=True)
    except FileNotFoundError:
            df = nova_linha

 elif opcao == "2":
        try:
            df = pd.read_csv(ARQUIVO_CSV)
            print(df.to_string(index=False))
        except FileNotFoundError:
            print("Nenhum aluno cadastrado ainda.")

  elif opcao == "3":
        df.to_csv(ARQUIVO_CSV, index=False)
        print("Dados salvos.")
        break