def image_plot(filename):
    import numpy as np
    from astropy.io import fits
    from astropy.wcs import WCS
    wcs = WCS(image[0].header)
    import matplotlib.pyplot as plt
    ax = plt.subplot(projection=wcs)   #normally has a projection=... keyword
    ax.imshow(image[0].data, origin='lower')
    ax.coords.grid(image[0].data,grid_type='contours',color='white',linewidth=0.3,linestyle='dashed')
    
image_plot('WISE_12.fits')
