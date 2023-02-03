codigos = {1: 4.00 , 2: 4.50 , 3: 5.00 , 4: 2.00 , 5: 1.5 }
codigo, qtd = map(int, input().split())
total = codigos[codigo] * qtd
print('Total: R$ {:.2f}'.format(total))
