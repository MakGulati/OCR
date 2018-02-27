import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from PIL import Image
from statistics import mean
from collections import Counter
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
def createExample():
    with open('numArEx.txt','a') as fp:
        numbersWeHave=range(0,10)
        decimalWeHave=range(1,10)
        for number in numbersWeHave:
            for decimal in decimalWeHave:
#                print(str(number)+"."+str(decimal))
                imageFilePath='images/numbers/'+str(number)+'.'+str(decimal)+'.png'
                i=Image.open(imageFilePath)
                iar=np.array(i)
                iarl=iar.tolist()
                fp.write(str(number)+'::'+str(iarl)+'\n')
                
        return("done")
#  createExample()       
def matchExample(pngFile):
    matchedAr=[]
    img=Image.open(pngFile)
    iar=np.array(img)
    iarl=iar.tolist()
    
    with open('numArEx.txt','r') as fp:
        lines=fp.read().split('\n')
        
#        print(lines)
        for line in lines:
            try:
            
                line_split=line.split('::')
                numb=line_split[0]
                ar=line_split[1]
                InQuestion=str(iarl)
                checkEx=ar.split("],")
                InQEx=InQuestion.split("],")
                x=0
                while(x<len(checkEx)):
                    if(checkEx[x]==InQEx[x]):
                        matchedAr.append(int(numb))
                    x+=1
            except Exception as e:
                print(str(e))
                    
        y=Counter(matchedAr)
        Xaxis=[]
        Yaxis=[]
        for key,value in y.items():
            Xaxis.append(key)
            Yaxis.append(value)
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(2,0), rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(Xaxis,Yaxis) 
    plt.ylim(400)           
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()

            
            
        
#                    
            
print(matchExample("images/test.png"))     
    
    
