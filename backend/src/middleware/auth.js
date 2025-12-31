function requireAdmin(req, res, next) {
  const token = req.headers['x-admin-token'] || req.query.admin_token;
  const admin = process.env.ADMIN_TOKEN;
  if (!admin) return res.status(403).json({ error: 'Admin token not configured' });
  if (!token || token !== admin) return res.status(401).json({ error: 'Unauthorized' });
  next();
}

module.exports = { requireAdmin };
