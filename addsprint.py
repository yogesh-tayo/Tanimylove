import json
import requests
import traceback

#Put Story id Here
StoryID = ["PROP-2010"]
my_headers = {'Authorization' : 'Basic YWthc2gua2Fuc2FsQG1hZ2ljYnJpY2tzLmNvbTpGaklPVmRiWmY2bWdmV0pNNkQ3REQyNDM=','Content-Type':'application/json'}
field = {"customfield_10600":7091}
body = {"fields":field}

for x in StoryID:
    AddSprint = requests.put("https://timesgroup.jira.com/rest/api/3/issue/"+x+"?notifyUsers=true&overrideScreenSecurity=false&overrideEditableFlag=false", json =body,headers=my_headers)
    print(x)
    print(AddSprint.status_code)
    print(AddSprint.content)