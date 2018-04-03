print("\n")
#word 1 = Vltimes
print("  ###          ###  ##        ########  ########  ##      ##  ########   ###### \n    ###      ###    ##           ##        ##     ###    ###  ##        ##       \n     ###    ###     ##           ##        ##     ## #  # ##  ######      #### \n       ##  ##       ##           ##        ##     ##  ##  ##  ##              ## \n         ##         ########     ##     ########  ##      ##  ########   ######  ")
# Lprint(" ## \n ## \n ## \n ## \n ########")
# Tprint("######## \n   ## \n   ## \n   ## \n   ##")
# Iprint("######## \n   ## \n   ## \n   ## \n########")
# Mprint("##      ## \n###    ### \n## #  # ## \n##  ##  ## \n##      ##")
# Aprint("       ##       \n     ##  ##     \n   ##########\n  ###      ###\n###          ###")
print("\n")
#word 2 = Milites
print("        ##      ##  ########  ##        ########  ########  ########   ###### \n        ###    ###     ##     ##           ##        ##     ##        ##      \n        ## #  # ##     ##     ##           ##        ##     ######      ####\n        ##  ##  ##     ##     ##           ##        ##     ##              ##\n        ##      ##  ########  ########  ########     ##     ########   ######  ")
print("\n \n")
print("                              Retreat to the Rhine                              ")
print("\n")
print("--------------------------------------------------------------------------------")
print("\n")
centurionname = input("Enter Player Name: ")
while True:
    if len(centurionname) < 1:
        centurionname = input("Re-Enter Player Name: ")
        continue 
    else:
        print("\nGreetings, Centurion", centurionname)
    break

