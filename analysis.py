# coding: utf-8
# Author：WangTianRui
# Date ：2021/4/9 16:07
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行

pesqs = []
stois = []
sisnrs = []


def get_info(csv_path, name, all_csvs):
    df = pd.read_csv(csv_path, encoding="utf_8_sig")
    all_csvs[name] = df.describe().loc[["std", "mean"]].drop(
        ['Unnamed: 0', "stft_snr"], axis=1)
    pesqs.append(all_csvs[name]["pesq_wb"].loc["mean"])
    stois.append(all_csvs[name]["stoi_score"].loc["mean"])
    sisnrs.append(abs(all_csvs[name]["time_sisnr_"].loc["mean"]))


def sort_csv(all_csvs, model_flag):
    scores = {}
    for key in all_csvs.keys():
        mean_measure = (
                               (all_csvs[key]["pesq_wb"].loc["mean"] - np.mean(pesqs)) / np.std(pesqs) +
                               (abs(all_csvs[key]["time_sisnr_"].loc["mean"] - np.mean(sisnrs))) / np.std(sisnrs) +
                               (all_csvs[key]["stoi_score"].loc["mean"] - np.mean(stois)) / np.std(stois)
                       ) / 3
        all_csvs[key]["mean_measure"] = mean_measure
        scores[key] = mean_measure
    scores_sort = sorted(scores.items(), key=lambda x: x[1], reverse=False)

    indexes = None
    scores_plot = {}
    methods = []
    for key in scores_sort:
        print("--" * 15, key[0], "--" * 15)
        methods.append(key[0].split(".")[0])
        print(all_csvs[key[0]])
        # if indexes is None:
        #     indexes = all_csvs[key[0]].columns.values
        #     for index in indexes:
        #         scores_plot[index] = [all_csvs[key[0]][index].loc["mean"]]
        # else:
        #     for index in indexes:
        #         scores_plot[index].append(all_csvs[key[0]][index].loc["mean"])

    # plt.figure(figsize=(12, 4), dpi=160)
    #
    # for i, index in enumerate(scores_plot.keys()):
    #     # print(500 + 10 + 10 * (i // 5) + 1 + i % 5)
    #     # plt.subplot(int(500 + 10 + 10 * (i // 5) + 1 + i % 5))
    #     print(methods)
    #     print(scores_plot[index])
    #     plt.bar(methods, scores_plot[index])
    #     plt.title(index)
    #     plt.savefig(os.path.join("./pics", "%s" % model_flag, "%s.png" % index))
    #     # plt.show()


if __name__ == '__main__':
    model_flag = str(sys.argv[1])
    all_csvs = {}
    info_path = {}
    all_csv_name = []
    number_flag = 150
    root = os.path.join("./results/", model_flag)
    for i in os.walk(root):
        all_csv_name = i[2]
        break
    for name in all_csv_name:
        if name.endswith("csv"):
            info_path[name] = os.path.join(root, name)
    for key in info_path.keys():
        get_info(info_path[key], key, all_csvs)
    sort_csv(all_csvs, model_flag)
