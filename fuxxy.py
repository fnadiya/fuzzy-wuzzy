import csv

def imp():
	with open('influencers.csv') as fuzzy:
		read = csv.reader(fuzzy)
		result = []
		for i in read:
			result.append(i)
	return result

def fetch(x):
	result = []
	y = x[1:100]
	for i in y:
		data = []
		data.append(float(i[1]))
		data.append(float(i[2]))
		result.append(data)
	return result

def followersNum(n): 
	result_fuzzy = []
	high = follower_high(n)
	fair = follower_fair(n)
	low = follower_low(n)
	result_fuzzy.append(high)
	result_fuzzy.append(fair)
	result_fuzzy.append(low)
	return result_fuzzy

def engagementNum(n):
	result_fuzzy = []
	high = engagement_high(n)
	fair = engagement_fair(n)
	low = engagement_low(n)
	result_fuzzy.append(high)
	result_fuzzy.append(fair)
	result_fuzzy.append(low)
	return result_fuzzy

#FOLLOWERS SCORING
def follower_high(n):
	if n>65000:
		result_fuzzy = 1
	elif n<=55000:
		result_fuzzy = 0
	else:
		result_fuzzy = (n-55000)/(65000-55000)
	return result_fuzzy

def follower_fair(n):
	if n>65000 or n<=5000:
		result_fuzzy = 0
	elif 25000<n<35000:
		result_fuzzy = 1
	elif 5000<n<=25000:
		result_fuzzy = (n-5000)/(25000-5000)
	else:
		result_fuzzy = (65000-n)/(65000-25000)
	return result_fuzzy

def follower_low(n):
	if n<5000:
		result_fuzzy = 1
	elif n>=10000:
		result_fuzzy = 0
	else:
		result_fuzzy = (10000-n)/(10000-5000)
	return result_fuzzy

#ENGAGEMENT SCORING
def engagement_high(n):
	if n>5:
		result_fuzzy = 1
	elif n<=4:
		result_fuzzy = 0
	else:
		result_fuzzy = (n-4)/(5-4)
	return result_fuzzy

def engagement_fair(n):
	if n<=0.5 or n>5:
		result_fuzzy = 0
	elif 2<n<=3:
		result_fuzzy = 1
	elif 0.5<n<=2:
		result_fuzzy = (n-0.5)/(2-0.5)
	else:
		result_fuzzy = (5-n)/(5-3)
	return result_fuzzy

def engagement_low(n):
	if n<0.5:
		result_fuzzy = 1
	elif n>=1.5:
		result_fuzzy = 0
	else:
		result_fuzzy = (1.5-n)/(1.5-0.5)
	return result_fuzzy

#FUZZY
def inference(n,m):
	outcome = []
	for p in n:
		for q in m:
			if p>q:
				outcome.append(p)
			else:
				outcome.append(q)
	return outcome

def approved(n):
	approve = []
	approve.append(n[0])
	approve.append(n[1])
	approve.append(n[3])
	result = max(approve)
	return result

def considered(n):
	cons = []
	cons.append(n[2])
	cons.append(n[4])
	cons.append(n[5])
	cons.append(n[6])
	result = max(cons)
	return result

def rejected(n):
	rjc = []
	rjc.append(n[7])
	rjc.append(n[8])
	result = max(rjc)
	return result

def sugeno(x,y,z):
	result = ((x*80)+(y*60)+(z*40))/(x+y+z)
	return result

def maxFuzzy(n):
	y = sorted(range(len(n)), key=lambda k:n[k], reverse=True)
	z = y[:20]
	maxx = []
	for i in z:
		maxx.append([n[i],[i+1]])
	return maxx

#MAIN PROGRAM
x = imp()
data = fetch(x)
outcome = []
for i in data:
	foll = followersNum(i[0])
	eng = engagementNum(i[1])
	inf = inference(foll, eng)
	approve = approved(inf)
	cons = considered(inf)
	rjc = rejected(inf)
	result = sugeno(approve, cons, rjc)
	outcome.append(result)
maxx = maxFuzzy(outcome)
print("============================================")
print("====== HERE'S THE TOP 20 FOR YOU!  <3 ======")
for i in maxx:
	print("============================================")
	print("	Fuzzy Value : ",i[0])
	print("	Index Data  : ",i[1])
print("============================================")
with open("result.csv", "w+") as my_csv:
	csvWrite = csv.writer(my_csv, delimiter=',')
	csvWrite.writerows(maxx)
