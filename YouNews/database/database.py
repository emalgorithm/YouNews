from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://user:pass@localhost/younews')
Base = declarative_base()
Session = sessionmaker(bind=engine)

Base.metadata.create_all()
