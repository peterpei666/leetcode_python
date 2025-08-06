#include <stdio.h>
#include <stdlib.h>

int findTheWinner(int n, int k)
{
    int i,ans=0;
    for(i=2;i<=n;i++)
    {
        ans=(ans+k)%i;
    }
    return ans+1;
}
