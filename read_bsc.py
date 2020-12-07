import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

from math import tau, exp, tanh
from tabulate import tabulate

from astro import *

# Read the contents of the catalogue into an array with each line
filename = 'bsc5/bsc5.dat'
with open(filename, 'r') as f:
    data = f.readlines()

# This function takes a name as it appears in the Bright Star Catalogue, and
# cleans it up.
def sanitize_name(name):
    assert len(name) == 14

    # Obtain the relevant fields.
    hr_number           = name[0:4].strip()
    flamsteed_number    = name[4:7].strip()
    bayer_letter        = name[7:11].strip()
    constellation       = name[11:14].strip()

    # Sanitize the name based on the following cases.
    sanitized_name = None
    if 'NOVA' in name:
        sanitized_name = name[4:14].strip()
    elif bayer_letter == '':
        if flamsteed_number == '':
            sanitized_name = 'HR' + ' ' + hr_number
        else:
            sanitized_name = flamsteed_number + ' ' + constellation
    else:
        sanitized_name = bayer_letter + ' ' + constellation

    return sanitized_name

# Plot a set of stars
def plot_stars(stars):
    fig = plt.figure()
    ax = plt.axes(
            #projection = ccrs.Robinson(central_longitude = -270),
            projection = ccrs.NorthPolarStereo(),
            )
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    #ax.outline_patch.set_edgecolor('white')
    ax.spines['geo'].set_edgecolor('white')
    ax.set_aspect('equal')


    # Limit the map to 45 degrees latitude and above.
    ax.set_extent([-180, 180, 90, 30], ccrs.PlateCarree())

    # Compute a circle in axes coordinates, which we can use as a boundary
    # for the map. We can pan/zoom as much as we like - the boundary will be
    # permanently circular.
    theta = np.linspace(0, tau, 1000)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    #ax.set_boundary(circle, transform=ax.transAxes)

    threshold = 3.5
    stars = filter(lambda s: s.magnitude < 5, stars)
    for star in stars:
        ax.plot(
                -star.ra * 360/tau,
                star.dec * 360/tau,
                'bo',
                transform = ccrs.PlateCarree(),
                markersize = 4 * star.magnitude_to_radius(),
                color = 'white',
                )

    #plt.title('World')
    #ax.coastlines()
    #ax.set_global()
    plt.show()

# We will now read the data and create a Star object for each entry.
stars = set()
for line in data:
    # Read the relevant fields.
    name    = line[0:14]
    RAh     = line[75:77]
    RAm     = line[77:79]
    RAs     = line[79:83]
    DE_sign = line[83]
    DEd     = line[84:86]
    DEm     = line[86:88]
    DEs     = line[88:90]
    Vmag    = line[102:107]

    # Sanitize the name
    name = sanitize_name(name)

    # Calculate declination and right ascension in radians.
    if line[75:107].strip() == '':
        continue
    Vmag = float(Vmag)
    RAh = float(RAh)
    RAm = float(RAm)
    RAs = float(RAs)
    sign = float(DE_sign + '1')
    DEd = float(DEd)
    DEm = float(DEm)
    DEs = float(DEs)
    ra = (tau/24) * (RAh + (1/60) * (RAm + (1/60) * RAs))
    dec = (tau/360) * sign * (DEd + (1/60) * (DEm + (1/60) * DEs))

    # Create the star object, and add it to the `stars` set.
    star = Star(name, ra, dec, Vmag)
    stars.add(star)

'''
table = tabulate(
        [[s.name,
            '%.2f' % s.ra,
            '%.2f' % s.dec,
            '%.2f' % s.magnitude] for s in stars],
        headers = ['Name', 'RA', 'Dec', 'Mag'])

print(table)
'''

plot_stars(stars)
