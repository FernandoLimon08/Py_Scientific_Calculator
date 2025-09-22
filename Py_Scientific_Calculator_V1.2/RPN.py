
def rpn(notation):
	pile=[]
	result=0
	#numbers=["0","1","2","3","4","5","6","7","8","9"]
	operators=["+","-","x","/","^","*"]
	operation=notation.copy()
	while len(operation)!=1:
		#print("Entro al while")
		for element in notation:
			#print(f"Entro al for con {element}")
			if element in operators:
				if element not in operators:
					continue
				#print(f"Entro al if con {element}")
				position=operation.index(element)
				num1=float(operation[position-2])
				num2=float(operation[position-1])
				#print(f"Position es {position}, numero 1 es {num1} y numero 2 es {num2}")
				if element=="+":
					result=num1+num2
				if element=="-":
					result=num1-num2
				if element in ["x","*"]:
					result=num1*num2
				if element=="/":
					result=num1/num2
				if element=="^":
					result=num1**num2
					print(notation)
					print("Num 1 es:",num1)
					print("Num 2 es:",num2)
				del operation[position]
				del operation[position-1]
				operation[position-2]=result
				#print(operation)
	return result

def main():
	equation=['-10', '2', '9', 'x', '+', '3', '-']
	result=rpn(equation)
	#equation=["9","3","/","4","+","2","*"]
	#result=rpn(equation)
	print(result)

if __name__ in "__main__":
	main()