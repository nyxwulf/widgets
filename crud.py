from sqlalchemy.orm import Session
from datetime import datetime

import models, schemas

def get_widget(db: Session, widget_id: int):
    return db.\
        query(models.Widget).\
        filter(models.Widget.widget_id == widget_id).\
        first()

def get_widget_by_name(db: Session, name: str):
    return db.\
        query(models.Widget).\
        filter(models.Widget.name == name).\
        first()

def get_widgets(db: Session, offset: int = 0, limit: int = 10):
    return db.\
        query(models.Widget).\
        offset(offset).\
        limit(limit).\
        all()

def create_widget(db: Session, widget: schemas.WidgetCreate):
    db_widget = models.Widget(name=widget.name, description=widget.description, \
                              num_parts=widget.num_parts)
    db_widget.created_at = datetime.utcnow()
    db.add(db_widget)
    db.commit()
    db.refresh(db_widget)
    return db_widget

def update_widget(db: Session, widget: schemas.WidgetUpdate):
    db_widget = db.query(models.Widget).\
        filter(models.Widget.widget_id == widget.widget_id).\
        one_or_none()
    if db_widget is None:
        return None

    for var, value in vars(widget).items():
        setattr(db_widget, var, value) if value else None

    db_widget.updated_at = datetime.utcnow()
    db.add(db_widget)
    db.commit()
    db.refresh(db_widget)
    return db_widget

def delete_widget(db: Session, widget_id: int):
    db_widget = db.\
        query(models.Widget).\
        filter(models.Widget.widget_id == widget_id).\
        one_or_none()
    if db_widget is None:
        return None

    db.delete(db_widget)
    db.commit()
    return db_widget

