#include <iostream>
#include <string>
using namespace std;

int main(){
    string word1 ="abc";
    string word2 ="pqr";
    string result ;
    string x ;
    int i;
    for (i=0;i<word2.length();i++)
    {
     x="";
     x= word1[i] + word2[i];
     result += x;
    }
    cout<<result;
    return 0;
}