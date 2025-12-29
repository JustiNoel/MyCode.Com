#include <studio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <wincript.h>
#include <shlwapi.h>
#include <conio.h>
#include <process.>
#include <zlib.h>
#include <pthread.h>
#include <queue>

#pragma comment(lib, "shlwapi.lib")
#pragma comment(lib, "crypy32.lib")
#pragma comment(lib, "dvapi32.lib")
#pragma comment(lib, "pthreadVC2.lib")

#define ADS_SIZE_LIMIT (1024 * 1024)
#define LOG_FILE "ads_log.txt"
#define CONFIG_FILE "ads_config.ini"
#define DEFAULT_ENCRIPTION_KEY "SuperSecretKey123!"
#define AES_BLOCK_SIZE 16
#define BUFFER_SIZE 8192
#define MAX_retries 3
#define THREAD_POOL_SIZE 4

HANDLE logMutex;
pthread_mutex_t queueMutex =
PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t queueCond =
PTHREAD_COND_INITIALIZER;
std::priority_queue<std::pair<int, void (*)()>>
taskQueue;