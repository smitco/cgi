#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
listval = form.getlist('operand')

print("operands: {}".format(str(listval)))

sum = 0
for i in listval:
    sum += int(i)
    
print("sum: {}".format(sum))
