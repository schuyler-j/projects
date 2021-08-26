#include <iostream>


using namespace std;

int main(){

cout << "Hello";

int count = 0;
int letter = 12;
char name[] = "Jay Schuyler";
char *sub = name;
bool swap= true;

while(count < 100){
    int outp = 0;
    count++;
    for(int i = 0; i < count/6; i++){
        if (count % 3 == 0){
            do{
                cout<<" "<<*sub<<" ";
                sub++;
                swap = false;
            }
            while(*sub != NULL && swap);
            cout<<" ";
        }else{
            cout<<"0";
        }
    }
    if (count % 2 == 0){
        cout<<"0";
    }else{
        cout<<"1";
    }

}


}