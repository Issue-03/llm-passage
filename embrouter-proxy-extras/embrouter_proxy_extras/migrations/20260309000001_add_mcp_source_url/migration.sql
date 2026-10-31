-- AlterTable: Add source_url field to EmbRouter_MCPServerTable for GitHub/docs link
ALTER TABLE "EmbRouter_MCPServerTable"
  ADD COLUMN IF NOT EXISTS "source_url" TEXT;
