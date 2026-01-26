from app.core.config import settings
import sys

def check_env():
    print(f"Project: {settings.PROJECT_NAME}")
    print(f"Admin Key Loaded: {'Yes' if settings.ADMIN_API_KEY else 'No'}")
    if settings.ADMIN_API_KEY:
        print(f"Key Length: {len(settings.ADMIN_API_KEY)}")
        print(f"First 5 chars: {settings.ADMIN_API_KEY[:5]}")
    else:
        print("ADMIN_API_KEY is None or Empty")

if __name__ == "__main__":
    check_env()
