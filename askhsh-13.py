from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
kino = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
kinodata= urlopen(kino).read()
x=str(data)
number=x[33:97]
strnumlist=[]
numlist=[]
modnumlist=[]

for i in range(0,len(number),2):
    strnumlist.append(number[i]+number[i+1])
print ("Data from cloudflare: " , number)
print ("randomness is: " , strnumlist)

for i in range(len(strnumlist)):
    hexnum=strnumlist[i]
    decnum=int(hexnum,16)
    numlist.append(decnum)
print ("Int is: " , numlist)
for i in range(len(numlist)):
    num=numlist[i]
    modnumlist.append(num%80)
print ("Modulo 80 is: ", modnumlist)
unique_list=list(set(modnumlist))
print ("Unique Numbers is: " , unique_list)
print (kinodata)
