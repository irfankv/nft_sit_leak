import xlrd
import re
import os
import xlwt
from xlutils.copy import copy
from collections import defaultdict
from smtplib import SMTP
from email.mime.text import MIMEText  # constructing messages
from jinja2 import Environment  # Jinja2 templating

workbook = xlrd.open_workbook("BUG LEAK ANALYSISbackup.xlsx")
worksheet = workbook.sheet_by_name("Sheet1")
wb = copy(workbook)
sheet = wb.get_sheet(0)
list_of_ddts = []
list_of_components = []
list_of_headlines = []


for i in range(worksheet.nrows):
    list_of_ddts.append(worksheet.cell_value(i, 0))
for j in range(worksheet.nrows):
    list_of_components.append(worksheet.cell_value(j, 2))
for k in range(worksheet.nrows):
    list_of_headlines.append(worksheet.cell_value(k, 6))
list_of_ddts_id = list_of_ddts[1:]
list_of_components_final = list_of_components[1:]
list_of_headlines_final = list_of_headlines[1:]
for i in range(worksheet.nrows - 1):
    k = i + 1
    print(k)
    j = os.popen("/usr/cisco/bin/findcr -D '' -i " + worksheet.cell_value(k, 0) + " -w DTPT-manager").read().split('\n')[0]
    if j:
        sheet.write(k, 8, j)
    else:
        component = worksheet.cell_value(k, 2)
        null = None
        cmd = ''' /usr/cisco/bin/pims gsr -report comp_access_control -cdets_name {} -format json'''.format(component)
        js = os.popen(cmd).read()
        if (re.search(r"\"dtpt_mgr\": \"(\w+)\"", js)):
            dtmgr = re.search(r"\"dtpt_mgr\": \"(\w+)\"", js).group(1)
        else:
            dtmgr = "mnamasev"
        sheet.write(k, 8, dtmgr)

sheet.write(0, 8, 'Test Mgr')
wb.save('final_workbook.xlsx')

workbook_final = xlrd.open_workbook("final_workbook.xlsx")
sheet = workbook_final.sheet_by_name("Sheet1")
list_of_test_mgrs = []
for m in range(sheet.nrows):
    list_of_test_mgrs.append(sheet.cell_value(m, 8))
list_of_test_mgrs_final = list_of_test_mgrs[1:]

l3 = zip(list_of_test_mgrs_final, list_of_ddts_id, list_of_components_final, list_of_headlines_final)
final_list = list(l3)
dic = defaultdict(list)
for manager, bug, component, headline in final_list:
    dic[manager].append(bug)
    dic[manager].append(component)
    dic[manager].append(headline)
for k, v in dic.items():
    final_list2 = []
    for i in range(0, len(v), 3):
        final_list2.append(v[i:i + 3])
    for x in final_list2:
        if (re.search(r"[Cc]losed?",(os.popen("/usr/cisco/bin/findcr -D '' -i " + x[0] + " -w Attribute").read().split('\n')[0]))):
            final_list2.remove(x)
    print(final_list2)
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
        <h4>Please Take corrective actions on the bugs on your name listed below:-  <h5 style="color:red">Add attribute "closed" after the action is successfully taken to avoid further mails on that particular bug</h5></h4>
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
    if final_list2:
        msg = MIMEText(
            Environment().from_string(TEMPLATE).render(
                list2=final_list2
            ), "html"
        )
        subject = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
        sender = "nft-to-sit-bug-leak-report@cisco.com"
        #recipient = k + '@cisco.com'
        recipient = ['ikyalnoo@cisco.com','mnamasev@cisco.com']
        msg['Subject'] = "NFT To SIT Bug Leak Report- Corrective actions to be taken"
        msg['From'] = "nft-to-sit-bug-leak-report@cisco.com"
        #msg['To'] = k + '@cisco.com'
        msg ['To'] = 'ikyalnoo@cisco.com'
        print(sender)
        print(k)
        print(recipient)

        # Send the message via our own local SMTP server.
        s = SMTP('outbound.cisco.com')
        s.sendmail(sender, recipient, msg.as_string())
        s.quit()




















