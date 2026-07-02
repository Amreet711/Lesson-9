units=int(input("How many units of electricity did you use?"))
if units < 50:
    print("Your electricity bill is",units*2+25,"rupees")
elif units > 50 and units < 100:
    print("Your electricity bill is",units*3+35,"rupees")
elif units > 100 and units < 200:
    print("Your electricity bill is", units*4.5+50,"rupees")
else:
    print("Your electricity bill is",units*6+70,"ruppes")