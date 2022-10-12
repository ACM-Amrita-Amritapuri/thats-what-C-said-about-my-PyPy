import re

def datecheck(date):
    day,month,year = date
    if month in ['04','06','09','11']:
            if int(day)<=30: return True
        
    if month=='02':
        if int(day)<=28: return True

        elif int(day)==29:
            if int(year)%4==0:
                if int(year)%100!=0 : return True

                else:
                    if int(year)%400==0: return True
    
    if month not in ['04','06','09','11']:
        if int(day)<=31: return True
        
    return False

dateregex = re.compile(r'''

    ([0-3][0-9])+       #Checks the Day part of the date
    /                
    ([0-1][0-9])+       #Checks the Month part of the date
    /
    ([1-2][0-9]{3})+    #Checks the Year part of the date

            ''',re.VERBOSE)

matchlst = dateregex.findall('22/12/202115/08/202230/04/299923/11/2999')

for i in matchlst:
    print("/".join([ element for element in i])," ",datecheck(i))