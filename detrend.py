import sys
from os import listdir
from pathlib import Path
import numpy as np
# import matplotlib.pyplot as plt

input_dir = './raw/'
output_dir = './detrended/'
filenames = [f for f in listdir(input_dir) if Path(input_dir + f).is_file()]
Path(output_dir).mkdir(parents=True, exist_ok=True)
for f in Path(output_dir).glob('*.*'):
    f.unlink()

for filename in filenames:
    with open(input_dir + filename, 'r', encoding='utf-8') as inf:
        v = [float(_.replace(',', '.')) for _ in inf.readlines()]
    n = len(v)
    v = np.array(v)
    t = np.linspace(0, (n - 1), n)
    x = np.concatenate([t[19:90], t[n - 50:n]])
    y = np.concatenate([v[19:90], v[n - 50:n]])
    s = np.polynomial.polynomial.Polynomial.fit(x, y, 1).convert().coef
    k, b = s[1], s[0]
    trend = k * t + b
    v_detrended = v - trend
    with open(output_dir + filename + '.asc', 'w', encoding='utf-8') as ouf:
        ouf.write(f'{filename}.asc\n')
        for _ in v_detrended:
            ouf.write(f'{_:.8f}\n')
print(sys.version)
print('Detrend done successfully!')

# fig, ax = plt.subplots()
# ax.plot(t, v, 'b')
# ax.plot(t, trend, 'r')
# ax.set_xlabel('time, s')
# ax.set_ylabel('voltage, V')
# ax.set_title('Frog retina response')
# ax.grid()
# fig.show()

# fig, ax = plt.subplots()
# ax.plot(t, v_detrended, 'g')
# ax.set_xlabel('time, s')
# ax.set_ylabel('voltage, V')
# ax.set_title('Frog retina response')
# ax.grid()
# fig.show()
# input('Press Enter...')
