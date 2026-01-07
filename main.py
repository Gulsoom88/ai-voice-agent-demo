from fastapi import FastAPI
from pydantic import BaseModel
from collections import deque
import random

# Import database
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# ----------------------
# DATABASE SETUP
# ----------------------
engine = create_engine("sqlite:///leads.db", echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class LeadDB(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True, index=True)
    service = Column(String)
    location = Column(String)
    status = Column(String)

# Create table if it doesn't exist
Base.metadata.create_all(engine)

# ----------------------
# FASTAPI SETUP
# ----------------------
app = FastAPI()

# Pydantic model for lead input
class Lead(BaseModel):
    name: str
    phone: str
    service: str
    location: str

# In-memory queue for processing leads
lead_queue = deque()

# ----------------------
# ENDPOINTS
# ----------------------

@app.get("/")
def home():
    return {"message": "AI Voice Agent Backend is running"}

@app.post("/lead")
def receive_lead(lead: Lead):
    # Check if lead already exists in database (by phone)
    if session.query(LeadDB).filter_by(phone=lead.phone).first():
        return {"message": "Lead already exists"}

    # Create new lead
    lead_data = LeadDB(
        name=lead.name,
        phone=lead.phone,
        service=lead.service,
        location=lead.location,
        status="pending"
    )

    # Save to database
    session.add(lead_data)
    session.commit()

    # Add to in-memory queue for call simulation
    lead_queue.append(lead_data)

    return {"message": "Lead saved to database and queued"}

@app.get("/leads")
def get_leads():
    # Fetch all leads from database
    all_leads = session.query(LeadDB).all()
    return [
        {
            "id": lead.id,
            "name": lead.name,
            "phone": lead.phone,
            "service": lead.service,
            "location": lead.location,
            "status": lead.status
        } for lead in all_leads
    ]

@app.post("/call-next")
def call_next():
    if lead_queue:
        lead = lead_queue.popleft()  # get next lead in queue
        # Simulate call result
        lead.status = random.choice(["called", "failed"])
        session.commit()  # update status in database
        return {
            "message": f"Lead {lead.name} processed",
            "lead": {
                "id": lead.id,
                "name": lead.name,
                "phone": lead.phone,
                "service": lead.service,
                "location": lead.location,
                "status": lead.status
            }
        }
    return {"message": "No pending leads in queue"}
