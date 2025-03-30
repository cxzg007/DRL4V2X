# rl_utils.py
import numpy as np

def moving_average(data, window_size):
    """计算移动平均值"""
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def forward_fill(data, window_size):
    mv_avg = moving_average(data, window_size)
    fill_value = mv_avg[-1]
    return np.concatenate((mv_avg, np.full(window_size - 1, fill_value)))
