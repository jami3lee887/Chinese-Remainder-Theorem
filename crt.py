a1 = int(input("a1: "))
b1 = int(input("b1: "))
m1 = int(input("m1: "))

a2 = int(input("a2: "))
b2 = int(input("b2: "))
m2 = int(input("m2: "))

print(f"your inputs are:  {a1}x = {b1} (mod {m1})")
print(f"and:  {a2}x = {b2} (mod {m2})")

eq1 =[a1,b1,m1]
eq2 =[a2,b2,m2]
print(eq1)
print(eq2)

# check:
# m1 m2 are coprime, as well as both are positive integers
#check LDET 1 RULES

#if thats good:
#check if a1 = 1
def get_gcd(beforepf_in):
    a = beforepf_in[0]
    b = beforepf_in[1]
    if a > b:
        x1, x2, y1, y2 = 1, 0, 0, 1
        r1, r2 = a, b 
    elif a < b:
        x1, x2, y1, y2 = 0, 1, 1, 0 
        r1, r2 = b, a 
    
    while r2 != 0:
        q = r1//r2 
        x3 = x1 - q * x2
        y3 = y1 - q * y2
        r3 = r1 - q * r2
        x1 = x2 
        y1 = y2 
        r1 = r2 
        x2 = x3 
        y2 = y3 
        r2 = r3
        if r2 == 0:
            return [x1, y1, r1]
        
def get_xy(beforepf_in):
    abc = get_gcd(beforepf_in)
    #print(f"gcd check: {abc}")
    a1 = abc[0]
    b1 = abc[1]
#     c1 = abc[2]
#     if (beforepf[2]/c1)%1 == 0.0:
#         factor = beforepf[2] / c1
    return [a1, b1] #has been tabbed ****************
        
#     elif type(beforepf[2]/c1) == float:
#         factor = beforepf[2] / c1
#         
#         return [int(a1 * factor), int(b1 * factor)]
#     else:
#         return None
#

if a1 != 1:
    ldetCoef = (get_xy([a1, m1, 1])[0])
    preppedEQ1 = [(a1* ldetCoef)%m1, (b1*ldetCoef)%m1, m1]
    
if a1 == 1:
    preppedEQ1 = [a1, b1, m1]
    
    
beforepf = [(a2*preppedEQ1[2]), (b2 - (a2*preppedEQ1[1])), m2]
mod = beforepf[2]
if beforepf[0] != 1:
    #ldet FN being ldet first number, which is the coefficient on the first value,
    #since the second value is useless, since it's the mod
    ldetCoef = (get_xy([beforepf[0], mod, 1])[0])
    afterpf = [(beforepf[0]* ldetCoef)%mod, (beforepf[1]*ldetCoef)%mod, mod]
    print(f"so now we have: {afterpf[0]}k = {afterpf[1]} (mod {mod})")
#i don't think case occurs much but i do think that it will happen sometimes
#just modding here to make numbers nicer
else:
    afterpf = [(a2*preppedEQ1[2])%mod, (b2 - (a2*preppedEQ1[1]))%mod, mod]
    
#first value is N(subscript 0), and second answer is simply just m1*m2, by CRT
finalAnswer = [(preppedEQ1[1] + (preppedEQ1[2]*afterpf[1])), (preppedEQ1[2]*mod)]
print(f"x = {finalAnswer[0]} (mod {finalAnswer[1]})")
        
        
        
        
        
        


    


    




