import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(np.int64) #np.intでは、実行時に非推奨である文が表示された。


x = np.array([-1.0, 1.0, 2.0])
print(step_function(x))