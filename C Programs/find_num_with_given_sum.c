/*Find all n-digit numbers with a given sum of digits*/
#include <stdio.h>
#include <string.h>
int c;
void append(char *s, char c)
{
        int len = strlen(s);
        s[len] = c;
        s[len+1] = '\0';
}
void findNdigitNums(char *res,int n,int sum)
{
  if(n && sum >= 0){
    char d = '0';

    char empty[] = "";
    if(strcmp(res, empty) == 0) d = '1';

    for(;d <= '9';d++){
        char str[10];
        strcpy(str, res);
        append(str, d);

      findNdigitNums(str, n-1, sum - (d - '0'));
    }
  }
  else if(n==0 && sum==0){
	  c++;
    printf("%s ", res);
  }
}
int main()
{

  int n,sum; scanf("%d %d", &n, &sum);
  char res[10] = "";
  findNdigitNums(res, n, sum);
  return 0;
}