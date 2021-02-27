#include<stdio.h>
int main(int arg,char* argv[])
{
  char t[100];
  char s[50]=" -d \'<?xml version=";
	  strcat(s,"\"1.0\"");
	  strcat(s,"?>");
	  strcat(s,"<methodCall><methodName>system.listMethods</methodName></methodCall>\'");
 char tmp[100]="curl \"";
 strcat(tmp,argv[1]);
 strcat(tmp,"\"");
 strcat(tmp,s);
 system(tmp);
 
}
