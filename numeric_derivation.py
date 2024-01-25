
def derive(f, x, h=0.0001):
    numeric_derivation = (f(x+h)-f(x))/h
    return numeric_derivation