V=90
p=0
q=0.349
lamda=0.813
mu=1.105
pn_1=0.319
pn_2=0.470
pm_0=0.494
pm_1=0.252

import numpy as np

P1 = np.array([
    [0,     0.349, 0.651,    0, 0,  0],
    [0.349, 0,     0.651,    0, 0,  0],
    [0.349, 0.651, 0, 0,     0,     0],
    [0.349, 0,     0, 0,     0.651, 0],
    [0.349, 0,     0, 0.651, 0,     0],
    [0,     0.349, 0, 0.651, 0,     0],
           ])

print("matrix{")
for i in P1:
    print(f"    {i[0]} # {i[1]} # {i[2]} # {i[3]} # {i[4]} # {i[5]} ##")
print("}")

P_list = [P1]
for i in range(1, 16):
  P_list.append(np.dot(P1, P_list[i-1]))

def mlatex(m):
    print("left (")
    print("matrix{")
    for i in m:
        s = []
        for value in i:
            if value == 0:
                s.append("0")
            else:
                s.append(f"{value:.5f}")
        print("    " + " # ".join(s) + " ##")
    print("}")
    print("right )")

#for i in P_list:
#  print(round(np.amax(i), 5))

for i in range (7, 16):
    print(i)
    print(mlatex(P_list[i]))
