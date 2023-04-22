#!/usr/bin/perl

print "Content-type: text/plain\n\n";

# stop the Apache service
system("sudo service apache2 stop");
