/*
 * obfn.h
 *
 *  Created on: 4 Jul 2019
 *      Author: vage
 */

#ifndef OBFN_CONF_H_
#define OBFN_CONF_H_

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 					// getopt
#include <stdarg.h>						// variable arguments

#define BEAM_ID_MAX 		   4
#define DEFAULT_WAVELENGTH	1553.0

/*
 * Print help message
 */
void print_help(char *cmd);

/*
 * Being more verbose..
 */
int verbose(const char * format, ...) ;

/*
 * Configure the real HW
 */
int obfn_conf();


#endif /* OBFN_CONF_H_ */
