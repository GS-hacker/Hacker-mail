import pyfiglet	
import requests

ascii_banner = pyfiglet.figlet_format("A2Z-Techs")
print(ascii_banner)

print("<<<<<<coded by {GS THE HACKER(youtuber)}>>>>>>")
print("                                              ")
print("<<<<<<Subscribe:   https://www.youtube.com/channel/UCTEQbefjWz_GBrkNTbsw42g>>>>>>")
print("                                                            ")
print("<<<<<<https://a2z-techs.blogspot.com>>>>>>")

to = raw_input('To>>')
subject = raw_input('Subject>>')
message = raw_input('Message>>')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})

if 'The e-mail has been sent' in email_req.text:
    print("[+] Email Sent!")
print("[+] In order to increase your privacy, the anonymous e-mail will be randomly delayed up to 1 hours")
print("[+] Thanks for using Hacker Mail")
