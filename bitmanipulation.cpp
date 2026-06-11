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