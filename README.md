string-compression
==================
========================================================================
Assignment:
========================================================================

Simple compression and decompression algorithms for strings written in python.
- The input is a string, and the output is a compressed string.
- A valid input consists of zero or more upper case english letters A-Z.
- To produce the compressed output, any run of two or more of the same character should be converted to two of that character plus a number indicating how many repeated runs were compressed. 
- Examples:
    - A --> A
    - AA --> AA0
    - AAA --> AA1
    - AAAA --> AA2
- Only one digit may be used at a time, so if the run is quite long, then you must use multiple character/number pairs
    - AAAAAAAAAA --> AA8
    - AAAAAAAAAAA --> AA9
    - AAAAAAAAAAAA --> AA9A
    - AAAAAAAAAAAAA --> AA9AA0
    - AAAAAAAAAAAAAA --> AA9AA1

The decompression algorithm simply reverses this process.

========================================================================
To Run Algorithms:
========================================================================
The algorithms 'compress' and 'decompress' are located in compression.py.
- The bash script compression.sh runs them easily from the command line.  
- The first argument should be 'compress' or 'decompress' to specify the algorithm.
- The script runs the main function which reads strings from standard input until EOF or CTRL+C.
- Example usage:
	- $ ./compress.sh compress
	- 	HELLOOOOO
	- 	HELL0OO3
	- 	^C
	- $ ./compress.sh decompress
	- 	HELL0OO3
	- 	HELLOOOOO
	- 	^C
- This input format allows the input of files with output to another file:
	- $ ./compress compress < toCompress.txt > output.txt

========================================================================
Tests:
========================================================================
Unit tests are located in tests.py
- To run Tests:
	- $ python tests.py



