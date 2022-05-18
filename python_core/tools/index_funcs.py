# list of useful functions for analysis

from numpy import where, abs, min


def tindex(time_arr, time_value, delta=2e-2):
    """ Outputs the index of given timevalue
    Inputs: timearr, timevalue, delta
        time_arr: numpy 1-D array of time values
        time_value: time value of interest
    Optional Inputs: delta
        delta: residual error for time value
    Outputs: tind
        tind: the index of corresponding to timevalue
    """
    tind = where(abs((time_arr)-(time_value)) < delta)
    tind = tind[0][0]
    return tind


def tindex_min(time_arr, time_value):
    """ Outputs the index of given timevalue based on 
        the lowerbound.
    Inputs: time_arr, time_value
        time_arr: numpy 1-D array of time values
        time_value: number of interest
    Outputs: tind
        tind: the index of corresponding time_value
    """
    min_val = min(abs((time_arr)-time_value))
    tind = where(abs((time_arr)-(time_value)) == min_val)
    tind = tind[0][0]
    return tind


def tindex_near(time_arr, time_value, threshold):
    """ Output the index of value of interest based on 
    the closest value to value of interest.
    Inputs: time_arr, time_value, threshold
        time_arr: numpy 1-D array
        time_value: value of interest
        threshold: threshold value
    Outputs:
        tinds: 1-D array of values falling within the threshold.
    """
    tinds = where(abs(time_arr-time_value) < threshold)
    return tinds


def first_zero(data):
    """ The index which the data reaches the first zero value.
    Inputs: data
        data: numpy 1-D array
    Outputs: zind
        zind: index of the first zero in data
    """
    for n in range(len(data)):
        zind = n
        if data[n] < 0:
            break
    return zind
