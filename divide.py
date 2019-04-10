##########################################
#Referencias: 
# https://www.geeksforgeeks.org (quest de mult) 
# https://www.pdfdrive.com/competitive-programming-3-e32649251.html
# Slides UFMG professor Loureiro
#
#SomaeSub
import sys 
import math

class Number:
    def _init_(self, str_n):
        self.n = str_n

    def _add_(self, other):
        aux = 0
        if len(self.n) < len(other.n):
            self.n, other.n = other.n, self.n
        a = self.n[::-1]
        b = other.n[::-1] + abs(len(self.n) - len(other.n)) * '0'
        r = str()
        for i in range(len(b)):
            r += str((int(a[i]) + int(b[i]) + aux) % 10)
            aux = int((int(a[i]) + int(b[i])) / 10)
        return Number(r[::-1])

    def _sub_(self, other):
        if len(self.n) < len(other.n):
            self.n, other.n = other.n, self.n
        a = self.n[::-1]
        b = other.n[::-1] + abs(len(self.n) - len(other.n)) * '0'
        r = str()
        for i in range(len(b)):
            p_a, p_b = int(a[i]), int(b[i])
            if p_a < p_b:
                for j in range(i, len(a)):
                    if int(a[j]) > 0:
                        print(str(int(a[j])-1)) 
                        a[j] = str(int(a[j]) - 1)
                        a[j + 1] = str(int(a[j + 1]) + 1)
                p_a, p_b = int(a[i]), int(b[i])
            r += str(p_a - p_b)
        return Number(r[::-1])

    def _str_(self):
        zero = True
        for i in range(len(self.n)):
            if self.n[i] != '0':
                zero = False
        return '0' if zero else self.n


x = Number('99') - Number('10')
print (x)

###################################################
#Divisão&Multiplicacao

    def _init_(self, str_n):
        self.n = str_n

    def _add_(self, other):
        aux = 0
        if len(self.n) < len(other.n):
            self.n, other.n = other.n, self.n
        a = self.n[::-1]
        b = other.n[::-1] + abs(len(self.n) - len(other.n)) * '0'
        r = str()
        for i in range(len(b)):
            r += str((int(a[i]) + int(b[i]) + aux) % 10)
            aux = int((int(a[i]) + int(b[i])) / 10)
        return Number(r[::-1])

    def _sub_(self, other):
        if len(self.n) < len(other.n):
            self.n, other.n = other.n, self.n
        a = self.n[::-1]
        b = other.n[::-1] + abs(len(self.n) - len(other.n)) * '0'
        r = str()
        for i in range(len(b)):
            p_a, p_b = int(a[i]), int(b[i])
            if p_a < p_b:
                for j in range(i, len(a)):
                    if int(a[j]) > 0:
                        print(str(int(a[j])-1)) 
                        a[j] = str(int(a[j]) - 1)
                        a[j + 1] = str(int(a[j + 1]) + 1)
                p_a, p_b = int(a[i]), int(b[i])
            r += str(p_a - p_b)
        return Number(r[::-1])

    def zeroPad(self,numberString, zeros, left = True):

        for i in range(zeros):

            if left:
                numberString = '0' + numberString
            else:
                numberString = numberString + '0'
        return numberString

     

    def multiply(x, y):

        x = str(x)
        y = str(y)

        zeroPadding = 0
        partialSum = 0

        for i in range(len(y) -1, -1, -1):       

            carry = 0
            partial = ''

            partial = zeroPad(partial, zeroPadding, False)

            for j in range(len(x) -1, -1, -1):

                z = int(y[i])*int(x[j])

                z += carry
                z = str(z)
                if len(z) > 1:

                    carry = int(z[0])

                else:

                    carry = 0   

                partial = z[len(z) -1] + partial
            if carry > 0:

                partial = str(carry) + partial    
            partialSum += int(partial)
            zeroPadding += 1

        return partialSum

    def _mul_(self, y ):


        x = str(self.n)

        y = str(y)
        if len(x) == 1 and len(y) == 1:

            return int(x) * int(y)

        if len(x) < len(y):

            x = self.zeroPad(x, len(y) - len(x))

        elif len(y) < len(x):

            y = self.zeroPad(y, len(x) - len(y))

        n = len(x)

        j = n//2

        if (n % 2) != 0:

            j += 1    

        BZeroPadding = n - j

        AZeroPadding = BZeroPadding * 2

        a = int(x[:j])

        b = int(x[j:])

        c = int(y[:j])

        d = int(y[j:])

        ac = a*c

        bd = b*d

        k = (a + b)* (c + d)

        A = int(self.zeroPad(str(ac), AZeroPadding, False))

        B = int(self.zeroPad(str(k - ac - bd), BZeroPadding, False))

        return A + B + bd

    def _str_(self):
        zero = True
        for i in range(len(self.n)):
            if self.n[i] != '0':
                zero = False
        return '0' if zero else self.n


x = Number('11')* Number('110')
print (x)  

##########
#exp: 
 def pow (a,b):
        result = 1
        while b:
            if b%2 == 1:
                result = multiply(result, a)
            b = dividy(b,2)
            a = multiply(a , a) 
        return result


###################################################
#Matrizes


def mor(p, n): 
    m = [[0 for x in range(n)] for x in range(n)] 

    for i in range(1, n): 
        m[i][i] = 0
  
    
    for L in range(2, n): 
        for i in range(1, n-L+1): 
            j = i+L-1
            m[i][j] = sys.maxint 
            for k in range(i, j): 
  
                
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 
                if q < m[i][j]: 
                    m[i][j] = q 
  
    return m[1][n-1] 

arr = [1, 2, 3 ,4] 
size = len(arr) 
  
print(str(mor(arr, size)))

