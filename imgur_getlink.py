import requests ,sys ,os,json
from subprocess import Popen
import string


client_id = '39d3497e01e320d'
secret = "309a212755ac0f529e95390b36812f37b2084431"
def makedir(path):
	try:
		os.makedirs(path)
	except OSError:
		pass

def chapter_down(hash):
	api = "https://api.imgur.com/3/album/"+hash+"/images"
	headers = {'Authorization': 'Client-ID '+client_id}
	response = requests.request("GET", api, headers=headers)
	images =  [i["link"].encode("utf-8") for i in json.loads(response.text)["data"]]
	i=0
	for image in images:
		i+=1
		x = image.split('.')[-1]
		Popen("wget -4 "+image+" -O "+str(i)+"."+x, shell=True)

if __name__ == '__main__':
	makedir(sys.argv[2])
	os.chdir(sys.argv[2])
	chapter_down(sys.argv[1])