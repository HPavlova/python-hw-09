from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.db import Base


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = relationship("Phone", cascade="all, delete-orphan", back_populates="contact")
    email = relationship("Email", cascade="all, delete-orphan", back_populates="contact")

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    phone = Column(String(50), nullable=True, default='No phone')
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship("Contact", back_populates="phone")


class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=True, default='No email')
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship("Contact", back_populates="email")
