def euclidean(a,b):
    if a<b:
        divisor = a
        dividend = b
    elif b<a:
        divisor = b
        dividend = a
    else:
        print "There's no point in doing this."

#know that we know which is the divisor and which is the dividend we can
#begin dividing and analyzing them.
    while dividend%divisor !=0:
        quotient = dividend / divisor
        remainder = dividend % divisor
        if remainder == 0:
            gcd = quotient
            print "Your greatest common divisor is %d" %(gcd)
            break;
        elif remainder != 0:
            newDividend=divisor
            newDivisor=dividend
            newRemainder=remainder
            dividend = divisor
            divisor = remainder
            remainder = divisor/remainder
            print "your greatest common divisor is %d" %(newRemainder)
        else:
            pass;

print euclidean(110,20)