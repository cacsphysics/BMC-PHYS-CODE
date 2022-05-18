# Some basic correlation functions
import numpy as np


def correlation(sing_1, sing_2, time, normalized=True, mode='same'):
    """ Outputs the correlation between two signals.
    Inputs: sing_1, sing_2, time
        sing_1: the reference 1-dimensional data [(N,) array-like]
        sing_2: the shifting 1-dimensional data [(M,) array-like]
        time: the ordering 1-dimensional data [max(N,M) array-like]
    Optional Inputs: normalized, mode
        normalized: Boolen value to determine if you want to normalized by the number of points correlated, 
            if unsure leave this value as true.
        mode: {'full', 'same', 'valid'} the parameter is the same as the numpy.correlate() mode parameter. 
            Verbatum:
                'full'--  returns the convolution at each point of overlap, with an output shape (N + M - 1,).
                        At the end points the signals do not overlap completely and boundary effects are seen.
                'same'--  Returns the output of length max(N,M), boundary effects are still seen.
                'valid'-- Returns the output of length max(N,M) - min(N,M) + 1. The correlation is only given
                            for points where the signals overlap completely. Values outside the signal boundary 
                            have no effect.
    """

    corr = np.correlate(sing_1, sing_2, mode=mode)
    dt = time[1] - time[0]
    tau = dt*(np.arange(corr.size) - corr.size/2)

    if normalized:
        normalization = np.zeros(tau.shape)
        time_Window = time[-1] - time[0]
        if (time_Window - np.abs(tau).any())/dt >= 16000:
            normalization = dt/(time_Window - np.abs(tau) - dt)
        else:
            normalization = 1/16000
        corr = normalization*corr

    return tau, corr
