#Realizado por:
#up201405426 João Rodrigues
#up201406368 João Pereira


from sys import stdout

printf = stdout.write

class Pol:
    def __init__(self, coeficiente, letra, expoente):
        self.coeficiente = coeficiente
        self.letra = letra
        self.expoente = expoente

    def __repr__(self):
        printf('%d%c^%d' %(self.coeficiente,self.letra, self.expoente))
        printf(" + ")
        return ""

    def soma(self, x, y, i):
        if x.expoente == y.expoente and x.letra == y.letra:
            x.coeficiente = x.coeficiente + y.coeficiente
            a.pop(i + 1)
            a.insert( i + 1, x)

    def primitiva(self, x, i):
        factor_n = x.expoente
        factor_n += 1
        if x.coeficiente % factor_n == 0:
            x.coeficiente = x.coeficiente / factor_n
            if (x.coeficiente == 0 or x.expoente == 0):
                print("Erro")
                return 0
            elif x.coeficiente == 1 and x.expoente != 0:
                printf('%c^%d ' % (x.letra, x.expoente + 1))
            elif (x.expoente == 1):
                printf('%d%c ' % (x.coeficiente, x.letra))
            elif (x.expoente == 0 and x.coeficiente == 1):
                printf('%c ' % x.letra)
            elif (x.expoente == 0 and x.coeficiente != 1):
                printf('%d%c ' % (x.coeficiente, x.letra))
            elif (x.expoente == 1 and x.coeficiente == 1):
                printf('%c' % (x.letra))
            else:
                printf('%d%c^d ' % (x.coeficiente, x.letra, x.expoente))
        else:
            printf(' (%d/%d)%c^%d' % (x.coeficiente, factor_n, x.letra, x.expoente + 1))
        if i < len(a) - 1:
            printf(' + ')
        if i == len(a) - 1:
            printf(" + C")

    def derivada(self, x, i):
        new_expoente = x.expoente - 1
        new_coeficiente = x.coeficiente * x.expoente
        if x.coeficiente == 0 or x.expoente == 0:
            print("Erro ")
            return 0;
        elif x.expoente == 1 and x.coeficiente == 1:
            printf('%d' % new_coeficiente)
        elif x.expoente == 1:
            printf('%d' % new_coeficiente)
        elif new_expoente == 1:
            printf('%d%c' % (new_coeficiente, x.letra))
        else:
            printf('%d%c^%d' % (new_coeficiente, x.letra, new_expoente))

        if i < len(a) - 1:
            printf(' + ')
        if i == len(a) - 1:
            printf("")

    def normalize(self,x,i):
        factor_n = x.expoente
        if(x.coeficiente==0 or x.expoente==0):
            printf("Erro")
            return
        if(x.coeficiente%factor_n == 0):
            x.coeficiente=x.coeficiente/factor_n
            if (x.coeficiente == 1 and x.expoente == 1):
             printf('%c' % x.letra)
            elif (x.coeficiente == 1):
                printf('%c^%d' % (x.letra, x.expoente))
            elif (x.expoente == 1):
             printf('%d%c' %( x.coeficiente, x.letra))
            else:
                printf('%d%c^%d'  % (x.coeficiente, x.letra, x.expoente))

        else:
            if (x.expoente == 1):
                printf('(%d/%d)%c ' % (x.coeficiente, factor_n, x.letra))
            else:
                 printf('(%d/%d)%c^%d'  % (x.coeficiente, factor_n, x.letra, x.expoente))
        if i < len(a)-1:
            printf(" + ")


print("Soma -> 1 | Normalização -> 2 | Primitivar -> 3 | Derivar -> 4 ")

choice = int(input())
quantity = int(input("how much?: "))

a = []
new_a = []

while (quantity != 0):
    print("Polinómio")
    print("Enter coeficiente: ")
    coef = int(input())
    letra = input("Enter variável: ")
    print("Enter expoente: ")
    exp = int(input())
    p = Pol(coef, letra, exp)
    a.append(p)
    quantity = quantity - 1

i = 0
tam=len(a)
if choice == 1:
    while i+1 < tam:
        a.sort(key=lambda a: a.expoente, reverse=False)  # soma while i + 1 < len(a)
        Pol.soma(a, a[i], a[i + 1], i)
        i = i + 1

    a = list(set(a))
    j = 0
    while j < len(a):
        if j ==0 :
            if a[j].expoente == 1 and a[j].coeficiente > 1:
                printf('%d%s ' % (a[j].coeficiente, a[j].letra))
            elif a[j].coeficiente == 0:
                printf("0")
            elif a[j].expoente == 0 and a[j].coeficiente != 0:
                printf("1")
            elif a[j].expoente == 1 and a[j].coeficiente == 1:
                printf('%s ' % a[j].letra)
            elif a[j].expoente != 1 and a[j].coeficiente != 0:
                printf('%d%s^%d ' % (a[j].coeficiente, a[j].letra, a[j].expoente))

        else:
            if a[j].expoente == 1 and a[j].coeficiente > 1:
                printf(' + %d%s ' % (a[j].coeficiente, a[j].letra))
            elif a[j].coeficiente == 0:
                printf("0")
            elif a[j].expoente == 0 and a[j].coeficiente!=0:
                printf("1")

            elif a[j].expoente == 1 and a[j].coeficiente == 1:
                printf(' + %s ' % a[j].letra)
            elif a[j].expoente != 1 and a[j].coeficiente != 0:
                printf('+ %d%s^%d ' % (a[j].coeficiente, a[j].letra, a[j].expoente))

        j = j + 1


if choice == 2:
    while i < len(a):
        a.sort(key=lambda a: a.expoente, reverse=False)
        Pol.normalize(a, a[i], i)
        i = i + 1

if choice == 3:
    while i + 1 < len(a):
        Pol.primitiva(a, a[i], i)
        i = i + 1
if choice == 4:
    while i < len(a):
        Pol.derivada(a, a[i], i)
        i = i + 1


from sys import stdout

printf = stdout.write

class Pol:
    def __init__(self, coeficiente, letra, expoente):
        self.coeficiente = coeficiente
        self.letra = letra
        self.expoente = expoente

    def __repr__(self):
        printf('%d%c^%d' %(self.coeficiente,self.letra, self.expoente))
        printf(" + ")
        return ""

    def soma(self, x, y, i):
        if x.expoente == y.expoente and x.letra == y.letra:
            x.coeficiente = x.coeficiente + y.coeficiente
            a.pop(i + 1)
            a.insert( i + 1, x)

    def primitiva(self, x, i):
        factor_n = x.expoente
        factor_n += 1
        if x.coeficiente % factor_n == 0:
            x.coeficiente = x.coeficiente / factor_n
            if (x.coeficiente == 0 or x.expoente == 0):
                print("Erro")
                return 0
            elif x.coeficiente == 1 and x.expoente != 0:
                printf('%c^%d ' % (x.letra, x.expoente + 1))
            elif (x.expoente == 1):
                printf('%d%c ' % (x.coeficiente, x.letra))
            elif (x.expoente == 0 and x.coeficiente == 1):
                printf('%c ' % x.letra)
            elif (x.expoente == 0 and x.coeficiente != 1):
                printf('%d%c ' % (x.coeficiente, x.letra))
            elif (x.expoente == 1 and x.coeficiente == 1):
                printf('%c' % (x.letra))
            else:
                printf('%d%c^%d ' % (x.coeficiente, x.letra, x.expoente))
        else:
            printf(' (%d/%d)%c^%d' % (x.coeficiente, factor_n, x.letra, x.expoente + 1))
        if i < len(a) - 1:
            printf(' + ')
        if i == len(a) - 1:
            printf(" + C")

    def derivada(self, x, i):
        new_expoente = x.expoente - 1
        new_coeficiente = x.coeficiente * x.expoente
        if x.coeficiente == 0 or x.expoente == 0:
            print("Erro ")
            return 0;
        elif x.expoente == 1 and x.coeficiente == 1:
            printf('%d' % new_coeficiente)
        elif x.expoente == 1:
            printf('%d' % new_coeficiente)
        elif new_expoente == 1:
            printf('%d%c' % (new_coeficiente, x.letra))
        else:
            printf('%d%c^%d' % (new_coeficiente, x.letra, new_expoente))

        if i < len(a) - 1:
            printf(' + ')
        if i == len(a) - 1:
            printf("")

    def normalize(self,x,i):
        factor_n = x.expoente
        if(x.coeficiente==0 or x.expoente==0):
            printf("Erro")
            return
        if(x.coeficiente%factor_n == 0):
            x.coeficiente=x.coeficiente/factor_n
            if (x.coeficiente == 1 and x.expoente == 1):
             printf('%c' % x.letra)
            elif (x.coeficiente == 1):
                printf('%c^%d' % (x.letra, x.expoente))
            elif (x.expoente == 1):
             printf('%d%c' %( x.coeficiente, x.letra))
            else:
                printf('%d%c^%d'  % (x.coeficiente, x.letra, x.expoente))

        else:
            if (x.expoente == 1):
                printf('(%d/%d)%c ' % (x.coeficiente, factor_n, x.letra))
            else:
                 printf('(%d/%d)%c^%d'  % (x.coeficiente, factor_n, x.letra, x.expoente))
        if i < len(a)-1:
            printf(" + ")


print("Soma -> 1 | Normalização -> 2 | Primitivar -> 3 | Derivar -> 4 ")

choice = int(input())
quantity = int(input("how much?: "))

a = []
new_a = []

while (quantity != 0):
    print("Polinómio")
    print("Enter coeficiente: ")
    coef = int(input())
    letra = input("Enter variável: ")
    print("Enter expoente: ")
    exp = int(input())
    p = Pol(coef, letra, exp)
    a.append(p)
    quantity = quantity - 1

i = 0
tam=len(a)
if choice == 1:
    while i+1 < tam:
        a.sort(key=lambda a: a.expoente, reverse=False)  
        Pol.soma(a, a[i], a[i + 1], i)
        i = i + 1

    a = list(set(a))
    j = 0
    while j < len(a):
        if j ==0 :
            if a[j].expoente == 1 and a[j].coeficiente > 1:
                printf('%d%s ' % (a[j].coeficiente, a[j].letra))
            elif a[j].coeficiente == 1:
                printf('%s^%d ' % ( a[j].letra,a[j].expoente))
            elif a[j].coeficiente == 0:
                printf("0")
            elif a[j].expoente == 0 and a[j].coeficiente != 0:
                printf("%d" %(a[j].coeficiente))
            elif a[j].expoente == 1 and a[j].coeficiente == 1:
                printf('%s ' % a[j].letra)
            elif a[j].expoente != 1 and a[j].coeficiente != 0:
                printf('%d%s^%d ' % (a[j].coeficiente, a[j].letra, a[j].expoente))
            elif a[j].expoente == 1 and a[j].coeficiente == -1:
                printf('-%s ' % (a[j].letra, a[j].expoente))
            elif a[j].expoente > 1 and a[j].coeficiente == -1:
                printf('-%s^%d ' % (a[j].letra, a[j].expoente))

        else:
            if a[j].expoente == 1 and a[j].coeficiente > 1:
                printf(' + %d%s ' % (a[j].coeficiente, a[j].letra))
            elif a[j].coeficiente == 1 and a[j].expoente:
                printf(' + %s^%d ' % (a[j].letra, a[j].expoente))
            elif a[j].coeficiente == 0:
                printf(" + 0")
            elif a[j].expoente == 0 and a[j].coeficiente!=0:
                printf(" + %d" % (a[j].coeficiente))

            elif a[j].expoente == 1 and a[j].coeficiente == 1:
                printf(' + %s ' % a[j].letra)
            elif a[j].expoente != 1 and a[j].coeficiente != 0:
                printf('+ %d%s^%d ' % (a[j].coeficiente, a[j].letra, a[j].expoente))
            elif a[j].expoente == 1 and a[j].coeficiente == -1:
                printf(' + -%s^%d ' % (a[j].letra, a[j].expoente))
            elif a[j].expoente == 1 and a[j].coeficiente == -1:
                printf(' + -%s ' % (a[j].letra, a[j].expoente))
            elif a[j].expoente > 1 and a[j].coeficiente == -1:
                printf(' + -%s^%d ' % (a[j].letra, a[j].expoente))

        j = j + 1


if choice == 2:
    while i < len(a):
        a.sort(key=lambda a: a.expoente, reverse=False)
        Pol.normalize(a, a[i], i)
        i = i + 1

if choice == 3:
    while i  < len(a):
        Pol.primitiva(a, a[i], i)
        i = i + 1
if choice == 4:
    while i < len(a):
        Pol.derivada(a, a[i], i)
        i = i + 1


