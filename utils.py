import matplotlib.pyplot as plt


def linear_line(x,intercept,slope):
    """[summary]
    compute the output of a linear line

    Args:
        x ([type]): [description]
        intercept (number): [description]
        slope (number): [description]

    Returns:
        [type]: [description]
    """
    return slope * x + intercept


def plot_with_residual(target_plt,X,Y,intercept,slope,color='g',linewidth=3):
    """[summary]
    plot data set X,Y vs linear line and residual i.e. the distance between actual - Y[i] and estimated - h[i]
    
    Args:
        target_plt () : e.g. plt or axs (plt.subplots)
        X ([number]): vector input
        Y ([number]): vector output
        intercept (number): value of linear line @ x=0
        slope (number): slope of linear line
        color (str, optional): color of residual line. Defaults to 'g'.
        linewidth (int, optional): width of residual line. Defaults to 3.
    """
    h = linear_line(X,intercept,slope)
    target_plt.plot(X,Y,'o',X,h)
    m = X.size
    i = 0
    while i < m:
        target_plt.plot([X[i],X[i]],[h[i],Y[i]],color=color,linewidth=linewidth)
        i += 1
