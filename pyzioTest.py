#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name:
#   pyzioTest.py
#
# Describe:
#
#   This file is used to test the lib file pyzio.py. The test
# cases can also be founded in test docs.
#
# File start at:
#   2017-09-11
#
# Last edit at:
#   2017-09-12
#
# Author:
#   Yeo Zach
#
# Contact me by:
#   zsz100e@126.com
#
# ALL rights reserved
#

import pyzio as tar#target

#
# function "ioD1Test":
#
def ioD1Test( ):

    # caseNo X.
    # all the cases in X are supposed to be interrupted
    # with an error thrown out

    # X No1:
    # simple one dimension empty List
    # supposed to be two errors, one in save, one in load
    # and no caseNoX1.txt file can be found
    a = []
    tar.saveListD1( a, '.\caseNoX1.txt' )
    b = tar.loadListD1( '.\caseNoX1.txt' )

    del a[ : ]
    del b[ : ]

    # X No2:
    # supposed input list is not a instance of list
    # supposed to be two errors, one in save, one in load
    # and no caseNoX2.txt file can be found
    a = 'Not a List'
    tar.saveListD1( a, '.\caseNoX2.txt' )
    b = tar.loadListD1( '.\caseNoX2.txt' )

    del a[ : ]
    del b[ : ]

    # caseNo 0.
    # simple one dimension int list
    # using save mode 'w' and load mode 'int'
    a = range( 0, 10 )
    tar.saveListD1( a, '.\caseNo0.txt' )
    b = tar.loadListD1( '.\caseNo0.txt', 'int' )
    printResult( a, b, 0 )

    del a[ : ]
    del b[ : ]

    # caseNo 1.
    # simple one dimension int list
    # using save mode 'a' and load mode 'int'
    fir = range( 0, 10 )
    sec = range( 10, 20 )
    a = fir + sec
    tar.saveListD1( fir, '.\caseNo1.txt' )
    tar.saveListD1( sec, '.\caseNo1.txt', 'a' )
    b = tar.loadListD1( '.\caseNo1.txt', 'int' )
    printResult( a, b, 1 )

    del fir[ : ]
    del sec[ : ]
    del a[ : ]
    del b[ : ]

    # caseNo 2.
    # simple one dimension string list
    # using save mode 'w' and load mode 'string'
    a = [ 'a', 'b', 'c', 'd' ]
    tar.saveListD1( a, '.\caseNo2.txt' )
    b = tar.loadListD1( '.\caseNo2.txt' )
    printResult( a, b, 2 )

    del a[ : ]
    del b[ : ]

    # caseNo 3.
    # simple one dimension string list
    # using save mode 'a' and load mode 'string'
    fir = [ 'a', 'b', 'c', 'd' ]
    sec = [ 'e', 'f', 'g', 'h' ]
    a = fir + sec
    tar.saveListD1( fir, '.\caseNo3.txt' )
    tar.saveListD1( sec, '.\caseNo3.txt', 'a' )
    b = tar.loadListD1( '.\caseNo3.txt' )
    printResult( a, b, 3 )

    del fir[ : ]
    del sec[ : ]
    del a[ : ]
    del b[ : ]

    # caseNo 4.
    # simple one dimension float list
    # using save mode 'w' and load mode 'float'
    a = [ 2315.125, 56233.15, 560.1, 54.301 ]
    tar.saveListD1( a, '.\caseNo4.txt' )
    b = tar.loadListD1( '.\caseNo4.txt', 'float' )
    printResult( a, b, 4 )

    del a[ : ]
    del b[ : ]

    # caseNo 5.
    # simple one dimension floatlist
    # using save mode 'a' and load mode 'float'
    fir = [ 2315.125, 56233.15, 560.1, 54.301 ]
    sec = [ 876.415, 87.51, 1634584.55, 40.23 ]
    a = fir + sec
    tar.saveListD1( fir, '.\caseNo5.txt' )
    tar.saveListD1( sec, '.\caseNo5.txt', 'a' )
    b = tar.loadListD1( '.\caseNo5.txt', 'float' )
    printResult( a, b, 5 )

    del fir[ : ]
    del sec[ : ]
    del a[ : ]
    del b[ : ]

#
# function "printResult":
#
def printResult( a, b, no = 0 ):

    print 'Test case No %d.' % no
    print '_________________'
    print 'Supposed output:'
    print 'Content:'
    print a
    print 'Total type:'
    print type( a )
    print 'Member type:'
    print type( a[ 0 ] )
    print '_________________'
    print 'Module ouyput:'
    print 'Content:'
    print b
    print 'Total type:'
    print type( b )
    print 'Member type:'
    print type( b[ 0 ] )
    print '_________________\n'


