def central_difference_h2(f,x,h):
    return [(f(X+h)-f(X-h))/(2*h)for X in x]
