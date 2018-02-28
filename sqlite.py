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
"""SQL functions for pyz python libs.

"""

#
# File start at:
#   2018-02-28
#
# Last edit at:
#   2018-02-28
#
# Author:
#   Zach Yeo
#
# Contact me by:
#   zsz100e@126.com
#

import sqlite3


class SQLLite(object):

    def __init__(self, db_name, col_names=None, types=None, sql_cmd=None):
        """

        :param db_name:
        :param col_names:
        :param types:
        :param sql_cmd:
        """
        self.db_name = db_name
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        if not col_names:
            pass
        elif not sql_cmd:
            pass
        conn.commit()
        conn.close()
