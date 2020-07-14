## Spectral-Disentangling

#### A collection of scripts to disentangle spectroscopic binary stars spectra

Here are a serie of scripts I developed in order to process spectra in the standard fits format, with the aim to test and apply the algoritm of spectral disentangling based in the algoritm developed by Marchenko et al. (1998) and succesfully applied by González and Levato (2006). 

PyAstronomy and Astropy as main Python libraries are used on these scripts, apart from NumPy and Matplotlib.

¡¡CAUTION!! This material is currently being  builded and tested

#### Script 1: Display spectrum library

This script is used only to display a collection of fits spectra located in a specified library, in order to experiment with basis of fits management.

#### Script 2: Retail spectrum

This script retails a fits spectrum introducing the initial and final lambda.

#### Script 3: Degrading spectra

Sometimes it is necessary to introduce noise into a spectrum, especially synthetic ones. This script allows to introduce random noise using the NumPy utility "random.normal".

#### Script 4: Broadening spectra

This script uses the utility rotBroad from PyAstronomy. It is a heavy process that requires some time in order to run all the operations, especially with high-resolution and large spectra.

#### Script 5: Doppler effect

This script can apply a Doppler shift to the overall spectrum. It reads the spectra using the library WCS, different from the other script and it can give problems with some fits files, so I suggest to implant the pyasl library if necessary.

#### Script 6: Combine 2 different spectra

In this example, we combine spectra from two different stars and, applying Doppler, obtain the combined spectrum for different radial speeds that will simulate different phases of the orbital period. A weighting factor will be introduced, so that we can vary the weight of each spectrum to the final combination.

#### Script 7: Normalize spectra

Even a full-corrected spectra will show a non-linear continuum due to the black-body energy profile that follows Planck's law. But in order to classify a spectrum or apply the disentangling algoritm, it is necessary to normalize the profile to a baseline with emission = 1.0. This script normalize all spectra but, due to an incompatibility betweem Jupyter Notebook and Matplotlib, it cannot be run under Jupyter's ipynb format, because it is necessary to work with mouse events.

You must try and click in n different points of the spectrum continuum where there is no absortion/emission lines. The program will ask you for the n value.

