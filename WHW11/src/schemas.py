from pydantic import BaseModel
from typing import Optional

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: Optional[str] = None
    additional_data: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int

class ContactListResponse(ContactBase):
    id: int

class ContactSearchResponse(ContactBase):
    id: int
