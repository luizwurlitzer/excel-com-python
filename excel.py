import pandas as pd


df = pd.DataFrame('C:/lab.xlsx', engine='xlsxwriter')


--------------------------

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(2.213,
4.426,
8.851,
17.7,
35.4,
70.81,
141.6,
283.8,
567.6,
1.135,
2.27,
4.541,
9.063
)
t2 = np.arange(0.5,
1,
2,
4,
8,
16,
32,
64,
128,
256,
512,
1024,
2048
)

#plt.figure(1)
#plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
