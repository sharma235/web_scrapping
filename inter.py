# This code takes nearly 10 minutes to fetch all the 504 members
# count is printed to know how many members are fetched
import pandas as pd  
import requests
import bs4
din = []
dr_nm = []
dsg = []
ap_dt = []
req = requests.get('https://www.zaubacorp.com/company/DR-REDDY-S-LABORATORIES-LTD/L85195TG1984PLC004507')
soup = bs4.BeautifulSoup(req.text,'lxml')
tables = soup.findAll('table')
count = 0;
rowss = tables[7].findAll('tr')
rows = []
for i in rowss:
	cc = len(i.findAll('td'))
	if(cc==5 or cc==3):
		rows.append(i)

for row in rows:
	print(count)
	col = row.findAll('td')
	ct = len(col)
	if(ct==5 and col[0].text!="DIN"):
		#print(col[0].text)
		for i in range(4):
			if(i==0):
				din.append(col[i].text)
			if(i==1):
				dr_nm.append(col[i].text)
			if(i==2):
				dsg.append(col[i].text)
			if(i==3):
				ap_dt.append(col[i].text)
		count=count+1;
	elif(ct==3):
		for link in col[0].findAll('a',href=True):
			l = link.get('href')
			req2 = requests.get(l)
			soup2 = bs4.BeautifulSoup(req2.text,'lxml')
			table2 = soup2.findAll('table')
			if(len(table2)>=7):
				row2 = table2[7].findAll('tr')
				for ro in row2:
					co2 = ro.findAll('td')
					ctt = len(co2)
					if(ctt==5 and co2[0].text!="DIN"):
						#print(co2[0].text)
						for i in range(4):
							if(i==0):
								din.append(co2[i].text)
							if(i==1):
								dr_nm.append(co2[i].text)
							if(i==2):
								dsg.append(co2[i].text)
							if(i==3):
								ap_dt.append(co2[i].text)
						count=count+1
			break
dict = {'DIN': din, 'Director Name': dr_nm, 'Designation': dsg , 'Appointment Date': ap_dt}       
df = pd.DataFrame(dict)    
df.to_csv('file1.csv')
