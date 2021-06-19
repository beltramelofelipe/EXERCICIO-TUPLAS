num = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoite', 'dezenove', 'vinte')

while True:
  a = int(input('Digite um número entre 0 a 20: '))
  if a >= 0 and a <= 20:
    break
  print('Tente novamente. ', end = '')
print(f'você digitou {num[a]}')
 
   
