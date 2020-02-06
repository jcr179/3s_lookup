REQUIREMENTS

To use the program, one needs to have both MPlayer and MediaInfo installed. MPlayer has been tested with versions 1.0 and 1.1 and MediaInfo with versions 0.7.57-1 and 0.7.61. One also needs to have Java installed. Tested versions are 1.6.0_22 and 1.6.0_24.

The user has to also fill the property file (GTEditor.properties) with the locations of MPlayer and MediaInfo, frame step (recommended to use 5), the folder where the frames can be extracted and the folder where the file browser will start.

Paths have to be written with slashes (/) or double backslashes (\\). 

E.g. 
/home/user/mplayer/
c:\\programs\\mplayer\\

EXECUTING THE PROGRAM

To run the program from command line, type the following in the program folder:

java -jar "GTEditor.jar"