#!/usr/bin/env python
#
# This file is part of postpic.
#
# postpic is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# postpic is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with postpic. If not, see <http://www.gnu.org/licenses/>.
#
# Copyright Stephan Kuschel 2015
#

def main():
    import timeit
    import numpy as np
    import postpic.cythonfunctions as cf

    # --- 1D

    def time1D(data, bins, weights, shape, tn):
        t = timeit.Timer(lambda: cf.histogram(data, range=(0.001,0.999), bins=bins, weights=weights, shape=shape))
        tc = t.timeit(number=5)/5.0
        ws = '       ' if weights is None else 'weights'
        print('1D, {:d} shape, {:s}: {:0.2e} sec -> factor {:5.2f} faster'.format(shape, ws, tc, tn/tc))

    bins = 1000
    npart = int(4e6)
    print('=== Histogram 1D bins: {:6d}, npart: {:.1e} ==='.format(bins, npart))
    data = np.random.random(npart)
    weights = np.random.random(npart)
    # time numpy function
    t = timeit.Timer(lambda: np.histogram(data, range=(0.001,0.999), bins=bins, weights=None))
    tn = t.timeit(number=2)/2.0
    t = timeit.Timer(lambda: np.histogram(data, range=(0.001,0.999), bins=bins, weights=weights))
    tnw = t.timeit(number=2)/2.0
    print('numpy        : {:0.2e} sec'.format(tn))
    print('numpy weights: {:0.2e} sec'.format(tnw))
    time1D(data, bins, None, 0, tn)
    time1D(data, bins, weights, 0, tnw)
    time1D(data, bins, None, 1, tn)
    time1D(data, bins, weights, 1, tnw)
    time1D(data, bins, None, 2, tn)
    time1D(data, bins, weights, 2, tnw)

    # --- 2D

    def time2D(datax, datay, bins, weights, shape, tn):
        t = timeit.Timer(lambda: cf.histogram2d(datax, datay, range=((0.01,0.99),(0.01,0.99)), bins=bins, weights=weights, shape=shape))
        tc = t.timeit(number=3)/3.0
        ws = '       ' if weights is None else 'weights'
        print('2D, {:d} shape, {:s}: {:0.2e} sec -> factor {:5.2f} faster'.format(shape, ws, tc, tn/tc))

    bins = (1000,700)
    npart = int(4e6)
    print('=== Histogram 2D bins: {:6s}, npart: {:.1e} ==='.format(str(bins), npart))
    datax = np.random.rand(npart)
    datay = np.random.rand(npart)
    weights = np.random.random(npart)
    # time numpy function
    t = timeit.Timer(lambda: np.histogram2d(datax, datay, range=((0.01,0.99),(0.01,0.99)), bins=bins, weights=None))
    tn = t.timeit(number=1)/1.0
    t = timeit.Timer(lambda: np.histogram2d(datax, datay, range=((0.01,0.99),(0.01,0.99)), bins=bins, weights=weights))
    tnw = t.timeit(number=1)/1.0
    print('numpy        : {:0.2e} sec'.format(tn))
    print('numpy weights: {:0.2e} sec'.format(tnw))
    time2D(datax,datay, bins, None, 0, tn)
    time2D(datax, datay, bins, weights, 0, tnw)
    time2D(datax,datay, bins, None, 1, tn)
    time2D(datax, datay, bins, weights, 1, tnw)
    time2D(datax,datay, bins, None, 2, tn)
    time2D(datax, datay, bins, weights, 2, tnw)


    # --- 3D

    def time3D(datax, datay, dataz, bins, weights, shape, tn):
        t = timeit.Timer(lambda: cf.histogram3d(datax, datay, dataz, range=((0.01,0.99),(0.01,0.99),(0.01,0.99)), bins=bins, weights=weights, shape=shape))
        tc = t.timeit(number=1)/1.0
        ws = '       ' if weights is None else 'weights'
        print('3D, {:d} shape, {:s}: {:0.2e} sec -> factor {:5.2f} faster'.format(shape, ws, tc, tn/tc))

    bins = (200,250,300)  # 15e6 Cells
    npart = int(4e6)
    print('=== Histogram 3D bins: {:6s}, npart: {:.1e} ==='.format(str(bins), npart))
    datax = np.random.rand(npart)
    datay = np.random.rand(npart)
    dataz = np.random.rand(npart)
    weights = np.random.random(npart)
    # time numpy function
    t = timeit.Timer(lambda: np.histogramdd((datax, datay, dataz), range=((0.01,0.99),(0.01,0.99),(0.01,0.99)), bins=bins, weights=None))
    tn = t.timeit(number=1)/1.0
    t = timeit.Timer(lambda: np.histogramdd((datax, datay, dataz), range=((0.01,0.99),(0.01,0.99),(0.01,0.99)), bins=bins, weights=weights))
    tnw = t.timeit(number=1)/1.0
    print('numpy        : {:0.2e} sec'.format(tn))
    print('numpy weights: {:0.2e} sec'.format(tnw))
    time3D(datax, datay, dataz, bins, None, 0, tn)
    time3D(datax, datay, dataz, bins, weights, 0, tnw)
    time3D(datax, datay, dataz, bins, None, 1, tn)
    time3D(datax, datay, dataz, bins, weights, 1, tnw)
    time3D(datax, datay, dataz, bins, None, 2, tn)
    time3D(datax, datay, dataz, bins, weights, 2, tnw)

if __name__=='__main__':
    main()

