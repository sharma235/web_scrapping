#value of depth is fixed to 2
#program takes some time to complete 
#count is printed to tell how much data is fetched
import pandas as pd  
import requests
import bs4
din = []
dr_nm = []
dsg = []
ap_dt = []
count = 0;

def main(req,depth):
	global count
	if(depth < 1):
		return
	soup = bs4.BeautifulSoup(req.text,'lxml')
	tables = soup.findAll('table')
	if(len(tables)<7):
		return
	rows = tables[7].findAll('tr')
	for row in rows:
		col = row.findAll('td')
		ct = len(col)
		if(ct==5 and col[0].text!="DIN"):
			for i in range(4):
				if(i==0):
					din.append(col[i].text)
				if(i==1):
					dr_nm.append(col[i].text)
				if(i==2):
					dsg.append(col[i].text)
				if(i==3):
					ap_dt.append(col[i].text)
			count=count+1
			print(count)
		elif(ct==3 and depth>1):
			for link in col[0].findAll('a',href=True):
				l = link.get('href')
				req2 = requests.get(l)
				main(req2,depth-1)

req = requests.get('https://www.zaubacorp.com/company/DR-REDDY-S-LABORATORIES-LTD/L85195TG1984PLC004507')
main(req,2)
#making csv file
dict = {'DIN': din, 'Director Name': dr_nm, 'Designation': dsg , 'Appointment Date': ap_dt}       
df = pd.DataFrame(dict)    
df.to_csv('file1.csv')
