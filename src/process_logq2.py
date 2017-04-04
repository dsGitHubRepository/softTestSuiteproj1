import numpy as np
import pandas as pd
from collections import Counter
import operator

pathinput='./log_input/log.txt'
# wc -l 4400644
datainput=open(pathinput,'r')

NoL=44#00644  # 4400644  # 4400644

byteList=[]
rsrcList=[]

for line in range(NoL):
    linetxt=datainput.readline()
    linetxtSplit=linetxt.split()
    if np.size(linetxtSplit)==10 :
        if linetxtSplit[9] != str('-'):
            rsrc=linetxtSplit[6]
            rsrcstr=str(rsrc)
            rsrcList.append(rsrcstr)
            q2byte=linetxtSplit[9]
            byteList.append(q2byte)

# Remove duplicate item from the list                        
rsrcNodupl=list(set(rsrcList))

# most timeconsuming part of the code

lprog=np.size(rsrcNodupl)/10
bandwidthList=[]
bandwidthList=[]
for lsrc1 in range(np.size(rsrcNodupl)):
    if lsrc1%lprog == 0:  
        print "progress : ", lsrc1/lprog   
    srcitem1=rsrcNodupl[lsrc1]
    srcitem1str=str(srcitem1)  # to be sure
    nc=0
    sumbyte=0 
    for lsrc2 in range(np.size(rsrcList)):  
        srcitem2str=rsrcList[lsrc2] 
        if srcitem1str==srcitem2str:
             idxstr=str(lsrc2)
             sumbyte=sumbyte+int(byteList[lsrc2])
             nc=nc+1    # repeated resources count
        sumbytePerfreq=sumbyte/(nc+1) # average out
    bandwidthList.append(sumbytePerfreq)
    
bandwListint=list(map(int, bandwidthList))    

pathoutRsrc='./log_output/resources.txt'
dataoutRsrc=open(pathoutRsrc,'wb')

for irsrc in range(10):
    RsrcMaxbw=max(bandwListint)
    idxMaxbw=pd.Series(bandwListint).idxmax()
    topMostRsrc=rsrcNodupl[idxMaxbw+irsrc]     # THIS LINE ME =rsrcNodupl[idxMaxbw+1]
    dataoutRsrc.write('%s \n' % topMostRsrc)
    #print "\n top", irsrc+1, ":", topMostRsrc, "bandwidth : ", RsrcMaxbw
    bandwListint.remove(max(bandwListint))
       
dataoutRsrc.close()

         
