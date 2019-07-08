/*
 ============================================================================
 Name        : obfn-conf.c
 Author      : Evangelos Grivas
 Version     : v0.1
 Copyright   : Eulambia Advanced Technologies 2019
 Description : OBFN configuration application. This gets called by the OBFN Agent.
  	  	  	   Parameters are passed as arguments and are being forwarded to
  	  	  	   OBFN HW through UART/USB (FDTI FT230X)
 ============================================================================
 */

#include "obfn-conf.h"

int VERBOSE = 0;

int main(int argc, char *argv[]) {

	/*
	 * Variables and Constants
	 */
	int 	beam_id			= 0; 				// obfn id 			-> default value: 	0 (1/4)
	float	beam_offset_x	= 0; 				// beam_offset_x 	-> default value:	0 (no offset)
	float	beam_offset_y	= 0; 				// beam_offset_x 	-> default value:	0 (no offset)
	float 	ref_wavelength 	= DEFAULT_WAVELENGTH;

	int 	c;

	char 	*cmd = argv[0];						// store the command

	if(argc == 1 || argc>11){
		print_help( cmd);
		exit(0);
	}

	/*
	 * Input parameters handling
	 */
	while( ( c = getopt(argc, argv, "hvw:i:x:y:") ) != -1 ){

		switch(c) {

			case 'v':
				VERBOSE = 1;
				verbose("<verbose> set\n");
				break;

			case 'i':
				beam_id = atoi(optarg);
				verbose("<beam_id> set to %d\n", beam_id);
				if(beam_id>=0 && beam_id <BEAM_ID_MAX){

				} else {
					printf("beam_id (%d) not supported\n", beam_id);
					print_help(cmd);
					exit(0);
				}
				break;

			case 'x':
				beam_offset_x = atof(optarg);
				verbose("<beam_offset_x> set to %+7.2f\n", beam_offset_x);
				break;

			case 'y':
				beam_offset_y = atof(optarg);
				verbose("<beam_offset_y> set to %+7.2f\n", beam_offset_y);
				break;

			case 'w':
				ref_wavelength = atof(optarg);
				verbose("<ref_wavelength> set to %7.2f\n", ref_wavelength);
				break;

			case 'h':
				print_help(cmd);
				exit(0);

			default:
				print_help(cmd);
				exit(0);
		}
	}


	return obfn_conf();
}

int obfn_conf(){

	int error =0;

	return(error);
}

void print_help(char *cmd){

	printf("usage: %s [-v] [-w] -i <beam_id> -x <beam_offset_x> -y <beam_offset_y>\n", cmd);
	printf("\n");
	printf("   -i,             set beam id [0-3]\n");
	printf("   -x,             set beam x offset [-90,90]\n");
	printf("   -y,             set beam y offset [-90,90]\n");
	printf("   -w,             set reference wavelength [optional], if omitted\n"
		   "                   the default reference wavelength (%7.2f) is used\n", DEFAULT_WAVELENGTH);
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
