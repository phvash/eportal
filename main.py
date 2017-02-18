import requests
from parser import Parser
import sys

def para(matric, password, year, semester):
	headers = {
	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	    "Accept-Encoding": "gzip, deflate",
	    "Accept-Language": "en-US,en;q=0.8",
	    "Cache-Control": "max-age=0",
	    "Connection": "keep-alive",
	    "Content-Length": "70",
	    "Content-Type": "application/x-www-form-urlencoded",
	    # "Cookie": "__utma=135605487.788700159.1481619800.1483540398.1483825883.5; __utmz=135605487.1481619800.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=b6hkcta6dd21huomnd0h31hab7",
	    "Host": "eportal.oauife.edu.ng",
	    "Origin": "http://eportal.oauife.edu.ng",
	    "Referer": "http://eportal.oauife.edu.ng/login.php",
	    "Upgrade-Insecure-Requests": "1",
	    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
	}

	data = {
	    "user_id": matric,
	    "pswd": password,
	    "SessionF": year,
	    "SemesterF": semester,
	    "Submit": "Submit"
	}

	return headers, data

def main():
	
	if sys.argv[1] == 'help':
		print '''Usage: main.py matric password session semester(1 for rain, 2 for semester)'''
		sys.exit(0)
	
	matric = sys.argv[1]
	password = sys.argv[2]
	this_session = sys.argv[3]
	year = this_session.split('/')[1]
	
	semester = sys.argv[4]
	
	headers, data = para(matric, password, year, semester)
	session = requests.Session()

	login = session.post("http://eportal.oauife.edu.ng/login1.php", data=data, headers=headers)
	home = session.get("http://eportal.oauife.edu.ng/undergraduatetasks.php")
	raw_score = session.get("http://eportal.oauife.edu.ng/viewrawscore1.php")
	Parser.parse_html(raw_score.text)

if __name__ == '__main__':
	main()


