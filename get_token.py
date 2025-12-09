import sys
sys.path.insert(0, '/home/jaiagosto/projects/assignment14')

from app.database import SessionLocal
from app.models.user import User
from app.auth.jwt import create_access_token

db = SessionLocal()
user = db.query(User).filter(User.username == "demo").first()

if user:
    token = create_access_token({"sub": user.username})
    print(f"Access Token: {token}")
    print(f"\nIn your browser console (F12), run:")
    print(f'localStorage.setItem("access_token", "{token}");')
    print(f'window.location.href = "/dashboard";')
else:
    print("User not found")

db.close()
