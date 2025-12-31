require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const membersRouter = require('./routes/members');
const guestbookRouter = require('./routes/guestbook');
const uploadRouter = require('./routes/upload');

const app = express();
app.use(cors());
app.use(express.json({ limit: '10mb' }));

const UPLOAD_DIR = process.env.UPLOAD_DIR || path.join(__dirname, '..', 'uploads');
if (!fs.existsSync(UPLOAD_DIR)) fs.mkdirSync(UPLOAD_DIR, { recursive: true });
app.use('/uploads', express.static(UPLOAD_DIR));

app.use('/api/members', membersRouter);
app.use('/api/guestbook', guestbookRouter);
app.use('/api/upload', uploadRouter);

app.get('/api/health', (req, res) => res.json({ ok: true }));

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
