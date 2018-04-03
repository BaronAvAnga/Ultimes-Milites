from random import *
romanlevel = 1
actrlevel = 11
rhealth = 80
exp = 0

germanlevel = 1
actglevel = 11
ghealth = randrange(81)
# need to devize defensive code again ghealth = 0
# ghealth = 0 causes traceback... use try except(?)
# try:
    # ghealth > 0
print("Your level", romanlevel , "century of", rhealth, " men encounters a level", germanlevel, "force of", ghealth, "Germanics \n")
print("Will they attack?  \n...\n...\n... \n")
rawbias = (rhealth*actrlevel)/(ghealth*actglevel)
intbias = int(rawbias)
# print(intbias)
diff = rhealth - ghealth
if diff < 50:
    x = randint(0, intbias)
    if x > 0 and ghealth > (rhealth/2):
        print("The angry, foolhardy Germanics assault your century! \n")
        r = randrange(actrlevel)
        g = randrange(actglevel)
        if  r > g:
            print("A decisive victory! \n")
            rcasualty = rhealth - (rhealth - g)
            gcasualty = ghealth - (ghealth - r)
            if rcasualty < 1:
                print("Not a single soldier was lost.  The benediction of the gods is upon your leadership! \n")
                exp = exp + 1.5
            else:
                print("You lost", rcasualty, "today.  They fought valiantly for Caesar. \n")
                print("The Germanics lost", gcasualty, "\n")
                rhealth = rhealth - rcasualty
                print("Your century, now", rhealth, "strong, marches on... \n")
                exp = exp + 1
                print("Your century gained", exp, "experience!\n")
        else:
	        print("You lost! \n\nAll of your men were viciously slain! \n")
    else:
        print("The Germanics let your force pass unmolested, and rightfully so. \n")
else:
    print("The size of your force intimidates the Germanics.  They leave your century alone. \n")		
	
#except:
    #continue
