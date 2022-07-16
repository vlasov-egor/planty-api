from sqlalchemy import Column, VARCHAR, ARRAY, JSON

from .base import BaseModel


class Plant(BaseModel):
    __tablename__ = "plants"

    name = Column(VARCHAR(255), nullable=False)
    short_name = Column(VARCHAR(255), nullable=False)
    full_names = Column(ARRAY(VARCHAR(255)), nullable=False)
    highlights = Column(ARRAY(VARCHAR(255)), nullable=False)
    favourite_activities = Column(JSON, nullable=False)
    quick_facts = Column(JSON, nullable=False)
    about_text = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return (
            f"id: {self.id}"
            f"name: {self.name}"
            f"short_name: {self.short_name}"
            f"full_name: {self.full_name}"
            f"highlights: {self.highlights}"
            f"favourite_activities: {self.favourite_activities}"
            f"quick_facts: {self.quick_facts}"
            f"about_text: {self.about_text}"
        )
