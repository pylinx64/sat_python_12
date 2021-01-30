import re
import webbrowser
import urllib.request
import urllib.parse

def youtube_open(command):		
	reg_ex = re.search('ютьюб (.+)', command)
	if reg_ex:
		domain = command.split("ютьюб",1)[1] 
		query_string = urllib.parse.urlencode({"search_query" : domain})
		print(query_string)
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
		print(search_results)
		#print("http://www.youtube.com/watch?v=" + search_results[0])
		#webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
		webbrowser.open("http://www.youtube.com/results?" + query_string)
		pass	

youtube_open('ютьюб котики')
