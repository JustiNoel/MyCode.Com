const express = require('express');
const router = express.Router();
const db = require('../db');
const { v4: uuidv4 } = require('uuid');
const { requireAdmin } = require('../middleware/auth');

// list members (flat)
router.get('/', async (req, res) => {
  try {
    const result = await db.query('SELECT * FROM members ORDER BY created_at');
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

// get single member
router.get('/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const r = await db.query('SELECT * FROM members WHERE id = $1', [id]);
    if (r.rows.length === 0) return res.status(404).json({ error: 'Not found' });
    res.json(r.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

// create member (protected)
router.post('/', requireAdmin, async (req, res) => {
  try {
    const { name, role, initials, bio, fun_fact, phone, email, birth_month, birth_year, parent_id } = req.body;
    const r = await db.query(
      `INSERT INTO members (name, role, initials, bio, fun_fact, phone, email, birth_month, birth_year, parent_id)
       VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10) RETURNING *`,
      [name, role, initials, bio, fun_fact, phone, email, birth_month, birth_year, parent_id]
    );
    res.status(201).json(r.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

// update member (protected)
router.put('/:id', requireAdmin, async (req, res) => {
  try {
    const id = req.params.id;
    const updates = req.body;
    const fields = [];
    const values = [];
    let i = 1;
    for (const key in updates) {
      fields.push(`${key} = $${i}`);
      values.push(updates[key]);
      i++;
    }
    if (fields.length === 0) return res.status(400).json({ error: 'No updates' });
    values.push(id);
    const q = `UPDATE members SET ${fields.join(', ')} WHERE id = $${i} RETURNING *`;
    const r = await db.query(q, values);
    if (r.rows.length === 0) return res.status(404).json({ error: 'Not found' });
    res.json(r.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

// add spouse (sets spouse_id for both)
// add spouse (protected)
router.post('/:id/spouse', requireAdmin, async (req, res) => {
  try {
    const id = req.params.id;
    const { name } = req.body;
    const spouseRes = await db.query('INSERT INTO members (name) VALUES ($1) RETURNING *', [name]);
    const spouse = spouseRes.rows[0];
    await db.query('UPDATE members SET spouse_id = $1 WHERE id = $2', [spouse.id, id]);
    await db.query('UPDATE members SET spouse_id = $1 WHERE id = $2', [id, spouse.id]);
    res.status(201).json(spouse);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

// add child (protected)
router.post('/:id/children', requireAdmin, async (req, res) => {
  try {
    const parentId = req.params.id;
    const { name } = req.body;
    const childRes = await db.query('INSERT INTO members (name, parent_id) VALUES ($1,$2) RETURNING *', [name, parentId]);
    res.status(201).json(childRes.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'DB error' });
  }
});

module.exports = router;
