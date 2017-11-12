#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2017 The Zach Yeo Author. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Recursive Neural Networks for pyz python libs."""

#
# File start at:
#   2017-11-12
#
# Last edit at:
#   2017-11-12
#
# Author:
#   ZachYeo
#
# Contact me by:
#   zsz100e@126.com
#

import numpy as np

def sigmoid( x ):
    """
    calculate sigmoid result of a scalar or ndarry
    :param x: scalar or ndarry
    :return: sigmoid result
    """
    res = 1 / ( 1 + np.exp( - x ) )
    return res

def sigmoid_derivative( x ):
    """
    calculate derivative of sigmoid result of a scalar or ndarry
    :param x: scalar or ndarry
    :return: derivative of sigmoid result
    """
    res = x * ( 1 - x )
    return res

def rnn3( input_series, target_value, input_dim = 3, hidden_dim = 10, output_dim = 4, max_iter = 10000 ):
    """"""
    # weight matrics
    weight_ih = 2 * np.random.random( ( input_dim, hidden_dim ) ) - 1
    weight_ho = 2 * np.random.random( ( hidden_dim, output_dim ) ) - 1
    weight_hh = 2 * np.random.random( ( hidden_dim, hidden_dim ) ) - 1

    # to update weight matrics
    weight_ih_update = np.zeros_like( weight_ih )
    weight_ho_update = np.zeros_like( weight_ho )
    weight_hh_update = np.zeros_like( weight_hh )

    for train_iter in np.arange( max_iter ):

        # prepare the input and output

        for moment_id in np.arange( len( input_series[ train_iter ] ) ):

            moment_input = input_series[ train_iter, moment_id ]



