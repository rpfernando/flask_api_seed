import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

path = 'sqlite:' + os.path.dirname(__file__)[:-3] + 'test.db'
print path
engine = create_engine(str(path), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def load(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
