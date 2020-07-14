from PyAstronomy import pyasl
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def readSpec(filename, path):
    
    sp = fits.open(path + filename)
    header = sp[0].header
      
    tf = sp[0].data
    tf = tf.flatten()
 
    wvl, flx = pyasl.read1dFitsSpec(path + filename)
 
    sp.close()

    date_obs = header['DATE']

    return header, wvl, flx, date_obs, tf

def saveSpec(filename, header, wave, flux, date_obs):
    print("Fecha obs:")
    print(date_obs)
     
    header['CRVAL1'] = wave[0]
    header['DATE'] = date_obs
    hdu = fits.PrimaryHDU(flux, header)
    hdu.writeto(filename, overwrite=True) 

def onClick(event):
    #global ix, iy
    ix, iy = event.xdata, event.ydata

    #global coords
    coords.append((ix, iy))

    if len(coords) == points:
        fig.canvas.mpl_disconnect(cid)
        plt.close()  

def plotSpectrum(wavelength, flux, legend):
    
    fig = plt.figure(figsize=(15,5))  #best: 15,5, but 6,4 is good for small size
    axes= fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(wavelength, flux)
    plt.xlabel(legend)
    plt.ylabel('flux')
    plt.show()

def resolution(wavelength):
    
    waveini = wavelength[0]
    waveend = wavelength[-1]
    res = np.abs(waveini - waveend)/len(wavelength)
    print("Waveini: " + str(waveini))
    print("Waveend: " + str(waveend))
    print("Resolution: " + str(res) + " A")
    print("Dimension array: " + str(len(wavelength)))
    
    return waveini, waveend, res

def normalize(wavelength, flux, coords):

    px = []
    py = []
    px = np.array(list(x[0] for x in coords))
    py = np.array(list(y[1] for y in coords))
    
    gr = int(input("Enter polynome grade to fit: "))    
    z = np.polyfit(px, py, gr) 
    
    p = np.poly1d(z)
    flux_n = flux / p(wavelength)
    
    return flux_n

### Core Program #####################

path = "/home/fran/PythonProjects/TFM/BD+532790/Normalizados_2017/"

fileSpectrum = input ("Enter spectrum to analyze:")
fileSpectrum += ".fits"
points = int(input("Enter number of points to fit normalization: "))

#Reading spectrum
header, wavelength, flux, date_obs, tf = readSpec(fileSpectrum, path)
print("All data")

#Plot spectrum and set normalization points
resolution(wavelength)
fig = plt.figure(figsize=(15,5))  #best: 15,5, but 6,4 is good for small size
axes= fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(wavelength, flux)
plt.xlabel('wavelength (A)')
plt.ylabel('flux')

coords = []
cid = fig.canvas.mpl_connect('button_press_event', onClick)
plt.show()

#Normalize and plot
flux_n = normalize(wavelength, flux, coords)
plotSpectrum(wavelength, flux_n, "wavelength(A)")

#Saving spectrum
saveData = input("Save normalized spectrum (y/N)?")
if saveData =="y":    
    fileSpectrum = input("Enter spectrum name:")
    fileSpectrum +=".fits"
    saveSpec(fileSpectrum, header, wavelength, flux_n, date_obs)
    print("Spectrum saved!")

print("End")
