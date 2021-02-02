pi = 3.141592653589793
import math
math.sqrt
import math
math.cos
import math
math.pow
import math
math.acos
import math
math.sin
import math
math.asin
import math
math.tan
import math
math.atan
r = 'angle' , 'side'
r = input('angle or side?')
if r== 'angle':
    x = 'cos', 'sin' , 'tan'
    x = input('cos, sin or tan?')
    if x == 'cos':
        a = 'yes' , 'no'
        a = input('do you need to find the hypotenuse?')
        if a == 'yes':
            b = float(input('what is the length of side one')) 
            c = float(input('what is teh lenght of side two'))
            z = math.sqrt((b * b) * (c * c))
            d = float(input('what is the length of the adjacent side'))
            print('theta:')
            print(math.acos(d/z) * (180/pi))
        elif a == 'no':
            k = float(input('what is the length of the hypotenuse'))
            e = float(input('what is the length of the adjacent side'))
            print('theta:')
            print(math.acos(e/k) * (180/pi))
    elif x == 'sin':
        a = 'yes' , 'no'
        a = input('do you need to find the hypotenuse?')
        if a == 'yes':
            b = float(input('what is the length of side one')) 
            c = float(input('what is teh lenght of side two'))
            z = math.sqrt((b * b) * (c * c))
            d = float(input('what is the length of the opposite side'))
            print('theta:')
            print(math.asin(d/z) * (180/pi)) 
        elif a == 'no':
            k = float(input('what is the length of the hypotenuse'))
            e = float(input('what is the length of the oppostie side'))
            print('theta:')
            print(math.asin(e/k) * (180/pi))
    elif x == 'tan':
        a = float(input('what is the length of the adjacent side?'))
        b = float(input('what is the length of the opposite side?'))
        print('theta')
        print(math.atan(b/a) * (180/pi))
elif r == 'side'
    
        
