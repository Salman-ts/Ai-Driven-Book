from fastapi import HTTPException, Header, Depends, status
from jose import jwt, JWTError
from datetime import datetime
from app.core.config import settings
from typing import Optional, Dict, Any
import secrets

async def verify_jwt(token: str) -> Dict[str, Any]:
    """
    Verify Better-Auth JWT and extract user claims.
    We assume Better-Auth signs with HS256 and the shared secret.
    """
    try:
        payload = jwt.decode(
            token, 
            settings.BETTER_AUTH_SECRET, 
            algorithms=["HS256"]
        )
        
        # Check expiry
        exp = payload.get("exp")
        if exp and datetime.utcfromtimestamp(exp) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def verify_admin(
    authorization: Optional[str] = Header(None)
) -> Dict[str, Any]:
    """
    Dependency to verify admin access.
    Checks for:
    1. Static ADMIN_API_KEY (Machine-to-machine)
    2. 'admin' role in JWT claims (User-based)
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication",
            headers={"WWW-Authenticate": "Bearer"},
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 1. Check Static Key
    if settings.ADMIN_API_KEY:
        # Secure constant-time comparison
        # Strip whitespace from token just in case
        clean_token = token.strip()
        if secrets.compare_digest(clean_token, settings.ADMIN_API_KEY):
            return {"sub": "system-admin", "role": "admin"}

    # 2. Check JWT Role
    try:
        payload = await verify_jwt(token)
        if payload.get("role") != "admin":
             raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return payload
    except HTTPException as e:
        # Re-raise authentication errors
        raise e
    except Exception:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate admin credentials",
        )

async def get_current_user(authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    """
    Dependency to get the current user from Bearer token.
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    return await verify_jwt(token)
