import pickle
l=pickle.load(open("bcd.pickle","rb"))
l=[]
d={}
def stud():
	
	n=input("entr name")
	a=int(input("enter age"))
	d={"name":"as","age":"2"}
	l.append(d)
	pickle.dump(l,open("bcd.pickle","wb"))
def readobject():
	l=pickle.load(open("bcd.pickle","rb"))
	print(l)
def menu():
	n=0
	while(n!=3):
		print("1.registration")
		print("2.view")
		print("3.exit")
		n=int(input("enter choice"))
		if(n==1):
			stud()
		elif(n==2):
			readobject()
		else:
			print("exit")
menu()
