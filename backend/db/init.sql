-- Initialize DB schema for Family Website

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS members (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  role text,
  initials text,
  bio text,
  fun_fact text,
  phone text,
  email text,
  birth_month text,
  birth_year text,
  photo_url text,
  parent_id uuid REFERENCES members(id) ON DELETE SET NULL,
  spouse_id uuid REFERENCES members(id) ON DELETE SET NULL,
  created_at timestamptz DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_members_parent ON members(parent_id);

CREATE TABLE IF NOT EXISTS guestbook (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  email text,
  message text NOT NULL,
  created_at timestamptz DEFAULT now()
);
