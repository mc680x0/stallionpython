#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# rndpwgen - a human-friendly random password generator
#            with a dangerously furry and distinctly geeky
#            sort of inclination
# Written by Horst Burkhardt <horst@wilcox-tech.com>
# Based on corgirpw.b by Andrew Wilcox <awilcox@wilcox-tech.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal with the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimers.
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimers in the
#      documentation and/or other materials provided with the distribution.
#   3. Neither the names of rndpwgen, nor Wilcox Technologies, nor the names of
#      its contributors may be used to endorse or promote products derived
#      from this Software without specific prior written permission.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# WITH THE SOFTWARE. 

import sys

# Some sanity so this will run on versions of Python that don't include the
# Mersenne Twister deterministic number generator. 
if (int(sys.version_info[0])) == (int(3)):
    from random import choice
    from random import randint
elif (int(sys.version_info[0])) == (int(2)):
    if (int(sys.version_info[1])) >= (int(4)):
        from random import choice
        from random import randint
    elif (int(sys.version_info[1])) <= (int(3)):
        from whrandom import seed
        from whrandom import choice
        from random import randint
        whrandom.seed
elif (int(sys.version_info[0])) == (int(1)): 
    from random import seed
    from random import choice
    from random import randint
    random.seed

# Stage 1 will randomise out an element of the natural world, via
# multiple-round selection. 

# Cat, Dog, or Horse? 

dogs = ['corgi','saluki','husky','malamut','yorkshire','labrador','heeler','beagle','dalmatian','poodle','cocker','collie','dachshund','greyhound','rottweiler','maltese','doberman','bichon','pomeranian','schaeferhund','terrier','bulldog','akita','mastiff','staffordshire','basset','whippet','pointer','chihuahua','setter','harrier','vallhund','kintamani','schnauzer','afghan','vizsla','mioritic','elkhound','samoyed','navarro','spitz','tahltan','papillon','posavac','sharpei','sloughi','lapphund','tamaskan','coonhound','foxhound','weimaraner','akbash','canaan','kelpie']
cats = ['russianblue','sphynx','englishblue','ragdoll','abyssinian','bengal','scottishfold','mist','balinese','siamese','birman','chartreux','savannah','burmilla','mau','javanese','korat','manx','mainecoon','napolean','ocelot','peterbald','selkirk','vankedisi','angora','levkoy','tonkinese','snowshoe','somali','ragamuffin','bobtail','nebelung','cymric','malayan']
horses = ['abtenauer','andalusian','arabian','criollo','brumby','auvergne','auxois','banker','bardigiano','brabant','blazer','castilian','catria','clydesdale','comtois','don','falabella','finnhorse','fjordhorse','freiberger','karabair','iomud','heihe','haflinger','gelderland','galiceno','gidran','hirzai','lipizzan','jutland','kladruber','kinsky','kustanair','lokai','lyngshest','fouta','malapolski','mecklenburger','messara','mongolian','ostfriesen','novokirghiz','nivernais','nangchen','pampa','percheron','pintabian','retuerta','quarab','qatgani','rhinelander','samolaco','sarcidano','silesian','sorraia','sokolsky','taishuh','tawleed','tersk','tolfetano','trakehner','uzunyayla','vlaamperd','waler','warlander','wielkopolski','xilingol','yonaguni']
# Final list of animals
fauna = []

# Stage 2 is a list of CPUs.
alus = ['Z80','R6502','65C02','MC6800','MC68030','Intel960','Intel386','Z8002','AXP20','PPC603ev','Intel486','MPC750','MPC640','MPC7400','MPC7450','Vger','PPC970','ARM7','ARM9','StrongARM','Athlon64','Am586','Am386','LispM','R2500','R4000','R12000','TMS9900','NSC800','WE32000','Crusoe','C3','C7','WinChip','SuperH']

# Stage 3 is a pair of symbols (not necessarily matching) encircling
# the CPU from Stage 2.
sympool = ['!','@','#','$','%','^','&','*','[','(','{',']',')','}',',',':','<','>','?','~','-','=','+']

# Stage 1 Selection
# Will result in array 'key1m' after multiple-round selection. 
key1a = []
key1b = []
key1m = []

for dognum in range(0,12):
    fauna.append(choice(dogs))
    continue

for catnum in range(0,12):
    fauna.append(choice(cats))
    continue

for horsenum in range(0,12):
    fauna.append(choice(horses))
    continue

for key1prog in range(0,8):
    key1a.append(choice(fauna))
    continue
    
fauna = []

for dognum in range(0,12):
    fauna.append(choice(dogs))
    continue

for catnum in range(0,12):
    fauna.append(choice(cats))
    continue

for horsenum in range(0,12):
    fauna.append(choice(horses))
    continue

for key1prog in range(0,8):
    key1b.append(choice(fauna))
    continue

fauna = []

for key1prog in range(0,4):
    key1m.append(choice(key1b))
    key1m.append(choice(key1a))
    continue

# Stage 2 multiple-round selection. Will result in array
# 'key2m' from which a final result may be chosen.
key2a = []
key2b = []
key2m = []

for key2prog in range(0,8):
    key2a.append(choice(alus))
    key2b.append(choice(alus))
    continue

for key2prog in range(0,4):
    key2m.append(choice(key2b))
    key2m.append(choice(key2a))
    continue

# Final key assembly

temppass = []
symencap = []

for symbol in range(0,2):
    symencap.append(choice(sympool))
    continue

temppass.append(str(int(randint(0,99))))
temppass.append(str(choice(key1m)))
temppass.append(str(symencap[1]))
temppass.append(str(choice(key2m)))
temppass.append(str(symencap[0]))
print "{0}{1}{2}{3}{4}".format(temppass[0], temppass[1], temppass[2], temppass[3], temppass[4])

sys.exit
