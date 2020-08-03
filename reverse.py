class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        x1=abs(x)
        while x1 !=0:
            cut=x1%10
            ans=ans*10+cut
            x1=x1//10
        if ans<2**31:
            return -ans if x<0 else ans
        else:
            return 0
