#include<iostream>
#include<string.h>
using namespace std;
int main() {
   cout<<"Enter the message:
";
   char msg[100];
   cin.getline(msg,100); 
   int i, j, length,choice,key;
   cout << "Enter key: ";
   cin >> key;  
   gth = strlen(msg);
   cout<<"Enter your choice 1. Encryption 2. Decryption ";
   cin>>choice;
   if (choice==1) 
      char ch;
      for(int i = 0; msg[i] != '\0'; ++i) {
         ch = msg[i];
         
         If (ch >= 'a' && ch <= 'z'){
            ch = ch + key;
            if (ch > 'z') {
               ch = ch - 'z' + 'a' - 1;
            }  
            msg[i] = ch;
         }
         else if (ch >= 'A' && ch <= 'Z'){
            ch = ch + key;
            if (ch > 'Z'){
               ch = ch - 'Z' + 'A' - 1;
            }
            msg[i] = ch;
         }
      }
      printf("Encrypted message: %s", msg);
   }
   else if (choice == 2) { 
      char ch;
      for(int i = 0; msg[i] != '\0'; ++i) {
         ch = msg[i];
         if(ch >= 'a' && ch <= 'z') {
            ch = ch - key;
            if(ch < 'a'){
               ch = ch + 'z' - 'a' + 1;
            }
            msg[i] = ch;
         }
         else if(ch >= 'A' && ch <= 'Z') {
            ch = ch - key;
            if(ch < 'A') {
               ch = ch + 'Z' - 'A' + 1;
            }
            msg[i] = ch;
         }
      }
      cout << "Decrypted message: " << msg;
   }
}