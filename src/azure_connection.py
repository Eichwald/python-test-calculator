from unittest import result
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Fill in with your personal access token and org URL
personal_access_token = 'kwfp7b6rw365femaulomm5ncnyqhewmxprnk3jvp2wv5dxuo77ga'
organization_url = 'https://dev.azure.com/eichwald'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()
test_client = connection.clients.get_test_client()

# Get all the projects
def get_projects():
    return core_client.get_projects()

def get_test_plans(project_name):
    return test_client.get_plans(project_name)

def get_test_suite(project_name, plan_id):
    return test_client.get_test_suites_for_plan(project_name, plan_id)

def get_test_cases_for_suite(project_name, plan_id, suite_id):
    return test_client.get_test_cases(project_name, plan_id, suite_id)

def upload_test_point_result(body, project_name, plan_id, suite_id, point_id):
    test_client.update_test_points(body, project_name, plan_id, suite_id, point_id)

def bulk_upload_test_point_result(list_body, project_name, plan_id, suite_id):
    for index, point_id in enumerate(list_body):
        print(index)
        test_client.update_test_points(list_body[index].get('results'), project_name, plan_id, suite_id, list_body[index].get('id'))

for projects in get_projects():
    print(projects.name)

for test_plans in get_test_plans("Calculator-test-project"):
    print(test_plans.name)      


# body = [{"id":6,"results":{"outcome":3}}, {"id":7,"results":{"outcome":3}}]
# test_client.update_test_points(body[0].get('results'), "Calculator-test-project", 16, 19, body[0].get('id'))
# bulk_upload_test_point_result(body, "Calculator-test-project", 16, 19)
for case in get_test_cases_for_suite("Calculator-test-project", 16, 19):
    print(case.test_case)
get_test_suite("Calculator-test-project", 16)