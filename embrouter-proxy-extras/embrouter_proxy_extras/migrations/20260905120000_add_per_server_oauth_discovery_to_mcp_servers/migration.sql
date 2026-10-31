-- AlterTable
ALTER TABLE "EmbRouter_MCPServerTable" ADD COLUMN IF NOT EXISTS "per_server_oauth_discovery" BOOLEAN NOT NULL DEFAULT false;
