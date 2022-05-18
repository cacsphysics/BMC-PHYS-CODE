# Some basic correlation functions
import numpy as np


def correlation(sing_1, sing_2, time, normalized=True, mode='same'):
    ####################################################################
    """ Different Normalization based on the number of point considered """
    ####################################################################
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
