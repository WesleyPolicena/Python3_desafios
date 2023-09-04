m = float(input('Informe a distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {:.2f}km corresponde a;'.format(m))
print('{:.2f}km'.format(km))
print('{:.2f}hm'.format(hm))
print('{:.2f}dam'.format(dam))
print('{:.2f}dm'.format(dm))
print('{:.2f}cm'.format(cm))
print('{:.2f}mm'.format(mm))
