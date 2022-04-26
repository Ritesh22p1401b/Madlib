madlib="______ man named Fred was _____ hard in his back garden, digging up the ground. After _____ hour of digging, Fred was very ______, so he sat _______ to rest. He laid his shovel down _______ him and took ______ his cap. He wiped the __________ off his forehead _________ his handkerchief."

print("Fill in the blanks with appropiate words. \n{}".format(madlib))

print('''{}  A , the, few, tired ,beside ,down , off , on , sweat , there , with, an  ''' .format("Chosse from thse words:"))

def grammer(i):
    l=['A','working','an','tired','down','beside','off','sweat','with']
    f=0
    for j in l:
        if j==i:
            f+=1
            return f


a=[]
for i  in range(9):
    r=input()
    a.append(r)

for i in a:
    x=grammer(i)
    if x!=1:
        print("incorrect")
        break

else:
    a = ['A','working','an','tired','down','beside','off','sweat','with']
    a1,a2,a3,a4,a5,a6,a7,a8,a9=a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]
    madlib=f"{a1} man named Fred was {a2} hard in his back garden, digging up the ground. After {a3} hour of digging, Fred was very {a4}, so he sat {a5} to rest. He laid his shovel down {a6} him and took {a7} his cap. He wiped the {a8} off his forehead {a9} his handkerchief."
    print(madlib)
