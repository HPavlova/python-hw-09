from src.db import session
from src.models import Contact, Phone, Email
from faker import Faker

fake = Faker()


def generate_fake_contacts():
    for i in range(20):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()

        contact = Contact(
            first_name=first_name,
            last_name=last_name
        )

        phone = Phone(
            phone=phone,
            contact=contact
        )

        email = Email(
            email=email,
            contact=contact
        )

        session.add(contact)
        session.add(phone)
        session.add(email)

        session.commit()


def add_phone(contact_id, phone):
    contact: object = session.query(Contact).filter(Contact.id == contact_id).first()
    phone = Phone(
        phone=phone,
        contact=contact
    )

    session.add(phone)
    session.commit()


def add_email(contact_id, email):
    contact: object = session.query(Contact).filter(Contact.id == contact_id).first()
    email = Email(
        email=email,
        contact=contact
    )

    session.add(email)
    session.commit()


def add_contact(first_name, last_name, phone, email):

    contact = Contact(
        first_name=first_name,
        last_name=last_name
    )

    phone = Phone(
        phone=phone,
        contact=contact
    )

    email = Email(
        email=email,
        contact=contact
    )

    session.add(contact)
    session.add(phone)
    session.add(email)

    session.commit()


def get_contact_by_id(contact_id):
    contact: object = session.query(Contact).filter(Contact.id == contact_id).first()
    return contact


def delete_contact(contact_id):
    contact: object = session.query(Contact).filter(Contact.id == contact_id).first()
    session.delete(contact)
    session.commit()
