#-*-coding:utf-8-*-

import sys
import requests

from bs4 import BeautifulSoup

if(__name__=="__main__"):
	runKeys={};
	args=sys.argv;
	i=1;
	while(i<len(args)):
		if(args[i].find("--")==-1):
			i=i+1;
			continue;
		runKeys[args[i]]=args[i+1];
		i=i+2;
	mandatoryKeys=["--email", "--password"];
	for mandatoryKey in mandatoryKeys:
		if(not mandatoryKey in runKeys):
			print("\"%s\" argument is missing!"%mandatoryKey);
			exit();

	session=requests.Session();
	loginHost="https://id.jobcan.jp";
	page=session.get(loginHost+"/users/sign_in");
	data=page.text;
	body=BeautifulSoup(data, "lxml");

	loginForm=body.find("form", {"id":"new_user"});
	payload={};
	for input in loginForm.findChildren("input"):
		payload[input["name"]]=input["value"] if(input.has_attr("value")) else "";
	payload["user[email]"]=runKeys["--email"];
	payload["user[password]"]=runKeys["--password"];
	session.post(loginHost+loginForm["action"], data=payload);

	page=session.get("https://ssl.jobcan.jp/jbcoauth/login");
