class Solution(object):
    # @return an integer
    def _reverse_helper(self, x):
        if -10 < x < 10:
            return x, 1
        else:
            rest, digits = self._reverse_helper(x / 10)
            return x % 10 * (10 ** digits) + rest, digits + 1
 
    def reverse2(self, x):
        if x < 0:   
            (result,digits) = self._reverse_helper(-x)
            result =result * -1
        else:       
            (result,digits) = self._reverse_helper(x)
 
        if -2147483648L <= result <= 2147483647L:   
            return result
        else:                                       
            return 0
        
    def reverse(self,x):
        num = 1
        if (x<0 ):
            x = x * -1
            num = -1
        result = 0
        while (x != 0 ):
            tail = x%10
            x = x/10
            result = result * 10 + tail
        result = result * num 
        if -2147483648L <= result <= 2147483647L:   
            return result
        else:                                       
            return 0
        return result
