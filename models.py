import datetime

from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship


class Model:
  pass


class Task(Model):
  
  __tablename__ = "task"
  
  id = Column(Integer, primary_key=True)
  created = Column(DateTime, default=datetime.utcnow)
  creator_id = Column(Integer, ForeignKey("User.id"))
  text = Column(Text, default="")
  due_date = Column(Date)
  closed = Column(Boolean, default=False)
  deleted = Column(Boolean, default=False)
  assignee_id = Column(Integer, ForeignKey("User.id"))

  comments = relationship("TaskComment", backref="task")
  log = relationship("TaskLogEntry", backref="task")
  attachments = relationship("TaskAttachment", backref="task")
 

class TaskComment(Model):
  
  __tablename__ = "task_comment"
  
  id = Column(Integer, primary_key=True)
  task_id = Column(Integer, ForeignKey("Task.id"))
  author_id = Column(Integer, ForeignKey("User.id"))
  created = Column(DateTime, default=datetime.utcnow)
  text = Column(Text, default="")
  
  attachments = relationship("TaskAttachment", backref="comment")

  
class TaskLogEntry(Model):
  
  __tablename__ = "task_log_entry"
  
  CHANGE = "change"
  CLOSE = "close"
  REOPEN = "reopen"
  DELETE = "delete"
  ASSIGN = "assign"
  
  id = Column(Integer, primary_key=True)
  task_id = Column(Integer, ForeignKey("Task.id"))
  user_id = Column(Integer, ForeignKey("User.id"))
  date = Column(DateTime, default=datetime.utcnow)
  action_flag = Column(String)
  text = Column(Text, default="")
  

class TaskAttachment(Model):
  
  __tablename__ = "task_attachment"
  
  id = Column(Integer, primary_key=True)
  task_id = Column(Integer, ForeignKey("Task.id"))
  comment_id = Column(Integer, ForeignKey("TaskComment.id"))
  
