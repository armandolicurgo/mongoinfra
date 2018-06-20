#implementar:

"""
/coletados/id 
/coletados/
/jobs/id/sites/
/jobs/id/
/jobs/


"""
{
    "id": "<item_id>", 
    "summary": "<one-line summary>"
}
{
    "id": "<item_id>", 
    "summary": "<one-line summary>", 
    "description" : "<free-form text field>"
}
import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
