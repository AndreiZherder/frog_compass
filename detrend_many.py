import sys
import numpy as np
import csv
import matplotlib.pyplot as plt


def main():
    filename = 'data/1.txt'

    with open(filename, 'r', encoding='utf-8') as inf:
        reader = csv.reader(inf, dialect='excel-tab')
        header = next(reader)
        rows = list(reader)
        n = len(rows)
        m = len(rows[0])
        vs = [[] for i in range(m)]
        for j in range(m):
            for i in range(n):
                if rows[i][j]:
                    vs[j].append(float(rows[i][j].replace(',', '.')))
    v = np.array(vs[6])
    n = len(v)
    t = np.linspace(0, (n - 1), n)
    x = np.concatenate([t[:450], t[n - 450:]])
    y = np.concatenate([v[:450], v[n - 450:]])
    s = np.polynomial.polynomial.Polynomial.fit(x, y, 1).convert().coef
    k, b = s[1], s[0]
    trend = k * t + b
    v_detrended = v - trend
    with open(filename[:-4] + '_det.txt', 'w', encoding='utf-8') as ouf:
        for num in v_detrended:
            ouf.write(f'{num:.8f}\n')
    print(sys.version)
    print('Detrend done successfully!')

    fig, ax = plt.subplots()
    ax.plot(t, v, 'b')
    ax.plot(t, trend, 'r')
    ax.set_xlabel('time, s')
    ax.set_ylabel('voltage, V')
    ax.set_title('response')
    ax.grid()
    fig.show()

    fig, ax = plt.subplots()
    ax.plot(t, v_detrended, 'g')
    ax.set_xlabel('time, s')
    ax.set_ylabel('voltage, V')
    ax.set_title('response')
    ax.grid()
    fig.show()


if __name__ == '__main__':
    main()
