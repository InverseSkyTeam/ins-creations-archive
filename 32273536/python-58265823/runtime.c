#define _CRT_SECURE_NO_WARNINGS
#include <stdint.h>
#include <stdio.h>

void print_int(int32_t value) { printf("%d", value); }
int32_t read_int() {
  int32_t a;
  scanf("%d", &a);
  return a;
}