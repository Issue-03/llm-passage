-- AlterTable
ALTER TABLE "EmbRouter_MCPServerTable" ADD COLUMN IF NOT EXISTS "pinned_tools" JSONB DEFAULT '{}';
