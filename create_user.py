import sys
sys.path.insert(0, '/home/jaiagosto/projects/assignment14')

from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = SessionLocal()

# Check if user exists
existing_user = db.query(User).filter(User.username == "demo").first()
if existing_user:
    print("User 'demo' already exists")
else:
    # Create user
    hashed_password = pwd_context.hash("Demo1234!")
    new_user = User(
        username="demo",
        email="demo@example.com",
        hashed_password=hashed_password,
        first_name="Demo",
        last_name="User"
    )
    db.add(new_user)
    db.commit()
    print("User 'demo' created successfully!")
    print("Username: demo")
    print("Password: Demo1234!")

db.close()
