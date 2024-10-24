# Faça um sistema que leia a idade de uma pessoa expressa em anos e mostre-a expressa em meses e em dias.

print('Bem vindo ao nosso sistema, primeiro precisamos que digite sua idade: ')
idade = int(input()) #utilizo a função int pois a função input armazena dados em string 
idadeEmMeses = idade * 12
idadeEmDias = idade * 365

print('Você viveu ' + str(idadeEmMeses) + ' meses e ' + str(idadeEmDias) + ' dias.')