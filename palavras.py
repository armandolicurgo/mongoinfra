import string
import json
import math

import matplotlib.pyplot as plt

import math


class Palavras:

        def __init__(self):
                pass

        def ret(self,pp):
                ff= open(  pp,"r")
                tx = ff.read()
                ff.close()
                return(tx)


        def rettx(self,pp):
                tx = self.ret(pp)
                tx = tx.lower()
                tx = tx.replace("\n\n"," ")
                tx = tx.replace("\n"," ")
                tx = tx.replace("\\n"," ")
                tx = tx.replace(","," ")
                tx = tx.replace(";"," ")
                #tx = tx.replace("."," ")
                tx = tx.replace("("," ")
                tx = tx.replace(")"," ")
                tx = tx.replace(":"," ")
                tx = tx.replace('"'," ")
                tx = tx.replace("  "," ")
                tx = tx.replace("..",".")
                return(tx)


        def tFIDF(self,palavras,n):
                x,y = [],[]
                for kk in palavras:
                        i =(kk)
                        f =(palavras[kk])
                        #print( i , f)
                        ax = math.log( (n-(f)) / (f)  )
                        if (ax > 0):
                                x.append(i)
                                y.append(ax)
                return x,y
	def variancia(x,d):
		#lento
		# d eh com zeros
		s = 0
		for y in x:
			s += y
		print(s,len(x))
		avg = s/len(x)
		for i in range(len(x)):
			d[i] = (x[i] - avg) 
			d[i] = d[i] * d[i]
		su = 0
		for i in range(len(x)):
			su+=d[i]
		return(su/(len(x)-1))

        
        def contagem(self,txa):
                n = 0    # cuidado com passagem nao explicita
                palavras = {}
                for txt in txa:
                        if len(txt) > 0:
                                if palavras.get(txt) == None:
                                        palavras[txt] = 1
                                else:
                                        palavras[txt] += 1
                                n+=1
                return(n,palavras)

        def graficoxy(self,x,y,y2=[]):

                #import matplotlib.pyplot as plt

                plt.style.use('seaborn-whitegrid')

                fig,ax = plt.subplots()

                ax.plot(x, y,"bo")
                if len(y2) > 0:
                        ax.plot(x, y2, "ro")
                plt.show()



        def modelo1(self,palavras):
                meta = {}
                metb = {}
                for pal in sorted(palavras):
                        #print(pal, palavras[pal])
                        if meta.get(palavras[pal]) == None:
                                meta[palavras[pal]] = 1
                                metb[palavras[pal]] = [pal]
                        else:
                                meta[palavras[pal]]+=1
                                metb[palavras[pal]].append(pal)

                for cada in sorted(metb):
                        print(cada, len(metb[cada]),metb[cada])
                        print("=============================")

                x,y = [],[]
                for kk in meta:
                        i =int(kk)
                        f =int(meta[kk])
                        print( i , f)
                        #ax = math.log( (n-(i*f)) / (i*f)  )
                        if (1 > 0):
                                x.append(i)
                                y.append(f)

                r = json.dumps(meta)
                #print(r)

        def dodefaultera(self,dicpt,assunto,etiqueta,saida,tipoabre,delim,delim2,procuro):
                e = Palavras()
                dic = (e.rettx(dicpt))
                tx1 = (e.rettx(assunto))
                sai = open(saida,tipoabre)
                txa=tx1.split(delim)
                n,palavras = e.contagem(txa)
                x,y = e.tFIDF(palavras,n)
                for c in range(len(y)):
                        #if (x[c].isalpha() and dic.find(x[c])!=-2):
                        if (x[c].isalpha() and procuro.find(","+x[c]+",")!=-1):
                                #sai.write(str(y[c])+"\t"+x[c]+"\t"+"\n")
                                sai.write(x[c]+delim2+etiqueta+delim2+str(y[c])+"\n")
                                #sai.write(str(y[c])+"\t"+x[c]+"\t"+"\t"+str(dic.find(x[c]))+"\n")
                                #sai.write(x[c]+"\t"+str(y[c])+"\t"+"\t"+str(dic.find(x[c]))+"\n")
                                #print(x[c])
                sai.close()

                """
                tx2 = tx1
                for i in range(0,len(tx1),4000):
                        tx1 = tx2[i:i+4000]
                        print(tx1)
                """
        def dodefault(self,dicpt,assunto,etiqueta,saida,tipoabre,delim,delim2,procuro):
                e = Palavras()
                dic = (e.rettx(dicpt))
                if (assunto[0:1]=="@"):
                    tx1 = (e.rettx(assunto[1:]))
                else:
                    tx1 = assunto        
                sai = open(saida,tipoabre)
                txa=tx1.split(delim)
                n,palavras = e.contagem(txa)
                x,aly = e.tFIDF(palavras,n)
                for c in procuro.split("\n"):
                    sai.write(str(tx1.count(c+" "))+" ")
                sai.write("\n")
                sai.close()


        def tf(self,word, blob):
                return blob.count(word) / blob.count(" ")

        def n_containing(self,word, bloblist):
                return sum(1 for blob in bloblist if word in blob.split(" "))

        def idf(self,word, bloblist):
                return math.log(len(bloblist) / (1 + self.n_containing(word, bloblist)))

        def tfidf(self,word, blob, bloblist):
                return self.tf(word, blob) * self.idf(word, bloblist)


if __name__ == "__main__":
        e = Palavras()
        procuro = e.ret("procuro.txt")
        print(procuro)
        o = open("saida1.txt","w")
        o.close()
        algo = e.ret("assunto.txt")
        for palav in procuro.split("\n"):
                print(e.tfidf( palav,algo, procuro.split("\n")  ),palav)

        document1 = e.rettx("assunto.txt")
        document2 = e.rettx("doc2.txt")
        document3 = e.rettx("doc3.txt")

        bloblist = [document1,document2]

        for i, blob in enumerate(bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: e.tfidf(word, blob, bloblist) for word in blob.split(" ")}
            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[0:5]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
