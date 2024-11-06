import json

def returnJSONDict():
  # return the existing data
  with open('tasks.json', 'r') as f:
    data = json.load(f)
  return data

def returnNewTaskId(data):
  if data["tasks"]:
    last_id = data["tasks"][-1]["id"]
    taskID = last_id + 1
  else:
    taskID = 1

  return taskID

def appendJSON(taskName, taskPriority, taksStatus):

  data = returnJSONDict()

  task = {
    "id" : returnNewTaskId(data),
    "name": taskName,
    "priority": taskPriority,
    "status": taksStatus
  }

  data["tasks"].append(task)

  with open('tasks.json', 'w') as f:
    json.dump(data, f, indent=2)
