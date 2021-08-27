# coding: utf-8
# Author：WangTianRui
# Date ：2021-08-24 14:15
import pandas as pd
import numpy as np
import os, sys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    flag = str(sys.argv[1])
    eps_root = r"./csvs/%s" % flag
    pesq = []
    sisnr = []
    stoi = []
    xs = []
    for i in os.walk(eps_root):
        for index, name in enumerate(i[2]):
            if flag == "eps":
                eps = str(name.split("_")[1])
                xs.append(eps)
            else:
                theta = str(name.split("_")[3].split(".csv")[0])

                xs.append(theta)
            df = pd.read_csv(os.path.join(eps_root, name))
            print(name)
            df = df[["pesq_wb", "time_sisnr_", "stoi_score"]]
            df.time_sisnr_ = abs(df.time_sisnr_)
            print(df.describe().loc["mean"])
            pesq.append(float(df.describe().loc["mean"]["pesq_wb"]))
            sisnr.append(abs(float(df.describe().loc["mean"]["time_sisnr_"])))
            stoi.append(float(df.describe().loc["mean"]["stoi_score"]))
            df.to_csv(os.path.join(eps_root, name))
        break
    print(pesq)
    print(sisnr)
    print(stoi)
    print(xs)
    plt.figure(figsize=(6, 8), dpi=160)
    plt.subplot(311)
    plt.plot(xs, pesq)
    # plt.title("PESQ")
    # plt.show()
    plt.subplot(312)
    plt.plot(xs, sisnr)
    # plt.title("SI-SNR")
    # plt.show()
    plt.subplot(313)
    plt.plot(xs, stoi)
    # plt.title("STOI")
    plt.savefig("./pics/%s.png" % flag)
    plt.show()
