from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Ορίζουμε πού θα αποθηκευτεί η βάση (ένα τοπικό αρχείο με όνομα datacenter.db στον ίδιο φάκελο)
SQLALCHEMY_DATABASE_URL = "sqlite:///./datacenter.db"

# 2. Φτιάχνουμε τη "μηχανή" (engine) που αποτελεί τη γέφυρα επικοινωνίας με την SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Φτιάχνουμε το Session, τον "μεταφραστή" που θα στέλνει τις εντολές μας στη βάση
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Φτιάχνουμε το βασικό πρότυπο (Base) πάνω στο οποίο θα χτίσουμε τους πίνακές μας
Base = declarative_base()