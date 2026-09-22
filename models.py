from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database import Base

# Φτιάχνουμε την κλάση που αντιπροσωπεύει τον πίνακα των μετρήσεων
class ServerMetric(Base):
    __tablename__ = "server_metrics"  # Το όνομα του πίνακα μέσα στη βάση δεδομένων

    # Ορίζουμε τις στήλες του πίνακα
    id = Column(Integer, primary_key=True, index=True) # Ο μοναδικός αριθμός της κάθε μέτρησης
    server_id = Column(Integer, index=True)            # Το ID του server (π.χ. 1, 2, 5)
    rack_name = Column(String, index=True)             # Το όνομα (π.χ. AWS-KOZANI-RACK-01)
    cpu_usage = Column(Integer)                        # Η χρήση CPU σε ποσοστό
    temperature = Column(Integer)                      # Η θερμοκρασία σε βαθμούς Κελσίου
    status = Column(String)                            # Η κατάσταση (Healthy, Warning, Critical)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc)) # Η ακριβής ώρα με ρητή δήλωση UTC