/*
 * arof-conf.h
 *
 *  Created on: 30 May 2019
 *      Author: vage
 */

#ifndef AROF_CONF_H_
#define AROF_CONF_H_

#define AROF_ID_MAX 4

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 					// getopt
#include <stdarg.h>						// variable arguments

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
int arof_conf(int arof_id, int enable);


#endif /* AROF_CONF_H_ */
