# ソフトマックス関数のpythonの関数としての定義

import numpy as np


def softmax(a):

    c = np.max(a)  # オーバーフローを考慮
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y