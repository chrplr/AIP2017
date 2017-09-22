#! /usr/bin/env python
# Time-stamp: <2016-08-03 16:49:04 cp983411>

""" Generate an EPI containing sinewaves, along time and Z dimensions.
Useful to test slice timing algorithms """

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")

shape = (64, 64, 40, 90)
nx, ny, nz, nt = shape

TR = 2000. 
#slices_times = np.array([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800] * 4) 
slices_times = np.linspace(0, 1950, nz) 
assert len(slices_times) == nz

PERIOD = 6000.

data = np.empty(shape, dtype='<i2')

slices = np.empty((nz, nt), dtype='<i2')

for t in range(nt):
     for k in range(nz):
         slices[k, t] = 500. + 100. *  \
                        np.sin(2. * np.pi * (t*TR + slices_times[k])/PERIOD)
#         slices[k, t] = 100. + 30. *  \
#                        np.sin(2. * np.pi * (slices_times[k]/TR))

for i in range(nx):
    for j in range(ny):
        data[i, j, :, :] = slices


# for t in range(nt):
#     for i in range(nx):
#         for j in range(ny):
#             for k in range(nz): 
#                 data[i, j, k, t] = 100. + 30. *  \
#                                    np.sin(2. * np.pi * (slices_times[k]/TR + t/10.))

slice_0 = data[26, :, :, 10]
slice_1 = data[:, 30, :, 10]
slice_2 = data[:, :, 16, 10]
show_slices([slice_0, slice_1, slice_2])
plt.suptitle("Center slices for EPI image") 
plt.show()

affine = np.array([[ -3.        ,   0.        ,   0.        ,  92.],
                   [  0.        ,   3.        ,   0.        , -92.],
                   [  0.        ,   0.        ,   3.        , -40.],
                   [  0.        ,   0.        ,   0.        ,   1.]])

new_image = nib.Nifti1Image(data, affine)
nib.save(new_image, "sinewave_50.nii")
