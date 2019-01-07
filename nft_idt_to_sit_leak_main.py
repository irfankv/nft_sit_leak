import os
import time
import re
from collections import defaultdict
import json
from smtplib import SMTP
from email.mime.text import MIMEText  # constructing messages
from jinja2 import Environment  # Jinja2 templating

def leak_attribute_not_changed(submitter,ddtsid,component,headline):
	print()
	final_ddts = [(ddtsid,component,headline)]
	k = submitter
	print ("inside TSHF-NFT-NACK ")
	print (submitter)
	TEMPLATE = """
	            <html>
	            <head>
	            <title>Bug Leak Report</title>
	            <style type="text/css" media="screen">
	            table{
	                background-color: #AAD373;
	                empty-cells:hide;
	            }
	            td.cell{
	                background-color: white;
	            }
	            </style>
	            </head>
	            <body>
	            <h4>Hi, </h4>
	            <h5>Please take corrective actions on the bugs on your name listed below:-</h5>
                <h4 style="color:red">Below DDTS submitted by you is TSHF-NFT-NACK.</h5>
	           <ol>
	               <li style="color:red">Please reach out to whoever has added TSHF-NFT-NACK attribute in CDETS for any clarification.</li>
	               <li style="color:red">Upon further analysis, please change the Bug Leak attribute to IDT(TSHF-IDT) or DEV(TSHF-DEV) or SIT(TSHF-SIT).</li>
	            </ol>
	            <table style="border: blue 1px solid;">
	            <tr>
	            <th class="cell">Bug Id</td><th class="cell">Component</td><th class="cell">Headline</td>
	            </tr>
	            {% for item in list2 %}
	            <tr>
	            <td class="cell"><a href="https://cdetsng.cisco.com/webui/#view={{ item[0] }}">{{ item[0] }}</a></td>
	            <td class="cell">{{ item[1] }}</td>
	            <td class="cell">{{ item[2] }}</td>
	            </tr>
	            {% endfor %}
	            </table>
	            <br>
	            <h5 style="color:black">For feedback please send email to nft-tools-team@cisco.com</h5>
	            <h5>Thanks,<br>NFT Tools Team</h5>
	            </body>
	            </html>
	            """
	# Create a text/html message from a rendered template
	msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_ddts), "html")
	subject = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
	sender = "nft-tools-team@cisco.com"
	recipient = k + '@cisco.com'
	#recipient = 'ikyalnoo@cisco.com'
	msg ['Subject'] = "Bug Leak attribute not changed for NFT NACK bugs- Corrective actions to be taken"
	msg ['From'] = "nft-tools-team@cisco.com"
	msg['To'] = k + '@cisco.com'
	#msg ['To'] = 'ikyalnoo@cisco.com'
	print (sender)
	print (recipient)

	# Send the message via our own local SMTP server.
	s = SMTP ('outbound.cisco.com')
	s.sendmail (sender, recipient, msg.as_string ())
	s.quit ()

def idt_leak_attribute_not_changed (submitter,ddtsid, component, headline):
	print()
	final_ddts = [(ddtsid,component,headline)]
	submitter =submitter
	print ("inside TSHF-IDT-NACK ")
	print (submitter)
	TEMPLATE = """
		            <html>
		            <head>
		            <title>Bug Leak Report</title>
		            <style type="text/css" media="screen">
		            table{
		                background-color: #AAD373;
		                empty-cells:hide;
		            }
		            td.cell{
		                background-color: white;
		            }
		            </style>
		            </head>
		            <body>
		            <h4>Hi, </h4>
		            <h5>Please take corrective actions on the bugs on your name listed below:-</h5>
	                <h4 style="color:red">Below DDTS submitted by you is TSHF-IDT-NACK.</h5>
		           <ol>
		               <li style="color:red">Please reach out to whoever has added TSHF-IDT-NACK attribute in CDETS for any clarification.</li>
		               <li style="color:red">Upon further analysis, please change the Bug Leak attribute to NFT(TSHF-IDT) or DEV(TSHF-DEV) or SIT(TSHF-SIT).</li>
		            </ol>
		            <table style="border: blue 1px solid;">
		            <tr>
		            <th class="cell">Bug Id</td><th class="cell">Component</td><th class="cell">Headline</td>
		            </tr>
		            {% for item in list2 %}
		            <tr>
		            <td class="cell"><a href="https://cdetsng.cisco.com/webui/#view={{ item[0] }}">{{ item[0] }}</a></td>
		            <td class="cell">{{ item[1] }}</td>
		            <td class="cell">{{ item[2] }}</td>
		            </tr>
		            {% endfor %}
		            </table>
		            <br>
		            <h5 style="color:black">For feedback please send email to nft-tools-team@cisco.com</h5>
		            <h5>Thanks,<br>NFT Tools Team</h5>
		            </body>
		            </html>
		            """
	# Create a text/html message from a rendered template
	msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_ddts), "html")
	subject = "IDT To SIT Bug Leak Report- Corrective actions to be taken"
	sender = "nft-tools-team@cisco.com"
	recipient = submitter+"@cisco.com"
	#recipient = 'ikyalnoo@cisco.com'
	msg ['Subject'] = "Bug Leak attribute not changed for IDT NACK bugs- Corrective actions to be taken"
	msg ['From'] = "nft-tools-team@cisco.com"
	msg['To'] = submitter+"@cisco.com"
	msg ['To'] = 'ikyalnoo@cisco.com'
	print (sender)
	print (manager)
	print (recipient)

	# Send the message via our own local SMTP server.
	s = SMTP ('outbound.cisco.com')
	s.sendmail (sender, recipient, msg.as_string ())
	s.quit ()


#command_NFT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'submitter-manager-org:hassans or submitter-manager-org:ahabbu or Submitter:[chanvija,prgoel,soumibha,bhavana,pamkrish,hsivasam] and Attribute:TSHF-NFT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on  Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"

command_NFT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'Project:CSC.ena,CSC.ot,CSC.hw and Status:S,N,A,O,W,H,I,P,M,R,V,D and Status:S[180301:] and Found:sys-test and Attribute:TSHF-NFT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on Found-during Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"

#command_IDT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'submitter-manager-org:hassans or submitter-manager-org:ahabbu or Submitter:[chanvija,prgoel,soumibha,bhavana,pamkrish,hsivasam] and Attribute:TSHF-IDT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on  Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"

command_IDT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'Project:CSC.ena,CSC.ot,CSC.hw and Status:S,N,A,O,W,H,I,P,M,R,V,D and Status:S[180301:] and Found:sys-test and Attribute:TSHF-IDT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on Found-during Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"
p_nft = os.popen(command_NFT)
output_nft = p_nft.read()
output_nft = json.loads(output_nft)
final_dtpmr_ddtd_head_line_comp = []

for record in output_nft :
	submittedon = record ['Submitted-on']
	date = int(submittedon.split(' ')[0])
	print(date)
	if date >= 180301:
		if not re.search(r"BL-NFT-CLOSED",record ['Attribute']):
			headline = record ['Headline']
			ddtsid = record ['Identifier']
			dtpt_mgr = record["DTPT-manager"]
			component = record["Component"]
			submitter = record["Submitter-id"]
			if not dtpt_mgr:
				print()
				null = None
				cmd = ''' /usr/cisco/bin/pims gsr -report comp_access_control -cdets_name {} -format json'''.format (
					component)
				js = os.popen (cmd).read ()
				if (re.search (r"\"dtpt_mgr\": \"(\w+)\"", js)):
					dtpt_mgr = re.search (r"\"dtpt_mgr\": \"(\w+)\"", js).group (1)
				else:
					dtpt_mgr = "mnamasev"
			if re.search(r"TSHF-NFT-NACK",record ['Attribute']):
				print()
				leak_attribute_not_changed(submitter,ddtsid,component,headline)
			else :
				final_dtpmr_ddtd_head_line_comp.append((dtpt_mgr,ddtsid,component,headline))
				print(final_dtpmr_ddtd_head_line_comp)

dic = defaultdict(list)

for manager, ddtsid , component , headline in final_dtpmr_ddtd_head_line_comp :
	dic [manager].append ((ddtsid,component,headline))
	#dic [manager].append (component)
	#dic [manager].append (headline)

#print(dic)

# for manager, final_ddts_comp_head_line in dic.items ():
# 	print(manager)
# 	print(final_ddts_comp_head_line)

for manager , final_ddts_comp_head_line in dic.items():
	TEMPLATE = """
            <html>
            <head>
            <title>Bug Leak Report</title>
            <style type="text/css" media="screen">
            table{
                background-color: #AAD373;
                empty-cells:hide;
            }
            td.cell{
                background-color: white;
            }
            </style>
            </head>
            <body>
            <h4>Hi, </h4>
            <h5>Please take corrective actions on the bugs on your name listed below:- </h4>
            <h4 style="color:red">If you acknowledge it is NFT miss then please follow below steps after the action is successfully taken to avoid further mails on the particular bug:</h5>
            <ol>
               <li style="color:red">Add attribute "BL-NFT-CLOSED".</li>
               <li style="color:red">Add an enclosure BUG-LEAK-ANALYSIS in CDETS.</li>
            </ol>
            <h4 style="color:red">If you do not acknowledge it is NFT miss then please Add attribute "TSHF-NFT-NACK" to avoid further mails on the particular bug:</h4>
            <h4 style="color:black"> Scrubber Link:<a href="https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=mnamasev-41">https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=mnamasev-41</a></h4>
            <table style="border: blue 1px solid;">
            <tr>
            <th class="cell">Bug Id</td><th class="cell">Component</td><th class="cell">Headline</td>
            </tr>
            {% for item in list2 %}
            <tr>
            <td class="cell"><a href="https://cdetsng.cisco.com/webui/#view={{ item[0] }}">{{ item[0] }}</a></td>
            <td class="cell">{{ item[1] }}</td>
            <td class="cell">{{ item[2] }}</td>
            </tr>
            {% endfor %}
            </table>
            <br>
            <h5 style="color:black">For feedback please send email to nft-tools-team@cisco.com</h5>
            <h5 style="color:black">Thanks,<br>NFT Tools Team</h5>
            </body>
            </html>
            """
	# Create a text/html message from a rendered template
	if final_ddts_comp_head_line:
		msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_ddts_comp_head_line), "html")
		subject = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
		sender = "nft-tools-team@cisco.com"
		recipient = manager + '@cisco.com'
		#recipient = 'ikyalnoo@cisco.com'
		msg ['Subject'] = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
		msg ['From'] = "nft-tools-team@cisco.com"
		msg['To'] = manager + '@cisco.com'
		#msg ['To'] = 'ikyalnoo@cisco.com'
		print (sender)
		print (manager)
		print (recipient)

		# Send the message via our own local SMTP server.
		s = SMTP ('outbound.cisco.com')
		s.sendmail (sender, recipient, msg.as_string ())
		s.quit ()
	else:
		print("No DDTS")


p_IDT = os.popen(command_IDT)
output_IDT = p_IDT.read()
output_IDT = json.loads(output_IDT)
final_ddtd_head_line_comp_IDT = []

for record in output_IDT:
	submittedon = record ['Submitted-on']
	date = int (submittedon.split (' ') [0])
	print (date)
	if date >= 180301:
		if not re.search (r"BL-IDT-CLOSED", record ['Attribute']):
			headline = record ['Headline']
			ddtsid = record ['Identifier']
			dtpt_mgr = record ["DTPT-manager"]
			component = record ["Component"]
			submitter = record["Submitter-id"]
			if ddtsid == 'CSCvk39455':
				print(record ['Attribute'])
				print("Irfan")
				print("Irfan")
			if re.search (r"TSHF-IDT-NACK", record ['Attribute']):
				print ()
				print(record ['Attribute'] )
				print("Irfan Pas")
				idt_leak_attribute_not_changed (submitter,ddtsid, component, headline)

			else:
				final_ddtd_head_line_comp_IDT.append((ddtsid,component,headline))


TEMPLATE = """
            <html>
            <head>
            <title>Bug Leak Report</title>
            <style type="text/css" media="screen">
            table{
                background-color: #AAD373;
                empty-cells:hide;
            }
            td.cell{
                background-color: white;
            }
            </style>
            </head>
            <body>
            <h4>Hi, </h4>
            <h4>Please take corrective actions on the bugs on your name listed below:- </h4>
            <h4 style="color:red">If you acknowledge it is IDT miss then please follow below steps after the action is successfully taken to avoid further mails on the particular bug:</h5>
            <ol>
               <li style="color:red">Add attribute "BL-IDT-CLOSED".</li>
               <li style="color:red">Add an enclosure BUG-LEAK-ANALYSIS in CDETS.</li>
            </ol>
            <h4 style="color:red">If you do not acknowledge it is IDT miss then please Add attribute "TSHF-IDT-NACK" to avoid further mails on the particular bug:</h4>
            <h4 style="color:black"> Scrubber Link:<a href="https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=mnamasev-59">https://wwwin-ottawa.cisco.com/tfoggoa/Scrubber/showquery.html?query=mnamasev-59</a></h4>
            <table style="border: blue 1px solid;">
            <tr>
            <th class="cell">Bug Id</td><th class="cell">Component</td><th class="cell">Headline</td>
            </tr>
            {% for item in list2 %}
            <tr>
            <td class="cell"><a href="https://cdetsng.cisco.com/webui/#view={{ item[0] }}">{{ item[0] }}</a></td>
            <td class="cell">{{ item[1] }}</td>
            <td class="cell">{{ item[2] }}</td>
            </tr>
            {% endfor %}
            </table>
            <br>
            <h5 style="color:black">For feedback please send email to nft-tools-team@cisco.com</h5>
            <h5 style="color:black">Thanks,<br>NFT Tools Team</h5>
            </body>
            </html>
            """
if final_ddtd_head_line_comp_IDT:
		msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_ddtd_head_line_comp_IDT), "html")
		subject = "IDT To SIT Bug Leak Report- Corrective actions to be taken"
		sender = "nft-tools-team@cisco.com"
		recipient = "idt-mgrs@cisco.com"
		#recipient = 'ikyalnoo@cisco.com'
		msg ['Subject'] = "IDT To SIT Bug Leak Report- Corrective actions to be taken"
		msg ['From'] = "nft-tools-team@cisco.com"
		msg['To'] = "idt-mgrs@cisco.com"
		#msg ['To'] = 'ikyalnoo@cisco.com'
		print (sender)
		#print (manager)
		print (recipient)

		# Send the message via our own local SMTP server.
		s = SMTP ('outbound.cisco.com')
		s.sendmail (sender, recipient, msg.as_string ())
		s.quit ()
print("Will run every one hour")
