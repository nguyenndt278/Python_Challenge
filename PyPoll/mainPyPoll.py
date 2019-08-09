import os
import csv
    
csvPath=os.path.join('C:\workspace\Resources','election_data.csv')

with open (csvPath,newline='') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    csvHeader=next(csvReader)

    tot=0
    khanc=[]
    correy=[]
    li=[]
    oley=[]
    
    for i in csvReader:
        tot=tot+1
        if i[2]=="Khan":
            khanc.append(i[2])
        if i[2]=="Correy":
            correy.append(i[2])
        if i[2]=="Li":
            li.append(i[2])
        if i[2]=="O'Tooley":
            oley.append(i[2])

    tots=tot-1
    x1=len(khanc)
    x2=len(correy)
    x3=len(li)
    x4=len(oley)
    y1=round(x1/tots*100,3)
    y2=round(x2/tots*100,3)
    y3=round(x3/tots*100,3)
    y4=round(x4/tots*100,3)

    if y1==max(y1,y2,y3,y4):
        winner="Khan"
    elif y2==max(y1,y2,y3,y4):
        winner="Correy"
    elif y3==max(y1,y2,y3,y4):
        winner="Li"
    elif y4==max(y1,y2,y3,y4):
        winner="O'Tooley"
        
    
    print('Election Results')
    print('----------------------')
    print('Total Votes: '+ str(tots))
    print('----------------------')
    print('Khan: '+str(y1)+'% ' + '('+ str(x1)+')')
    print('Correy: '+str(y2)+'% ' + '('+ str(x2)+')')
    print('Li: '+str(y3)+'% ' + '('+ str(x3)+')')
    print("O'Tooley: "+str(y4)+'% ' + '('+ str(x4)+')')
    print("Winner: " + winner)
    
output_path =os.path.join('C:\workspace\Resources','pyPollResult.txt')

with open(output_path, 'w') as newFile:
    
    newf=csv.writer(newFile)
    
    newf.writerow(['Election Results'])
    newf.writerow(['----------------------'])
    newf.writerow(['Total Votes: '+ str(tots)])
    newf.writerow(['----------------------'])
    newf.writerow(['Khan: '+str(y1)+'% ' + '('+ str(x1)+')'])
    newf.writerow(['Correy: '+str(y2)+'% ' + '('+ str(x2)+')'])
    newf.writerow(['Li: '+str(y3)+'% ' + '('+ str(x3)+')'])
    newf.writerow(["O'Tooley: "+str(y4)+'% ' + '('+ str(x4)+')'])
    newf.writerow(["Winner: " + winner])
