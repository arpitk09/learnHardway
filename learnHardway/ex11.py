from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s " % (from_file, to_file)

# open file and read file operations
in_file = open(from_file) #first assign a variable with open a file
indata = in_file.read() # after that assign a variable to read the file

print "The input file os %d bytes long" % len(indata)

print "Does the output file exixt? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("?")

out_file = open(to_file, "w")
out_file.write(indata)

print "Allright, all done."

out_file.close()
in_file.close()


