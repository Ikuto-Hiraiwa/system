
#include <stdlib.h>

int main(void){
	setuid(0);
	system("LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i \"/usr/local/lib/input_uvc.so -y -r 320x240 -f 10 -d /dev/video0 -y\" -o \"/usr/local/lib/output_http.so -p 8080 -w www\" -b");
	return 0;
}

