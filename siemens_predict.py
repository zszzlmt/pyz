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


def drop_center(data, datetime, frac=5):
    data['L2'] = L2(data)
    L2_group = framing(data, datetime, ['L2'])
    tb = L2_group['L2'].agg({'top': lambda x: np.percentile(x, 100 - frac)})

    data_me = pd.merge(left=data, right=tb, left_on='datetime_sec', right_index=True)

    data_drop_center = data_me[data_me['L2'] > data_me['top']]

    data_drop_center_group = data_drop_center.groupby('datetime_sec')
    L2_sec_mean = data_drop_center_group['L2'].mean()
    log_L2_sec_mean = np.log(L2_sec_mean)

    return log_L2_sec_mean

def calZCR(my_array):
    my_array = np.array(my_array)

    preState = 0  # 0+1-
    if my_array[0] < 0:
        preState = 1

    res = 0
    for i in my_array:

        if (i > 0 and preState == 1) or (i < 0 and preState == 0):
            preState = 1 - preState
            res = res + 1
    res = float(res) / len(my_array)


def L2(data):

    return np.sqrt(((data) ** 2).sum(axis=1))

def framing(data, datetime, columns):
    if 'datetime_sec' not in data.columns:
        data['datetime_sec'] = datetime.map(lambda x: x - timedelta(microseconds=x.microsecond))
    return data[columns + ['datetime_sec']].groupby('datetime_sec')


def buildFeature(data):
    L2_train = pd.DataFrame(drop_center(data[['X_VALUE', 'y_VALUE', 'z_VALUE']], data['TIME']), columns=['L2'])
    zcr_group = framing(data, data.index, ['X_VALUE', 'y_VALUE', 'z_VALUE'])

    zc = zcr_group[['X_VALUE', 'y_VALUE', 'z_VALUE']].agg({'ZCR': calZCR})
    zc['ZCR_sum'] = zc['ZCR'].sum(axis=1)

    attr = pd.merge(zc[['ZCR_sum']], L2_train, left_index=True, right_index=True)
    attr.columns = ['ZCR_sum', 'L2']

    return attr

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

    # model_path = './models/2017-08-16 12-46-49_cluster.model'
    # model = joblib.load( model_path )
    #
    # feature = buildFeature( data )
    # pre = pd.Series( model.predict( feature ), index = feature.index )
    #
    # return mode( pre )

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
