x = {
  "entity": "event",
  "account_id": "acc_Nu6qHrmvAcMZZu",
  "event": "qr_code.credited",
  "contains": ["payment", "qr_code"],
  "payload": {
    "payment": {
      "entity": {
        "id": "pay_SSmaF5rM7L38X3",
        "entity": "payment",
        "amount": 100,
        "currency": "INR",
        "status": "captured",
        "order_id": None,
        "invoice_id": None,
        "international": False,
        "method": "upi",
        "amount_refunded": 0,
        "refund_status": None,
        "captured": None,
        "description": "QRv2 Payment",
        "card_id": None,
        "bank": None,
        "wallet": None,
        "vpa": "8096226158@ybl",
        "email": None,
        "contact": None,
        "notes": [],
        "fee": 1,
        "tax": 0,
        "error_code": None,
        "error_description": None,
        "error_source": None,
        "error_step": None,
        "error_reason": None,
        "acquirer_data": {
          "rrn": "241421477114"
        },
        "created_at": 1773857442,
        "reward": None,
        "upi": {
          "payer_account_type": "bank_account",
          "vpa": "8096226158@ybl",
          "flow": "intent"
        }
      }
    },
    "qr_code": {
      "entity": {
        "id": "qr_SQlRDZoVmnVKG6",
        "entity": "qr_code",
        "created_at": 1773416728,
        "name": None,
        "usage": "multiple_use",
        "type": "upi_qr",
        "image_url": "https://rzp.io/rzp/ABmzfFj",
        "payment_amount": None,
        "status": "active",
        "description": "sample",
        "fixed_amount": False,
        "payments_amount_received": 3100,
        "payments_count_received": 15,
        "notes": [],
        "customer_id": None,
        "close_by": None,
        "closed_at": None,
        "close_reason": None,
        "tax_invoice": []
      }
    }
  },
  "created_at": 1773857443
}

print(x['payload']['payment']['entity']['amount'])
print(x['payload']['qr_code']['entity']['id'])