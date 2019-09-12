#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
	int coeficiente;
	char letra;
	int expoente;
	struct node *next;
	struct node *previous;

};

struct node *head = NULL;
struct node *current = NULL;
struct node *prev = NULL;

char d;
int err=0;
//display the list
void print_list(){
	struct node *current = head;
   //struct node *current = (struct node*) malloc(sizeof(struct node));
	while(current != NULL){
		if (current->coeficiente==1 && current->expoente==1 )
			printf("%c",current->letra);
		else if(current->coeficiente==1 && current->expoente==1)
			printf("(%c)",current->letra);
		else if(current->expoente==1)
			printf("(%d%c)",current->coeficiente,current->letra);
		else if(current->coeficiente==1)
			printf("(%c^%d)",current->letra,current->expoente);
		else
			printf("(%d%c^%d)",current->coeficiente ,current->letra,current->expoente);
		if(current->next !=NULL)
			printf(" + ");
		current = current -> next;
	}	
	printf("\n");
}
//insert link at the first location

void insertFirst(int coeficiente,char letra, int expoente) {
   //create a link
	struct node *link = (struct node*) malloc(sizeof(struct node));

	link->coeficiente = coeficiente;
	link->letra = letra;
	link->expoente = expoente;


   //point it to old first node
	link->next = head;

   //point first to new first node
	head = link;
}

int length() {
	int length = 0;
	struct node *current;

	for(current = head; current != NULL; current = current->next) {
		length++;
	}

	return length;
}

void sort() {

	int i, j, k, tempcoeficiente, tempexpoente;
	char tempchar;
	struct node *current;
	struct node *next;
	int size = length();
	k = size ;

	for ( i = 0 ; i < size - 1 ; i++, k-- ) {
		current = head;
		next = head->next;

		for ( j = 1 ; j < k ; j++ ) {   

			if ( current->expoente < next->expoente) {
				tempexpoente = current->expoente;
				current->expoente = next->expoente;
				next->expoente = tempexpoente;

				tempcoeficiente = current->coeficiente;
				current->coeficiente = next->coeficiente;
				next->coeficiente = tempcoeficiente;


				tempchar = current->letra;
				current->letra = next->letra;
				next->letra = tempchar;
			}

			current = current->next;
			next = next->next;
		}
	}   
}

void reverse(struct node** head_ref) {
	struct node* prev   = NULL;
	struct node* current = *head_ref;
	struct node* next;

	while (current != NULL) {
		next  = current->next;
		current->next = prev;   
		prev = current;
		current = next;
	}

	*head_ref = prev;
}
void normalize(){
	struct node *current = head;
	int factor_n=current->expoente;
	while(current != NULL){
		if(current->coeficiente==0 || current->expoente==0){
			printf("Erro \n");
			return;
		}
		if(current->coeficiente%factor_n == 0){
			current->coeficiente=current->coeficiente/factor_n;
			if(current->coeficiente==1 && current->expoente==1)
				printf("%c",current->letra);
			else if(current->coeficiente==1)
				printf("%c^%d ",current->letra,current->expoente);
			else if(current->expoente==1)
				printf("%d%c",current->coeficiente,current->letra);
			else
				printf("%d%c^%d ",current->coeficiente,current->letra,current->expoente);

		}
		else{
			if(current->expoente==1)
				printf("(%d/%d)%c ",current->coeficiente,factor_n,current->letra);
			else
				printf("(%d/%d)%c^%d ",current->coeficiente,factor_n,current->letra,current->expoente);
		}
		if(current->next!=NULL)
			printf(" + ");
		if(current->next==NULL)
			printf("\n");
		current = current -> next;
	}
}
void normalize_p(struct node *current, int factor_n){
	//struct node *current = head;
	factor_n +=1;
	if(current->coeficiente%factor_n ==0){
		current->coeficiente=current->coeficiente/factor_n;
		if(current->coeficiente==0 || current->expoente==0){
			printf("Erro \n");
			return;
		}
		else if(current->coeficiente==1 && current->expoente!=0)
			printf("%c^%d ",current->letra,current->expoente+1);
		else if(current->expoente == 1)
			printf("%d%c ", current->coeficiente,current->letra);
		else if(current->expoente == 0 && current->coeficiente==1)
			printf("%c ",current->letra);
		else if(current->expoente == 0 && current->coeficiente!=1)
			printf("%d%c ", current->coeficiente,current->letra);
		else if(current->expoente == 1 && current->coeficiente == 1)
			printf("%c ", current->letra);
		else 
			printf("%d%c^%d ",current->coeficiente,current->letra,current->expoente+1);
	}
	else
		printf("(%d/%d)%c^%d ",current->coeficiente,factor_n,current->letra,current->expoente+1);
	if(current->next!=NULL)
		printf("+ ");
	if(current->next==NULL)
		printf("+ constante\n");
}


void normalize_d(struct node *current){
	int expoente = current->expoente-1;
	int coeficiente = current->coeficiente*current->expoente;

	if(current->coeficiente==0 || current->expoente==0){
		printf("Erro \n");
		return;
	}
	else if(current->expoente==1 && current->coeficiente==1)
		printf("%d",coeficiente);
	else if(current->expoente==1)
		printf("%d",coeficiente);
	else if(expoente==1)
		printf("%d%c",coeficiente,current->letra);
	else
		printf("%d%c^%d",coeficiente,current->letra,expoente);

	if(current->next!=NULL)
		printf(" + ");
	if(current->next==NULL)
		printf("\n");
}

void soma(){
	struct node *current =head;
	if(current->coeficiente==0 || current->expoente==0){
		printf("Erro \n");
		err=1;
		return;
	}

	while(current->next != NULL ){

		if(current->letra == current->next->letra && current->expoente == current->next->expoente){

			current->coeficiente = current->coeficiente + current->next->coeficiente;
			current->letra = current->next->letra;
			current->expoente = current->next->expoente;
			if(current->next!=NULL)
				current->next = current->next->next;
		}
		else{
			current = current ->next;
		}

	}
}

void primitiva(){
	struct node *current = head;
	while(current != NULL){
		//current->expoente=1;
		//current->coeficiente /= current->expoente;
		normalize_p(current,current->expoente);
		current = current ->next;
	}
}
void derivada(){
	struct node *current = head;
	while(current != NULL){
		normalize_d(current);
		current = current->next;
	}
}
int main() {
	struct node *current =(struct node*) malloc(sizeof(struct node));
	int flag=0;
	int n,i=0,a,c;
	char b;
	printf("Quantos polinomios sao?\n");
	scanf("%d",&n);	
	printf("Que operacao quer fazer ?\n");
	printf("1 - Primitiva | 2 - Derivada | 3 - Normalizar | 4 - Somar\n");
	scanf("%d",&flag);
	while(flag!=1 && flag!=2 && flag!=3 && flag!=4) {
		if(flag==1 || flag==2 || flag==3 || flag==4)
			break;
		printf("Numero invalido, volte a inserir !\n");
		printf("Que operacao quer fazer ?\n");
		printf("1 - Primitiva | 2- Derivada | 3 - Normalizar | 4 - Somar\n");
		scanf("%d",&flag);
	}
	while(i<n){
		printf("Coeficiente do %d polinomio: ",i+1);
		scanf("%d",&a);
		printf("Variável do %d polinomio: ",i+1);
		getchar();
		scanf("%c",&b);
		printf("Expoente do %d polinomio: ",i+1);
		scanf("%d",&c);
		insertFirst(a,b,c);
		reverse(&head);
		printf("\n");
		i++;
	}
	printf("Resultado: ");
	if(flag==1){
		sort();
		primitiva();
	}
	else if(flag==2){
		sort();
		derivada();
	}
	else if(flag==3){
		sort();
		normalize();
		//print_list(); 

	}
	else if(flag==4){
		sort();
		soma();
		if(err!=1)
			print_list();

	}

}
