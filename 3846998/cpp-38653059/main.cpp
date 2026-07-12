#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define stack_element_type int
#define stack_element_size 4
typedef struct cstack{
    stack_element_type *elements;
    int element_number;
    int maxsize;
} cstack;
cstack*new_cstack(){
    cstack*res=(cstack*)malloc(sizeof(cstack*));
    res->elements=(stack_element_type*)malloc(8*stack_element_size);
    res->element_number=0;
    res->maxsize=8;
    return res;
}
stack_element_type*cstack_top(cstack*v){
    return v->elements+v->element_number-1;
}
stack_element_type*create(stack_element_type*old,int oldsize){
    stack_element_type*_new=(stack_element_type*)malloc(oldsize*stack_element_size*2);
    memcpy(_new,old,oldsize*stack_element_size);
    return _new;
}
void cstack_pop(cstack*v){
    v->element_number--;
}
void cstack_push(cstack*v,stack_element_type value){
    if(v->element_number==v->maxsize) v->elements=create(v->elements,v->maxsize);
    v->elements[v->element_number++]=value;
}
#undef stack_element_type
#undef stack_element_size
int main()
{
    cstack*v=new_cstack();
    cstack_push(v,10);
    cstack_push(v,20);
    cstack_push(v,10);
    cstack_push(v,20);
    cstack_push(v,10);
    cstack_push(v,20);
    cstack_push(v,10);
    cstack_push(v,20);
    cstack_push(v,10);
    cstack_push(v,20);
    printf("%d",*cstack_top(v));
    return 0;
}