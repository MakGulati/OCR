import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from statistics import mean
import time
def threshold(imageArray):

    balanceAr = []
    newAr = imageArray
    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] =255 
                eachPix[1] =255
                eachPix[2] =255
                eachPix[3] =255
                
            else:
                eachPix[0] =0 
                eachPix[1] =0
                eachPix[2] =0
                eachPix[3] =255
    return (newAr)

                
i1=Image.open('images/numbers/0.1.png')
iar1=np.array(i1) 
           
i2=Image.open('images/numbers/y0.4.png')
iar2=np.array(i2) 

i3=Image.open('images/numbers/y0.5.png')
iar3=np.array(i3) 

i4=Image.open('images/sentdex.png')
iar4=np.array(i4)

#plt.imshow(threshold(iar3))
fig=plt.figure() 
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4=plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

ax1.imshow(threshold(iar1))
ax2.imshow(threshold(iar2))
ax3.imshow(threshold(iar3))
ax4.imshow(threshold(iar4))

plt.show()
  