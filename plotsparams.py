# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:31:40 2013

@author: tisimst
"""
import matplotlib.pyplot as plt
import skrf as rf
def plotsparams(fin, n=None, m=None, scale='db', title=None):
    """
    S-Parameter plotter
    
    Parameters
    ----------
    fin : str
        Input file name, preferrably an '.s?p' file.
    n : int
        Output port number (zero-based)
    m : int
        Input port number (zero-based)
    scale : str
        The following are valid values: 'db', 'mag', 're', 'im'. An error
        occurs for all others.
    title : str
        A custom plot title.
        
    Examples
    --------
    ::
        
        fin = 'filter.s2p'
        
        # Plot S2,1 on dB scale
        plotsparams(fin, 1, 0, 'Filter $S_{2 1}$')
        
        # Plot S1,1 on linear scale
        plotsparams(fin, 0, 0, scale='mag', 'Filter $S_{1 1}$')
    
    """
    ntwk = rf.Network(fin)
    
    if scale=='db':
        ntwk.plot_s_db(n=n, m=m)
    elif scale=='mag':
        ntwk.plot_s_mag(n=n, m=m)
    elif scale=='re':
        ntwk.plot_s_re(n=n, m=m)
    elif scale=='im':
        ntwk.plot_s_im(n=n, m=m)
    else:
        raise ValueError, 'Invalid value for keyword "scale": {:}'.format(scale)
    
    if title is not None and isinstance(title, str):
        plt.title(title)
    
    plt.show()

if __name__=='__main__':
    import sys, os
    
    def display_help():
        print 'Basic S-Parameter plotter\n'
        print 'Syntax: plotsparams [OPTIONS]\n'
        print 'Valid Options:'
        print '  -i            Input ".s?p" file name'
        print '  -n            Output port number'
        print '  -m            Input port number'
        print '  -s, --scale   Plot scale, "db", "mag", "re", "im"'
        print '  -t, --title   Plot title'
        print '  -h, --help    Display this help and exit'
        exit(0)
        
    if len(sys.argv)==1:
        display_help()
    
    fin = None
    n = None
    m = None
    scale = 'db'
    title = None
        
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg=='-i':
            fin = args[i + 1]
        elif arg=='-n':
            n = int(args[i + 1])
        elif arg=='-m':
            m = int(args[i + 1])
        elif arg=='-s' or arg=='--scale':
            scale = args[i + 1]
        elif arg=='-t' or arg=='--title':
            title = args[i + 1]
        elif arg=='-h' or arg=='--help':
            display_help()
    
    if fin is None or not os.path.isfile(fin):
        print '**ERROR: Input file name invalid or file does not exist'
        exit(-1)
    if not any([scale=='db', scale=='mag', scale=='re', scale=='im']):
        print '**ERROR: Invalid plot scale'
        exit(-1)
    
    plotsparams(fin, n, m, scale, title)
