import os,pygame,sys
if len(sys.argv[1:])!=2: sys.exit()

if(os.path.exists(sys.argv[1])!=True): sys.exit()

filedir = os.getcwd()

os.chdir(sys.argv[1])
cdir = os.getcwd()
filename = "Files in "+cdir[cdir.rfind("\\")+1:]+".txt"
pygame.init()
width = 640
height = 800

win = pygame.display.set_mode((width,height))

pygame.display.set_caption(filename)

def viewdir(dir,indent):
        lst = []
        for i in os.scandir(dir):
                if i.is_dir():
                    # print(" "*indent+"🔒 "+i.name)
                    lst.append(" "*indent+"< > "+i.name)
                    lst.extend(viewdir(i,indent+5))
                else:
                    # print(" "*indent+"----->",i.name)
                    lst.append(" "*indent+"-----> "+i.name)
        return lst

outputlst = []

print("Files/Folders in %s"%os.getcwd()+"\n")
for dir in os.scandir():
    if(dir.is_dir()):
        # print("🔒 "+dir.name)
        outputlst.append("< >"+dir.name)
        outputlst.extend(viewdir(dir,5))
        # print(viewdir(dir,5))
    else:
        # print("-----> "+dir.name)
        outputlst.append("-----> "+dir.name)


for i in outputlst:
    print(i)

os.chdir(filedir)
with open(filename,'w') as f:
    for i in outputlst:
            f.write(i+"\n")

def main():
    mainfont = pygame.font.SysFont("calibri",20)

    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
        count=0
        for i in outputlst:
            main_label = mainfont.render(i,1,(255,255,255))
            # space_label = mainfont.render(" ",1,(0,0,0))
            # space_label_rect = space_label.get_rect()

            # space_label_rect.center = (width//2,outputlst.index(i)+1)
            main_label_rect = main_label.get_rect()

            main_label_rect.center = (0+main_label.get_width()//2,count+30)
            win.blit(main_label, main_label_rect)
            # win.blit(space_label, space_label_rect)
            count+=30
        

        pygame.display.update()

main()

