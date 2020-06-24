# Jira Checks for ZenGRC

A small script to extract debug info needed for the Jira integration with ZenGRC

### Requirements
- Python3
- python-jira module
- Valid credentials to a Jira instance


### How to set up
- pip install jira
- open jira_checks.py and set the server_url and credentials to your own values, you will also need to indicate the ID of a Jira issue that has attachments linked

### Running
- python3 jira_checks.py
- To run and save the output to a file: python3 jira_checks.py > outfile.txt
- Make sure you get output for multiple accounts with different access levels

