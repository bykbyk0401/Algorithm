#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a,b;
    cin >> a >> b;

    int* x = new int[a];

    for(int i=0; i<a; i++){
        cin >> x[i];
    }

    for(int i=0; i<a; i++){
        if(x[i]<b) cout << x[i] << " ";
    }

    
}