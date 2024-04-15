def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

    """
    h = 1e-50   丸め誤差が発生する
    return (f(x+h) - f(x)) / h  微分誤差が発生する
    """