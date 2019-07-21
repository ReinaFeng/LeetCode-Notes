# 326. Power of Three

# Loop
    while(n>1):
        if n%3 !=0:
            return False
        else:
            n=n//3
            
    return True



# No loop
return n > 0 and 1162261467 % n == 0

#Math
return n > 0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10