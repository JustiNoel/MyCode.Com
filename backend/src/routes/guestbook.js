const express = require('express');
const router = express.Router();
const db = require('../db');
const { notifyGuestbook } = require('../utils/notify');

router.get('/', async (req, res) => {
  try {
    const r = await db.query('SELECT * FROM guestbook ORDER BY created_at DESC');
    res.json(r.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

router.post('/', async (req, res) => {
  try {
    const { name, email, message } = req.body;
    const r = await db.query('INSERT INTO guestbook (name, email, message) VALUES ($1,$2,$3) RETURNING *', [name, email, message]);
    // send notifications if configured
    try {
      notifyGuestbook(r.rows[0]).catch(console.error);
    } catch (err) {
      console.error('notify error', err);
    }
    res.status(201).json(r.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

module.exports = router;
