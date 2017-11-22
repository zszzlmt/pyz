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
"""Apriori algorithm tests for pyz python libs."""

#
# File start at:
#   2017-11-21
#
# Last edit at:
#   2017-11-22
#
# Author:
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import numpy as np
import pandas as pd
import pyzio as io
import copy

def _cut_tail( input_series, tail_length = 6 ):

    res = [ ]

    for i in input_series:

        res.append( copy.deepcopy( i[ : -tail_length ] ) )

    return res

def _group( input_df, target_index, group_index ):

    res = [ ]
    tmp = [ ]
    l = len( input_df )

    pre_value = input_df[ group_index ][ 0 ]
    tmp.append( copy.deepcopy( input_df[ target_index ][ 0 ] ) )
    for i in np.arange( 1, l ):

        now_value = input_df[ group_index ][ i ]
        if now_value == pre_value:

            tmp.append( copy.deepcopy( input_df[ target_index ][ i ] ) )

        else:

            pre_value = now_value
            res.append( copy.deepcopy( tmp ) )
            tmp = [ copy.deepcopy( input_df[ target_index ][ i ] ) ]

    res.append( copy.deepcopy( tmp ) )
    return res


if __name__ == '__main__':

    current = io.in_csv( '../current.csv' )
    distance = io.in_csv( '../distance.csv' )
    human = io.in_csv( '../human.csv' )
    vib = io.in_csv( '../vibarnt.csv' )

    current_time = _cut_tail( current[ 'TIME' ] )
    distance_time = _cut_tail( distance[ 'TIME' ] )
    human_time = _cut_tail( human[ 'TIME' ] )
    vib_time = _cut_tail( vib[ 'TIME' ] )

    del current[ 'ID' ]
    del distance[ 'ID' ]
    del human[ 'ID' ]
    del vib[ 'ID' ]

    del current[ 'TIME' ]
    del distance[ 'TIME' ]
    del human[ 'TIME' ]
    del vib[ 'TIME' ]

    current[ 'TIME' ] = current_time
    distance[ 'TIME' ] = distance_time
    human[ 'TIME' ] = human_time
    vib[ 'TIME' ] = vib_time

    current_group = _group( current, 'VALUE', 'TIME' )
    distance_group = _group( distance, 'VALUE', 'TIME' )
    human_group = _group( human, 'VALUE', 'TIME' )
    vib_group_x = _group( vib, 'X_VALUE', 'TIME' )
    vib_group_y = _group( vib, 'y_VALUE', 'TIME' )
    vib_group_z = _group( vib, 'z_VALUE', 'TIME' )

    del current
    del distance
    del human
    del vib

    
