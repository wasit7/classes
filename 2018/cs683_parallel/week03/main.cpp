/* freopen example: redirecting stdout */
#include <stdio.h>
#include <iostream>
using namespace std;

int main ()
{
    freopen ("myfile.txt","w",stdout);
    cout<<"This sentence is redirected to a file.\n";
    fclose (stdout);
    return 0;
}