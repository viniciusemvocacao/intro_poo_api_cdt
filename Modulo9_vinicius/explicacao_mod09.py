def aula_tratamento_erro():
   
 try:
   
   numerador = int(input("Digita o numerador"))
   denominador = int(input("Digita o denominador:"))
   resultado = numerador / denominador

 except ValueError:
   
   print("Erro: Digita apenas o números inteiros!")
 except ZeroDivisionError:
   print ("Erro: não podes dividir por zero.")
 except Exception as erro:
   print(f"Erro inesperado:{erro}")
 else:
   print(f"Sucesso! Resultado: {resultado}")
 finally:
   print("---Fim da divisão---")

aula_tratamento_erro()