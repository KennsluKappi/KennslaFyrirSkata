import random

nafn = input("Hvað heitir þú?")
lif = 10
styrkur = 2
sneak = 3

alfurNafn = "Stebbi"
alfurLif = 5
alfurStyrkur = 2
athygli = 2

introdution = """
Einu sinni var gæi sem hét Hængur. Hann var stolin af álfum og þeir héldu honum fyrir himin hátt lausnargjald.
Hængur langar að sleppa.
Hvernig á hann að sleppa?

1. Picka lásin og reyna að læðast út?
2. Picka lásin og berjast út?
"""
print(introdution)
val = input("Sláðu inn valkostin sem þú velur: ")
if val == "1":
    sneakEinkunn = random.randint(1,20)
    athygliEinkunn = random.randint(1, 20)
    print(sneakEinkunn)
    print(athygliEinkunn)
if val == "2":
    pass