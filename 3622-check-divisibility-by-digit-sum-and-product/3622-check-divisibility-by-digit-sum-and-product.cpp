class Solution {
public:
    bool checkDivisibility(int n) {
        int sum=0;
        int prod=1;
        int rem;
        int temp=n;
        while(n!=0){
            rem=n%10;
            sum+=rem;
            prod=prod*rem;
            n=n/10;
        }
        int s=sum+prod;
        if(temp%s==0){
            return true;
        }    
        return false;
        }
};