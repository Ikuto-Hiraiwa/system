
#include <stdlib.h>

int main(void){
	setuid(0);
	system("sudo kill -9 `pidof mjpg_streamer`");
	return 0;
}
