/*
 ============================================================================
 Name        : obfn-conf.c
 Author      : Evangelos Grivas
 Version     : v0.2
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
	int 	beam_id			=  0; 				// beam id 			-> default value: 	0 (1/4)
	int		beam_enable		=  0;				// beam enable		-> default value: 	0 (disabled)
	float	beam_offset_x	=  0; 				// beam_offset_x 	-> default value:	0 (no offset)
	float	beam_offset_y	=  0; 				// beam_offset_x 	-> default value:	0 (no offset)
	float 	beam_width		= 10;				// beam_width		-> default value:  10 (beam width half angle of 10deg)
	int 	ref_wavelength 	= DEFAULT_WAVELENGTH;

	int 	c;

	char 	*cmd = argv[0];						// store the command

	if(argc == 1 || argc>15){
		print_help( cmd);
		exit(0);
	}

	/*
	 * Input parameters handling
	 */
	while( ( c = getopt(argc, argv, "hvw:i:e:x:y:z:") ) != -1 ){

		switch(c) {

			case 'v':
				VERBOSE = 1;
				verbose("<verbose> set\n");
				break;

			case 'i':
				beam_id = atoi(optarg);
				verbose("<beam_id>       set to %4d\n", beam_id);
				if(beam_id>=0 && beam_id <BEAM_ID_MAX){

				} else {
					printf("beam_id (%d) not supported\n", beam_id);
					print_help(cmd);
					exit(0);
				}
				break;

			case 'e':
				beam_enable = atoi(optarg);
				verbose("<beam_enable>   set to %4d\n", beam_enable);
				break;

			case 'x':
				beam_offset_x = atof(optarg);
				verbose("<beam_offset_x> set to %+7.2f\n", beam_offset_x);
				break;

			case 'y':
				beam_offset_y = atof(optarg);
				verbose("<beam_offset_y> set to %+7.2f\n", beam_offset_y);
				break;

			case 'z':
				beam_width = atof(optarg);
				verbose("<beam_width>    set to %7.2f\n", beam_width);
				break;

			case 'w':
				ref_wavelength = atoi(optarg);
				verbose("<ref_wavelength>set to %4d\n", ref_wavelength);
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

	printf("usage: %s [-v] -w <ref_wavelength> -i <beam_id> -e <beam_enable> -x <beam_offset_x> -y <beam_offset_y> -z <beam_width>\n", cmd);
	printf("\n");
	printf("   -i,             set beam id [0-3]\n");
	printf("   -e,             enable beam [0,1] with id <beam_id>\n");
	printf("   -x,             set beam x offset [-90,90]\n");
	printf("   -y,             set beam y offset [-90,90]\n");
	printf("   -z,             set beam width half-angle [0,90]\n");
	printf("   -w,             set reference wavelength in ITU Channel [1-72]\n");
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
