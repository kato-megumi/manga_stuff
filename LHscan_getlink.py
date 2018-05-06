import requests ,sys ,os
from lxml import html
from bs4 import BeautifulSoup
from subprocess import Popen
import string

root="http://rawlh.com/"
def makedir(path):
	try:
		os.makedirs(path)
	except OSError:
		pass

def chapter_down(link):
	r = requests.get(link)
	img = BeautifulSoup(r.content, "html.parser").findAll("img", class_="chapter-img")
	images = [ str(i['src']) for i in img]
	images=filter(lambda c: c!='', images)
	i=0
	for image in images:
		image=filter(lambda c: c!='\n', image)
		tail = image.split(".")[-1]
		i+=1
		command = "wget -4 -q  "+ image+" -O "+str(i)+"."+tail
		# print command
		Popen(command, shell=True)

def link_chapter(Blink,low,up):
	r = requests.get(Blink)
	a = BeautifulSoup(r.content, "html.parser").findAll("a", class_="chapter")
	links = [ str(i['href']) for i in a]
	links=filter(lambda c: c!='', links)
	for link in links:
		rl = root+link
		number = float(filter(lambda c: c in string.digits+',', link))
		if (number>=low and number <=up):
			if (number).is_integer():
				str_num = str(int(number))
			else:
				str_num = str(number)
			makedir("chapter"+str_num)
			os.chdir("chapter"+str_num)
			chapter_down(rl)
			os.chdir('../')

name,low,up =  sys.argv[1:4]
#name = link[6:-9]
current = os.path.dirname(os.path.realpath(__file__))
makedir(name)
os.chdir(name)
link_chapter(root+'manga-'+name+'-raw.html',int(low),int(up))
