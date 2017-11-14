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
#   2017-11-14
#
# Author:
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import numpy as np
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml import NetworkWriter
from pybrain.tools.xml import NetworkReader
from pybrain.structure import TanhLayer


def ann_pybrain3( input, target, input_dim, hidden_dim, output_dim, max_iter = 10000, bias = True, output_bias = True ):
    '''

    :param input: supposed to be a ndarry object with m * n dimensions. here the m is the amount of the
    training samples, each of which has n dimension features
    :param target: supposed to be a ndarry object with m * k dimensions, here the m is the amount of the
    training samples, each of which is a k dimension result vector
    :param input_dim: dimension of input layer
    :param hidden_dim: dimension of hidden layer
    :param output_dim: dimension of output layer
    :param max_iter: maximum training iteration, if less than training samples, stop the training when samples are
    used out
    :param bias: whether or not to use bias in hidden layer
    :param output_bias: whether or not to use bias in output layer
    :return: pybrain neural network object, training error and validation error
    '''

    data = SupervisedDataSet( input.shape[ 1 ], target.shape )

    for i in np.arange( input.shape[ 0 ] ):

        data.addSample( input[ i ], target[ i ] )

    model = buildNetwork( input_dim, hidden_dim, output_dim, bias = bias, outputbias = output_bias )
    trainer = BackpropTrainer( model, data )
    train_error, valid_error = trainer.trainUntilConvergence( maxEpochs = max_iter )

    return model, train_error, valid_error

def save_pybrain3( model, path ):
    '''

    :param model: pybrain neural network object that need to be saved
    :param path: path to save the model
    :return: none
    '''
    NetworkWriter.writeToFile( model, path )

def load_pybrain3( path ):
    '''

    :param path: path to load the model
    :return: pybrain neural network object loaded just now
    '''
    model = NetworkReader.readFrom( path )
    return model