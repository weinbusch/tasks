from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import relationship


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
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.utcnow())
    path = Column(String)
    
    def open(self, mode="rb"):
        return open(self.path, mode)
    
    def read(self):
        with self.open() as f:
            return f.read()
            
    def write(self, data):
        with self.open('wb') as f:
            f.write(data)
