import multiprocessing

def function_square(data):
    result = data * data
    return result



inputs = list(range(1000000))
pool = multiprocessing.Pool(processes=10)
pool_outputs = pool.map(function_square, inputs)
pool.close()
pool.join()
print("Pool :", pool_outputs)