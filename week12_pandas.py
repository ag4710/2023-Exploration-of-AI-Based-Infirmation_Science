import pandas as pd

data1 = {
    "a": [11, -2, 7],
    "b": [9, 0, 77],
    "c": [7, 33, 19]
}

def double(n):
    """
    x2
    :return:
    """
    return n * 2

data2 = [
            [11, 9, 7],
            [-2, 0, 33],
            [7, 77, 19],
            [7, 19]
]


df2 = pd.DataFrame(data2, index=[1, 2, 3, 4], columns=["a", "b", "c"])
print(df2)
# print(df2.apply(double))
# print(df2.apply(lambda x: x * x))

# df2 = df2.dropna()  #delete rows
df2 = df2.fillna(19.666667)  # fill mean value
# df2 = df2.fillna(19)  # fill median value
print(df2)
print(df2.describe())
