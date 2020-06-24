
# You will need to install this module: https://jira.readthedocs.io/en/master/index.html
# pip install jira

#Run with Python 3
#if possible, run a couple of times with accounts of different access levels and save the output to a file
#Sample of how to run and save the output to a file on MacOS and Linux:
#python3.7 jira_check.py > output.txx

from jira import JIRA
from jira.resources import User


#Basic config, set these with the proper details
server_address = "https://sample.atlassian.net"
user = 'example@testmail.com'
pass_or_token = 'GddXaaLqxyk2gE758cBNPE0E0'

#Set this to a jira issue that has attachments associated
test_issue_with_attachment = "POP-35"

j = JIRA(
    server=server_address,
    basic_auth=(user, pass_or_token)
    )

def section_header(label):
    print("==========================")
    print(label)
    print("==========================")


def check_projects():
    section_header("Checking Projects")
    projects = j.projects()
    count = len(projects)
    if count > 0:
        print("OK")
    else:
        print("FAILED TO LIST")
    return count
        


def check_issue_types():
    section_header("Checking Issue Types")
    issue_types = j.issue_types()
    for itype in issue_types:
        print(f"Name {itype.name} ID {itype.id}")

    return len(issue_types)

def check_issue_fields():
    section_header("Issue Fields")
    issue = j.issue(test_issue_with_attachment)

    fields = issue.fields

    if(hasattr(fields, 'issuetype')):
        itype = fields.issuetype
        print("----------------------")
        print(f"Issue type is {itype}")
        print("----------------------")
        print(dir(itype))
    else:
        print("ERROR: Issue type field not available")

    if(hasattr(fields, 'issuerestriction')):
        print("----------------------")
        print(f"Restrictions field: {fields.issuerestriction}")
        print("----------------------")
        print(dir(fields.issuerestriction.issuerestrictions))
        print(fields.issuerestriction.issuerestrictions)
    else:
        print("Issue resctriction field not available")    

    
    print('------ Fields ------')
    print(dir(fields))
    
    if hasattr(fields, "attachment"):
        print('------ Attachments ------')
        for attachment in fields.attachment:
            print(f"Attempting to download {attachment}")
            data = attachment.get()
            if data:
                print("OK")
                return "OK"
            else:
                print("Error: Attachment could not be downloaded")
                return "FAILED"
        print("NO ATTACHMENTS AVAILABLE")
        return "FAILED"
    else:
        print("ATTACHMENT FIELD NOT AVAILABLE")

        return "FAILED"



results = dict()
results['Projects Access count '] = check_projects()
results['Issue Types count '] = check_issue_types()
results['Issue Fields '] = check_issue_fields()


section_header("RESULTS")

for (key,value) in results.items():
    print(f"{key} {value}")


print("==========================")
print("==========================")