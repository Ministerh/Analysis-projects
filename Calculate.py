import numpy as np

def Calculate(list):
    if len(list) < 9:
        raise ValueError ('list must contain nine  numbers')
    input_list = np.array(list)
    matrix = input_list.reshape(3,3)

    row_mean = matrix.mean(axis=1).tolist()
    column_mean = matrix.mean(axis=0).tolist()
    mean = matrix.mean()

    row_variance = matrix.var(axis=1).tolist()
    column_variance = matrix.var(axis=0).tolist()
    variance = matrix.var()

    row_std = matrix.std(axis=1).tolist()
    column_std = matrix.std(axis=0).tolist()
    std = matrix.std()

    row_max = matrix.max(axis=1).tolist()
    column_max = matrix.max(axis=0).tolist()
    max = matrix.max()

    row_min = matrix.min(axis=1).tolist()
    column_min = matrix.min(axis=0).tolist()
    min = matrix.min()

    row_sum = matrix.sum(axis=1).tolist()
    column_sum = matrix.sum(axis=0).tolist()
    sum = matrix.sum()

    calculations = {

        'mean': [column_mean, row_mean, mean],
        'variance': [column_variance, row_variance, variance],
        'standard deviation': [column_std, row_std, std],
        'max': [column_max, row_max, max],
        'min': [column_min, row_min, min],
        'sum': [column_sum, row_sum, sum]
        
    } 
    return calculations

