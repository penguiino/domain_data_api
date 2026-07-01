from fastapi import Request, HTTPException, status

# Replace/add real API keys here
API_KEYS = {
    "demo-key-123",
}

def require_api_key(request: Request):
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )
