'''
AlgoExpert - run-length encoding - strings
'''

def runLengthEncoding(string):
	esc = []
	crl = 1
	for i in range(1, len(string)):
		cc = string[i]
		pc = string[i - 1]
		
		if cc != pc or crl == 9:
			esc.append(str(crl))
			esc.append(pc)
			crl = 0
		
		crl += 1
	
	esc.append(str(crl))
	esc.append(string[len(string) - 1])
	
	return "".join(esc)
