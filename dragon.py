stop=0
exit=0
print ("FBM Database")
while (stop==0):
    pw=input ("Password: ")
    if (pw=="2011"):
        print ("When the blocks came out with the monster")
    if (pw=="FBM"):
        print ("Federal Burrow of Monsters, to protect this country from what it does not want to see")
    if (pw=="again"):
        print ("The dragon enjoys keeping its pray in time loops. Reason unclear.")
    if (pw=="A113"):
        print ("""Data Base Accsesed
Go to file "Exit" to return to passward input
File: Dragon
Appearance: The body of its current target with the head of a "Minecraft Ender Dragon"
Powers: Glitches recording of it, time and space manipulation, extream durrablity, body control
Danger: High""")
        while (exit==0):
            file=input("File: ")
            if (file=="Exit"):
                exit=1
                print ("Exiting Data Base...")
            if (file=="notch"):
                print ("""Appearence: Fat Sweetish man
Notes: In 2011 he released a small indie game known as "Minecraft". Little did he know he had released a monster as well.
He was twisted beyond recognition and his body was kidnaped by the FBM for further investigation. This, unfotunately,
brought it to the US where the FBM has been hunting  it ever since.""")
            if (file!="Exit" and file!="notch"):
                print ("No file found")
    if (pw!="2011" and pw!="FBM" and pw!="again" and pw!="A113"):
        print ("Incorrect")