# coding: utf-8
# Author：WangTianRui
# Date ：2021/3/30 9:47
import torch
import torch.nn as nn
import numpy as np
import constant as constant


class AcousticScaler(nn.Module):
    def __init__(self, theta=0.01, eps=1.0, mag_bins=256, no_grad=True):
        self.no_grad = no_grad
        self.eps = eps
        super(AcousticScaler, self).__init__()
        self.register_buffer(
            "zwicker_power",
            torch.tensor(constant.get_zwicker_power_to_nftt(mag_bins), dtype=torch.float).unsqueeze(0).unsqueeze(0)
        )
        self.theta = theta
        self.mag_bins = mag_bins

    def forward(self, est, clean=None):
        """`
        :param est: B,2*F,T
        :param clean:B,2*F,T
        :return: B,2*F,T
        """
        need_pad = 0
        if self.no_grad:
            with torch.no_grad():
                est = est.permute(0, 2, 1)  # B,T,2*F
                clean = clean.permute(0, 2, 1)
                est_real, est_imag = torch.chunk(est, 2, dim=-1)
                clean_real, clean_imag = torch.chunk(clean, 2, dim=-1)
                if est_real.size(-1) != self.mag_bins:
                    est_real, est_imag = est_real[..., :self.mag_bins], est_imag[..., :self.mag_bins]
                    clean_real, clean_imag = clean_real[..., :self.mag_bins], clean_imag[..., :self.mag_bins]
                    need_pad = est_real.size(-1) - self.mag_bins
                est_power = (est_real ** 2 + est_imag ** 2)  # B,T,F
                clean_power = (clean_real ** 2 + clean_imag ** 2)  # B,T,F
                est_scales = ((est_power + self.eps) ** ((self.zwicker_power - 1) * 0.5))
                clean_scales = ((clean_power + self.eps) ** ((self.zwicker_power - 1) * 0.5))
                return self.double_size(est_scales, need_pad).clamp_(self.theta, 1), \
                       self.double_size(clean_scales, need_pad).clamp_(self.theta, 1)
        else:
            est = est.permute(0, 2, 1)  # B,T,2*F
            clean = clean.permute(0, 2, 1)
            est_real, est_imag = torch.chunk(est, 2, dim=-1)
            clean_real, clean_imag = torch.chunk(clean, 2, dim=-1)
            if est_real.size(-1) != self.mag_bins:
                est_real, est_imag = est_real[..., :self.mag_bins], est_imag[..., :self.mag_bins]
                clean_real, clean_imag = clean_real[..., :self.mag_bins], clean_imag[..., :self.mag_bins]
                need_pad = est_real.size(-1) - self.mag_bins
            est_power = (est_real ** 2 + est_imag ** 2)  # B,T,F
            clean_power = (clean_real ** 2 + clean_imag ** 2)  # B,T,F
            est_scales = ((est_power + self.eps) ** ((self.zwicker_power - 1) * 0.5))
            clean_scales = ((clean_power + self.eps) ** ((self.zwicker_power - 1) * 0.5))
            return self.double_size(est_scales, need_pad).clamp_(self.theta, 1), \
                   self.double_size(clean_scales, need_pad).clamp_(self.theta, 1)


def double_size(inp, need_pad):
    """
    :param inp:B,T,F
    :return: B,2*F,T
    """
    if need_pad != 0:
        return torch.nn.functional.pad(
            inp, [0, need_pad, 0, 0], value=1e-8
        ).repeat(1, 1, 2).permute(0, 2, 1)
    else:
        return inp.repeat(1, 1, 2).permute(0, 2, 1)
