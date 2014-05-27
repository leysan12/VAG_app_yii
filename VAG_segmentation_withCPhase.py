#!/usr/bin/env python2.7
import numpy
from numpy import log10
from matplotlib import pyplot, mlab
import helpers
import time
import peak_finder
from  scipy.signal import filtfilt, iirdesign

import csv

#Script for visualizing rescaled angular measurements (0 to 90 degrees), smoothing/simplifying signals
#Moving average filter, segmentation based on relative minima and maxima

ts = time.time()

#sname = ['Session-25/R_pcb_pat','Session-25/R_piezo_pat','Session-25/R_pcb_tibmed','Session-25/R_piezo_tibmed',
#       'Session-26/R_pcb_pat','Session-26/R_piezo_pat','Session-26/R_pcb_tibmed','Session-26/R_piezo_tibmed',
#        'Session-27/R_pcb_pat','Session-27/R_piezo_pat','Session-27/R_pcb_tibmed','Session-27/R_piezo_tibmed',
#        'Session-30/R_pcb_pat','Session-30/R_piezo_pat','Session-30/R_piezo_pat2','Session-30/R_pcb_tiblat',
#        'Session-30/R_piezo_tiblat','Session-30/R_pcb_tiblat2']

session = 'Session-42/'
sname = ['c0f07a282fdbe6e86b6d6a954ed8f896-L-2014-05-07-11-02-PCB352A24-Patella-MediM4s-Basic-2-5-15']
        
        
vec_ma = list()
vec_mi = list()
vec_maxv = list()
vec_minv = list()
vec_cs = list()
vec_snr = list()
vec_nump = list()

for name in range(len(sname)):
    print 'For', sname[name]
    if __name__ == "__main__":

	   from scipy.io import wavfile
	   import argparse

	   # segmented by hand, 4 good measurements
	   parser = argparse.ArgumentParser()
	   parser.add_argument("file", type=argparse.FileType('r'), help="file to read", nargs="?", default=None)
	   parser.add_argument("-s","--save", type=argparse.FileType('w'), help="save figure to file")
	   args = parser.parse_args()
	   if not args.file:
	      	  fsamp = session + sname[name]
	   else:
		  fname = args.file.name

	   fs, samples = wavfile.read(fsamp+'.wav')
	   
	   #Apply high pass filter (fc = 500 Hz)
	   signals = helpers.hpf(samples[:,0],fs=fs,fg=500.0)
           signals = numpy.array(signals, dtype = float)
           #Separating angular values for segmentation
           angles = samples[:,1]
           

           # IIR design pass, stop (for low pass)
           Fpass = 1
           Fstop = 10

           wn = float(Fpass)/float(fs/2)
           
           # iirdesign agruements
           Wip = float(Fpass)/float(fs/2)
           Wis = float(Fstop)/float(fs/2)
           Rp = 1             # passband ripple
           As = 40            # stopband attenuation

           # The iirdesign takes passband, stopband, passband ripple, 
           # and stop attenuation.
           bc, ac = iirdesign(Wip, Wis, Rp, As, ftype='butter')  
           filt_ang = filtfilt(bc,ac, angles)
           
    	   #Rescaling angle measurements to 0-90 degrees
           mi = min(filt_ang)
           ma = max(filt_ang)
   	   ang_rescale = numpy.array(map(lambda x: 90*(x-mi)/(ma-mi), filt_ang))

	   ang_vel = numpy.gradient(ang_rescale)
      
	   peaks = list(peak_finder.maxdet(ang_rescale,20))
	   #Filtering where values are greater than 53 degrees
	   peaks = filter(lambda x: ang_rescale[x]>53, peaks)
	   
	   relmin = mlab.find(numpy.round(ang_vel, decimals = 4)==0.0000)
	   #Filtering where values are less than 40 degrees
	   relmin = filter(lambda x: ang_rescale[x]<53, relmin)
	   
	   section = list(peaks)
	   section.extend((0,len(ang_rescale)-1))
	   section = numpy.sort(section)
	   newrelmin = list()

	   #Between peaks, defining thresholds based on standard deviations
	   for pk in range(len(section)-1): 
	       pos = filter(lambda x: x>section[pk] and x<section[pk+1],relmin)
	       mean = numpy.mean(ang_rescale[pos])
	       std = numpy.std(ang_rescale[pos])
	       tokeep = filter(lambda x: ang_rescale[x]<=mean+std/2, pos)
	       newrelmin.extend(tokeep)
	   
	   #Definitions for search for max and min to the left, right
	   combined = sorted(peaks + newrelmin)
	   segments = list()
	   for pk in peaks:
	       pos = combined.index(pk)
	       segments.extend((combined[pos-1],combined[pos+1]))
	   
	   #Calibration Phase values for rescaling angular values
	   win = 50000
	   pos_1 = segments[0] + numpy.argmax(ang_rescale[segments[0]:segments[0]+win])
	   pos_2 = segments[1]-win + numpy.argmax(ang_rescale[segments[1]-win:segments[1]])
	   
	   new_mi = numpy.mean(filt_ang[0:segments[0]])
	   new_ma = numpy.mean(filt_ang[pos_1:pos_2])
	   
	   #Rescaling Angular values for storing, segmentation
	   new_angles = numpy.array(map(lambda x: 90*(x-new_mi)/(new_ma-new_mi), filt_ang))
	   
           #Find Time derivative (angular velocity)
	   new_angvel = numpy.gradient(new_angles)	   
	   
	   #Redefine segments for segmentation, storage
	   new_segs = segments[2:]
	   	   
	   #Plot generation
	   pyplot.figure()
	   pyplot.plot(new_angles,'b',lw=1)
	   pyplot.plot(peaks[1:],new_angles[peaks[1:]],'go')
	   pyplot.plot(new_segs, new_angles[new_segs], 'ro')
	   pyplot.xlim([0,len(ang_rescale)])
	   pyplot.title('Angular measurements for '+str(fsamp))
	   pyplot.xlabel('Time (seconds)')
	   pyplot.ylabel('Angles extension (degrees)')
	   pyplot.show()

#	   pyplot.savefig(session+'FigNum_'+str(name)+'.png')


	   pyplot.figure()
	   pyplot.plot(signals,'b',lw=1)
	   pyplot.plot(new_segs, numpy.zeros(len(new_segs)), 'ro')
	   pyplot.xlim([0,len(signals)])
	   pyplot.title('Angular measurements for '+str(fsamp))
	   pyplot.xlabel('Time (seconds)')
	   ticks = range(0,len(signals),fs*10)
	   pyplot.xticks(ticks,range(0,len(ticks)*10,10))
	   pyplot.ylabel('Amplitude')
	   pyplot.show()

	   #Generate New files in folder named after the fname defined above
	   seg_separ = range(0,len(new_segs)-1,2)
	   noise_separ = range(1,len(new_segs)-1,2)
	   
    
#    print 'Max angle (90 degrees): ',new_ma,'Min angle (0 degrees):', new_mi
#    print 'Max angular velocity:', max(new_angvel)*fs,'degrees/second Min angular velocity:', min(new_angvel)*fs, 'degrees/second'
    
    maxv = max(new_angvel)*fs
    minv = min(new_angvel)*fs
    sig_only = []
    cycle_speed = list()
                    
    for x in seg_separ:
        sig_name = session+str(name)+'/'+str(x/2+1)+'.wav'
        ang_name = sig_name[0:-4]+'_ang.wav'
        samp_store = signals[new_segs[x]:new_segs[x+1]]
        

        sig_only = numpy.concatenate((sig_only,samp_store))
        ang_store = new_angles[new_segs[x]:new_segs[x+1]]

        pos = numpy.argmax(ang_store)
        up_cycle = (ang_store[pos]-ang_store[0])*fs/pos
        down_cycle = (ang_store[pos]-ang_store[-1])*fs/(len(ang_store)-pos)
        cycle_speed.extend((up_cycle, down_cycle))
        open(sig_name,'w')
        open(ang_name,'w')
        wavfile.write(sig_name,fs,samp_store)
        wavfile.write(ang_name,fs,ang_store)
    mean_cs = numpy.mean(cycle_speed)
        
    a_sig = numpy.mean(map(lambda x: x**2, sig_only))**0.5
    
    noise_only = []
    for x in noise_separ:
        noise_only = numpy.concatenate((noise_only, signals[new_segs[x]:new_segs[x+1]]))   

    a_noise = numpy.mean(map(lambda x: x**2, noise_only))**0.5 	   	   	   	   	   	   	   	   	   
    snr_db = 20*log10(a_sig/a_noise)
    
#    print 'SNR estimation:', snr_db,'dB'
#    print 'RMS', 'Cycle speed:', mean_cs, 'degrees/second'
    
#    csvname = fsamp+'/segments.csv'
#    with open(csvname,'w') as csvfile:
#        swriter = csv.writer(csvfile)
#        swriter.writerow(new_segs)

    #Vector Storage
    vec_ma.append(new_ma)
    vec_mi.append(new_mi)
    vec_maxv.append(maxv)
    vec_minv.append(minv)
    vec_snr.append(snr_db)
    vec_cs.append(mean_cs)
    vec_nump.append(len(peaks[1:]))
            
print 'Run time ',time.time()-ts, 'seconds'

#metadat = numpy.column_stack((sname,vec_nump, vec_ma, vec_mi, vec_maxv, vec_minv, vec_snr, vec_cs))
#metadat = numpy.vstack((['File Name','Number of Peaks','Max angle (90 deg)','Min angle (0 deg)','Max angular vel (deg/sec)','Min angular vel (deg/sec)','SNR (dB)','Cycle Speed (deg/sec)'],metadat))
#csvname = session+ 'metadata.csv'
#with open(csvname,'w') as csvfile:
#    swriter = csv.writer(csvfile)
#    for row in range(metadat.shape[0]):
#        swriter.writerow(metadat[row,:])