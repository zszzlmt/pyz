import numpy as np
import pandas as pd
from sklearn.externals import joblib
from datetime import datetime, timedelta
import random

def mode( x ):

    if len( x ) == 0:

        return -1

    di = { }
    for i in x:
        if i not in di :

            di[ i ] = 0

        else:

            di[i] += 1

    return max( di, key = lambda key : di[ key ] )

def identify_human( data ):

    if mode( data ) == 1:

        return 1

    else:

        return 0

def identify_distance( data ):

    if max( data ) < 100:

        return 1

    else:

        return 0

def identify_current(data):

	dm = float( sum( data ) ) / len( data )

	if dm < 20:

		return 0

	elif ( dm > 20 ) and ( dm < 130 ):

		return 2

	else:

		return 1

def identify_vib( data ):

    return random.randint( 0, 2 )

def predict( vib, human, distance, current ):

    res = [ ]
    tmp_res = [ ]
    l = len( human )

    for id in np.arange( l ):

        tmp_dict = { 'x' : vib.iloc[ id, 0 ], 'y' : vib.iloc[ id, 1 ], 'z' : vib.iloc[ id, 2 ] }
        vib_tf = pd.DataFrame( tmp_dict )

        tmp_res.append( identify_vib( vib_tf ) )
        tmp_res.append( identify_human( human[ id ] ) )
        tmp_res.append( identify_distance( distance[ id ] ) )
        tmp_res.append( identify_current( current[ id ] ) )

        res.append( tmp_res )
        tmp_res = [ ]

    return res
