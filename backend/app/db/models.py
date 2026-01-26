from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, JSON, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True) # ID from Better-Auth
    email = Column(String, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    point_logs = relationship("PointLog", back_populates="user")
    chat_logs = relationship("ChatLog", back_populates="user")

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), unique=True)
    software_skill = Column(String) # beginner, intermediate, expert
    hardware_skill = Column(String) # none, rpi, etc
    learning_goal = Column(String)
    
    user = relationship("User", back_populates="profile")

class PointLog(Base):
    __tablename__ = "point_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    points = Column(Integer)
    reason = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="point_logs")

class ChatLog(Base):
    __tablename__ = "chat_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    query = Column(Text)
    response = Column(Text)
    context_used = Column(JSON) # Store citations/metadata
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="chat_logs")

class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    chunk_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    doc_id = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    content_hash = Column(String(64), nullable=False, index=True)
    source_url = Column(String(512), nullable=False)
    meta_data = Column(JSON, nullable=False)
    token_count = Column(Integer, nullable=False)
    qdrant_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class IngestionJob(Base):
    __tablename__ = "ingestion_jobs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False) # pending, processing, completed, failed
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    chunks_processed = Column(Integer, default=0)
    error_log = Column(Text, nullable=True)

class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True) # Nullable for anonymous
    query_text = Column(Text, nullable=False)
    mode = Column(String(50), nullable=False) # global, selection
    latency_ms = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
