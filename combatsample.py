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
#try:
    #ghealth > 0
print("Your level", romanlevel , "century of", rhealth, " men encounters a level", germanlevel, "force of", ghealth, "Germanics")
print("Will they attack?")
rawbias = (rhealth*actrlevel)/(ghealth*actglevel)
intbias = int(rawbias)
#print(intbias)
diff = rhealth - ghealth
if diff < 50:
    x = randint(0, intbias)
    if x > 0 and ghealth > (rhealth/2):
        print("The angry, foolhardy Germanics accost your century!")
        r = randrange(actrlevel)
        g = randrange(actglevel)
        if  r > g:
            print("A decisive victory!")
            rcasualty = rhealth - (rhealth - g)
            gcasualty = ghealth - (ghealth - r)
            if rcasualty < 1:
                print("Not a single soldier was lost.  The benediction of the gods is upon your leadership.")
                exp = exp + 1.5
            else:
                print("You lost", rcasualty, "today.  They fought valiantly for Caesar.")
                print("The Germanics lost ", gcasualty)
        else:
	        print("You lost! All your men were viciously slain!")
    else:
        print("The Germanics let your force pass unmolested, and rightfully so.")
else:
    print("The size of your force intimidates the Germanics.  They leave your century alone.")		
	
#except:
    #continue