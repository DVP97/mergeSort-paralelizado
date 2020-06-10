from multiprocessing import Pool
import time
from random import randint
import multiprocessing

def main():
    n_exp=21835672
    arr= []        # Array que contendrá los números aleatorios
    for a in range(0, n_exp):           # Generamos ints aleatorios y los inserta en arr hasta que contenga 21835672 elementos
        b = randint(1,1000000)          # Generación de un int random entre 1 y 1000000
        arr.insert(a,b)                # Insertamos el número generado en arr
    print('Array aleatoria creada.')
    print('Comenzando mergeSort paralelizado')
    n = multiprocessing.cpu_count()
    ini = time.time()
    arr = mergeSortParallel(arr, n) # comienza el mergeSort para arr
    fin = time.time() - ini

    print('Tiempo transcurrido: %f sec' %fin)
    print('\n+ Array final ordenada mediante mergeSort por paralelización en función de cores de la maquina:',arr)
    ime.sleep(5) # Pausa para apreciar la ejecución del programa
# REVISADO Y FINALIZADO
    

def merge(left, right):
    # se compara progresivamente cada array de tamaño 1 ordenando de menor a mayor todos los elementos
    ret = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1
    if li == len(left):
        ret.extend(right[ri:])
    else:
        ret.extend(left[li:])
    return ret

def mergesort(arr):
    # funcion recursiva para dividir el array "arr" original hasta descomponerlo en arrays de tamaño 1
    if len(arr) <= 1:
        return arr
    ind = len(arr)//2
    return merge(mergesort(arr[:ind]), mergesort(arr[ind:]))

def mergeWrap(AandB):
    a,b = AandB
    return merge(a,b)

def mergeSortParallel(arr, n):
    # funcion para realizar en paralelo el mergeSort en funcion de los cores
    endpoints = [int(x) for x in linspace(0, len(arr), n+1)]
    args = [arr[endpoints[i]:endpoints[i+1]] for i in range(n)]

    pool = Pool(processes = n)
    sublistas = pool.map(mergesort, args)

    while len(sublistas) > 1:
        args = [(sublistas[i], sublistas[i+1]) \
				for i in range(0, len(sublistas), 2)]
        sublistas = pool.map(mergeWrap, args)

    return sublistas[0]
     
def linspace(a,b,nsteps):

    ssize = float(b-a)/(nsteps-1)
    return [a + i*ssize for i in range(nsteps)]

if __name__ == '__main__':  # protección para que no se ejecute de nuevo un proceso cuando ya está en ejecución
    main()
