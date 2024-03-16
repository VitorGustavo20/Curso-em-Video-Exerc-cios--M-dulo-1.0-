'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é a sua altura? (M) '))
IMC = peso / ( altura ** 2 )

print(f'Seu IMC é de {IMC:.2f}.')

if IMC < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO.')
elif 18.5 <= IMC < 25:
    print('VOCÊ TEM O PESO IDEAL.')
elif 25 <= IMC < 30:
    print('VOCÊ ESTÁ EM SOBREPESO.')
elif 30 <= IMC < 40:
    print('VOCÊ ESTÁ EM OBESIDADE.')
else:
    print('VOCÊ ESTÁ EM OBOESIDADE MÓRBIDA.')