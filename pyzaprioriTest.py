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
import siemens_predict
import pyzapriori

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

    tmp_dict = {'x': vib_group_x, 'y': vib_group_y, 'z': vib_group_z}
    tmp_df = pd.DataFrame(tmp_dict, index = vib[ 'TIME' ].unique( ) )

    del vib
    del human
    del distance
    del current

    pre_res = siemens_predict.predict( tmp_df, human_group, distance_group, current_group )

    # vib     human distance  current
    # 3       2     2         3
    # 0 1 2 | 0 1 | 0 1     | 0 1 2
    # 1 2 3 | 4 5 | 6 7     | 8 9 10

    apriori_input = [ ]
    tmp = [ ]

    for i in pre_res:

        if i[ 0 ] == 0:

            tmp.append( 1 )

        elif i[ 0 ] == 1:

            tmp.append( 2 )

        else:

            tmp.append( 3 )

        if i[ 1 ] == 0:

            tmp.append( 4 )

        else:

            tmp.append( 5 )

        if i[ 2 ] == 0:

            tmp.append( 6 )

        else:

            tmp.append( 7 )

        if i[ 3 ] == 0:

            tmp.append( 8 )

        elif i[ 3 ] == 1:

            tmp.append( 9 )

        else:

            tmp.append( 10 )

        apriori_input.append( tmp )
        tmp = [ ]

    print len( pre_res )
    print len( apriori_input )

    set_pre_res = set( )
    set_apriori_input = set( )

    for i in pre_res:

        if tuple( i ) not in set_pre_res:

            set_pre_res.add( tuple( i ) )

    for i in apriori_input:

        if tuple( i ) not in set_apriori_input:

            set_apriori_input.add( tuple( i ) )

    print set_pre_res, len( set_pre_res )
    print set_apriori_input, len( set_apriori_input )

    res, support_info = pyzapriori.apriori( apriori_input )

    frequent_item_cnt = 0
    for Lk in res:

        frequent_item_cnt += len( Lk )

    print len( res ), frequent_item_cnt
    print len( support_info )

    print res
    print support_info
