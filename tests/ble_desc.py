import sys
from bluepy.btle import Peripheral

if len(sys.argv) != 2:
    print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
    sys.exit()

p = Peripheral(sys.argv[1], "random")

descriptors=p.getDescriptors(1,0x00F) #Bug if no limt is specified the function wil hang 

print("UUID                                  Handle UUID by name")
for descriptor in descriptors:
    print " "+ str(descriptor.uuid) + "  0x" + format(descriptor.handle,"02X") +"   "+ str(descriptor)
