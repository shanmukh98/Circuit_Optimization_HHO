import random
from math import cos,exp
import subprocess
import os
import time
import numpy as np
from HHO import HHO
DELAY_MAX = 6.049812433e-12



def updateFront(swarm, oldFront):
    newFront = list()
    for i in range(len(oldFront)):
	for j in range(len(swarm)):
	    cost_n = list()
	    cost_n = func5(swarm[j].position_i)
	    if (cost_n[0] <= DELAY_MAX and cost_n[1] <= DELAY_MAX and cost_n[2] <= DELAY_MAX and cost_n[3] <= DELAY_MAX and cost_n[4] <= DELAY_MAX and cost_n[5] <= DELAY_MAX):
		cost_o = list()
		cost_o = func5(oldFront[i].position_i)
		if(cost_n[6] <= cost_o[6] and cost_n[7] <= cost_o[7] and cost_n[8] <= cost_o[8] and cost_n[9] <= cost_o[9] and cost_n[10] <= cost_o[10] and cost_n[11] <= cost_o[11] and cost_n[12] <= cost_o[12] and cost_n[13] <= cost_o[13]):
		    newFront.append(swarm[j])
    if len(newFront) == 0:
	return oldFront
    return newFront

def func5(ind):
    cost = list()
    delay = list()
    leakage = list()
    delay = dela(ind)
    leakage = leak(ind)
    cost.extend(delay)
    cost.extend(leakage)
    return cost

def leak(ind):
    with open('fa_leak_25,0.8.sp','r') as file:
        data=file.readlines()
        #data[188]='Mp1	nodez	nodea	vddd!	vddd!	pmos	w=' + str(ind[0]) + 'n ' + 'l=' + str(ind[1]) + 'n\n'
        data[34] = 'Mp1    1   nodea   vdd   vdd   pmos  l=' + str(ind[0]) + 'n ' + 'w=' + str(ind[1]) + 'n\n'
        data[35] = 'Mp2    1   nodeb   vdd   vdd   pmos  l=' + str(ind[2]) + 'n ' + 'w=' + str(ind[3]) + 'n\n'
        data[36] = 'Mp3    nodecon nodec   1   vdd   pmos l=' + str(ind[4]) + 'n ' + 'w=' + str(ind[5]) + 'n\n'
        data[37] = 'Mn1    5   nodea   gnd   gnd   nmos  l=' + str(ind[6]) + 'n ' + 'w=' + str(ind[7]) + 'n\n'
        data[38] = 'Mn2    5   nodeb   gnd   gnd   nmos  l=' + str(ind[8]) + 'n ' + 'w=' + str(ind[9]) + 'n\n'
        data[39] = 'Mn3    nodecon nodec   5   gnd   nmos l=' + str(ind[10]) + 'n ' + 'w=' + str(ind[11]) + 'n\n'
        data[40] = 'Mp4    4   nodea   vdd   vdd   pmos  l=' + str(ind[12]) + 'n ' + 'w=' + str(ind[13]) + 'n\n'
        data[41] = 'Mp5    nodecon nodeb   4   vdd   pmos  l=' + str(ind[14]) + 'n ' + 'w=' + str(ind[15]) + 'n\n'
        data[42] = 'Mn4    nodecon nodeb   node4   gnd   nmos l=' + str(ind[16]) + 'n ' + 'w=' + str(ind[17]) + 'n\n'
        data[43] = 'Mn5    node4   nodea   gnd   gnd   nmos l=' + str(ind[18]) + 'n ' + 'w=' + str(ind[19]) + 'n\n'
        data[44] = 'Mp6    2   nodea   vdd   vdd   pmos  l=' + str(ind[20]) + 'n ' + 'w=' + str(ind[21]) + 'n\n'
        data[45] = 'Mp7    2   nodeb   vdd   vdd   pmos l=' + str(ind[22]) + 'n ' + 'w=' + str(ind[23]) + 'n\n'
        data[46] = 'Mp8    2   nodec   vdd   vdd   pmos l=' + str(ind[24]) + 'n ' + 'w=' + str(ind[25]) + 'n\n'
        data[47] = 'Mp9    nodes0n nodecon 2   vdd   pmos l=' + str(ind[26]) + 'n ' + 'w=' + str(ind[27]) + 'n\n'
        data[48] = 'Mn6    3   nodea   gnd   gnd   nmos l=' + str(ind[28]) + 'n ' + 'w=' + str(ind[29]) + 'n\n'
        data[49] = 'Mn7    3   nodeb   gnd   gnd   nmos l=' + str(ind[30]) + 'n ' + 'w=' + str(ind[31]) + 'n\n'
        data[50] = 'Mn8    3   nodec   gnd   gnd   nmos l=' + str(ind[32]) + 'n ' + 'w=' + str(ind[33]) + 'n\n'
        data[51] = 'Mn9    nodes0n nodecon 3   gnd   nmos l=' + str(ind[34]) + 'n ' + 'w=' + str(ind[35]) + 'n\n'
        data[52] = 'Mp10   9   nodea   vdd   vdd   pmos  l=' + str(ind[36]) + 'n ' + 'w=' + str(ind[37]) + 'n\n'
        data[53] = 'Mp11   8   nodeb   9   vdd   pmos    l=' + str(ind[38]) + 'n ' + 'w=' + str(ind[39]) + 'n\n'
        data[54] = 'Mp12   nodes0n nodec   8   vdd   pmos l=' + str(ind[40]) + 'n ' + 'w=' + str(ind[41]) + 'n\n'
        data[55] = 'Mn10   7   nodea   gnd   gnd   nmos  l=' + str(ind[42]) + 'n ' + 'w=' + str(ind[43]) + 'n\n'
        data[56] = 'Mn11   6   nodeb   7   gnd   nmos    l=' + str(ind[44]) + 'n ' + 'w=' + str(ind[45]) + 'n\n'
        data[57] = 'Mn12   nodes0n nodec   6   gnd   nmos  l=' + str(ind[46]) + 'n ' + 'w=' + str(ind[47]) + 'n\n'
        data[58] = 'Mp13   nodeco  nodecon vdd   vdd   pmos l=' + str(ind[48]) + 'n ' + 'w=' + str(ind[49]) + 'n\n'
        data[59] = 'Mn13   nodeco  nodecon gnd   gnd   nmos l=' + str(ind[50]) + 'n ' + 'w=' + str(ind[51]) + 'n\n'
        data[60] = 'Mp14   nodes0  nodes0n vdd   vdd   pmos l=' + str(ind[52]) + 'n ' + 'w=' + str(ind[53]) + 'n\n'
        data[61] = 'Mn14   nodes0  nodes0n gnd   gnd   nmos  l=' + str(ind[54]) + 'n ' + 'w=' + str(ind[55]) + 'n\n'        


    with open('test_leak.sp','w') as file:
         file.writelines(data)

    from subprocess import call
    call(["hspice", "test_leak.sp","-mt","6"])

    with open('test_leak.ms0','r') as file:
         data=file.readlines()


    final_list=list()
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[14].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[21].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[28].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[35].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[42].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[49].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[56].split()])
    final_list.append(list_of_elements[0])
    list_of_elements=list()
    list_of_elements.extend([float(x) for x in data[63].split()])
    final_list.append(list_of_elements[0])
    return final_list
	
def dela(ind):
    with open('fa_del_25,0.8.sp','r') as file:
        data=file.readlines()
        #data[206]='Mp1	nodez	nodea	vddd!	vddd!	pmos	w=' + str(ind[0]) + 'n ' + 'l=' + str(ind[1]) + 'n\n'
        data[34] = 'Mp1    1   nodea   vdd   vdd   pmos  l=' + str(ind[0]) + 'n ' + 'w=' + str(ind[1]) + 'n\n'
        data[35] = 'Mp2    1   nodeb   vdd   vdd   pmos  l=' + str(ind[2]) + 'n ' + 'w=' + str(ind[3]) + 'n\n'
        data[36] = 'Mp3    nodecon nodec   1   vdd   pmos l=' + str(ind[4]) + 'n ' + 'w=' + str(ind[5]) + 'n\n'
        data[37] = 'Mn1    5   nodea   gnd   gnd   nmos  l=' + str(ind[6]) + 'n ' + 'w=' + str(ind[7]) + 'n\n'
        data[38] = 'Mn2    5   nodeb   gnd   gnd   nmos  l=' + str(ind[8]) + 'n ' + 'w=' + str(ind[9]) + 'n\n'
        data[39] = 'Mn3    nodecon nodec   5   gnd   nmos l=' + str(ind[10]) + 'n ' + 'w=' + str(ind[11]) + 'n\n'
        data[40] = 'Mp4    4   nodea   vdd   vdd   pmos  l=' + str(ind[12]) + 'n ' + 'w=' + str(ind[13]) + 'n\n'
        data[41] = 'Mp5    nodecon nodeb   4   vdd   pmos  l=' + str(ind[14]) + 'n ' + 'w=' + str(ind[15]) + 'n\n'
        data[42] = 'Mn4    nodecon nodeb   node4   gnd   nmos l=' + str(ind[16]) + 'n ' + 'w=' + str(ind[17]) + 'n\n'
        data[43] = 'Mn5    node4   nodea   gnd   gnd   nmos l=' + str(ind[18]) + 'n ' + 'w=' + str(ind[19]) + 'n\n'
        data[44] = 'Mp6    2   nodea   vdd   vdd   pmos  l=' + str(ind[20]) + 'n ' + 'w=' + str(ind[21]) + 'n\n'
        data[45] = 'Mp7    2   nodeb   vdd   vdd   pmos l=' + str(ind[22]) + 'n ' + 'w=' + str(ind[23]) + 'n\n'
        data[46] = 'Mp8    2   nodec   vdd   vdd   pmos l=' + str(ind[24]) + 'n ' + 'w=' + str(ind[25]) + 'n\n'
        data[47] = 'Mp9    nodes0n nodecon 2   vdd   pmos l=' + str(ind[26]) + 'n ' + 'w=' + str(ind[27]) + 'n\n'
        data[48] = 'Mn6    3   nodea   gnd   gnd   nmos l=' + str(ind[28]) + 'n ' + 'w=' + str(ind[29]) + 'n\n'
        data[49] = 'Mn7    3   nodeb   gnd   gnd   nmos l=' + str(ind[30]) + 'n ' + 'w=' + str(ind[31]) + 'n\n'
        data[50] = 'Mn8    3   nodec   gnd   gnd   nmos l=' + str(ind[32]) + 'n ' + 'w=' + str(ind[33]) + 'n\n'
        data[51] = 'Mn9    nodes0n nodecon 3   gnd   nmos l=' + str(ind[34]) + 'n ' + 'w=' + str(ind[35]) + 'n\n'
        data[52] = 'Mp10   9   nodea   vdd   vdd   pmos  l=' + str(ind[36]) + 'n ' + 'w=' + str(ind[37]) + 'n\n'
        data[53] = 'Mp11   8   nodeb   9   vdd   pmos    l=' + str(ind[38]) + 'n ' + 'w=' + str(ind[39]) + 'n\n'
        data[54] = 'Mp12   nodes0n nodec   8   vdd   pmos l=' + str(ind[40]) + 'n ' + 'w=' + str(ind[41]) + 'n\n'
        data[55] = 'Mn10   7   nodea   gnd   gnd   nmos  l=' + str(ind[42]) + 'n ' + 'w=' + str(ind[43]) + 'n\n'
        data[56] = 'Mn11   6   nodeb   7   gnd   nmos    l=' + str(ind[44]) + 'n ' + 'w=' + str(ind[45]) + 'n\n'
        data[57] = 'Mn12   nodes0n nodec   6   gnd   nmos  l=' + str(ind[46]) + 'n ' + 'w=' + str(ind[47]) + 'n\n'
        data[58] = 'Mp13   nodeco  nodecon vdd   vdd   pmos l=' + str(ind[48]) + 'n ' + 'w=' + str(ind[49]) + 'n\n'
        data[59] = 'Mn13   nodeco  nodecon gnd   gnd   nmos l=' + str(ind[50]) + 'n ' + 'w=' + str(ind[51]) + 'n\n'
        data[60] = 'Mp14   nodes0  nodes0n vdd   vdd   pmos l=' + str(ind[52]) + 'n ' + 'w=' + str(ind[53]) + 'n\n'
        data[61] = 'Mn14   nodes0  nodes0n gnd   gnd   nmos  l=' + str(ind[54]) + 'n ' + 'w=' + str(ind[55]) + 'n\n'

    print("PRINTING DATA", data)

    with open('test_delays.sp','w')as file:
        file.writelines(data)

    from subprocess import call
    call(["hspice","test_delays.sp","-mt","6"])

    with open('test_delays.mt0','r') as file:
        data=file.readlines()
    final_list=list()
    final_list.extend([float(x) for x in data[4].split()])
    tp = data[5].split()
    final_list.append(float(tp[0]))
    final_list.append(float(tp[1]))
    return final_list

p1 =[  22.        ,  375.17834589,   22.        ,  326.78948823,
         22.        ,  289.44224125,   22.        ,  658.03736161,
         22.        ,  197.34783652,   22.        ,  161.86961581,
         22.        ,  512.97321667,   22.        ,  286.1264645 ,
         22.        ,  101.72225615,   22.        ,  538.79812629,
         22.        ,  101.72225615,   22.        ,  101.72225615,
         22.        ,  111.77744152,   22.        ,  101.72225615,
         22.        ,  499.69512915,   22.        ,  109.45785457,
         22.        ,  214.18530547,   22.        ,  121.97610806,
         22.        ,  695.66668798,   22.        ,  410.67930954,
         22.        ,  179.36333952,   22.        ,  468.85036846,
         22.        ,  101.72225615,   22.        ,  196.35750991,
         22.        ,  144.35457928,   22.        ,  205.28652764,
         22.        ,  101.72225615,   22.        ,  101.72225615]
p2 = [  22.        ,  218.01856702,   22.        ,  205.34637683,
         22.        ,  217.13048908,   22.        ,  100.        ,
         22.        ,  100.        ,   22.        ,  186.71781725,
         22.        ,  215.53234749,   22.        ,  215.09689703,
         22.        ,  220.95831162,   22.        ,  100.        ,
         22.        ,  216.19122122,   22.        ,  212.24112744,
         22.        ,  211.99621844,   22.        ,  100.26733519,
         22.        ,  217.32149945,   22.        ,  100.        ,
         22.        ,  100.        ,   22.        ,  212.21531182,
         22.        ,  100.        ,   22.        ,  220.06644106,
         22.        ,  100.        ,   22.        ,  100.        ,
         22.        ,  100.        ,   22.        ,  210.61421434,
         22.        ,  100.        ,   22.        ,  100.        ,
         22.        ,  206.25968188,   22.        ,  208.19979901]
d1 = dela(p1)
d2 = dela(p2)
l1 = leak(p1)
l2 = leak(p2)
print d1,d2,l1,l2
exit(0)
def obj(param):
    try:
        delay = max(dela(param))
        # leakage = sum(leak(param))
    except:
        return 10
    return np.log10(delay)	


# print "delay"
# print dela([
# 22,352,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,176,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,352,
# 22,352,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,176,
# 22,176,
# 22,528,
# 22,528,
# 22,528,
# 22,264,
# 22,264,
# 22,264,
# 22,352,
# 22,176,
# 22,352,
# 22,176
# ])
#weighted sum by assigning multiplying 1/2 to them;
class objective():
    def __init__(self,c):
        self.c = c
    def obj(self,param):
        try:
            delay = max(dela(param))
            leakage = sum(leak(param))
        except:
            return 100
        return (np.log10(delay)*self.c)+((1-self.c)*np.log10(leakage))

# print obj([
# 22,352,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,176,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,352,
# 22,352,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,176,
# 22,176,
# 22,528,
# 22,528,
# 22,528,
# 22,264,
# 22,264,
# 22,264,
# 22,352,
# 22,176,
# 22,352,
# 22,176
# ])



lb = [
22,100,
22,100,
22,100,
22,100,
22,100,
22,100,
22,100,
22,100,22,100,
22,100,
22,100,
22,100,22,100,
22,100,
22,100,
22,100,22,100,
22,100,
22,100,
22,100,22,100,
22,100,
22,100,
22,100,22,100,
22,100,
22,100,
22,100
]
ub = [
28,1500,
28,1500,
28,1500,
28,1500,
28,1500,
28,1500,
28,1500,
28,1500,28,1500,
28,1500,
28,1500,
28,1500,28,1500,
28,1500,
28,1500,
28,1500,28,1500,
28,1500,
28,1500,
28,1500,28,1500,
28,1500,
28,1500,
28,1500,28,1500,
28,1500,
28,1500,
28,1500
]
population = 100
iterations = 60
dim = len(lb)
history = []
import pickle

i=0

objec = objective(1-1/(3**i))
out = HHO(objec.obj,np.asarray(lb),np.asarray(ub),dim,population,iterations)
history.append(out)
with open("test_"+str(i)+".txt", "wb") as fp:
    pickle.dump(history, fp)


# out = HHO(obj,np.asarray(lb),np.asarray(ub),dim,population,iterations)
# print out.bestIndividual
# print out.best
# print (obj([
# 22,352,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,176,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,352,
# 22,352,
# 22,352,
# 22,352,
# 22,176,
# 22,176,
# 22,176,
# 22,176,
# 22,528,
# 22,528,
# 22,528,
# 22,264,
# 22,264,
# 22,264,
# 22,352,
# 22,176,
# 22,352,
# 22,176
# ]))
# def func3(ind):
#     return 0.5 * (float(func1(ind)) + float(func2(ind)))

# class Particle:
#     def __init__(self,pp):
#         self.pos_best_i=list()
#         self.position_i=list()
#         self.err_i=list()
#         self.err_best_i=list()
#         self.density_i=list()

#         for i in xrange(0,num_dim):
#             self.density_i.append(random.uniform(-1,1))
#             self.position_i.append(pp[i])

# #this is evaluating pareto function - similar to PSO

#     def evalPareto(self, costFunc):
# 	self.err_i = costFunc(self.position_i)
# 	if len(self.err_best_i) == 0:
# 	    self.pos_best_i = self.position_i
# 	    self.err_best_i = self.err_i
# 	else:
# 	    flag = 0
# 	    for i in range(0, 6):
# 		if(self.err_i[i] > DELAY_MAX):
# 		    flag = 1
# 	    for i in range(6, 14):
# 		if(self.err_i[i] > self.err_best_i[i]):
# 		    flag = 1
# 	    if flag == 0:
# 		self.pos_best_i = self.position_i
# 		self.err_best_i = self.err_i

# #updating the density of parcular edge/particle
#     def upd_density(self,pos_best_g):
#         w=0.5
#         c1=1
#         c2=2
#         for i in xrange(0,num_dim):
#             print ("=========================================", self.pos_best_i[i])
#             r1=random.random()
#             r2=random.random()
#             D1=c1*r1*(self.pos_best_i[i] - self.position_i[i])
#             D2=c2*r2*(pos_best_g[i]-self.position_i[i])
#             self.density_i[i]=w*self.density_i[i]+D1+D2
#             print("++++++++++++++++++++++",self.density_i[i])

# #updating the postion of best results - till now which part has greater density 

#     def upd_pos(self,bounds):
#         for i in range(0,num_dim):
#             self.position_i[i]=self.position_i[i]+self.density_i[i]

#             if self.position_i[i]>bounds[i][1]:
#                 self.position_i[i]=bounds[i][1]

#             if self.position_i[i] < bounds[i][0]:
#                 self.position_i[i]=bounds[i][0]
#             print("@@@@@@@@@@@@@@@@@@@", self.position_i[i])

# class swarm_AI():
#     def __init__(self,costFunc,pp,bounds,totpar,maxiter):
#         global num_dim
#         swarm=list()
#         num_dim=len(pp)
#         err_best_g=list()
#         pos_best_g=list()

#         for i in xrange(0,totpar):
#             swarm.append(Particle(pp))
#         for i in xrange(0, len(swarm)):
#             print (i, "--->>>>", swarm[i].pos_best_i)
#         i=0
# 	paretoFront = list()
# 	paretoFront = swarm
#         #mover is the ant which is moving in the direction of better results
# 	while i < maxiter:
# 	    print("ITERATION -", i)
#             for j in xrange(0,totpar):
#                 swarm[j].evalPareto(costFunc)
# 	    mover = random.randint(0, len(swarm) - 1)

# 	    err_best_g = func5(swarm[mover].position_i)
# 	    pos_best_g = swarm[mover].position_i

#             for j in xrange(0,totpar):
#                 swarm[j].upd_density(pos_best_g)
#                 swarm[j].upd_pos(bounds)
#             i+=1
# 	#this paretoFront is updated to obtain the optimized results
# 	    paretoFront = updateFront(swarm, paretoFront)

#         print('OUTPUT')
#         print (pos_best_g)

# wp1=132
# lp1=22
# wp2=132
# lp2=22
# wp3=132
# lp3=22
# wn1=132
# ln1=22
# wn2=132
# ln2=22
# wn3=132
# ln3=22
# #initial=[float(wp),float(wn), float(lp), float(ln)]
# print(wp1, lp1, wp2, lp2, wp3, lp3, wn1, ln1, wn2, ln2, wn3, ln3)
# initial=[float(wp1), float(lp1), float(wp2),float(lp2), float(wp3), float(lp3), float(wn1), float(ln1), float(wn2), float(ln2), float(wn3), float(ln3)]
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",initial)
# #exit()
# bounds=[(90, 1500), (22, 25), (90, 1500), (22, 25), (90, 1500), (22, 25), (90, 1500), (22, 25), (90, 1500), (22, 25), (90, 1500), (22, 25)]

# no_of_ants =20
# no_of_iterations =200

# swarm_AI(func5,initial,bounds,totpar=no_of_ants,maxiter=no_of_iterations)

