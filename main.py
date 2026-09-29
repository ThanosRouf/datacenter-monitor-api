from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel 
from fastapi import FastAPI, Depends, Form
import random

# Εισάγουμε τα αρχεία που μόλις φτιάξαμε
import models
from database import engine, SessionLocal

class ServerMetricCreate(BaseModel):
    server_id: int
    rack_name: str
    cpu_usage: int
    temperature: int

# Εντολή-Κλειδί: Λέμε στο SQLAlchemy να δημιουργήσει το αρχείο της βάσης και τους πίνακες!
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Συνάρτηση για να ανοίγουμε και να κλείνουμε με ασφάλεια τη βάση σε κάθε αίτημα
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Data Center Monitor API", "status": "Active"}

# Βάλαμε το db: Session = Depends(get_db) για να έχει πρόσβαση στη βάση αυτό το endpoint
@app.get("/servers/{server_id}")
def get_server_status(server_id: int, db: Session = Depends(get_db)):
    cpu = random.randint(10, 95)
    temp = random.randint(30, 85)
    
    if temp > 75:
        status = "Critical - Cooling Required"
    elif temp > 60:
        status = "Warning - High Load"
    else:
        status = "Healthy"
        
    # 1. Ετοιμάζουμε το "πακέτο" των δεδομένων με βάση το μοντέλο μας
    new_metric = models.ServerMetric(
        server_id=server_id,
        rack_name=f"AWS-KOZANI-RACK-{server_id:02d}",
        cpu_usage=cpu,
        temperature=temp,
        status=status
    )
    
    # 2. Το βάζουμε στη βάση (add) και αποθηκεύουμε μόνιμα (commit)
    db.add(new_metric)
    db.commit()
    db.refresh(new_metric) # Φέρνουμε πίσω τα δεδομένα για να δούμε το ID και την ώρα που μπήκαν αυτόματα
    
    # 3. Τα δείχνουμε στον browser
    return new_metric

# Νέο endpoint για την ανάγνωση του ιστορικού από τη βάση δεδομένων
@app.get("/servers/{server_id}/history")
def get_server_history(server_id: int, db: Session = Depends(get_db)):
    # Ζητάμε από τη βάση τις 5 πιο πρόσφατες μετρήσεις του συγκεκριμένου server
    history = db.query(models.ServerMetric)\
                .filter(models.ServerMetric.server_id == server_id)\
                .order_by(models.ServerMetric.timestamp.desc())\
                .limit(5)\
                .all()
    
    return history

@app.post("/servers/")
def create_server_metric(
    server_id: int = Form(...),
    rack_name: str = Form(...),
    cpu_usage: int = Form(...),
    temperature: int = Form(...),
    db: Session = Depends(get_db)
):
    # Υπολογίζουμε αυτόματα το status βάσει της θερμοκρασίας
    if temperature > 75:
        status = "Critical - Cooling Required"
    elif temperature > 60:
        status = "Warning - High Load"
    else:
        status = "Healthy"
        
    # Ετοιμάζουμε την εγγραφή για τη βάση
    new_metric = models.ServerMetric(
        server_id=server_id,
        rack_name=rack_name,
        cpu_usage=cpu_usage,
        temperature=temperature,
        status=status
    )
    
    # Την αποθηκεύουμε μόνιμα
    db.add(new_metric)
    db.commit()
    db.refresh(new_metric) 
    
    return new_metric