from RPN import rpn
from tokens import tokens as token


def shuting_yard(expretion):
	#print(equation)
	operator_level={ "+":1,
					 "-":1,
					 "x":2,
					 "*":2,
					 "/":2,
					 "**":3,
					 "^":3}
	order={ "+": "left",
			"-": "left",
			"x": "left",
			"*": "left",
			"/": "left", 
			"^": "left"}
	#numbers=["0","1","2","3","4","5","6","7","8","9"]
	operators=[]
	exit_line=[]
	#expretion=equation
	for element in expretion:
		if element not in operator_level and element not in ["(",")"]:			#numero
			exit_line.append(element)

		if element in operator_level:	#operador
			while operators:
				last_op=operators[-1]
				if last_op not in ["(",")"]:
					if ((operator_level[last_op]>operator_level[element]) or \
						(operator_level[last_op]==operator_level[element] and order[element]=="left")):
						exit_line.append(operators.pop())
					else:
						break
				else:
					break
			operators.append(element)

		if element=="(":				#parentesis abierto
			operators.append(element)

		if element==")":				#parentesis cerrado
			while operators[-1]!="(":
				exit_line.append(operators[-1])
				del operators[-1]
				#print(operators[-1])
			forlong=list(range(0,operators.index(operators[-1])+1))
			for i in forlong:
				j=len(forlong)-1-i
				if operators[j]=="(":
					del operators[j]
		#print("element:",element)
		#print("Operadores:",operators)
		#print("exit line:",exit_line)
	for _ in range(0,len(operators)):
		exit_line.append(operators.pop())
	return exit_line



#value="10+2x9-3"
value="3^2+4^2"
print("Expresion:",value)
value=token(value)
print("Token:",value)
value=shuting_yard(value)
print("SHuting yard:",value)
respuesta=rpn(value)
print("RPN:",respuesta)