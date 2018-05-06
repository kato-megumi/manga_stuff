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
	img = BeautifulSoup(r.content, "html.parser").findAll("a", class_="img-num")
	images = [ str(i['href']) for i in img]
	images=filter(lambda c: c!='', images)
	images = [ i[:i.index('?')] for i in images]
	for image in images:
		Popen("wget -4 "+ "http:"+image, shell=True)

def link_chapter(Blink,low,up):
	r = requests.get(Blink)
	a = BeautifulSoup(r.content, "html.parser").findAll("a", class_="chapter")
	links = [ str(i['href']) for i in a]
	links=filter(lambda c: c!='', links)
	for link in links:
		rl = root+link
		number = int(filter(lambda c: c in string.digits, link))
		if (number>=low and number <=up):
			makedir("chapter"+str(number))
			os.chdir("chapter"+str(number))
			chapter_down(rl)
			os.chdir('../')

#name,low,up =  sys.argv[1:4]
##name = link[6:-9]
#current = os.path.dirname(os.path.realpath(__file__))
#makedir(name)
#os.chdir(name)
#link_chapter(root+'manga-'+name+'-raw.html',int(low),int(up))
chapter_down("https://mangapark.me/manga/genshiken-nidaime-the-society-for-the-study-of-modern-visual-culture-ii/s2/v12/c72?zoom=2")