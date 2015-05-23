# prompt for file name
fname = raw_input('Enter the file name: ')

try:
# Easter Egg
	if fname == 'na na boo boo':
		print "NA NA BOO BOO, I'M MORE CLEVER THAN YOU!"
# checks to see if file name is valid
	else:
		fhandle = open(fname)
except:
	print 'File cannot be opened: ', fname
	exit()

# set count to 0
count = 0

for line in fhandle:
# searches for desired line
	if line.startswith('X-DSPAM-Confidence:'):
# ups the count by 1
		count = count + 1

print 'There were', count, 'subject lines in', fname