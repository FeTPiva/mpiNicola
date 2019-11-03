import contagem
import re
import string
from mpi4py import MPI
#http://ccom.uprrp.edu/~jortiz/cpath/mpi.html#(19)
#https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html
#https://mpi4py.readthedocs.io/en/stable/tutorial.html
#https://www.howtoforge.com/tutorial/distributed-parallel-programming-python-mpi4py/

pronome = 'pronomes.txt'
absoluta = 'absoluta.txt'
triste = 'triste.txt'
#textoAnalisado = 'analisando.txt'

comm = MPI.COMM_WORLD   # Defines the default communicator
num_procs = comm.Get_size()  # Stores the number of processes in size.
rank = comm.Get_rank()  # Stores the rank (pid) of the current process
stat = MPI.Status()

#msg =  "Hello world, say process %s !" % rank


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
if rank == 0:
    fd = open("analisando.txt", "r")
    dna = fd.read()
else:
    dna = None

dna = comm.bcast(dna, root=0) 


#pronomes 
p = contagem.contandoCoisasPrint(dna, pronome)

#palavras absolutas 
a = contagem.contandoCoisasPrint(dna, absoluta)

#contagem triste 
t = contagem.contandoCoisasPrint(dna, triste)

'''

if rank == 0:
    # Master work
    print(p)
    for i in range(num_procs - 1):
        p = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=stat)
        print(p)
    
else:
    # Worker work
    comm.send(p, dest = 0)
    print('to no else ')

'''




teste = contagem.criaLista(p, a, t)

print(teste)