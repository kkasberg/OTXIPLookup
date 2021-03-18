import requests
import json

def getIPrepdata(ip):
  apiiplist = "https://otx.alienvault.com/api/v1/indicator/IPv4/" + str(ip) + "/reputation"
  iplist = requests.get(apiiplist)
  ipdata = iplist.json()
  return ipdata

def dedupeList(x):
  return  list(dict.fromkeys(x))

def getinput():
  ip = '184.168.221.57'
  x = input("What IP do you want to research?\nIP " + ip + " will be used if left blank.\n->")
  if x != '':
    ip = str(x)
  return(ip)

def run():
  ip = getinput()
  global ipresult
  ipresult = getIPrepdata(ip)  
  list = getIPrep(ip)
  returnList(list)

def returnList(items):
  for i in items:
    print(i)

def getIPrep(ip):
  lines = []
  dedupe = []
  if  ipresult["reputation"]:
    for records in (ipresult["reputation"]["activities"]):
      name = records["name"]
      fd = records.get("first_date")
      ld = records.get("last_date")
      record = ip + " known for " + name
      lines.append(record)
  else:
      lines.append("IP has no reputation data for bad activity.")
  for x in lines:
    if x not in dedupe:
      dedupe.append(x)
  return dedupe



run()
