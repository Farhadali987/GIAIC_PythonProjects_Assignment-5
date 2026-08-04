from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from clerk_backend_api import Clerk
from app.core.config import settings

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        # Assuming Clerk is initialized or we verify using SDK
        # This is a simplified example. You might need to initialize Clerk with settings.CLERK_SECRET_KEY
        clerk = Clerk(bearer_auth=settings.CLERK_SECRET_KEY)
        user = clerk.users.verify_token(token)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
