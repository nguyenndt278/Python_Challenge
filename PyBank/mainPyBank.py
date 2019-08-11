import os
import csv
    
csvPath=os.path.join('C:\workspace\Resources','budget_data.csv')

with open (csvPath,newline='') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    csvHeader=next(csvReader)

    TotalMonth=0
    Sums=0
    Maxs=[]
    Maxs_Change=[]
    Mins=[]
    maxchange=0
    minchange=0
    lastprofit=0
    change=0
    maxdate=0
    mindate=0

    for i in csvReader:
        TotalMonth=TotalMonth+1
        Sums=int(i[1])+ Sums
        Maxs.append(int(i[1]))
        Mins.append(int(i[1]))
        Maxs_Change.append(int(i[1])-int(i[-1]))
        Maxn=max(Maxs)
        Minn=min(Mins)

        if int(i[1])==Maxn:
            x=i
        if int(i[1])==Minn:
            y=i
        change=int(i[1])-lastprofit
        if change> maxchange:
            maxchange=change
            maxdate=i[0]
        if change< minchange:
            minchange=change
            mindate=i[0]
        lastprofit=int(i[1])
        aveCh=Sums/TotalMonth
   
    Ave= int(Sums)/int(TotalMonth)
    print("Financial Analysis")
    print('------------------')
    print('Total Months: '+ str(TotalMonth))
    print('Total: $'+ str(Sums))
    print('Average Change: $'+ str(round(Ave,2)))
    print('Greatest Increase in Profits: '+ str(maxdate)+' ($'+ str(maxchange)+ ')')
    print('Greatest Decrese in Profits: '+ str(mindate)+ ' ($'+str(minchange)+ ')')
   
output_path = os.path.join('C:\\Users\\admin\\Desktop\\Homework\\Week_3\\Python_Challenge\\PyBank', 'pyBankResult.txt')

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Months: '+ str(TotalMonth)])
    csvwriter.writerow(['Total: $'+ str(Sums)])
    csvwriter.writerow(['Average Change: $'+ str(round(Ave,2))])
    csvwriter.writerow(['Greatest Increase in Profits: '+ str(maxdate)+' ($'+ str(maxchange)+ ')'])
    csvwriter.writerow(['Greatest Decrese in Profits: '+ str(mindate)+ ' ($'+str(minchange)+ ')'])


  
   
                          
