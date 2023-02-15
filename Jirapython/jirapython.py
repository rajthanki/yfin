from jira import JIRA
import csv

# Connect to JIRA
options = {
    'server': 'https://your-jira-instance.com'
}
jira = JIRA(options, basic_auth=('username', 'password'))

# Get the issues (stories) from the project
project_key = 'PROJECT_KEY'
issues = jira.search_issues(f'project={project_key} and issuetype=Story')

# Write the issues to a CSV file
with open('stories.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Key', 'Summary', 'Description', 'Assignee', 'Status'])
    # Write the data rows for each issue
    for issue in issues:
        writer.writerow([issue.key, issue.fields.summary, issue.fields.description, issue.fields.assignee, issue.fields.status])
