#ifndef _LIB_LOGGING_H_
#define _LIB_LOGGING_H_

#include <malloc.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define STRING_BUF_SIZE 64u

#define DEFAULT_LOGGING_LEVEL "INFO"
#define DEFAULT_LOGGING_FILE_PATH "app.log"
#define DEFAULT_APP_NAME "Application"

// LEVEL DATE DESC
#define DEFAULT_FORMAT "[%s] %s : %s\n"

#define LOG_LEVEL_INFO "INFO"
#define LOG_LEVEL_ERROR "ERROR"
#define LOG_LEVEL_WARN "WARN"
#define LOG_LEVEL_DEBUG "DEBUG"

#define NOT_NULL_ELSE(v, replace) v != NULL ? v : replace
#define MAKE(type) (type *)malloc(sizeof(type))
#define MAKE_ARRAY(type, length) (type *)malloc(sizeof(type) * length)
#define MAKE_STRING(length) MAKE_ARRAY(char, length)

typedef struct {
  const char *application_name;
  const char *log_path;
  const char *format;
  FILE *log_file;
  bool file_closed;
} Logger;

char *_format_date_time() {
  char *str = MAKE_STRING(STRING_BUF_SIZE);
  memset(str, 0, STRING_BUF_SIZE);
  time_t t;
  struct tm *tm_info;
  time(&t);
  tm_info = localtime(&t);
  strftime(str, STRING_BUF_SIZE, "%Y-%m-%d %H:%M:%S", tm_info);
  return str;
}

Logger *Log_New(const char *app_name, const char *log_path, const char *format) {
  const char *name = NOT_NULL_ELSE(app_name, DEFAULT_APP_NAME);
  const char *log = NOT_NULL_ELSE(log_path, DEFAULT_LOGGING_FILE_PATH);
  const char *format_ins = NOT_NULL_ELSE(format, DEFAULT_FORMAT);
  FILE *file = fopen(log, "a");
  Logger *log_instance = MAKE(Logger);
  log_instance->file_closed = false;
  log_instance->log_file = file;
  log_instance->application_name = name;
  log_instance->log_path = log;
  log_instance->format = format_ins;
  return log_instance;
}

Logger *Log_New_StdOut(const char *app_name, const char *log_path,
                       char *format) {
  const char *name = NOT_NULL_ELSE(app_name, DEFAULT_APP_NAME);
  const char *log = NOT_NULL_ELSE(log_path, DEFAULT_LOGGING_FILE_PATH);
  const char *format_ins = NOT_NULL_ELSE(format, DEFAULT_FORMAT);
  FILE *file = stdout;
  Logger *log_instance = MAKE(Logger);
  log_instance->file_closed = false;
  log_instance->log_file = file;
  log_instance->application_name = name;
  log_instance->log_path = log;
  log_instance->format = format_ins;
  return log_instance;
}

void Log_Info(Logger *self, char *str) {
  fprintf(self->log_file, self->format, LOG_LEVEL_INFO, _format_date_time(),
          str);
}
void Log_Debug(Logger *self, char *str) {
  fprintf(self->log_file, self->format, LOG_LEVEL_DEBUG, _format_date_time(),
          str);
}
void Log_Error(Logger *self, char *str) {
  fprintf(self->log_file, self->format, LOG_LEVEL_ERROR, _format_date_time(),
          str);
}
void Log_Warn(Logger *self, char *str) {
  fprintf(self->log_file, self->format, LOG_LEVEL_WARN, _format_date_time(),
          str);
}

void Log_SetFormat(char *format_new);

void Log_Close(Logger *self) {
  if (!self->file_closed && self->log_file != stdout) {
    fclose(self->log_file);
  }
  free(self);
}

#endif


// #include "liblog/logging.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
  Logger *log = Log_New_StdOut(NULL, NULL, NULL);
  Log_Info(log, "C语言日志库.");
  Log_Close(log);
  return EXIT_SUCCESS;
}