from matplotlib.colors import SymLogNorm
import matplotlib.pyplot as plt
import numpy
from matplotlib import mlab, cm
from scipy.interpolate import interp1d

def interp(r):
    s = interp1d(numpy.arange(len(r)), r)
    xnew = numpy.arange(0, len(r)-1, .1)
    return s(xnew)

#sname = ['Session-25/R_pcb_pat','Session-25/R_piezo_pat','Session-25/R_pcb_tibmed','Session-25/R_piezo_tibmed',
#       'Session-26/R_pcb_pat','Session-26/R_piezo_pat','Session-26/R_pcb_tibmed','Session-26/R_piezo_tibmed',
#        'Session-27/R_pcb_pat','Session-27/R_piezo_pat','Session-27/R_pcb_tibmed','Session-27/R_piezo_tibmed',
#        'Session-30/R_pcb_pat','Session-30/R_piezo_pat','Session-30/R_piezo_pat2','Session-30/R_pcb_tiblat',
#        'Session-30/R_piezo_tiblat','Session-30/R_pcb_tiblat2']

prename = 'Session-38/0/'
names = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
ang = ['1_ang','2_ang','3_ang','4_ang','5_ang','6_ang','7_ang','8_ang','9_ang','10_ang','11_ang','12_ang','13_ang','14_ang','15_ang']

event_total = []
amp_total = []

xs = range(len(names))
ys = range(len(names))

click_total = range(len(names))
rescale_time = []

ext_ang_total = range(len(names))
flex_ang_total = range(len(names))

energy_total = []

extend_energy = range(len(names))
flex_energy = range(len(names))

extend_ang = range(len(names))
flex_ang = range(len(names))

samp_total = []
time_total = []

ext_total = range(len(names))
flex_total = range(len(names))

z_axis = range(len(names))

sav_exenergy = range(len(names))
sav_exang = range(len(names))


sav_fenergy = range(len(names))
sav_fang = range(len(names))

for num in range(len(names)):
        if __name__ == "__main__":

	   from scipy.io import wavfile
	   import argparse

	   # segmented by hand, 4 good measurements
	   parser = argparse.ArgumentParser()
	   parser.add_argument("file", type=argparse.FileType('r'), help="file to read", nargs="?", default=None)
	   parser.add_argument("-s","--save", type=argparse.FileType('w'), help="save figure to file")
	   args = parser.parse_args()
	   if not args.file:
	       fname = prename + names[num] + '.wav'
	       ang_name = prename + ang[num] + '.wav'
	   else:
	       fname = args.file.name
	       
           #input
           fs, samples = wavfile.read(fname)
           fs, angles = wavfile.read(ang_name)
           samples = numpy.array(samples, dtype = float)
	   noise_percentile = 0.75
	   event_threshold = 20
    
	   s = abs(samples)

	   s_sorted = numpy.sort(s)
	   noise_amplitude_estimate = s_sorted[int(len(s_sorted)*noise_percentile)]
	  
	   #Define rescale factor
	   rescale = 500
	   
	   # find events
	   ind = mlab.find(s>noise_amplitude_estimate*event_threshold)
	   # rescale to 500 samples to account for different speeds
	   ind_rescale = rescale*ind/len(s);
	   event_acc = numpy.zeros(len(s))
	   event_acc[ind] = s[ind];
	   event_acc_rescale = numpy.zeros(rescale)
	   event_acc_rescale[ind_rescale] = s[ind]/noise_amplitude_estimate # store relative strengths
	      
	   # Compiled clicks
	   click_total[num] = event_acc_rescale
	   rescale_time = numpy.concatenate((rescale_time, range(rescale)))
	   # Energy over angle
	   divider = numpy.argmax(angles)
	   energy_total = numpy.concatenate((energy_total, s))
	   
	   #For 'up' movmement
	   exenergy = s[0:divider]
	   exang = numpy.array(angles[0:divider],dtype=int)

	   scale_exang = range(0,91)
	   scale_exenergy = numpy.zeros(91)
	   exang_set = numpy.sort(list(set(scale_exang)))
	   
	   for n in range(len(exang_set)):
	       angle = exang_set[n]
	       pos = mlab.find(exang==angle)
	       av_energy = numpy.sum(exenergy[pos])
	       scale_exenergy[angle] = av_energy
	   
	   sav_exenergy[num] = scale_exenergy
	   sav_exang[num] = scale_exang
	   
	   	   	   
	   #For 'down' movement
	   fenergy = s[divider:]
	   fang = numpy.array(angles[divider:],dtype=int)
	   
	   scale_fang = range(0,91)
	   scale_fenergy = numpy.zeros(91)
	   fang_set = numpy.sort(list(set(scale_fang)))
	   
	   for n in range(len(fang_set)):
	       angle = fang_set[n]
	       pos = mlab.find(fang==angle)
	       av_energy = numpy.sum(fenergy[pos])
	       scale_fenergy[angle] = av_energy
	   
	   sav_fenergy[num] = scale_fenergy
	   sav_fang[num] = scale_fang
	   
	   flex_energy = numpy.concatenate((flex_energy,fenergy))
	   flex_ang = numpy.concatenate((flex_ang,fang))
   
	   #Create sets for time, amplitude storage (mean value stored, not last value 'read')   
	       
	   #Compiled
	   samp_total = numpy.concatenate((samp_total, samples))
	   time_total = numpy.concatenate((time_total, range(len(samples))))

#output
fig = plt.figure()
ax = fig.add_subplot(111)

new_ext = numpy.vstack([interp(r) for r in sav_fenergy])

ax.imshow(new_ext,aspect='auto',interpolation='nearest',cmap=cm.jet, norm=SymLogNorm(linthresh=10),vmin=1000)
plt.title('EXTENSION: Signal Energy for ' + prename)
plt.xlabel('Knee Angle (degrees)')
plt.ylabel('Measurement Segment')
plt.xticks(range(0,901,100),range(0,91,10))
plt.yticks(range(15),range(1,16))
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111)

new_flex = numpy.vstack([interp(r) for r in sav_exenergy])

ax.imshow(new_flex,aspect='auto',interpolation='nearest',cmap=cm.jet, norm=SymLogNorm(linthresh=10),vmin=1000)
plt.title('FLEXION: Signal Energy for '+prename)
plt.xlabel('Knee Angle (degrees)')
plt.ylabel('Measurement Segment')
plt.xticks(range(0,901,100),range(0,91,10))
plt.yticks(range(15),range(1,16))
plt.show()
