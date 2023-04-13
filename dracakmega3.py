import random
import turtle
def RegLokFun():
    return(int(tx*11+ty))
kres = turtle.Turtle()
planek = []
reka = []
polex = []
polex.append(0)
polex.append(14)
bplanek = []
cplanek = []
dplanek = []
mplanek = []
poleLokaci = []
poleLokacib = []
poleLokaciNaVyb = []
add = open('lokace.txt', 'r')
kkk = add.readlines()
kkk = str(kkk)
allla = str()
z = len(kkk)
z = int(z)
for i in kkk:
    if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
        z = int(z)
    elif ord(i)== 44:
        poleLokaci.append(allla)
        poleLokacib.append(allla)
        poleLokaciNaVyb.append(allla)
        allla = str()
    else:
        allla += i
del poleLokaciNaVyb[5]
del poleLokaciNaVyb[4]
del poleLokaciNaVyb[3]
del poleLokaciNaVyb[2]
del poleLokaciNaVyb[1]
del poleLokaciNaVyb[0]
allla = random.choice(poleLokaciNaVyb)
Lokace = allla
DataOLok = (poleLokaci.index(Lokace,0,len(poleLokaci)))
for i in range(225):
    planek.append(0)
    bplanek.append(0)
    cplanek.append(0)
    dplanek.append(0)
    mplanek.append(0)
y = random.randint(0,14)
if y == 0 or y==14:
    x = random.randint(0,14)
else:
    x = random.choice(polex)
if planek [x*15+y]==0:
    schval=0
    while schval==0:
        allla = random.choice(poleLokaciNaVyb)
        Lokace = allla
        DataOLok = (poleLokaci.index(Lokace,0,len(poleLokaci)))
        planek [x*15+y]=DataOLok
        bplanek[x*15+y]=DataOLok
        dplanek[x*15+y]=DataOLok
        cplanek[x*15+y]=1
        mplanek[x*15+y]=1
        HlavLok=x*15+y
        if DataOLok>4:
            schval=1
               
nahodaschvalena=0
rekapromx=0
rekapromy=0
while nahodaschvalena==0:
    nahodareka=random.randint(1,13)
    if planek [nahodareka]==0:
        nahodaschvalena=1
        planek [int(nahodareka)]=1
        bplanek[int(nahodareka)]=1
        cplanek[int(nahodareka)]=1
        dplanek[int(nahodareka)]=1
        mplanek[int(nahodareka)]=1
        reka.append(int(nahodareka))
        posrek=nahodareka
        if nahodareka//15>7:
            x = ((nahodareka//15)-7)*30
        elif nahodareka//15==7:
            x = 0
        else:
            x = ((nahodareka//15)-7)*30
        if (nahodareka)%15==7:
            y = 0
        elif (nahodareka%15)>7:
            y = (((nahodareka)%15)-7)*30
        else:
            y = ((nahodareka%15)-7)*30
    kres.penup()
    kres.setpos(y, x)
    nahodaschvalena=1
    rekapromx=0
    posrek=nahodareka
kres.color("cyan")
for i in range(14):
    kres.width(9)
    kres.pendown()
    rekamoznost = []
    if (posrek%15 !=1 and planek[posrek+14]==0):
        rekamoznost.append(int(posrek+14))
    if (posrek%15 !=13 and planek[posrek+16]==0):
        rekamoznost.append(int(posrek+16))    
    if (planek[posrek+15]==0):
        rekamoznost.append(posrek+15)        
    nahodareka = random.choice(rekamoznost)
    planek [nahodareka]=1
    bplanek[nahodareka]=1
    cplanek[nahodareka]=1
    dplanek[nahodareka]=1
    mplanek[nahodareka]=1
    reka.append(nahodareka)
    if nahodareka//15>7:
        x = ((nahodareka//15)-7)*30
    elif nahodareka//15==7:
        x = 0
    else:
        nahodareka//15
        x = ((nahodareka//15)-7)*30
    if (nahodareka)%15==7:
        y = 0
    elif (nahodareka%15)>7:
        y = (((nahodareka)%15)-7)*30
    else:
        y = ((nahodareka%15)-7)*30
    kres.pendown
    kres.setpos(y, x+10)
    posrek=nahodareka
    kres.penup()
    
if (planek[112]==1):
    planek [112]=2
    bplanek[112]=2
    cplanek[112]=2
    dplanek[112]=2
    mplanek[112]=1
    del reka[6]
    del reka[6]
    del reka[6]
    promennacislojedna=random.choice(reka)
    planek [promennacislojedna]=2
    bplanek[promennacislojedna]=2
    cplanek[promennacislojedna]=2
    mplanek[promennacislojedna]=1
else:
    nahodmost=random.randint(0,14)
    nahodmostcis = reka[int(nahodmost)]
    planek [nahodmostcis]=2
    bplanek[nahodmostcis]=2
    cplanek[nahodmostcis]=2
    dplanek[nahodmostcis]=2
    mplanek[nahodmostcis]=1
    if nahodmost==0:
        del reka[0]
        del reka[0]
    elif nahodmost==14:
        del reka[14]
        del reka[13]
    else:
        del reka[int(nahodmost)-1]
        del reka[int(nahodmost)-1]
        del reka[int(nahodmost)-1]
    
    promennacislojedna = random.choice(reka)
    planek [promennacislojedna]=2
    bplanek[promennacislojedna]=2
    cplanek[promennacislojedna]=2
    dplanek[promennacislojedna]=2
    mplanek[promennacislojedna]=1
               
LokaceBaz = HlavLok
for i in range(random.randint(1,3)):
    while mplanek [LokaceBaz]!=0:
        x = random.randint(0,14)
        y = random.randint(0,14)
        LokaceBaz= int(x*15+y) 
    planek [LokaceBaz]=3
    bplanek[LokaceBaz]=3
    cplanek[LokaceBaz]=3
    dplanek[LokaceBaz]=3
    mplanek[LokaceBaz]=1
while mplanek [LokaceBaz]!=0:
    x = random.randint(0,14)
    y = random.randint(0,14)
    LokaceBaz= int(x*15+y) 
planek [LokaceBaz]=5
bplanek[LokaceBaz]=5
cplanek[LokaceBaz]=5
dplanek[LokaceBaz]=5
mplanek[LokaceBaz]=1
LokaceBaz = HlavLok
for i in range(1):
    while mplanek [LokaceBaz]!=0:
        x = random.randint(0,14)
        y = random.randint(0,14)
        LokaceBaz= int(x*15+y) 
    planek [LokaceBaz]=4
    bplanek[LokaceBaz]=4
    cplanek[LokaceBaz]=4
    dplanek[LokaceBaz]=4
    mplanek[LokaceBaz]=1
        
for i in range(1,random.randint(7,10)):
    kres.width(5)
    x = random.randint(0,14)
    y = random.randint(0,14)
    if planek [x*15+y]==0:
        schval=0
    while schval==0:
        allla = random.choice(poleLokaciNaVyb)
        Lokace = allla
        DataOLok = (poleLokaci.index(Lokace,0,len(poleLokaci)))
        planek [x*15+y]=DataOLok
        bplanek[x*15+y]=DataOLok
        dplanek[x*15+y]=DataOLok
        cplanek[x*15+y]=1
        mplanek[x*15+y]=1
        HlavLok=x*15+y
        if DataOLok>4:
            schval=1
polmal = planek      
for i in range(2,len(poleLokaci)):
    while i in polmal:
            kres.width(3)
            povpol = polmal.index(int(i))
            kres.setpos(y, x)
            polmal[povpol]=0
            kres.penup()
            if i==2:
                kres.color("brown")
            elif i==3:
                kres.color("turquoise")
                kres.width(9)
            elif i==4:
                kres.color("orange")
                kres.width(9)
            elif i==5:
                kres.color("magenta")
                kres.width(9)
            
            else:
                kres.color("black")
            if povpol==HlavLok:
                kres.color("yellow")
            if povpol//15>7:
                x = ((povpol//15)-7)*30
            elif povpol//15==7:
                x = 0
            else:
                povpol//15
                x = ((povpol//15)-7)*30
            if (povpol)%15==7:
                y = 0
            elif (povpol%15)>7:
                y = (((povpol)%15)-7)*30

            else:
                y = ((povpol%15)-7)*30
            kres.setpos(y, x)
            kres.pendown()
            kres.circle(6,360)
kres.penup()
kres.speed(0)
kres.color("green")
while int(0) in cplanek:
    povpol = cplanek.index(int(0))        
    if povpol//15>7:
        x = ((povpol//15)-7)*30
        lox=povpol//15
    elif povpol//15==7:
        x = 0
        lox=povpol//15
    else:
        povpol//15
        x = ((povpol//15)-7)*30
        lox=povpol//15
    if (povpol)%15==7:
        y = 0
        loy=povpol%15
    elif (povpol%15)>7:
        y = (((povpol)%15)-7)*30
        loy=povpol%15

    else:
        y = ((povpol%15)-7)*30
        loy=povpol%15
    cplanek[povpol]=1
    kres.setpos(y, x+3)
    kres.pendown()
    kres.setpos(y,x+9)
    kres.begin_fill()
    kres.setpos(y-2,x+4)
    kres.setpos(y+2,x+4)
    kres.setpos(y,x+9)
    kres.end_fill()
    kres.penup()
        
kres.penup()
kres.setpos(0, 0)
kres.pendown()
kres.color("red")
kres.circle(6,360)                
tx = 7
ty = 7
pzx=0
pzy=6
#vytvorte funkci, ktera vrati pole,
#ktere obsahuje vsechna cisla od 1
#do 100, ktera maji alespon 5
#delitelu

'''
def funkce():
    pole = []
    for i in range(1,101):
        pocet = 0
        for j in range(1,i+1):
          if i % j == 0:
            pocet += 1
        if pocet == 2:
            print(i, end = ", ")

   # return pole
funkce()
#print()
'''
'''
import random

def funkce():

    pole = ["Shnila bramboro",
            "Pouzity toaletaku",
            "Predpotopni opice",
            "Propichnuty krecku",
            "Neumyta pohovko"
            ]
    return random.choice(pole)
    return pole[random.randint(0,4)]

for i in range(7):
    print(funkce())
'''

 
def prisera():
    polePriser = []
    if RegLok!=4:
        add = open('priseraob.txt', 'r')
        kkk = add.readlines()
        kkk = str(kkk)
        allla = str()
        z = len(kkk)
        z = int(z)
        for i in kkk:
            if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
                z = int(z)
            elif ord(i)== 44:
                polePriser.append(allla)
                allla = str()
            else:
                allla += i
    else:
        add = open('draci.txt', 'r')
        kkk = add.readlines()
        kkk = str(kkk)
        allla = str()
        z = len(kkk)
        z = int(z)
        for i in kkk:
            if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
                z = int(z)
            elif ord(i)== 44:
                polePriser.append(allla)
                allla = str()
            else:
                allla += i
    PriseraPoc = str(random.choice(polePriser))
    return(PriseraPoc)

def silapris():
    SiList = []
    add = open('sila.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                SiList.append(allla)
                allla = str()
        else:
             allla += i
    return (SiList[CisRegPris])

def silaIt():
    SiItList = []
    add = open('vecisila.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                SiItList.append(allla)
                allla = str()
        else:
             allla += i
    return (SiItList[CisRegItem])
def Zivotky():
    ZivList = []
    add = open('obleceni.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                ZivList.append(allla)
                allla = str()
        else:
             allla += i
    DataOOblec=(ZivList.index(Oblec,0,len(ZivList)))
    return (DataOOblec)
def zdravi():
    polezdravi = []
    add = open('oblecenisila.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                polezdravi.append(allla)
                allla = str()
        else:
             allla += i
    return(polezdravi [CisRegOblec])
def item():

    poleItemu = []
    add = open('veci.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                poleItemu.append(allla)
                allla = str()
        else:
             allla += i
    ItemPoc = str(random.choice(poleItemu))
    return(ItemPoc)

def Oblecis():
    poleObleceni = []
    add = open('obleceni.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                poleObleceni.append(allla)
                allla = str()
        else:
             allla += i
    return(poleObleceni[OblecPoc])
def obleceni():
    poleObleceni = []
    add = open('obleceni.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                poleObleceni.append(allla)
                allla = str()
        else:
             allla += i
    OblecPoc = str(random.choice(poleObleceni))
    return(OblecPoc)

    
def boj():
    ZZZZivoty=int(Ziv)
    if RegLok != 4:
        TvujHod = int(random.choice(kostka))
        PriseryHod = int(random.choice(kostka))
        print(f"Tobe padlo {TvujHod} a prisere padlo {PriseryHod}")
        if int(TvujHod + int(silait))>int(PriseryHod+ int(sila)):
              a = 2
              print(f"Hrdinne jsi zabil {pris}. Gratuluju")
              if tx*15+ty==HlavLok:
                  print("Prisera zabita, nasel si poklad.")
                  print("Konec hry.")
                  print("Muzes volne chodit po mape, nebo restartovat hru.")
              if( pris != str("mluviciho kozla")):
                 MoznyItem = item()
                 print(f"Chces vymenit,{it} za {MoznyItem}.")
                 ans =input("A,N")
                 while ans not in ["A","N"]:
                    ans = input("Spatna akce, vyber z techto dvou: A,N")
                 if ans =="A":
                    return(MoznyItem)
                 else:
                     return(int(Ziv))
              else:
                MoznyItem = "studeny salam"
                print(f"Chces vymenit,{it} za {MoznyItem}.")
                ans =input("A,N")
                while ans not in ["A","N"]:
                    akce = input("Spatna akce, vyber z techto dvou: A,N")
                if ans =="A":
                    return(MoznyItem)
                else:
                    return(int(Ziv))
        

            
        elif int(TvujHod + int(silait))<int(PriseryHod + int(sila)):
             print(f"Kamo, mas jen {it}.")
             print("Prisera te porazila.")
             if Ziv==0:
                 print("Nechal ses sezrat... hra pro tebe konci.")
             ZZZZivoty-=1
             return(ZZZZivoty)
         
            
         
        else:
             ddddddddd = int(Ziv)
             print(f"Vidis utikat pryc {pris}. Gratuluju prezil si")
             return(ddddddddd)
    else:
        add = open('draci.txt', 'r')
        poleDraci = []
        kkk = add.readlines()
        kkk = str(kkk)
        allla = str()
        z = len(kkk)
        z = int(z)
        for i in kkk:
            if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
                z = int(z)
            elif ord(i)== 44:
                poleDraci.append(allla)
                allla = str()
            else:
                allla += i
        DrakReg= int(poleDraci.index(PriseraPoc,0,len(polePriser)))
        poleDraciZiv = []
        add = open('draciziv.txt', 'r')
        kkk = add.readlines()
        kkk = str(kkk)
        allla = str()
        z = len(kkk)
        z = int(z)
        for i in kkk:
            if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
                z = int(z)
            elif ord(i)== 44:
                    poleDraciZiv.append(allla)
                    allla = str()
            else:
                 allla += i
        DraciZiv=int(poleDraciZiv [DrakReg])     
        while(ZZZZivoty!=-1 and DraciZiv!=-1):
            TvujHod = int(random.choice(kostka))
            PriseryHod = int(random.choice(kostka))
            print(f"Tobe padlo {TvujHod} a drakovi padlo {PriseryHod}")
            if int(TvujHod + int(silait))>int(PriseryHod+ int(sila)):
                  a = 2
                  print(f"Zasadil jsi drakovi uder")
                  DraciZiv-=1
                                         

            
            elif int(TvujHod + int(silait))<int(PriseryHod + int(sila)):
                 print(f"Drak te popalil.")
                 ZZZZivoty-=1
         
            
         
            else:
                 print("Uskocil jsi plamenu!")
            input("OK")
            print(DraciZiv)
            print(ZZZZivoty)

        if ZZZZivoty==-1:
            print("Prohral jsi, drak te spalil na popel.")
            print("Hra pro tebe konci.")
            return(-5)
        else:
            print("Gratuluju.")
            print("Drak je mrtev.")
            print("Dohral jsi celou hru.")
            return(-5)
             
            

name = input("Jak se jmenujes? ")
print(f"Jsi {name} a jsi dobrodruh.")
kostka = [1,
                  2,
                  4,
                  3,
                  5,
                  6]
v = 1
Item = item()
a=2
Oblec = obleceni()
CisRegOblec= Zivotky()
Ziv= zdravi()
zlataky = 0
if name == "vyvojar":
    Item = "studeny salam"
    zlataky=80
while(int(Ziv)>-1):
    if type(a)==str:
        Item = a
    kammoznosti =[]
    if ty>0 and planek[ty-1+tx*15]!=1:
        kammoznosti.append("Z")
    if ty<14 and planek[ty+1+tx*15]!=1:
        kammoznosti.append("V")
    if tx<14 and planek[ty+(tx+1)*15]!=1:
        kammoznosti.append("S")
    if tx>0 and planek[ty+(tx-1)*15]!=1:
        kammoznosti.append("J")
    akce = input(kammoznosti)
    while akce not in kammoznosti:
        akce = input(kammoznosti)
    if akce=="Z":
        ty-=1
        pzx-=30
        kres.setpos(pzx,pzy)
    if akce=="V":
        ty+=1
        pzx+=30
        kres.setpos(pzx,pzy)
    if akce=="S":
        tx+=1
        pzy+=30
        kres.setpos(pzx,pzy)
    if akce=="J":
        tx-=1
        pzy-=30
        kres.setpos(pzx,pzy)
    if type(v)==str or v==2:
        vyhra()
    x=int(tx*15)
    y=int(ty)
    poleLokaci = []
    add = open('lokace.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
            poleLokaci.append(allla)
            allla = str()
        else:
            allla += i
    planreg=tx*15+ty
    xy =int (x+y)
    planpoc=planreg
    RegLok =int(bplanek[xy])
    if RegLok ==3:
        print("Spadl jsi do baziny- hra pro tebe konci.")
        while(True):
            GlokGlokGlok=1
    Lokace = poleLokacib[int(RegLok)]
    if RegLok != 0 and RegLok != 4 and RegLok != 5:
        OblecMoz = obleceni()
        print(f"Chces vymenit {Oblec} za {OblecMoz}")
        Rozhod=input("A,N")
        while Rozhod not in ["A","N"]:
                Rozhod = input("Spatna akce, vyber z techto dvou: A,N")
        if Rozhod=="A":
            Oblec=OblecMoz
            CisRegOblec= Zivotky()
            Ziv= zdravi()
            v==type(v)
        else:
            print(f"Prodal jsi to za 10 zlataku a momentalne mas v mesci {10+zlataky} zlataku.")
            zlataky+=10
    lokkon = str()
    for i in Lokace:
        if ord(i)!= 34:
           lokkon += i
    v = 1
    if int(Ziv)==1:
        print(f"Jsi {lokkon} a mas {Ziv} zivot.")
    if int(Ziv)==0:
        print(f"Jsi {lokkon} a mas {Ziv} zivotu.")
    if int(Ziv)>1:
        print(f"Jsi {lokkon} a mas {Ziv} zivoty.")
    ItemPoc = Item
    ZZZZivoty=Ziv
    allla = str(ItemPoc)
    ItemKonk = str()
    for i in allla:
        if ord(i)!= 34:
            ItemKonk += i
    it = ItemKonk
    poleItemu = []
    add = open('veci.txt', 'r')
    kkk = add.readlines()
    kkk = str(kkk)
    allla = str()
    z = len(kkk)
    z = int(z)
    for i in kkk:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            z = int(z)
        elif ord(i)== 44:
                poleItemu.append(allla)
                allla = str()
        else:
                allla += i
    poleItemu.append("studeny salam")
    if RegLok==5:
        print("Chces si koupit bezovou hulku za 100 zlataku?")
        akce = input("K,N")
        while akce not in ["K","N"]:
            akce = input("Spatna akce, vyber z techto dvou: K,N")
        if akce == "K":
            if zlataky>90:
                print("Koupil jsi si bezovou hulku.")
                Item =poleItemu[5]
                zlataky-=100
            else:
                print("Nemas dost zlataku")
   
    else:    
        PriseraPoc = prisera()
        allla = str(PriseraPoc)
        PriseraKonk = str()
        for i in allla:
            if ord(i)!= 34:
                PriseraKonk += i
        pris = PriseraKonk
        polePriser = []
        add = open('prisera.txt', 'r')
        kkk = add.readlines()
        kkk = str(kkk)
        allla = str()
        z = len(kkk)
        z = int(z)
        for i in kkk:
            if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
                z = int(z)
            elif ord(i)== 44:
                polePriser.append(allla)
                allla = str()
            else:
                allla += i

        DataOPriscis=(polePriser.index(PriseraPoc,0,len(polePriser)))
        DataOItecis=(poleItemu.index(ItemPoc,0,len(poleItemu)))
        CisRegPris = int(DataOPriscis)
        CisRegItem = int(DataOItecis)
        sila = silapris()
        silait = silaIt()
        print(f"Vidis {pris} a mas {it}.")
        print("co chces udelat? Zabit priseru, utect, nechat se sezrat: ")
        akce = input("Z,U,NSS")
        while akce not in ["Z","U","NSS"]:
            akce = input("Spatna akce, vyber z techto tri: Z,U,NSS")
        if akce == "NSS":
            print("Nechal ses sezrat... hra pro tebe konci.")
            Ziv = -5
        elif akce == "U":
            print("Utekl jsi, zbabelce!")
            if int(random.choice(kostka))>int(random.choice(kostka)+1):
                print(f"Slysis za sebou utikat {pris}.")
                akce = input("Z,NSS")
                while akce not in ["Z","NSS"]:
                    akce = input("Spatna akce, vyber z techto dvou: Z,NSS")
                if akce == "NSS":
                    print("Nechal ses sezrat... hra pro tebe konci.")
                    Ziv = -5
                else:
                    a=boj()
                    if int==type(a):
                        zzzzzzz=a
                        Ziv=zzzzzzz  
        else:
            a=boj()
            if (int==type(a)):
                zzzzzzz=a
                Ziv=zzzzzzz 
                        
                 
        
