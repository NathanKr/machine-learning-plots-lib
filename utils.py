import matplotlib.pyplot as plt


def linear_line(x,intercept,slope):
    return slope * x + intercept

def plot_with_residual(X,Y,intercept,slope,color='g',linewidth=3):
    h = linear_line(X,intercept,slope)
    plt.plot(X,Y,'o',X,h)
    m = X.size
    i = 0
    while i < m:
        plt.plot([X[i],h[i]],[X[i],Y[i]],color=color,linewidth=linewidth)
        i += 1
