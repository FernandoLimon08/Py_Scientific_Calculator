
def tokens(expretion):
	numbers=["0","1","2","3","4","5","6","7","8","9"]
	operators=["+","-","*","x","/","(","^"]
	token=[]
	number=""
	expretion=list(expretion)
	for digit in expretion:
		if digit.isdigit() or digit ==".":
			number+=digit
			#print(number)
	#	elif expretion[0]="-" or (digit=="-" and prev="("):
	#		number="-"+number
		else:
			if number:
				token.append(number)
				number=""
			if not digit.isspace() :
				token.append(digit)
		prev=digit
	token.append(number)
	if token[-1]=="":
		del token[-1]
	#if token[0] in ["(","-"]:
	for i,element in enumerate(token):
		if element.isdigit() and token[i-1]=="-" and (token[i-2] in operators or token[0]=="-"):
			token[i-1]=token[i-1]+element
			del token[i]
			#break

	return token

def main():
	eq="-5+3"
	#print(eq)
	#lista=tokens(eq)
	#print(lista)
	#value="-15"
	#print(value)
	#print(value.isdigit())

if __name__ in "__main__":
	main()
