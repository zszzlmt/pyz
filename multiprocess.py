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
"""Multiprocess realization for pyz python libs.

"""

#
# File start at:
#   2018-02-13
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

import multiprocessing
import time


def get_process_lock():
    """
    return a multiprocessing.Lock object to control access of any sensitive resource.

    :return: multiprocessing.Lock object.
    """
    return multiprocessing.Lock()


def new_process(func, lock=None, daemon=False):
    """
    new a process to do jobs specified in function func, with or without lock, set daemon True or False.

    :param func: jobs that are wished to be done by process.
    :param lock: multiprocessing.Lock object if necessary. None is default, otherwise use of lock should be specified
        in function func.
    :param daemon:
        True: if main process died, all the child process should go die
        False: main process should always wait the finish of child process

    :return: PyzProcess object
    """
    return PyzProcess(func, lock, daemon)


def new_process_and_run(func, lock=None, daemon=False):
    """
    new a process to do jobs specified in function func, with or without lock, set daemon True or False.
    run it after creation

    :param func: jobs that are wished to be done by process.
    :param lock: multiprocessing.Lock object if necessary. None is default, otherwise use of lock should be specified
        in function func.
    :param daemon:
        True: if main process died, all the child process should go die
        False: main process should always wait the finish of child process

    :return: PyzProcess object
    """
    PyzProcess(func, lock, daemon).start()


def run_process(process):
    """
    run a process

    :param process: process to run
    :return: no return for now
    """
    process.start()


def wait_process(process, timeout=None):
    """
    wait a process to finish no matter whether the attribute daemon is True or False

    :param process: process that main process is waiting for
    :param timeout: maximum time each one process can use, if exceed, kill it

    :return: when child process finished or timeout, return
    """
    if timeout is None:
        process.join()
    process.join(timeout)


class PyzProcess(multiprocessing.Process):
    """
    Class to handle things about multi-process programming.
    """

    @classmethod
    def help(cls):
        print "<--Class %s-->" % cls.__name__
        print cls.__doc__

    def __init__(self, func, lock, daemon):
        multiprocessing.Process.__init__(self)
        self.func = func
        self.lock = lock
        self.daemon = daemon

    def run(self):
        """
        all the works for process to do is supposed to be done here.
        if there's a lock as input in initialization, check the lock.

        :return: no return for now
        """
        if self.lock is not None:
            self.lock.acquire()
        self.func()
        if self.lock is not None:
            self.lock.release()

