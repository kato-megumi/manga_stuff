import requests ,sys ,os
from lxml import html
from bs4 import BeautifulSoup
from subprocess import Popen
import string

root="http://rawlh.com/"

def chapter_down(link):
	r = requests.get(link)
	img = BeautifulSoup(r.content, "html.parser").findAll("img", class_="chapter-img")
	images = [ str(i['src']) for i in img]
	images=list(filter(lambda c: c!='', images))
	for image in images:
		Popen("wget -4 "+ image, shell=True)
def link_chapter(Blink,low,up):
	r = requests.get(Blink)
	a = BeautifulSoup(r.content, "html.parser").findAll("a", class_="chapter")
	links = [ str(i['href']) for i in a]
	links=list(filter(lambda c: c!='', links))
	for link in links:
		rl = root+link
		number = int(''.join(list(filter(lambda c: c in string.digits, link))))
		os.makedirs("chapter"+str(number),exist_ok=True)
		os.chdir("chapter"+str(number))
		if (number>=low and number <=up):
			chapter_down(rl)
		os.chdir('../')

name,low,up =  sys.argv[1:4]
current = os.path.dirname(os.path.realpath(__file__))
os.makedirs(name,exist_ok=True)
os.chdir(name)
link_chapter(root+'manga-'+name+'-raw.html',int(low),int(up))
