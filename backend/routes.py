from fastapi import FastAPI,HTTPException
from CRUD import Get_Tasks ,Task,Create_Task,Delete_Tasks,Mark_Completed

app=FastAPI()

@app.get("/")
def home():
  return('well-come to do list application')


@app.get("/tasks")
def All_tasks():
  ack,all_tasks=Get_Tasks()
  if ack:
    return(all_tasks)
  else:
    raise HTTPException(status_code=500 , detail="Internal Server Error")

@app.post("/tasks/Add")
def Add_task(task:Task):
  try:
      creaed , msg = Create_Task(task)
  except Exception as e:
    raise HTTPException(status_code=500,detail='internal server error')

  if creaed:
    return("Task Added successfully")
  else:
    raise HTTPException(status_code=409 ,detail='task all ready exists')
  

@app.post("/tasks/MarkasCompleted")
def mark(taskid:int):
  try:
    ack , msg = Mark_Completed(taskid=taskid)
  except Exception as e:
    raise HTTPException(status_code=500,detail="internal server error")
  if ack:
    return("Marked successfully")
  else:
    raise HTTPException(status_code=409 ,detail=f"task dose'nt exists {msg}")
  

#completed 
@app.delete("/task/delete")
def RemoveTask(taskid:int):
  try:
    ack,msg = Delete_Tasks(taskid=taskid)
  except Exception as e:
    raise HTTPException(status_code=500,detail="internal server error")
  if ack:
    return("tasks deleted successfully")
  else:
    raise HTTPException(status_code=409 ,detail=f"task dose'nt exists {msg}")