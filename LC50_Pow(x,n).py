
"""
x^n :
2^7 =  2^3*2^3*2^1
2^3 =  2^1*2^1*2
2^1 = 2^0 *2^0*2
2^0 =1
for odd n, we do (x^n/2)(x^n/2)(x)
for even n, we dont have to multiply with extra 2 i.e. x

TC = O(n) as we will multiply x for n times.
SC = O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n ==0:
            return 1
        if n<0:
            n=n*-1
            x=1/x
        
        result = self.myPow(x,n//2)
        if n%2 == 0:
            return result*result
        else:

            return result*result*x
            