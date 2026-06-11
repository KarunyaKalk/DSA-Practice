class Solution {
public:
    int hammingWeight(int n) {
      int c=0;
      while(n){
        c+=n%2;
        n/=2;
      }
      return c;  
    }
};

class Solution {
public:
    int hammingWeight(int n) {
      int c=0;
      while(n){
        n=n&n-1;
        c++;
      }
      return c;  
    }
};