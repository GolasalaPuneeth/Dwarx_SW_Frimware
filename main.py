from fastapi import FastAPI, Request, Header, HTTPException
import hmac
import hashlib
import json
import uvicorn

app = FastAPI()
WEBHOOK_SECRET = "mysecret123"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/razhook")
async def razorpay_webhook(
    request: Request,
    x_razorpay_signature: str = Header(None),
    x_razorpay_event_id: str = Header(None)
    ):
    # 1. Read raw body
    body = await request.body()

    # 2. Verify signature
    generated_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(generated_signature, x_razorpay_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")

    # 3. Parse JSON
    payload = json.loads(body)
    event = payload.get("event")

    print("Event:", event)

    # 4. Handle events
    if event == "qr_code.credited":
        data = payload["payload"]["qr_code"]["entity"]

        payment_id = data.get("payment_id")
        amount = data.get("amount")

        print("Payment received:", payment_id, amount)
        # print(payload)
        print(payload['payload']['payment']['entity']['amount'])
        print(payload['payload']['qr_code']['entity']['id'])
    return {"status": "ok"}


if __name__=="__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=3001)