def turboPascalHexToFloat(real48):
    """
    real48 is a 6 bytes arry of int
    return the float value of a 48-bits pascal array as define at 
    http://www.shikadi.net/moddingwiki/Turbo_Pascal_Real
    """
    exponentbase = 129
    exponent = real48[0] - exponentbase #The exponent is offset so deduct the base.
    #Now Calculate the mantissa
    mantissa = 0.0
    value = 1.0
    #For Each Byte.
    for i in range(5,0,-1):
        startbit = 7
        if (i == 5):
            startbit = 6    #skip the sign bit.
        #For Each Bit
        for j in range(startbit,-1,-1):
            value = value / 2#Each bit is worth half the next bit but we're going backwards.
            if (((real48[i] >> j) & 1) == 1):    #if this bit is set.
                mantissa += value #add the value.
    
    if (mantissa == 1.0 and real48[0] == 0): #Test for null value
        return 0.0
    if ((real48[5] & 0x80) == 1): #Sign bit check
        mantissa = -mantissa
    return (1 + mantissa) * 2.0**exponent

#expect as input an array in hex 
#for exemple: "8B 00 00 00 00 16" is equal to 1200
list_hex = input()
a = list(map(lambda a: int(a,16),list_hex.split()))
r = turboPascalHexToFloat(a)
print(r)