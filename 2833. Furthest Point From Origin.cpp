#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int furthestDistanceFromOrigin(const string& moves)
    {
        int n = (int)moves.size();
        int l = 0, r = 0;
        for (int i = 0; i < n; i++)
        {
            l += moves[i] == 'L';
            r += moves[i] == 'R';
        }
        return abs(l - r) + (n - l - r);
    }
};
