-- Add static_headers and extra_headers to EmbRouter_AgentsTable

ALTER TABLE "EmbRouter_AgentsTable"
  ADD COLUMN IF NOT EXISTS "static_headers" JSONB DEFAULT '{}',
  ADD COLUMN IF NOT EXISTS "extra_headers"  TEXT[] DEFAULT ARRAY[]::TEXT[];
