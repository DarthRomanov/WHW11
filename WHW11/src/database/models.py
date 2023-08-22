from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .db import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, index=True, nullable=False)
    birthday = Column(Date)
    additional_data = Column(String)

    # Зв'язок з тегами (якщо вам потрібно)
    # tags = relationship("Tag", secondary=contact_m2m_tag, back_populates="contacts")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    # Зв'язок з контактами (якщо вам потрібно)
    # contacts = relationship("Contact", secondary=contact_m2m_tag, back_populates="tags")
