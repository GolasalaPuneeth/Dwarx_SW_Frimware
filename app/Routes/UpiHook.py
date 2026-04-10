from fastapi import APIRouter, HTTPException, status, Request, Header, Depends
from dotenv import load_dotenv
from app.ServiceLayer import IcustomerRequest,CustomerRequest
import os
import hmac
import hashlib
import json


load_dotenv()
Payments : APIRouter = APIRouter(prefix="/payX",tags=["Razorpay UPI Hook"])

if not os.getenv("RAZ_WEBHOOK_SECRET"):
        raise ValueError(f"Missing required environment variable: {"RAZ_WEBHOOK_SECRET"}")
else:
     WEBHOOK_SECRET = os.getenv("RAZ_WEBHOOK_SECRET")

Services : IcustomerRequest  = CustomerRequest()

@Payments.post("/razhook")
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
        # data = payload["payload"]["qr_code"]["entity"]

        # payment_id = data.get("payment_id")
        # amount = data.get("amount")

        # print("Payment received:", payment_id, amount)
        # print(payload)
        Amount = payload['payload']['payment']['entity']['amount']
        Qr_ID = payload['payload']['qr_code']['entity']['id']
        await Services.push_service(qrid=Qr_ID,amount=Amount,vpa="saple@123")
        print(Amount,Qr_ID)
    return {"status": "ok"}
