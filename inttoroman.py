def int_to_roman(s):
    int1=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    symbol=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    roman=""
    i=12                                                                                                                                                                                
    if s>=4000 :
        return "INVALID,TRY ANOTHER ONE"
    else:
        while s!=0:
            if int1[i]<=s:
                s -= int1[i]
                roman+=symbol[i]
            else:
                i -= 1 
        return roman
h=int(input("How many times you wanna do it?  "))
for u in range(h):
    j=int(input("no.:   "))
    print(int_to_roman(j))



















