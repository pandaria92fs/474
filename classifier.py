from nltk.stem import PorterStemmer
import math
import numpy as np

file="traindata.txt"
file1="trainlabels.txt"

D=open("traindata.txt", "r")
D_test=open("trainlabels.txt", "r")

def loadDataSet():
	list =D.read().split() 
	return list

def loadlines():
	list1=[]
	labels=[]
	with open("traindata.txt") as f:
		for line in f:
			val = line.split(" ")
			list1.append(val)
		k=open("trainlabels.txt", "r")
		labels=k.read().split() 
		labels= list(map(int, labels))
		for i in range(len(list1)):
			list1[i].append(labels[i])
	f.close()
	k.close()
	return list1
		#print(labels[i])
	
	
	
def count_doc(count,file):
	with open(file) as f:
		for line in f:
			count=count+1
	return count
def countdocsinclass(cs):
	acc=0
	#ecl=D_test.readlines()
	list1=[]
	D_test1=open("trainlabels.txt", "r")
	list1=D_test1.read().split() 
	list1 = list(map(int, list1))
	for i in list1:
		#print(i)
		if i==cs:
			acc+=1
	#print(list)
	D_test1.close()
	return acc

def  countdocsinclasscontainterm(c,t):
	lst=loadlines()
	count=0
	#print(lst)
	for i in range(len(lst)):
		#print(lst[i])
		if c==lst[i][-1]:
			for j in range(len(lst[i])):
				#print (lst[i][j])
				if lst[i][j]==t:
					count+=1
	return count
		
		
		
#class re(object): 
#	def __init__(self,V,prior,CondP0,CondP1): 
#		self.V = V
#		self.prior=prior  			
#		self.CondP0=CondP0
#		self.CondP1=CondP1

def TRAINbernoulliNB(D):
	big_c=[1,0]
	prior=[]
	CondP0={}
	CondP1={}
	count=0
	V=loadDataSet()
	N=count_doc(0,D)
	for i in big_c:
		#print(i)
		Nc=countdocsinclass(i)
		#print (Nc)
		prior.append(Nc/N)
		for j in V:
			#print(j)
			#print(i)
			Nct=countdocsinclasscontainterm(i,j)
			if i==0:
				CondP0[j]=(Nct+1)/(Nc+2)
			else:
				CondP1[j]=(Nct+1)/(Nc+2)
	#print(prior,condprob,V)
	return (V,prior,CondP0,CondP1)
def extractermsfromdoc(V,file):
	with open(file) as f:
		lst=f.read().split()
		result=[]
		for i in lst:
			for j in V:
				if i==j:
					result.append(i)
	return list(set(result))
		
def extractermsfromdoc1(V,file,po):
	with open(file) as f:
		lst=f.readlines()
		result=[]
		lst1=lst[0].split()
		for i in lst1:
			for k in V:
				if i==k:
					result.append(i)
	return lst1
		
def ApplybernoulliNB(V,file,prior,CondP0,CondP1):
	Vd=extractermsfromdoc1(V,file,0)
	big_c=[0,1]
	score=[]
	for i in big_c:
		score.append (math.log(prior[i]))
		for j in V:
			for k in Vd:
				if i==0:
					if j==k:
						score[i]+=math.log(CondP0[j])
						#print(score[i])
					else:
						score[i]+=math.log(1-CondP0[j])
						#print(score[i])
				else:
					if j==k:
						score[i]+=math.log(CondP1[j])
						#print(score[i])
					else:
						score[i]+=math.log(1-CondP1[j])
						#print(score[i])
	print(score)
	return  np.argmax(score)
#loadlines()	
#print(loadlines())	
#print(countdocsinclasscontainterm(1,"will"))
#c=count_doc(0,file)
#print("a")
#print(c)
#print(loadDataSet())
V,prior,CondP0,CondP1=TRAINbernoulliNB(file)
print(ApplybernoulliNB(V,file,prior,CondP0,CondP1))
#extractermsfromdoc1(V,file,0)
#print(V)
#print (extractermsfromdoc(V,file))
#countdocsinclass(1)
#print(c)
#print(countdocsinclasscontainterm('1','is'))