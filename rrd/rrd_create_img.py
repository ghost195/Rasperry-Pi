import sys
import rrdtool
 
ret = rrdtool.graph( "net.png", "--start", "-1d", "--vertical-label=Bytes/s",
                     "DEF:inoctets=test1.rrd:input:AVERAGE",
                     "DEF:outoctets=test1.rrd:output:AVERAGE",
                     "AREA:inoctets#00FF00:In traffic",
                     "LINE1:outoctets#0000FF:Out traffic\\r",
                     "CDEF:inbits=inoctets,8,*",
                     "CDEF:outbits=outoctets,8,*",
                     "COMMENT:\\n",
                     "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
                     "COMMENT:  ",
                     "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps\\r",
                     "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
                     "COMMENT: ",
                     "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
