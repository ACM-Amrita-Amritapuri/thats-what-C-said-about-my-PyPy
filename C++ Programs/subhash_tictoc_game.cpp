# include <iostream>
# include <vector>
using namespace std;
class gameu{
    public :
    vector<int> v2 = {00,01,02,10,11,12,20,21,22};
    vector<int> g = {0,1,2,3,4,5,6,7,8};
    vector<string> v;
    vector<string> v1 = { " "," "," "," "," "," "," "," "," "};
    void boxes(){
    
    int k = 0;
    v = { "0","1","2","3","4","5","6","7","8"};
    for (int i=0;i<v.size();i++){
cout << "|" <<v[i] ;


if(k == 2){
    cout << "\n";
    k = -1;
}
k++;

    }}
    void inputt1(){
    int l;
    while(true){


    cout << "Enter The Location user1" << endl;
    cin >> l ;


        if(l>8){
            cout << "Please input the number between 0-8"<<endl;
        }
        else if(v1[l] == "O"){
cout << "please insert another place" << endl;
    }
    else if(v1[l] == "X"){
        cout << "Already u have inserted it ";
    }

    else{
        v1[l] = "X";
        break;
    }}

}
void inputt2(){
    int l1;
    while(true){


    cout << "Enter The Location user2" << endl;
    cin >> l1 ;
        if(l1>8){
            cout << "Please input the number between 0-8"<<endl;
        }
        else if(v1[l1] == "X"){
cout << "please insert another place" << endl;
    }
    else if(v1[l1] == "O"){
        cout << "Already u have inserted it ";
    }

    else{
        v1[l1] = "O";
        break;
    }}

}
 void realtimeprint(){
    
    int k = 0;

    for (int i=0;i<v1.size();i++){
cout << "|" <<v1[i] ;

if(k == 2){
    cout << "\n";
    k = -1;
}
k++;

    }
    }
 bool diagonal(){
        if((v1[0] == v1[4] && v1[4] == v1[8] && v1[0] != " ")  ){
        return  true;}
        if((v1[2] == v1[4] && v1[4] == v1[6] && v1[2] != " ")
                ){
            return (true);
        }
        return (false);
}
bool coloumn(){
    for(int j=0;j<3;j++){
        if((v1[j] == v1[j+3] && v1[j+3] == v1[j+6] && v1[j] != " ")){return (true);
        }
       }
    return (false);
    }

 bool row(){
        int k = 0;

            for(int j=0;j<3;j++){
                if(j == 1){
                    k = 3;
                }
                if(j == 2){
                    k = 6;
                }
                if(
                        (v1[k] == v1[k+1] && v1[k+1] == v1[k+2] && v1[k] != " ")){

                    return (true);
                }
                k++;



            }
    return (false);
}


inline bool over(){
        return row() || coloumn() || diagonal();
    }
    bool tie(){
        for (int kk = 0; kk<v1.size();kk++){
            if(v1[kk] != " "){
                return true;
            }
        }
        return false;
    }
};





int main(){
gameu sd;
sd.boxes();
cout << "----------------------" << "\n";
sd.realtimeprint();
while(true){
  sd.inputt1();
  sd.realtimeprint();

  if(sd.over()){
      cout <<  " Input user1 won the match" << endl;
      break;
  }
  sd.inputt2();
  sd.realtimeprint();
    if(sd.over()){
        cout <<  " Input user2 won the match" << endl;
        break;
    }


  }
if(sd.tie()){
    cout << "   ########        (Game Over)  --   TIE   --      #############" <<endl;
}





    return 0;
}