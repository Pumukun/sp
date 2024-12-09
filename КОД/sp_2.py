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
from random import randint



I = [1]
t_sob = [0]
Type = ['S_n(1)']
t_zh1 = [np.random.exponential(1/lamda)]
t_zh2 = [-1]
C = [[1, 0]]
t_ozh = [t_zh1[0]]
J_kzh = [1]
Gen_kzh = ['N']
J = [1]
Gen = ['N']
t_b = [0]
t_l = [t_zh1[0]]
t_d = [t_b[0] + t_l[0]]
Des1 = [-1]
Des2 = [-1]
for i in range(1, 100):
  I.append(i+1)
  t_sob.append(t_sob[i-1] + t_ozh[i-1])
  prob = randint(0, 1000) / 1000
  n_ob = t_d.index(t_sob[-1])
  if (Gen_kzh[-1] == 'N'):
    if (prob < pn_1): ##N0
      Type.append('S_n(1)')
      t_zh1.append(np.random.exponential(1/lamda))
      t_zh2.append(-1)
      C.append([C[-1][0], C[-1][1]])
      j = max(J) + 1
      Des1.append(-1)
      Des2.append(-1)
      J.append(j)
      Gen.append('N')
      t_b.append(t_sob[i])
      t_l.append(t_zh1[i])
      t_d.append(t_sob[i] + t_zh1[i])
      Des1[n_ob] = j
      Des2[n_ob] = -1
    if (prob > pn_1 and prob < pn_1 + pn_2): ##NN
      Type.append('S_n(2)')
      t_zh1.append(np.random.exponential(1/lamda))
      t_zh2.append(np.random.exponential(1/lamda))
      C.append([C[-1][0] + 1, C[-1][1]])
      if (t_zh1[-1] <= t_zh2[-1]):
        j1 = max(J) + 1
        J.append(j1)
        j2 = j1 + 1
        J.append(j2)
        t_l.append(t_zh1[-1])
        t_l.append(t_zh2[-1])
        t_d.append(t_sob[-1] + t_zh1[-1])
        t_d.append(t_sob[-1] + t_zh2[-1])
        Des1[n_ob] = j1
        Des2[n_ob] = j2
      else:
        j2 = max(J) + 1
        J.append(j2)
        j1 = j2 + 1
        J.append(j1)
        t_l.append(t_zh2[-1])
        t_l.append(t_zh1[-1])
        t_d.append(t_sob[-1] + t_zh2[-1])
        t_d.append(t_sob[-1] + t_zh1[-1])
        Des1[n_ob] = j2
        Des2[n_ob] = j1
      Des1.append(-1)
      Des1.append(-1)
      Des2.append(-1)
      Des2.append(-1)
      Gen.append('N')
      Gen.append('N')
      t_b.append(t_sob[-1])
      t_b.append(t_sob[-1])
    else: ##NM
      Type.append('S_n(3)')
      t_zh1.append(np.random.exponential(1/lamda))
      t_zh2.append(np.random.exponential(1/mu))
      C.append([C[-1][0], C[-1][1] + 1])
      if (t_zh1[-1] <= t_zh2[-1]):
        j1 = max(J) + 1
        J.append(j1)
        j2 = max(J) + 1
        J.append(j2)
        t_l.append(t_zh1[-1])
        t_l.append(t_zh2[-1])
        t_d.append(t_sob[-1] + t_zh1[-1])
        t_d.append(t_sob[-1] + t_zh2[-1])
        Des1[n_ob] = j1
        Des2[n_ob] = j2
        Gen.append('N')
        Gen.append('M')
      else:
        j2 = max(J) + 1
        J.append(j2)
        j1 = max(J) + 1
        J.append(j1)
        t_l.append(t_zh2[-1])
        t_l.append(t_zh1[-1])
        t_d.append(t_sob[-1] + t_zh2[-1])
        t_d.append(t_sob[-1] + t_zh1[-1])
        Des1[n_ob] = j2
        Des2[n_ob] = j1
        Gen.append('M')
        Gen.append('N')
      Des1.append(-1)
      Des1.append(-1)
      Des2.append(-1)
      Des2.append(-1)
      t_b.append(t_sob[-1])
      t_b.append(t_sob[-1])
  else:
    if (prob < pm_0):##00
      Type.append('S_m(0)')
      t_zh1.append(-1)
      t_zh2.append(-1)
      C.append([C[-1][0], C[-1][1] - 1])
    if (prob > pm_0 and prob < (pm_0 + pm_1)):##M0
      Type.append('S_m(1)')
      t_zh1.append(np.random.exponential(1/mu))
      t_zh2.append(-1)
      C.append([C[-1][0], C[-1][1]])
      j = max(J) + 1
      Des1.append(-1)
      Des2.append(-1)
      J.append(j)
      Gen.append('M')
      t_b.append(t_sob[-1])
      t_l.append(t_zh1[-1])
      t_d.append(t_sob[-1] + t_zh1[-1])
      Des1[n_ob] = j
      Des2[n_ob] = -1
    else:##MN
      Type.append('S_m(2)')
      t_zh1.append(np.random.exponential(1/lamda))
      t_zh2.append(np.random.exponential(1/mu))
      C.append([C[-1][0] + 1, C[-1][1]])
      if (t_zh1[-1] <= t_zh2[-1]):
        j1 = max(J) + 1
        J.append(j1)
        j2 = max(J) + 1
        J.append(j2)
        t_l.append(t_zh1[-1])
        t_l.append(t_zh2[-1])
        t_d.append(t_sob[-1] + t_zh1[-1])
        t_d.append(t_sob[-1] + t_zh2[-1])
        Des1[n_ob] = j1
        Des2[n_ob] = j2
        Gen.append('N')
        Gen.append('M')
      else:
        j2 = max(J) + 1
        J.append(j2)
        j1 = max(J) + 1
        J.append(j1)
        t_l.append(t_zh2[-1])
        t_l.append(t_zh1[-1])
        t_d.append(t_sob[-1] + t_zh2[-1])
        t_d.append(t_sob[-1] + t_zh1[-1])
        Des1[n_ob] = j2
        Des2[n_ob] = j1
        Gen.append('M')
        Gen.append('N')
      Des1.append(-1)
      Des1.append(-1)
      Des2.append(-1)
      Des2.append(-1)
      t_b.append(t_sob[-1])
      t_b.append(t_sob[-1])
  t_ozh.append(1000000)
  for k in t_d:
    if (k > t_sob[-1] and k < t_ozh[-1]):
      t_ozh[-1] = k
  J_kzh.append(J[t_d.index(t_ozh[-1])])
  Gen_kzh.append(Gen[t_d.index(t_ozh[-1])])
  t_ozh[-1] = t_ozh[-1] - t_sob[-1]

#print(I)
#print(t_sob)
#print(Type)
#print(t_zh1)
#print(t_zh2)
#print(C) # > 0
#print(t_ozh)
#print(J_kzh)
#print(Gen_kzh)

print("I;t_sob;Type;t_zh1;t_zh2;C;t_ozh;J_kzh;Gen_kzh")
for i in range(100):
  print(f"{I[i]};{t_sob[i]};{Type[i]};{t_zh1[i]};{t_zh2[i]};({C[i][0]}, {C[i][1]});{t_ozh[i]};{J_kzh[i]};{Gen_kzh[i]}")

#print(J)
#print(Gen)
#print(t_b)
#print(t_l) # > 0
#print(t_d)
#print(Des1)
#print(Des2)

print("J;Gen;t_b;t_l;t_d;Des1;Des2")
for i in range(100):
  print(f"{J[i]};{Gen[i]};{t_b[i]};{t_l[i]};{t_d[i]};{Des1[i]};{Des2[i]}")

Type_old = Type
Type = Type[0:100]
for i in ['S_n(1)', 'S_n(2)', 'S_n(3)', 'S_m(0)', 'S_m(1)', 'S_m(2)']:
  print(Type.count(i))
print(len(Type))

# 4.2
print(Gen.count('N'))
print(Gen.count('M'))

# N - S_n(1,2,3)
# M - S_m(1,2,3)

sost = []
cnt = []
time = []
for i in range(99):
  if C[i] not in sost:
    sost.append(C[i])
    cnt.append(1)
    time.append(t_sob[i+1] - t_sob[i])
  else:
    cnt[sost.index(C[i])] += 1
    time[sost.index(C[i])] += (t_sob[i+1] - t_sob[i])

print("№;Состояние;N_сост;%nu_сост;T_сост;%DELTA_сост")

for i in range(len(sost)):
  print(f"{i};({sost[i][0]}, {sost[i][1]});{cnt[i]};{cnt[i] / 100};{time[i]};{round(time[i] / t_sob[-1], 5)}")

for i in cnt:
  print(i / 100)

for i in time:
  print(round(i / t_sob[-1], 5))

print(time)

for i in range(len(sost)):
    print(sost[i][1])
