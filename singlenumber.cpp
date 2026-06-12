class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }
        return ans;
    }
};


//single number 2
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans=0;
        for(int i=0;i<32;i++){
            int c=0;
             for(int x:nums){
                if ((x>>i)&1)c++;
             }
             if(c%3)ans|=(1<<i);
        }
        return ans;
    }
};

//single number 3
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xorsum=0;
        for(int x:nums)xorsum^=x;
        int lowbit=xorsum&(-xorsum);
        int a=0,b=0;
        for(int x:nums){
            if(x&lowbit)a^=x;
            else b^=x;
        }
        return {a,b};
    }
};

//single number 3
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long long xorsum = 0;

        for (int x : nums)
            xorsum ^= x;

        long long lowbit = xorsum & (-xorsum);

        int a = 0, b = 0;

        for (int x : nums) {
            if (x & lowbit)
                a ^= x;
            else
                b ^= x;
        }

        return {a, b};
    }
};