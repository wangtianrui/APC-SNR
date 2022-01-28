# coding: utf-8
# Author：WangTianRui
# Date ：2021/1/6 10:59
import numpy as np

np.set_printoptions(threshold=1000000)  # 全部输出
# bark域的频域跨度
nr_of_hz_bands_per_bark_band_16k = [1, 1, 1, 1, 1,
                                    1, 1, 1, 2, 1,
                                    1, 1, 1, 1, 2,
                                    1, 1, 2, 2, 2,
                                    2, 2, 2, 2, 2,
                                    3, 3, 3, 3, 4,
                                    3, 4, 5, 4, 5,
                                    6, 6, 7, 8, 9,
                                    9, 12, 12, 15, 16,
                                    18, 21, 25, 20]

# bark域的中心
centre_of_band_bark_16k = [0.078672, 0.316341, 0.636559, 0.961246, 1.290450,
                           1.624217, 1.962597, 2.305636, 2.653383, 3.005889,
                           3.363201, 3.725371, 4.092449, 4.464486, 4.841533,
                           5.223642, 5.610866, 6.003256, 6.400869, 6.803755,
                           7.211971, 7.625571, 8.044611, 8.469146, 8.899232,
                           9.334927, 9.776288, 10.223374, 10.676242, 11.134952,
                           11.599563, 12.070135, 12.546731, 13.029408, 13.518232,
                           14.013264, 14.514566, 15.022202, 15.536238, 16.056736,
                           16.583761, 17.117382, 17.657663, 18.204674, 18.758478,
                           19.319147, 19.886751, 20.461355, 21.043034]

# # 在频域上bark域的中心
centre_of_band_hz_16k = [7.867213, 31.634144, 63.655895, 96.124611, 129.044968,
                         162.421738, 196.259659, 230.563568, 265.338348, 300.588867,
                         336.320129, 372.537140, 409.244934, 446.448578, 484.568604,
                         526.600586, 570.303833, 619.423340, 672.121643, 728.525696,
                         785.675964, 846.835693, 909.691650, 977.063293, 1049.861694,
                         1129.635986, 1217.257568, 1312.109497, 1412.501465, 1517.999390,
                         1628.894165, 1746.194336, 1871.568848, 2008.776123, 2158.979248,
                         2326.743164, 2513.787109, 2722.488770, 2952.586670, 3205.835449,
                         3492.679932, 3820.219238, 4193.938477, 4619.846191, 5100.437012,
                         5636.199219, 6234.313477, 6946.734863, 7796.473633]

# # 每个bark在频域上对应的宽度
width_of_band_hz_16k = [15.734426, 31.799433, 32.244064, 32.693359, 33.147385,
                        33.606140, 34.069702, 34.538116, 35.011429, 35.489655,
                        35.972870, 36.461121, 36.954407, 37.452911, 40.269653,
                        42.311859, 45.992554, 51.348511, 55.040527, 56.775208,
                        58.699402, 62.445862, 64.820923, 69.195374, 76.745667,
                        84.016235, 90.825684, 97.931152, 103.348877, 107.801880,
                        113.552246, 121.490601, 130.420410, 143.431763, 158.486816,
                        176.872803, 198.314697, 219.549561, 240.600098, 268.702393,
                        306.060059, 349.937012, 398.686279, 454.713867, 506.841797,
                        564.863770, 637.261230, 794.717285, 931.068359]


def get_nr_of_hz_bands_per_bark_bank_16k(n_fft):
    if n_fft == 256:
        return nr_of_hz_bands_per_bark_band_16k
    else:
        aranges = []
        for index in range(len(centre_of_band_hz_16k)):
            width = width_of_band_hz_16k[index] / 2
            arange = [centre_of_band_hz_16k[index] - width, centre_of_band_hz_16k[index] + width]
            aranges.append(arange)
        result = np.zeros(len(aranges))
        hz_per_fft_bin = 8000 / n_fft
        for fft_bin in range(0, n_fft):
            hz_now = fft_bin * hz_per_fft_bin
            # print(hz_now)
            for index in range(len(aranges)):
                if aranges[index][0] <= hz_now < aranges[index][1]:
                    result[index] += 1
                    break
    return result.astype(np.int)


def get_zwicker_power_to_nftt(n_fft=256):
    """
    :param n_fft: <=256
    :return:
    """
    zp = zwicker_power(49)
    zp_nfft = np.zeros(n_fft)
    nr_of_hz_bands_per_bark_band_16k_ = get_nr_of_hz_bands_per_bark_bank_16k(n_fft)
    current_inx_of_f = 0
    for inx, item in enumerate(nr_of_hz_bands_per_bark_band_16k_):
        zp_nfft[current_inx_of_f:current_inx_of_f + item] += zp[inx]
        current_inx_of_f += item
    return zp_nfft


def zwicker_power(nb):
    modified_zwicker_power = np.zeros(nb)
    for band in range(nb):
        if centre_of_band_bark_16k[band] < 4:
            h = 6 / (centre_of_band_bark_16k[band] + 2)
        else:
            h = 1
        if h > 2:
            h = 2
        h = h ** 0.15
        modified_zwicker_power[band] = 0.23 * h
    return modified_zwicker_power


if __name__ == '__main__':
    print(get_zwicker_power_to_nftt(256))
