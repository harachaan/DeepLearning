from socket import gaierror
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    return x


def init_network():
    network = {}  # リストではなく辞書を作ってる ''でくくられてるやつはkey?
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])

    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])

    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):  # xは入力？
    # この等号の使い方覚えとくとよさそう
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y
# ここまでが使う関数の定義


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)  # [0.31682708 0.69627909]

# ----------------------------------------
# 日本語の説明：

# ここでは，init_network(), forward()という２つの関数を定義した．

# init_network()関数で，重みとバイアスの初期化を行い，それらをディクショナリ型のnetworkに格納する
# このディレクショナリ型の関数networkには，それぞれの層で必要なパラメータ(重みとバイアス)が格納されている．

# そして，forward()関数では，入力信号が出力へと変換されるプロセスがまとめて実装されている．

# ちなみに，"forward"とは，入力から出力方向への伝達処理を表している
# --------------------------------------
