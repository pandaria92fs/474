from nltk.stem import PorterStemmer


file="traindata.txt"
file1="trainlabels.txt"

D=open("traindata.txt", "r")
D_test=open("trainlabels.txt", "r")

def loadDataSet():
	list =D.read().split() 
	#ps=PorterStemmer()"
	#for line in D:
		#val = line.split(" ")
		#val = line.strip("/n")

	#for i in list:
	#	print(i)
	return list
def count_doc(count,file):
	with open(file) as f:
		for line in f:
			count=count+1
	return count
def countdocsinclass(cs):
	acc=0
	#ecl=D_test.readlines()
	clist=[]
	for i in D_test:
		#val1 = i.split(" ")
		#print(val1)
		clist.append(int(i))
	for i in clist:	
		if i==cs:
			acc+=1
	return acc

def  countdocsinclasscontainterm(c,t):
	list1=[]
	count=0
	for line in D:
		val = line.split(" ")
		list1.append(val)
	for i in list1:
		for j in i:
			if j==t
				
			
	
	
def TRAINbernoulliNB(C,D):
	big_c=[0,1]
	count=0
	V=loadDataSet()
	N=count_doc(D)
	for i in big_c:
		Nc=countdocsinclass(i)
		prior[i]=Nc/N
		
		
	
	
	
countdocsinclasscontainterm(1,"will")
#c=count_doc(count,file)
#print(loadDataSet())