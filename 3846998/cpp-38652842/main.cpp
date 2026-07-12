#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define vector_element_type int
#define vector_element_size 4
typedef struct cvector{
    vector_element_type *elements;
    int element_number;
    int maxsize;
} cvector;
cvector*new_cvector(){
    cvector*res=(cvector*)malloc(sizeof(cvector*));
    res->elements=(vector_element_type*)malloc(8*vector_element_size);
    res->element_number=0;
    res->maxsize=8;
    return res;
}
vector_element_type*cvector_get_element(cvector*v,int p){
    return v->elements+p;
}
vector_element_type*create(vector_element_type*old,int oldsize){
    vector_element_type*_new=(vector_element_type*)malloc(oldsize*vector_element_size*2);
    memcpy(_new,old,oldsize*vector_element_size);
    return _new;
}
void cvector_pop_back(cvector*v){
    v->element_number--;
}
void cvector_push_back(cvector*v,vector_element_type value){
    if(v->element_number==v->maxsize) v->elements=create(v->elements,v->maxsize);
    v->elements[v->element_number++]=value;
}
void cvector_print(cvector*v){
    printf("cvector object{");
    int i=0;
    for(i=0;i<v->element_number;i++) printf("%d,",v->elements[i]);
    printf("}\n");
}
#undef vector_element_type
#undef vector_element_size
int main()
{
    cvector*v=new_cvector();
    cvector_push_back(v,10);
    cvector_push_back(v,20);
    cvector_push_back(v,10);
    cvector_push_back(v,20);
    cvector_push_back(v,10);
    cvector_push_back(v,20);
    cvector_push_back(v,10);
    cvector_push_back(v,20);
    cvector_push_back(v,10);
    cvector_push_back(v,20);
    cvector_print(v);
    return 0;
}