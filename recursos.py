#implementar:
import crud

interf = """/test/coletados/_id/ 
/test/coletados/
/test/jobs/_id/
/test/jobs/"""
inter = inter.split("\n")

def return_(p):
	print(p)
def exec_(rq_find,rq)
	print(rq_find,rq)
	x = Crud(rq_find.split("/"),rq.split("/"))
	return_("200",x)
def trataRequest(rq):
	i=0	
	for one in interf:
		rq_find = rq.find(one)
		if (rq_find != -1):
			return_(exec_(rq_find,rq))
			break
		i+=1
	if (i>len(inter)):
		return_("501")

trataRequest("http://test/jobs/")
trataRequest("http://test/clientes/")
