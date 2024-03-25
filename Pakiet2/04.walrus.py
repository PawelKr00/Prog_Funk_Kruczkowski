lista = [1,2,3,4,5,6,7]

lista_kwadratow = [x for i in lista if (x := i * i) > 10]

print(lista_kwadratow)