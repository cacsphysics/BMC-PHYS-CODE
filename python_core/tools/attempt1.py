import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm

num_cores = multiprocessing.cpu_count()
inputs = [*range(1, 1000)]

inputs = tqdm(inputs)


def processInput(i):
    return i * i


if __name__ == "__main__":
    print(inputs)
    processed_list = Parallel(n_jobs=num_cores)(delayed(processInput)(i)
                                                for i in inputs)

    print(processed_list)
