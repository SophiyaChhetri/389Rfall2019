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
	struct cipher_params params;

	int fd;
    fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    read(fd, fd_key_hash, 16);

	if(fd==NULL){
		printf("File does not exist");
		exit(7)
	}

	memset(&params, 0, sizeof(struct cipher_params));
}
