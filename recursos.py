#implementar:

interf = """/test/coletados/_id/ 
/test/coletados/
/test/jobs/_id/
/test/jobs/"""
inter = inter.split("\n")

def retornar(p):
	print(p)

def trataRequest(rq):
	i=0	
	for one in interf:
		rq_find = rq.find(cada)
		if (rq_find != -1):
			break
		i+=1
	if (i>len(inter)):
		retornar("501")

trataRequest("http://test/jobs/")
