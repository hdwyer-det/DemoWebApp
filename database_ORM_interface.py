from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Extension(Base):
    __tablename__ = "extension"

    extID = Column(Integer, primary_key=True)
    name = Column(String)
    hyperlink = Column(String)
    about = Column(String)
    image = Column(String)
    language = Column(String)

    def __repr__(self):
        return f"<Extension(extID={self.extID}, name='{self.name}', hyperlink='{self.hyperlink}', about='{self.about}', image='{self.image}', language='{self.language}')>"


def listExtensionORM():
    engine = create_engine("sqlite:///.database/database.db", echo=True)
    session = Session(engine)
    extensions = session.query(Extension).all()
    session.close()

    return extensions


