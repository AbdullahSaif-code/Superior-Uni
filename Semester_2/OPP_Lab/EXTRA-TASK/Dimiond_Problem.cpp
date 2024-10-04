#include <iostream>
using namespace std;

class a{
    protected: 

    private: 

    public:
     a(){
        cout<<"grandfather\n";
    }
};
class b: public a{
    public:
     b(){
        cout<<"father\n";
     }
};
class c: public a{
    public:
     c(){
        cout<<"mather\n";
     }
};
class d: public b, public c{
    public:
     d(){
        cout<<"son\n";
     }
};

int main(){
    d obj1;
    
}