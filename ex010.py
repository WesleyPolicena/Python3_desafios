saldo = float(input('Qual o seu saldo? '))
doll = saldo / 4.91
euro = saldo / 5.30

print('Com este saldo de R${:.2f}, você pode comprar US{:.2f}$ ou EU{:.2f}€'.format(saldo, doll, euro))
