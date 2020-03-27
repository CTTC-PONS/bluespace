/*
 ===================================================================================
 Name        : 	arof-conf.c
 Author      : 	Evangelos Grivas
 Version     : 	0.2
 Copyright   : 	Eulambia Advanced Technologies 2019
 Description :	ARoF configuration application. This gets called by the ARoF Agent.
                Parameters are passed as arguments and are being forwarded to
                ARoF HW through? -> ARoF HW hasn't been fully described yet..
                This was brought to the plenary meeting in Eindhoven and decided to
                pass arof status (on/off) to a pin (3.3V LVTTL). Also pass this
                infor to a on-board led for visualization of the arof status.
 ===================================================================================
 */

#include "arof-conf.h"

int VERBOSE = 0;

int main(int argc, char *argv[]) {

	/*
	 * Variables and Constants
	 */
	int 	arof_id		= 0; 				// arof id 			-> default value: 	0 (1/4)
	int		enable		= 0; 				// arof enable 		-> default value:	0 (false)
	int 	wavelength	= 1;				// arof wavelength	-> default value: 	1 (DWDM ITU Channel 1)

	int 	c;

	char 	*cmd = argv[0];					// store the command

	if(argc<5 || argc>9){
		print_help( cmd);
		exit(0);
	}

	/*
	 * Input parameters handling
	 */
	while( ( c = getopt(argc, argv, "hvi:e:w:") ) != -1 ){

		switch(c) {

			case 'v':
				VERBOSE = 1;
				verbose("<verbose> set\n");
				break;

			case 'i':
				arof_id = atoi(optarg);
				verbose("<arof_id> set to %d\n", arof_id);
				if(arof_id>=0 && arof_id <AROF_ID_MAX){

				} else {
					printf("unknown <arof_id> (%d)\n", arof_id);
					print_help(cmd);
					exit(0);
				}
				break;

			case 'e':
				enable = atoi(optarg);
				verbose("<enable> set to %d\n", enable);
				break;

			case 'w':
				wavelength = atoi(optarg);
				verbose("<wavelength> set to %d\n", wavelength);
				break;

			case 'h':
				print_help(cmd);
				exit(0);

			default:
				print_help(cmd);
				exit(0);
		}
	}


	return arof_conf(arof_id, enable, wavelength);
}

int arof_conf(int arof_id, int enable, int wavelength){

	int error =0;

	if (enable){
		verbose("Enabling ARoF HW with id->%d @DWDM ITU channel: %d\n", arof_id, wavelength);
	} else {
		verbose("Disabling ARoF HW with id->%d\n", arof_id);
	}

	return(error);
}

void print_help(char *cmd){

	printf("usage: %s [-v] -i <arof_id> -e <enable> -w <DWDM ITU channel>\n", cmd);
	printf("\n");
	printf("   -i,             set arof id [0-3]\n");
	printf("   -e,             set enable [0,1]\n");
	printf("   -w,             set wavelength [DWDD ITU channel], default: 1 (190.1THz)\n");
	printf("   -v,             set verbose [optional]\n");
	printf("   -h              print this message\n");
}

int verbose(const char * format, ...) {
    if( !VERBOSE )
        return 0;

    va_list args;
    va_start(args, format);
    int ret = vprintf(format, args);
    va_end(args);

    return ret;
}
