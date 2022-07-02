import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm
"""
This python script implementing parallization.
"""
num_cores = multiprocessing.cpu_count() #outputs the total number of cpus.
inputs = [*range(1, 1000)]

inputs = tqdm(inputs)


def processInput(i):
    return i * i


if __name__ == "__main__":
    print(inputs)
    processed_list = Parallel(n_jobs=num_cores)(delayed(processInput)(i)
                                                for i in inputs)
    # n_jobs=num_cores as is currently defined uses all the cpus available, this should be avoided if running on a servers with mutliple users. 
    # Set tn_jobs or num_cores above.
    print(processed_list)
