from bs4 import BeautifulSoup
from datetime import date
import requests, random, shutil, time, math, os, sys, getopt
def RandSearchTerm():
	term = []
	characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	length = random.randint(8, 16)
	for i in range(1, length):
		index = random.randint(1, len(characters)-1)
		term.append(characters[index])
	return("".join(term))
def GetImageURLs(term):
	results = []
	url = "https://www.google.com/search?q=" + term + "&tbm=isch&ved=2ahUKEwidspnT_4buAhUbgUsFHZZdAS4Q2-cCegQIABAA&oq=erjgkldfb&gs_lcp=CgNpbWcQAzoFCAAQsQM6AggAOggIABCxAxCDAToECAAQGDoGCAAQChAYUJQUWIcZYPEaaABwAHgAgAHtAYgBzQuSAQUwLjQuNJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=R4P1X93yEJuCrtoPlruF8AI&bih=665&biw=1280"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	for link in soup.find_all('img'):
	    results.append(link.get('src'))
	return results[1:]
def ChooseImage(list):
	index = random.randint(0, len(list)-1)
	return list[index]
def DownloadImage(image_url, search_term):
	day = str(date.today())
	if(os.path.isdir("Images/" + day) == False):
		os.mkdir("Images/" + day)
		print("Created directory:", "Images/" + day)

	filename = "Images/" + str(day) + "/" + search_term

	# Open the url image, set stream to True, this will return the stream content.
	r = requests.get(image_url, stream = True)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
	    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	    r.raw.decode_content = True
	    
	    # Open a local file with wb ( write binary ) permission.
	    with open(filename,'wb') as f:
	        shutil.copyfileobj(r.raw, f)
	        
	    print('Image sucessfully Downloaded:',filename)

	else:
	    print('Image Couldn\'t be retreived')

argv = sys.argv[1:]
try:
	args = getopt.getopt(sys.argv[1:], 'n:')
except getopt.GetoptError as err:
	print("Error: " + str(err))
	print("Available arguments are: ")
	print("-n : Specify how many images to download.")
	sys.exit()
if argv:
	number = int(args[0][0][1])
	for i in range(1, number+1):
		Search = RandSearchTerm()
		DownloadImage(ChooseImage(GetImageURLs(Search)), Search)	
else:
	Search = RandSearchTerm()
	DownloadImage(ChooseImage(GetImageURLs(Search)), Search)