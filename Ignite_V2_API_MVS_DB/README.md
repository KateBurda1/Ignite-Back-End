# Ignite V2 Agentic API – DB-backed (MVS)

**Base URL:** https://app.ingnityourgrowth.com

## Public (GET)
- /api/data
- /api/valuescores
- /api/insights
- /api/recommendations
- /api/segments
- /api/fields
- /api/sample/flyinghorse

## Private (POST Ingest)
- /internal/ingest/data
- /internal/ingest/valuescores
- /internal/ingest/insights
- /internal/ingest/recommendations
- /internal/ingest/segments

### Auth
Header: `x-api-key: <your key>`

### Database
Set `DATABASE_URL` (e.g., Supabase Postgres).

### Tables (run in SQL editor)
See `docs/sql/create_tables.sql` for schema.
