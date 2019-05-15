def cargarListas():
    return [x.split() for x in open("lista.txt").readlines()]

def mostrarLista(lista,n):
    print(cargarListas()[i][0], "", cargarListas()[i][0].count("1"))

if __name__ == '__main__':
    for i in range(0,len(cargarListas())):
        mostrarLista(cargarListas()[i],i)

