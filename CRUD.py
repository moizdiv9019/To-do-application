from db import check_database_is_active
from pydantic import BaseModel, ConfigDict, Field
from typing import Union

class Task(BaseModel):
    taskid: int = Field(..., alias="TID")
    taskname: str = Field(..., alias="Tname")
    taskdescreption: str = Field(..., alias="Tdescreption")
    is_completed: bool

    model_config = ConfigDict(populate_by_name=True)

class Tasks(BaseModel):
    tasks: list[Task]

    model_config = ConfigDict(from_attributes=True)

def is_present(taskid:int):
    ack , db = check_database_is_active()
    if not ack:
        raise RuntimeError(f"Database connection failed: {db}")
    cursor = db.cursor()
    Query="SELECT TID FROM TASKS;"
    cursor.execute(Query)
    tasksids=cursor.fetchall() 
    db.commit()
    cursor.close()
    db.close()

    for each in tasksids:
        if taskid==each[0]:
            return True
    return False


def Create_Task(task:Task | dict) -> bool|str:
    if isinstance(task, dict):
        task = Task(**task)

    ack, db = check_database_is_active()
    if not ack:
        raise RuntimeError(f"Database connection failed: {db}")

    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO TASKS (Tid, Tname, Tdescreption, is_completed) VALUES (%s, %s, %s, %s)",
            (task.taskid, task.taskname, task.taskdescreption, task.is_completed),
        )
        db.commit()
        cursor.close()
        db.close()
        return(True,'Done')
    except Exception as e:
        cursor.close()
        db.close()
        return (False,e)
    

def Get_Tasks()-> bool|Task:
    ack,db=check_database_is_active()
    if not ack:
        raise RuntimeError(f"Database connection failed: {db}")
    
    try:
       cursor = db.cursor()
       query = 'SELECT TID, Tname, Tdescreption, is_completed FROM tasks;'
       cursor.execute(query)
       rows = cursor.fetchall()
       columns = [column[0] for column in cursor.description]
       task_items = [Task(**dict(zip(columns, row))) for row in rows]
       cursor.close()
       db.close()
       return (True, Tasks(tasks=task_items))
    except Exception as e:
        cursor.close()
        db.close()
        return (False, f"can't get tasks error {e}")
    


#pendding work , bugs 
def Delete_Tasks(taskid:int)-> Union[bool,str] :
    ack, db = check_database_is_active()
    if not ack:
        raise RuntimeError(f"Database connection failed: {db}")

    cursor = db.cursor()
    try:
        isnot_esixts=True
        qurey=f'SELECT TID FROM TASKS'
        cursor.execute(qurey)
        tids=cursor.fetchall()
        for each in range(len(tids)):
         if taskid == tids[each][0]:
            isnot_esixts=False
        if isnot_esixts:
            return (False,'Unknown taks')
    except Exception as e:
         pass

    try:
        qurey=f'DELETE FROM TASKS WHERE TID={taskid}'
        cursor.execute(qurey)
        cursor.close()
        db.close()
        return (True,'tasks deleted')
    except Exception as e:
        return(False,f"can't delete the task error:{e}")


def Mark_Completed(taskid:int)->bool|str:
    is_in_tasks = is_present(taskid=taskid)
    if not is_in_tasks:
        return(False,'Unknown task')
    ack , db = check_database_is_active()
    if not ack:
        raise RuntimeError(f"Database connection failed: {db}")

    cursor = db.cursor()
    try:
        Query=f'UPDATE TASKS SET IS_COMPLETED=1 WHERE TID={taskid}'
        cursor.execute(Query)
        db.commit()
        cursor.close()
        db.close()
        return(True,'Done')
    except Exception as e:
        db.commit()
        cursor.close()
        db.close()
        return(False,e)


ack,msg=Delete_Tasks(1)
print(ack,msg)