print "testin file creation"
import  os
try:
    fo=open("7.py","r")
    o=fo.read(13)
    t=fo.tell()
    print "o is ---->",o
    print "t is -->",t
except IOError, b:
    print "didnt find that file chintu",b
    d=os.getcwd()
    print d
else:
    print "calling else block after try as there is no exception"

finally:
    print "called finaly block"

