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
"""IO functions for pyz python libs."""

#
# File start at:
#   2017-09-08
#
# Last edit at:
#   2017-11-24
#
# Author:
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import string
import os.path
import numpy as np
import pandas as pd

def in_csv( path ):
    '''
    read in a csv format file, and return the pandas.DataFrame object
    :param path:
    :return:
    '''
    if not os.path.exists( path ):
        return False
    res = pd.read_csv( path, index_col = False )
    return res

def out_df_csv( df, path ):
    '''

    :param df:
    :param path:
    :return:
    '''
    df.to_csv( path, index = False )

def out_sln_csv( target, path, name = 'value' ):
    '''
    save the target Series/list/ndarray with the csv format and path specified
    if no column name is specified, 'res' is default one
    :param target:
    :param path:
    :param name:
    :return:
    '''
    tmp_dict = { name: target }
    res_df = pd.DataFrame( tmp_dict )
    res_df.to_csv( path )

# #
# # function "saveListD1":
# #
# def saveListD1(l, path, append = 'w'):
#
#     if l == None or len(l) == 0 or not (isinstance(l, list)):
#
#         return
#
#     fp = open(path, append)# file pointer and write only if not specified
#     if fp == None:
#
#         #err
#         return
#
#     for row in l:
#
#         fp.write(str(row))
#         fp.write('\n')
#
#     fp.close()
#
# #
# # function "loadListD1":
# #
# def loadListD1(path, type = 'string'):
#
#     if not os.path.exists(path):
#
#         #err
#         pass
#
#     elif not os.path.getsize(path):
#
#         #err
#         pass
#
#     fp = open(path, 'r')
#     if fp == None:
#
#         #err
#         pass
#
#     res = []
#
#     if type == 'string':
#
#         func = str
#
#     elif type == 'int':
#
#         func = int
#
#     elif type == 'float':
#
#         func = float
#
#     for row in fp:
#
#         res.append(func(row))
#
#     fp.close()
#
#     return res
#
# #
# # function "saveListD2":
# #
# def saveListD2(l, path, append = 'w'):
#
#     if l == None or len(l) == 0 or not (isinstance(l, list)):
#
#         return
#
#     fp = open(path, append)# file pointer and write only if not specified
#     if fp == None:
#
#         #err
#         return
#
#     for row in l:
#
#         for col in row:
#
#             fp.write(str(col))
#             fp.write('\n')
#
#         fp.write('!-#-!\n')
#
#     fp.close()
#
# #
# # function "loadListD2":
# #
# def loadListD2(path, type = 'string'):
#
#     if not os.path.exists(path):
#
#         #err
#         pass
#
#     elif not os.path.getsize(path):
#
#         #err
#         pass
#
#     fp = open(path, 'r')
#     if fp == None:
#
#         #err
#         pass
#
#     res = []
#     tmp = []
#
#     if type == 'string':
#
#         func = str
#
#     elif type == 'int':
#
#         func = int
#
#     elif type == 'float':
#
#         func = float
#
#     for row in fp:
#
#         if row == '!-#-!\n':
#
#             res.append(tmp)
#             del tmp[:]
#
#         else:
#
#             tmp.append(func(row))
#
#
#     fp.close()
#
#     return res
