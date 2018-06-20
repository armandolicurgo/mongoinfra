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
#------------------------------
task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

#------------------------------
# The shortcut.
resp = requests.post('https://todolist.example.com/tasks/', json=task)
# The equivalent longer version.
resp = requests.post('https://todolist.example.com/tasks/',
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json'},
#-----------------------------
# todo.py
def get_tasks():
    pass
def describe_task(task_id):
    pass
def add_task(summary, description=""):
    pass
def task_done(task_id):
    pass
def update_task(task_id, summary, description):
    pass
#---------------------------------
                     
def _url(path):
    return 'https://todo.example.com' + path
#-----
import requests

def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={
        'summary': summary,
        'description': description,
        })
 #--
import todo

resp = todo.add_task("Take out trash")
if resp.status_code != 201:
    raise ApiError('Cannot create task: {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

resp = todo.get_tasks()
if resp.status_code != 200:
    raise ApiError('Cannot fetch all tasks: {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
#----
                    
  [
  { "id": 3643, "summary": "Wash car" },
  { "id": 3697, "summary": "Visit gym" }
]
#------
                     
