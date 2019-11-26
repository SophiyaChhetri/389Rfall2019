#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

//#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

int main(int argc, char **argv) {
    // TODO: implement

	int fd;
    fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    read(fd, fd_key_hash, 16);
}
