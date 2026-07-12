#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef void (*freer_t)(void *);

/*
我可不希望Rusp泛型是这样实现的（
*/

#define VEC(T)                                                                 \
  struct {                                                                     \
    size_t len, cap;                                                           \
    T *data;                                                                   \
  }

#define VEC_INIT(VECT)                                                         \
  ({                                                                           \
    VECT vec;                                                                  \
    vec.len = 0;                                                               \
    vec.cap = 8;                                                               \
    vec.data = malloc(sizeof(typeof(*vec.data)) * vec.cap);                    \
    vec;                                                                       \
  })

#define VEC_PUSH(vec, val)                                                     \
  do {                                                                         \
    if (vec.len == vec.cap) {                                                  \
      vec.cap *= 2;                                                            \
      vec.data = realloc(vec.data, sizeof(typeof(*vec.data)) * vec.cap);       \
    }                                                                          \
    vec.data[vec.len++] = val;                                                 \
  } while (0)

#define VEC_POP(vec) vec.data[--vec.len]

#define VEC_GET(vec, i) vec.data[i]

#define VEC_FREE(vec, freer)                                                   \
  do {                                                                         \
    if (freer) {                                                               \
      for (size_t i = 0; i < vec.len; i++) {                                   \
        ((freer_t)freer)(&vec.data[i]);                                        \
      }                                                                        \
    }                                                                          \
    free(vec.data);                                                            \
  } while (0)

typedef VEC(char) string;

/*
来坨大的（
*/

size_t get_hash(char *key);

#define HASHTABLE(T)                                                           \
  struct {                                                                     \
    size_t len, cap;                                                           \
    struct {                                                                   \
      size_t hash;                                                             \
      char *key;                                                               \
      T val;                                                                   \
    } *data;                                                                   \
  }

#define TABLE_INIT(TABLET)                                                     \
  ({                                                                           \
    TABLET table;                                                              \
    table.len = 0;                                                             \
    table.cap = 8;                                                             \
    table.data = calloc(table.cap, sizeof(typeof(*table.data)));               \
    table;                                                                     \
  })

#define TABLE_GET(table, KEY)                                                  \
  ({                                                                           \
    size_t hash = get_hash(KEY);                                               \
    typeof(table.data[0].val) *val = NULL;                                     \
    for (size_t i = hash % table.cap, cnt = 0; cnt < table.cap;                \
         i = (i + 1) % table.cap, cnt++) {                                     \
      if (table.data[i].key && hash == table.data[i].hash &&                   \
          strcmp(table.data[i].key, KEY) == 0) {                               \
        val = &table.data[i].val;                                              \
      }                                                                        \
    }                                                                          \
    val;                                                                       \
  })

#define TABLE_INS(table, KEY, VAL)                                             \
  do {                                                                         \
    size_t hash = get_hash(KEY);                                               \
    bool found = false;                                                        \
    for (size_t i = hash % table.cap, cnt = 0; cnt < table.cap;                \
         i = (i + 1) % table.cap, cnt++) {                                     \
      if (table.data[i].key && table.data[i].hash == hash &&                   \
          strcmp(table.data[i].key, KEY) == 0) {                               \
        table.data[i].val = VAL;                                               \
        found = true;                                                          \
        break;                                                                 \
      }                                                                        \
    }                                                                          \
    if (!found) {                                                              \
      if (table.len == table.cap / 2) {                                        \
        typeof(table.data) newdata =                                           \
            calloc(table.cap * 2, sizeof(typeof(*table.data)));                \
        for (size_t i = 0; i < table.cap; i++) {                               \
          if (!table.data[i].key)                                              \
            continue;                                                          \
          for (size_t j = table.data[i].hash % (table.cap * 2), cnt = 0;       \
               cnt < table.cap * 2; j = (j + 1) % (table.cap * 2), cnt++) {    \
            if (!newdata[j].key) {                                             \
              newdata[j] = table.data[i];                                      \
              break;                                                           \
            }                                                                  \
          }                                                                    \
        }                                                                      \
        free(table.data);                                                      \
        table.data = newdata;                                                  \
        table.cap *= 2;                                                        \
      }                                                                        \
      for (size_t i = hash % table.cap, cnt = 0; cnt < table.cap;              \
           i = (i + 1) % table.cap, cnt++) {                                   \
        if (!table.data[i].key) {                                              \
          table.data[i].hash = hash;                                           \
          table.data[i].key = KEY;                                             \
          table.data[i].val = VAL;                                             \
          table.len++;                                                         \
          break;                                                               \
        }                                                                      \
      }                                                                        \
    }                                                                          \
  } while (0)

#define TABLE_FREE(table, freer)                                               \
  do {                                                                         \
    if (freer) {                                                               \
      for (size_t i = 0; i < table.cap; i++) {                                 \
        if (table.data[i].key) {                                               \
          ((freer_t)freer)(&table.data[i].val);                                \
        }                                                                      \
      }                                                                        \
    }                                                                          \
    free(table.data);                                                          \
  } while (0)

size_t get_hash(char *key) {
  size_t hash = 0;
  for (int i = 0; key[i]; i++) {
    hash = hash * 31 + key[i];
  }
  // printf("%s %llu\n", key, hash);
  return hash;
}

typedef HASHTABLE(int) itable;

void test_string() {
  string s = VEC_INIT(string);
  VEC_PUSH(s, 'H');
  VEC_PUSH(s, 'e');
  VEC_PUSH(s, 'l');
  VEC_PUSH(s, 'l');
  VEC_PUSH(s, 'o');
  VEC_PUSH(s, '\0');
  printf("%s\n", s.data);
  VEC_FREE(s, 0);
}

void test_hashtable() {
  // 抽象测试
  itable table = TABLE_INIT(itable);
  TABLE_INS(table, "aaa", 0);
  TABLE_INS(table, "aab", 1);
  TABLE_INS(table, "aac", 2);
  TABLE_INS(table, "aba", 3);
  TABLE_INS(table, "abb", 4);
  TABLE_INS(table, "abc", 5);
  TABLE_INS(table, "aca", 6);
  TABLE_INS(table, "acb", 7);
  TABLE_INS(table, "acc", 8);
  TABLE_INS(table, "aaa", 9);
  TABLE_INS(table, "baa", 10);
  TABLE_INS(table, "bab", 11);
  TABLE_INS(table, "bac", 12);  
  TABLE_INS(table, "bba", 13);
  TABLE_INS(table, "bbb", 14);
  TABLE_INS(table, "bbc", 15);
  TABLE_INS(table, "bca", 16);
  TABLE_INS(table, "bcb", 17);
  TABLE_INS(table, "bcc", 18);
  TABLE_INS(table, "caa", 19);
  TABLE_INS(table, "cab", 20);
  TABLE_INS(table, "cac", 21);  
  TABLE_INS(table, "cba", 22);
  TABLE_INS(table, "cbb", 23);
  TABLE_INS(table, "cbc", 24);
  TABLE_INS(table, "cca", 25);
  TABLE_INS(table, "ccb", 26);
  TABLE_INS(table, "ccc", 27);
  printf("aaa %d\n", *TABLE_GET(table, "aaa"));
  printf("aab %d\n", *TABLE_GET(table, "aab"));
  printf("aac %d\n", *TABLE_GET(table, "aac"));
  printf("aba %d\n", *TABLE_GET(table, "aba"));
  printf("abb %d\n", *TABLE_GET(table, "abb"));
  printf("abc %d\n", *TABLE_GET(table, "abc"));
  printf("aca %d\n", *TABLE_GET(table, "aca"));
  printf("acb %d\n", *TABLE_GET(table, "acb"));
  printf("acc %d\n", *TABLE_GET(table, "acc"));
  printf("baa %d\n", *TABLE_GET(table, "baa"));
  printf("bab %d\n", *TABLE_GET(table, "bab"));
  printf("bac %d\n", *TABLE_GET(table, "bac"));
  printf("bba %d\n", *TABLE_GET(table, "bba"));
  printf("bbb %d\n", *TABLE_GET(table, "bbb"));
  printf("bbc %d\n", *TABLE_GET(table, "bbc"));
  printf("bca %d\n", *TABLE_GET(table, "bca"));
  printf("bcb %d\n", *TABLE_GET(table, "bcb"));
  printf("bcc %d\n", *TABLE_GET(table, "bcc"));
  printf("caa %d\n", *TABLE_GET(table, "caa"));
  printf("cab %d\n", *TABLE_GET(table, "cab"));
  printf("cac %d\n", *TABLE_GET(table, "cac"));
  printf("cba %d\n", *TABLE_GET(table, "cba"));
  printf("cbb %d\n", *TABLE_GET(table, "cbb"));
  printf("cbc %d\n", *TABLE_GET(table, "cbc"));
  printf("cca %d\n", *TABLE_GET(table, "cca"));
  printf("ccb %d\n", *TABLE_GET(table, "ccb"));
  printf("ccc %d\n", *TABLE_GET(table, "ccc"));
  TABLE_FREE(table, 0);
}

int main() {
  test_string();
  test_hashtable();
  return 0;
}
