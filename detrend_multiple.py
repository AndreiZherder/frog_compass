import sys
import numpy as np
import csv
# import matplotlib.pyplot as plt


def main():
    filename = './data/1.txt'
    output_file = filename[:-4] + '_det.txt'

    with open(filename, 'r', encoding='utf-8') as inf:
        reader = csv.reader(inf, dialect='excel-tab')
        headers = next(reader)
        rows = list(reader)
        n = len(rows)
        m = len(rows[0])
        vs = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if rows[j][i]:
                    vs[i].append(float(rows[j][i].replace(',', '.')))

    responses = []
    for v in vs:
        v = np.array(v)
        n = len(v)
        t = np.linspace(0, (n - 1), n)
        x = np.concatenate([t[:450], t[n - 450:]])
        y = np.concatenate([v[:450], v[n - 450:]])
        s = np.polynomial.polynomial.Polynomial.fit(x, y, 1).convert().coef
        k, b = s[1], s[0]
        trend = k * t + b
        response = v - trend
        responses.append(response)

    lines_number = max(len(response) for response in responses)
    with open(output_file, 'w', encoding='utf-8') as ouf:
        for header in headers:
            ouf.write(f'{header}\t')
        ouf.write('\n')
        for i in range(lines_number):
            for response in responses:
                if i < len(response):
                    ouf.write(f'{response[i]:.8f}\t')
                else:
                    ouf.write(f'\t')
            ouf.write('\n')

    print(sys.version)
    print('Detrend done successfully!')

    # fig, ax = plt.subplots()
    # ax.plot(t, v, 'b')
    # ax.plot(t, trend, 'r')
    # ax.set_xlabel('time, s')
    # ax.set_ylabel('voltage, V')
    # ax.set_title('response')
    # ax.grid()
    # fig.show()
    #
    # fig, ax = plt.subplots()
    # ax.plot(t, response, 'g')
    # ax.set_xlabel('time, s')
    # ax.set_ylabel('voltage, V')
    # ax.set_title('response')
    # ax.grid()
    # fig.show()


if __name__ == '__main__':
    main()
