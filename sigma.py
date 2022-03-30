def sigma(array):
    avg = sum(i for i in array) / len(array)
    sum_ = sum(((i - avg) ** 2) for i in array)
    return (sum_ / len(array)) ** .5
