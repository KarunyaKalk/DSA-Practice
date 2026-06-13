#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> fs(26, 0), ft(26, 0);

        for (char c : s) {
            fs[c - 'a']++;
        }

        for (char c : t) {
            ft[c - 'a']++;
        }

        return fs == ft;
    }
};

int main() {
    Solution obj;

    string s = "anagram";
    string t = "nagaram";

    if (obj.isAnagram(s, t))
        cout << "true" << endl;
    else
        cout << "false" << endl;

    return 0;
}