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
"""Apriori algorithm for pyz python libs."""

#
# File start at:
#   2017-11-21
#
# Last edit at:
#   2017-11-21
#
# Author:
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import numpy as np
import pandas as pd

def _create_C1( transaction_set ):
    ''''''
    res = []
    for transaction in transaction_set:

        for item in transaction:

            if [ item ] not in res:

                res.append( [ item ] )

    res.sort( )
    return map( frozenset, res )

def _calcu_support( transaction_set, candidates, thres_support ):
    ''''''
    res_item = [ ]
    res_support = { }
    bin_dict = { }

    for transaction in transaction_set:

        for item in candidates:

            bin_dict[ item ] = bin_dict.get( item, 0 ) + 1

    N_transactions = float( len( transaction_set ) )

    for key in bin_dict:

        support = bin_dict[ key ] / N_transactions

        res_support[ key ] = support

        if support >= thres_support:

            res_item.append( key )

    return res_item, res_support

