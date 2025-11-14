-- Ignite MVS schema
CREATE TABLE IF NOT EXISTS data (
  id SERIAL PRIMARY KEY,
  parent_company_id TEXT,
  child_company_id TEXT,
  business_unit_id TEXT,
  revenue_segment_id TEXT,
  micro_segment_id TEXT,
  revenue NUMERIC,
  cost NUMERIC,
  profit_margin NUMERIC,
  growth_rate NUMERIC,
  transactions INT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS value_scores (
  id SERIAL PRIMARY KEY,
  parent_company_id TEXT,
  business_unit_id TEXT,
  revenue_segment_id TEXT,
  micro_segment_id TEXT,
  revenue NUMERIC,
  profit_margin NUMERIC,
  growth_rate NUMERIC,
  value_score NUMERIC,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS insights (
  id SERIAL PRIMARY KEY,
  parent_company_id TEXT,
  business_unit_id TEXT,
  revenue_segment_id TEXT,
  micro_segment_id TEXT,
  title TEXT,
  summary TEXT,
  confidence NUMERIC,
  source TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS recommendations (
  id SERIAL PRIMARY KEY,
  parent_company_id TEXT,
  business_unit_id TEXT,
  revenue_segment_id TEXT,
  micro_segment_id TEXT,
  recommendation TEXT,
  priority TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS segments (
  id SERIAL PRIMARY KEY,
  json_data JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
