from Tkinter import *
import math
import random
#Chromosomes are 4 bits long
L_chromosome=32
N_chains=2**L_chromosome
#Lower and upper limits of search space
a=-5.12
b=5.12
crossover_point=L_chromosome/2


def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.1:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome

#Number of chromosomes
N_chromosomes=10
#probability of mutation
prob_m=0.5

F0=[]
fitness_values=[]

for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)

#binary codification
def decode_chromosome(chromosome):
    global L_chromosome,N_chains,a,b
    value=0
    value2 = 0
    for p in range(L_chromosome / 2):
        value+=(2**p)*chromosome[-1-p]
    for p in xrange(L_chromosome / 2, L_chromosome):
        value2 += (2 ** p) * chromosome[-1-p]

    return (a + (b - a) * float(value) / (N_chains - 1), a + (b - a) * float(value2) / (N_chains - 1))


def f(x, y):
     return ((20.0) + ((x ** 2) - (10.0 * (math.cos((2.0 * math.pi) * x)))) + ((y ** 2) - (10.0 * (math.cos((2.0 * math.pi) * y)))))



def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        v1, v2 = decode_chromosome(F0[p])
        fitness_values[p]=f(v1, v2)
        

def compare_chromosomes(chromosome1,chromosome2):
    vc1x, vc1y = decode_chromosome(chromosome1)
    vc2x , vc2y = decode_chromosome(chromosome2)
    fvc1 = f(vc1x, vc1y)
    fvc2 = f(vc2x, vc2y)
    if fvc1 > fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1


suma=float(N_chromosomes*(N_chromosomes+1))/2.

Lwheel=N_chromosomes*10

def create_wheel():
    global F0,fitness_values

    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        acc+=maxv-fitness_values[p]
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel
##    print fraction
    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2
##    print fraction

    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
        
F1=F0[:]
contador = 0
def nextgeneration():
    global contador
    print contador
    contador += 1
    F0.sort(cmp=compare_chromosomes)
    print "Best solution so far:"
    x, y = decode_chromosome(F0[0])
    print "f(",decode_chromosome(F0[0]),")= ", f(x, y)
                                                                    
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    for i in range(0,(N_chromosomes-2)/2):
        roulette=create_wheel()
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    #The generation replaces the old one
    F0[:]=F1[:]

F0.sort(cmp=compare_chromosomes)
evaluate_chromosomes()

for i in xrange(100):
    nextgeneration()