while True:
   print("__ Calculadora __\n" 
   "1- Somar \n"
   "2- Subtrair \n"
   "3- Multiplicar \n"
   "4- Sair \n")
   opcao = int(input("Escolha uma opção: "))
   if opcao == 4:
      print("Encerrando calculadora...")
      break
   if opcao == 1:
      print("Você escolheu Somar")
      break
   elif opcao == 2: 
      print("Você escolheu Subtrair")   
      break
   elif opcao == 3:
      print("Você escolheu Multiplicar:")
      break
   else:
      print("Opção inválida!")