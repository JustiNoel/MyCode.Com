# Family Website - Backend

This is a Node.js + Express backend for the Family Website. It uses Postgres to store members and guestbook entries and provides endpoints for uploads.

Quick start (Docker):

1. Copy `.env.example` to `.env` and edit if needed.
2. Start services:

```bash
docker compose up --build
```

3. Once Postgres is ready, run DB initialization:

```bash
# inside container or from host if psql is available
docker compose exec db bash -c "psql -U postgres -d familydb -f /app/db/init.sql"
```

Note: `init.sql` is present in `backend/db/init.sql` and will create `members` and `guestbook` tables.

Environment variables (backend/.env):
- `ADMIN_TOKEN` : simple admin token for protecting write endpoints (set to a random value)
- `SENDGRID_API_KEY` : optional SendGrid API key to send notification emails
- `SENDGRID_FROM_EMAIL` : optional from email for SendGrid
- `NOTIFY_EMAIL_TO` : email address to receive guestbook/contact notifications
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_FROM` : optional Twilio credentials to send WhatsApp messages
- `NOTIFY_WHATSAPP_TO` : phone number to receive WhatsApp notifications (without 'whatsapp:' prefix)

Local dev (without Docker):

- Ensure Postgres is available and `DATABASE_URL` in `.env` points to it.
- Install deps: `npm install`
- Run: `npm run dev`

API Endpoints:
- `GET /api/members` - list all members
- `GET /api/members/:id` - get single member
- `POST /api/members` - create member
- `PUT /api/members/:id` - update member
- `POST /api/members/:id/spouse` - add spouse (creates member and links)
- `POST /api/members/:id/children` - add child
- `POST /api/upload` - upload image (form field `file`), returns `{ url }`
- `GET /api/guestbook` - list guestbook entries
- `POST /api/guestbook` - create guestbook entry

Next integration steps:
- Wire frontend to call these endpoints and replace local in-memory state.
- Add authentication and authorization as needed.
- Add server-side email/WhatsApp integration (SendGrid/Twilio) if needed.
