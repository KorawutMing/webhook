# Vercel LINE Webhook Forwarder

A minimal Python Flask app to receive LINE webhook events and let a local backend poll them.  
This keeps all sensitive credentials on your local machine while allowing LINE to trigger events via a public URL.

---

## Folder Structure

vercel_webhook/
├─ api/
│ └─ webhook.py # Flask webhook
├─ requirements.txt # Python dependencies
└─ README.md