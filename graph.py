import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

k = 1.38e-23
e = 1.62e-19

sheet_names = ["Yellow LED", "Red LED", "White LED", "Solar Battery"]
n = [-8, -9, -8]
datasets = []
text_loc2 = [[(0.3, -8), (1.3, 0)],[(0.5, -8.5), (1.4, 0)], [(0.5, -8), (2.5, 3)]]
text_loc1 = [(1.5, 6), (1.4, 8), (2, 20), (0.8, 12)]
for sheet_number in range(4):
    datasets.append(pd.read_excel('./data.xlsx', sheet_name=sheet_number))
    plt.figure(sheet_number + 1, figsize=(12, 6))
    plt.suptitle(sheet_names[sheet_number])
    plt.subplot(1, 3, 1)
    plt.plot(datasets[sheet_number]['V'], datasets[sheet_number]['I'], marker='x')
    fp = np.polyfit(datasets[sheet_number]['V'][-4:], datasets[sheet_number]['I'][-4:], 1)
    f = np.poly1d(fp)
    fy = f(datasets[sheet_number]['V'])
    plt.plot(datasets[sheet_number]['V'][fy > 0], fy[fy > 0], c='r', ls='--')
    plt.text(*text_loc1[sheet_number], "gradient\n{}".format(fp[0].round(4)), color='r', wrap=True)
    plt.grid(True)
    plt.xlabel("Applied Voltage[V]")
    plt.ylabel("Current [A]")
    plt.subplot(1, 3, 2)
    plt.plot(datasets[sheet_number]['V'], datasets[sheet_number]['I'], marker='x')
    plt.yscale('log')
    plt.grid(True, which='both')
    plt.xlabel("Applied Voltage[V]")
    plt.ylabel("Current In Logscale [A]")
    plt.subplot(1, 3, 3)
    ln_A = np.log(datasets[sheet_number]['I'])
    plt.plot(datasets[sheet_number]['V'], ln_A, marker='x', label="log(I)")

    if sheet_number < 3:
        domain1 = ln_A < n[sheet_number]
        domain2 = ln_A > n[sheet_number]
        if sheet_number > 0:
            fp1 = np.polyfit(datasets[sheet_number]['V'][domain1], ln_A[domain1], 1)
        else:
            fp1 = np.polyfit(datasets[sheet_number]['V'][3:9], ln_A[3:9], 1)

        fp2 = np.polyfit(datasets[sheet_number]['V'][domain2], ln_A[domain2], 1)
        f1 = np.poly1d(fp1)
        f2 = np.poly1d(fp2)
        plt.plot(datasets[sheet_number]['V'], f1(datasets[sheet_number]['V']), c='r', ls='--')
        plt.plot(datasets[sheet_number]['V'], f2(datasets[sheet_number]['V']), c='r', ls='--')
        plt.text(*text_loc2[sheet_number][0], "gradient\n{}".format(fp1[0].round(4)), color='r', wrap=True)
        plt.text(*text_loc2[sheet_number][1], "gradient\n{}".format(fp2[0].round(4)), color='r', wrap=True)
        print('n{} is '.format(sheet_number + 1), e / ((fp1[0]) * k * 300))
        print('n{}\' is '.format(sheet_number + 1), e / ((fp2[0]) * k * 300))
    else:
        fp1 = np.polyfit(datasets[sheet_number]['V'], ln_A, 1)
        f1 = np.poly1d(fp1)
        plt.plot(datasets[sheet_number]['V'], f1(datasets[sheet_number]['V']), c='r', ls='--')
        plt.text(0.4, 0, "gradient\n{}".format(fp1[0].round(4)), color='r', wrap=True)
        print('n{} is '.format(sheet_number + 1), e / ((fp1[0]) * k * 300))

    plt.grid(True)
    plt.xlabel("Applied Voltage[V]")
    plt.ylabel("Current [log(A)]")
    plt.subplots_adjust(left=0.05, right=0.95, wspace = 0.25, hspace=0.6)





