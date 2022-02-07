from sqlalchemy.orm import Session

import models, schemas

def get_widget(db: Session, widget_id: int):
    return db.query(models.Widget).filter(models.Widget.widget_id == widget_id).first()

def get_widget_by_name(db: Session, name: str):
    return db.query(models.Widget).filter(models.Widget.name == name).first()

def get_widgets(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Widget).offset(offset).limit(limit).all()


def create_widget(db: Session, widget: schemas.WidgetCreate):
    db_widget = models.Widget(name=user.name, description=user.description, num_parts=user.num_parts)
    db.add(db_widget)
    db.commit()
    db.refresh(db_widget)
    return db_widget
