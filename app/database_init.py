# app/database_init.py
"""
Database initialization module.

This module provides functions to initialize and drop database tables.
Used primarily for testing and initial setup.
"""

import logging
from app.database import Base, engine
from app.models.user import User
from app.models.calculation import Calculation

logger = logging.getLogger(__name__)

def init_db():
    """
    Initialize the database by creating all tables.
    
    This function creates all tables defined in the SQLAlchemy models.
    It's safe to call multiple times - if tables already exist, they won't be recreated.
    """
    try:
        logger.info("Initializing database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully!")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise

def drop_db():
    """
    Drop all database tables.
    
    WARNING: This will delete all data in the database!
    Use with caution, primarily for testing purposes.
    """
    try:
        logger.info("Dropping all database tables...")
        Base.metadata.drop_all(bind=engine)
        logger.info("Database tables dropped successfully!")
    except Exception as e:
        logger.error(f"Error dropping database: {str(e)}")
        raise

if __name__ == "__main__":
    # Allow running this module directly to initialize the database
    logging.basicConfig(level=logging.INFO)
    init_db()