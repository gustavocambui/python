# esse código pretende somar os números de 0 a 100.

total = 0 # começamos declarando a variavél total
for num in range (101): # aqui o código determina a quantidade de vezes que ocorrerá o loop. enquanto num for menor que 101, ocorrerá.
    total = total + num # aqui total está dentro do loop e recebe seu valor + o valor de num
print(total)