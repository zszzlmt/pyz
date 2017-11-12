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
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml import NetworkWriter
from pybrain.tools.xml import NetworkReader
from pybrain.structure import TanhLayer


def ann_pybrain3( input, target, input_dim, hidden_dim, output_dim, max_iter ):
    ''''''

    data = SupervisedDataSet( input.shape[ 1 ], target.shape )


    pass