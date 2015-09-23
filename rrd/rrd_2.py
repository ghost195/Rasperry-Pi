import rrdtool
 rrdtool.create('/tmp/test.rrd', 'DS:foo:GAUGE:20:0:U')
