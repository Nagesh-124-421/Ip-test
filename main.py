from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Adjust this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/my-endpoint')
async def my_endpoint(request: Request):
    forwarded_for = request.headers.get('X-Forwarded-For')
    if forwarded_for:
        # Get the first IP in the X-Forwarded-For list, which is the client's IP
        ip = forwarded_for.split(',')[0]
    else:
        # Fallback to the request's client IP (likely to be the proxy's IP)
        ip = request.client.host

    print(ip)
    return {'status': 1, 'message': 'ok'}
