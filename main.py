from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/widgets/", response_model=schemas.Widget)
def create_widget(widget: schemas.WidgetCreate, db: Session = Depends(get_db)):
    db_widget = crud.get_widget_by_name(db, name=widget.name)
    if db_widget:
        raise HTTPException(status_code=400, detail="Widget name already created")
    return crud.create_widget(db=db, widget=widget)

@app.get("/widgets/", response_model=List[schemas.Widget])
def list_widgets(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    widgets = crud.get_widgets(db, offset=offset, limit=limit)
    return widgets

@app.patch("/widgets/", response_model=schemas.Widget)
def update_widget(widget: schemas.WidgetUpdate, db: Session = Depends(get_db)):
    db_widget = crud.update_widget(db=db, widget=widget)
    if db_widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    return db_widget

@app.delete("/widgets/{widget_id}", response_model=schemas.Widget)
def delete_widget(widget_id: int, db: Session = Depends(get_db)):
    db_widget = crud.delete_widget(db=db, widget_id=widget_id)
    if db_widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    return db_widget


@app.get("/widgets/{widget_id}", response_model=schemas.Widget)
def read_widget(widget_id: int, db: Session = Depends(get_db)):
    db_widget = crud.get_widget(db, widget_id=widget_id)
    if db_widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    return db_widget
