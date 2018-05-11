2 assembly lines

            S1       S2       S3     S4
L1:


L2:


F(i,l): Optimal cost of doing tass[i+1:], assuming  task i was done in line


Introduction to algorithms - Cormen

F(i,l):

L1  =  Cost of doing tasks[i+1:]
 assuming task i was done in line l


F(i,l) = min ( F(i+1,l)  + cost( ))
