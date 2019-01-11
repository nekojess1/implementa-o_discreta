def code_isbn():
	code=input('Digite os 12 primeiros dígitos do código ISBN a ser gerado o dígito verificador:\n')
	posições_impares=0
	posições_pares=0
	quantificador=1
	for x in range(len(code)):
		if quantificador%2==0:
			posições_pares+=(int(code[x]))*3
		elif quantificador%2==1:
		    posições_impares+=(int(code[x]))
		quantificador+=1
	calculo=(posições_impares+posições_pares)%10
	resultado=10-calculo
	print('O dígito verificador é: {}'.format(resultado))


code_isbn()

