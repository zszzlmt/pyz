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
"""IO functions for pyz python libs.

"""

#
# File start at:
#   2017-09-08
#
# Last edit at:
#   2018-02-13
#
# Author:
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import string
import os.path
import pickle
import numpy as np
import pandas as pd


def in_csv(path, my_index_col=0):
    """
    read in a csv format file, and return the pandas.DataFrame object.

    :param path: the path to fetch the csv file
    :param my_index_col:
        0: #(es) of existing columns to be the index of DataFrame, can be multiple columns with format list of #es
        None: add a new column to be index
        False: considered as 0 in most time, but may be abandoned

    :return: pandas.DataFrame object corresponding to the csv file
    """
    if not os.path.exists(path):
        return None
    res = pd.read_csv(path, index_col=my_index_col)
    return res


def out_df_csv(df, path, my_index=True):
    """
    write out a csv format file.

    :param df: pandas.DataFrame object to write out
    :param path: the path to write out the csv file
    :param my_index:
        True: (default)write out csv file with a lead index column
        False: without any lead index column added

    :return: no return for now
    """
    df.to_csv(path, index=my_index)


def out_sln_csv(target, path, name='value', my_index=True):
    """
    save the target pandas.Series/List/Ndarray with the csv format to the path specified.
    if no column name is specified, 'value' is default one.
    supposed to be fine with one dimension input for now.

    :param target: pandas.Series/List/Ndarray object to write out
    :param path: the path to write out the csv file
    :param name: column name of the values
    :param my_index: param used in function out_df_csv()

    :return: no return for now
    """
    tmp_dict = {name: target}
    tmp_df = pd.DataFrame(tmp_dict)
    out_df_csv(tmp_df, path, my_index=my_index)


def in_pkl(path):
    """
    input a pkl file(recommended) from path, deserialized it to a target and return
    using default protocol of pickle.dump and pickle.load, which can be fine in most cases
    before python2.6, protocol is in [0, 1, 2] and negative to be the highest protocol, default 0
    after python3.x, protocol is in [3, 4] and negative to be the highest protocol, default 3

    :param path: path to fetch the pkl file

    :return: object that is deserialized
    """
    option = 'rb'
    with open(path, option) as file:
        target = pickle.load(file)
    return target


def out_pkl(target, path):
    """
    serialize a target and output to path as a pkl file(recommended)
    using default protocol of pickle.dump and pickle.load, which can be fine in most cases
    before python2.6, protocol is in [0, 1, 2] and negative to be the highest protocol, default 0
    after python3.x, protocol is in [3, 4] and negative to be the highest protocol, default 3

    :param target: object to serialize and write out
    :param path: path to write out the pkl file

    :return: no return for now
    """
    option = 'wb'
    with open(path, option) as file:
        pickle.dump(target, file)
