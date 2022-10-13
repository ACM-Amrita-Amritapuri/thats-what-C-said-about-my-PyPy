import re,time

begintime = float(time.process_time())
mainstr = input()
substr=input()
substrreg = re.compile(r'((^|\b|\s)?'+substr+'(\b|\s|$)?)')

found = substrreg.search(mainstr)

if found==None : quit()

print("Given string contains substring "+substr)

print("TIme taken : ",float(time.process_time())-begintime)