class Solution {
public:
    bool isPowerOfFour(int n) {
        int res;
     if (n<=0)return false;
     res = 1;
     while (res<n)res*=4;
     return res == n;   
    }
};