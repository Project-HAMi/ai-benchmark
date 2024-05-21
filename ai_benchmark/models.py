# -*- coding: utf-8 -*-
# Copyright 2019-2020 by Andrey Ignatov. All Rights Reserved.

from ai_benchmark.utils import tf
from ai_benchmark.model_utils import *


def LSTM_Sentiment(input_tensor):

    #  Reference Paper: https://www.bioinf.jku.at/publications/older/2604.pdf

    # Create a basic LSTM cell
    lstmCell = tf.keras.layers.LSTMCell(1024)
    # Convert cell to LSTM layer and get the output
    lstmLayer = tf.keras.layers.RNN(lstmCell, return_sequences=True, return_state=True)
    output_rnn, _ , _ = lstmLayer(input_tensor)

    # Dense layer to predict the output
    denseLayer = tf.keras.layers.Dense(2)
    
    output = output_rnn[:, -1, :]
    
    return tf.identity(denseLayer(output), name="output")


def PixelRNN(inputs):

    #  Reference Paper: https://arxiv.org/abs/1601.06759
    #  Reference Code: https://github.com/carpedm20/pixel-rnn-tensorflow

    normalized_inputs = inputs / 255.0
    output = conv2d(normalized_inputs, 16, [7, 7], mask_type="a", scope="conv_inputs")

    for idx in range(7):
        output = diagonal_bilstm(output, scope='LSTM%d' % idx)

    for idx in range(2):
        output = tf.nn.relu(conv2d(output, 32, [1, 1], mask_type="b", scope='CONV_OUT%d' % idx))

    conv2d_out_logits = conv2d(output, 3, [1, 1], mask_type="b", scope='conv2d_out_logits')
    return tf.nn.sigmoid(conv2d_out_logits) * 255
