import os
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import relationship


UPLOAD_FOLDER = ""


Base = declarative_base()


class Document(Base):
    '''
    Document wrapper containing metadata and a link to the actual file
    '''
    pass
    

class File(Base):
    '''
    File stored on the file system
    '''
    
    __tablename__ = "file"
    
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.utcnow())
    path = Column(String)
    
    def open(self, mode="rb"):
        path = os.path.join(UPLOAD_FOLDER, self.path)
        return open(path, mode)
    
    def read(self):
        with self.open() as f:
            return f.read()
            
    def write(self, data):
        with self.open('wb') as f:
            f.write(data)
            
    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        
    @classmethod
    def before_flush(session, flush_context, instances):
        for obj in session.new:
            if isinstance(obj, File):
                obj.save_file()
                
    def save_file(self):
        if hasattr(self, "data") and self.data:
           self.write(self.data)
