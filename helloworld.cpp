//#include<stdio.h>
//#include<stdlib.h>
//int compare(const void *x,const void*y){
//	int intx=*((int*) x);int inty=*((int*)y);
//	if(intx>inty){return 1;
//	}
//	else if(intx==inty){
//		return 0;
//	}else{return -1;
//	}
//}
//int main(){
//	 int arr[] = {5, 2, 9, 1, 5, 6};
//	 qsort(arr,6,sizeof(int),compare);
//	 for(int i=0;i<6;i++){
//	 	printf("%d",arr[i]);
//	 }
//	

#include<stdio.h>
#include<stdlib.h>
int compare(const void* x,const void* y){
	int xValue=*((int*)x);int yValue=*((int* )y);
	if(xValue<yValue){
		return -1;
	}if(xValue==yValue){return 0;
	}else{return 1;
	}
	
}
int main(){
	int arr[5]={5,4,3,2,1};
	qsort(arr,5,sizeof(int),compare);
	for(int i=0;i<5;i++){
		printf("%d",arr[i]);	}
}






