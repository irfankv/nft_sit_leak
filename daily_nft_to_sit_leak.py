import os
import time
import re
from collections import defaultdict
import json
from smtplib import SMTP
from email.mime.text import MIMEText  # constructing messages
from jinja2 import Environment  # Jinja2 templating
from time import gmtime, strftime
from datetime import date, timedelta

def leak_attribute_not_changed(dtpt_mgr,ddtsid,component,headline):
	print()
	final_ddts = [(ddtsid,component,headline)]
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
	            <h4>Please take corrective actions on the bugs on your name listed below:-  <h5 style="color:red">You have acknowledged that below DDTS is not NFT miss but not changed Bug Leak attribute. Please change the Bug Leak attribute to IDT(TSHF-IDT) or DEV(TSHF-DEV)</h5></h4>
	            <h5 style="color:red">If you don't Acknowledge its NFT miss then Please  Add attribute "TSHF_NFT_NACK" to avoid further mails on that particular bug</h5></h4>
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
	            <h5> Please don't reply to this email. For feedback please send email to Manjusha(mnamasev)</h5>
	            <h5>Thanks,<br>NFT TEAM</h5>
	            </body>
	            </html>
	            """
	# Create a text/html message from a rendered template
	msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_ddts), "html")
	subject = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
	sender = "nft-to-sit-bug-leak-report@cisco.com"
	# recipient = k + '@cisco.com'
	recipient = 'ikyalnoo@cisco.com'
	msg ['Subject'] = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
	msg ['From'] = "nft-to-sit-bug-leak-report@cisco.com"
	# msg['To'] = k + '@cisco.com'
	msg ['To'] = 'ikyalnoo@cisco.com'
	print (sender)
	print (recipient)

	# Send the message via our own local SMTP server.
	s = SMTP ('outbound.cisco.com')
	s.sendmail (sender, recipient, msg.as_string ())
	s.quit ()

def idt_leak_attribute_not_changed (ddtsid, component, headline):
	print()
	final_ddts = [ddtsid, component, headline]
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
		            <h4>Please take corrective actions on the bugs on your name listed below:-  <h5 style="color:red">You have acknowledged that below DDTS is not NFT miss but not changed Bug Leak attribute. Please change the Bug Leak attribute to IDT(TSHF-IDT) or DEV(TSHF-DEV)</h5></h4>
		            <h5 style="color:red">If you don't Acknowledge its NFT miss then Please  Add attribute "TSHF_NFT_NACK" to avoid further mails on that particular bug</h5></h4>
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
		            <h5> Please don't reply to this email. For feedback please send email to Manjusha(mnamasev)</h5>
		            <h5>Thanks,<br>NFT TEAM</h5>
		            </body>
		            </html>
		            """
	# Create a text/html message from a rendered template
	msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_ddts), "html")
	subject = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
	sender = "nft-to-sit-bug-leak-report@cisco.com"
	# recipient = k + '@cisco.com'
	recipient = 'ikyalnoo@cisco.com'
	msg ['Subject'] = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
	msg ['From'] = "nft-to-sit-bug-leak-report@cisco.com"
	# msg['To'] = k + '@cisco.com'
	msg ['To'] = 'ikyalnoo@cisco.com'
	print (sender)
	print (manager)
	print (recipient)

	# Send the message via our own local SMTP server.
	s = SMTP ('outbound.cisco.com')
	s.sendmail (sender, recipient, msg.as_string ())
	s.quit ()
#command_NFT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'submitter-manager-org:hassans or submitter-manager-org:ahabbu or Submitter:[chanvija,prgoel,soumibha,bhavana,pamkrish,hsivasam] and Attribute:TSHF-NFT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on  Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"
yesterday = date.today() - timedelta(3)
yesterday = (yesterday.strftime('%y%m%d'))
command_NFT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'Project:CSC.ena,CSC.ot,CSC.hw and Status:S,N,A,O,W,H,I,P,M,R,V,D and Status:S[180301:] and Found:sys-test and Attribute:TSHF-NFT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on Found-during Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"

command_NFT = "/auto/qddtscache/qddtsnxt/bin/query.pl 'Project:CSC.ena,CSC.ot,CSC.hw and Status:S,N,A,O,W,H,I,P,M,R,V,D and Status:S[%s:] and Found:sys-test and Attribute:TSHF-NFT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on Found-during Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager" %(yesterday)

#command_IDT ="/auto/qddtscache/qddtsnxt/bin/query.pl 'submitter-manager-org:hassans or submitter-manager-org:ahabbu and Attribute:TSHF-IDT'  | /auto/qddtscache/qddtsnxt/bin/qbugval.pl -json Identifier  Submitted-on  Component Submitter-id Submitter-manager-org Headline Product Attribute ENCLOSURES Version DTPT-manager"

p_nft = os.popen(command_NFT)
output_nft = p_nft.read()
output_nft = json.loads(output_nft)
final_dtpmr_ddtd_head_line_comp = []
yesterday = date.today() - timedelta(3)
yesterday = int(yesterday.strftime('%y%m%d'))
print(yesterday)
for record in output_nft :
	submittedon = record ['Submitted-on']
	date = int(submittedon.split(' ')[0])
	print(date)
	headline = record ['Headline']
	ddtsid = record ['Identifier']
	dtpt_mgr = record["DTPT-manager"]
	component = record["Component"]
	final_dtpmr_ddtd_head_line_comp.append((ddtsid,component,headline))
	print(final_dtpmr_ddtd_head_line_comp)


if final_dtpmr_ddtd_head_line_comp:
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
            <h4>For the date {{ date }}</h4>

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
            <h5>Thanks,<br>NFT TEAM</h5>
            </body>
            </html>
            """
	# Create a text/html message from a rendered template
	msg = MIMEText (Environment ().from_string (TEMPLATE).render (list2=final_dtpmr_ddtd_head_line_comp,date=strftime("%d %b %Y", gmtime())), "html")
	subject = "Daily incoming NFT to SIT leak " + strftime("%d %b %Y", gmtime())
	sender = "nft-tools-team@cisco.com"
	# recipient = k + '@cisco.com'
	recipient = 'ikyalnoo@cisco.com'
	msg ['Subject'] = "Daily incoming: NFT to SIT leak for " + strftime("%d %b %Y", gmtime())
	msg ['From'] = "nft-tools-team@cisco.com"
	# msg['To'] = k + '@cisco.com'
	msg ['To'] = 'ikyalnoo@cisco.com'
	print (sender)
	print (recipient)

	# Send the message via our own local SMTP server.
	s = SMTP ('outbound.cisco.com')
	s.sendmail (sender, recipient, msg.as_string ())
	del msg
	s.quit ()
else:
	print("None DDTS found")
