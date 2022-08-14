import os, sys

tempStr = ""



try:
    game = open("locale_game.txt", "r")
    newdoc = open("newdoc.txt", "w")
    log = open("log.txt", "w")
except:
    os.system("PAUSE")
    sys.exit()

for i in game.readlines():
    tempStr = i.split("\t")[0]
    game_tr = open("locale_game_tr.txt", "r")
    for j in game_tr.readlines():
        #print(tempStr,j.split("\t")[0])
        if tempStr == j.split("\t")[0]:
            # print(tempStr)
            tempStr += "\t" + j.split("\t")[1]
            newdoc.writelines(tempStr)
            break
    else:
        log.writelines("{x}".format(x = tempStr) + "\t\n")

    game_tr.close()
newdoc.close()
game.close()