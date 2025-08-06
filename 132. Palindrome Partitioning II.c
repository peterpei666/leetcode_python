#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static inline int min(int a,int b)
{
    return a<b?a:b;
}

int palindrome(int n,int pal[n+1][n+1],char* s,int i,int j)
{
    if(i>=j) return 1;
    if(pal[i][j]!=-1) return pal[i][j];
    if(s[i]==s[j]) return pal[i][j]=palindrome(n,pal,s,i+1,j-1);
    return pal[i][j]=0;
}

int dfs(int n,int t[n+1][n+1],int pal[n+1][n+1],char* s,int i,int j)
{
    if(i>=j||palindrome(n,pal,s,i,j))
    {
        return 0;
    }
    if(t[i][j]!=-1)
    {
        return t[i][j];
    }
    int res=INT_MAX;
    for(int k=i;k<j;k++)
    {
        if(palindrome(n,pal,s,i,k))
        {
            int r=(t[k+1][j]!=-1)?t[k+1][j]:(t[k+1][j]=dfs(n,t,pal,s,k+1,j));
            res=min(res,r+1);
        }
    }
    return t[i][j]=res;
}

int minCut(char* s)
{
    int n=(int)strlen(s);
    int pal[n+1][n+1];
    memset(pal,-1,sizeof(pal));
    int t[n+1][n+1];
    memset(t,-1,sizeof(t));
    return dfs(n,t,pal,s,0,n-1);
}
