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
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import numpy as np
import copy

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

def rnn3( input_series, target_value, input_dim = 3, hidden_dim = 10, output_dim = 4, step = 0.1, max_iter = 10000 ):
    """
    recursive neural network model with 3 layer: input, hidden, and output
    :param input_series: supposed to be a ndarry object with m * t * n dimensions. here the m is the amount of the
    training samples, each of which has t time observation point, and n features in each observation.
    :param target_value: supposed to be a ndarry object with m * t * k dimensions. here the m is the amount of the
    training samples, each of which has t time observation point, and k dimension result in each observation.
    :param input_dim: dimension in input layer
    :param hidden_dim: dimension in hidden layer
    :param output_dim: dimension in output layer
    :param step: represent the speed in the learning process
    :param max_iter: maxmum training iteration, if less than training samples, stop the training when samples are
    used out
    :return:
    """
    # weight matrics
    weight_ho = 2 * np.random.random( ( hidden_dim, output_dim ) ) - 1
    weight_hh = 2 * np.random.random( ( hidden_dim, hidden_dim ) ) - 1
    weight_ih = 2 * np.random.random( ( input_dim, hidden_dim ) ) - 1

    # to update weight matrics
    weight_ho_update = np.zeros_like( weight_ho )
    weight_hh_update = np.zeros_like( weight_hh )
    weight_ih_update = np.zeros_like( weight_ih )

    for train_iter in np.arange( max( input_series.shape[ 0 ], max_iter ) ):

        # previous residual and value
        output_delta_value = list( )
        hidden_value = list( )
        hidden_value.append( np.zeros( hidden_dim ) )

        train_length = len( input_series[ train_iter ] )

        for moment_id in np.arange( train_length ):

            # prepare the input and output
            moment_x = input_series[ train_iter, moment_id ]
            moment_y = target_value[ train_iter, moment_id ]

            # forward propagation
            hidden_layer = sigmoid( np.dot( moment_x, weight_ih ) + np.dot( hidden_value[ -1 ], weight_hh ) )
            output_layer = sigmoid( np.dot( hidden_layer, weight_ho ) )

            moment_residual = moment_y - output_layer
            output_delta_value.append( moment_residual * sigmoid_derivative( output_layer ) )

            hidden_value.append( copy.deepcopy( hidden_layer ) )

        hidden_delta_future = np.zeros( hidden_dim )

        for moment_id in np.arrange( train_length ):

            moment_x = input_series[ train_iter, train_length - moment_id - 1 ]
            hidden_layer = hidden_value[ -moment_id - 1 ]
            hidden_layer_before = hidden_value[ -moment_id - 1 - 1 ]
            output_delta = output_delta_value[ -moment_id - 1 ]
            hidden_delta = ( np.dot( hidden_delta_future, weight_hh.T ) + np.dot( output_delta, weight_ho.T ) ) * sigmoid_derivative( hidden_layer )

            weight_ho_update += np.dot( np.atleast_2d( hidden_layer ).T, output_delta )
            weight_hh_update += np.dot( np.atleast_2d( hidden_layer_before ).T, hidden_delta )
            weight_ih_update += np.dot( moment_x.T, hidden_delta )

            hidden_delta_future = hidden_delta

        weight_ho += weight_ho_update * step
        weight_hh += weight_hh_update * step
        weight_ih += weight_ih_update * step

        weight_ho_update *= 0
        weight_hh_update *= 0
        weight_ih_update *= 0

    res = { 'input_dim'     :   input_dim,  \
            'hidden_dim'    :   hidden_dim, \
            'output_dim'    :   output_dim, \
            'weight_ho'     :   weight_ho,  \
            'weight_hh'     :   weight_hh,  \
            'weight_ih'     :   weight_ih   }
