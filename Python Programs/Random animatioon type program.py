import sys , time

indent=0
indentIncreasing = True


try:
    while True:
        print(' '*indent,end='')
        print('********',end='\r')
        time.sleep(0.1)

        if indentIncreasing :
            indent+=1
            if indent==20:
                indentIncreasing = False
        else:
            indent-=1
            if indent==0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()            