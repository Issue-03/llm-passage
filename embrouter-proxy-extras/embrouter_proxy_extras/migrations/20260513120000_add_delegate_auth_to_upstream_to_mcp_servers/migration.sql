-- AlterTable
ALTER TABLE "EmbRouter_MCPServerTable" ADD COLUMN IF NOT EXISTS "delegate_auth_to_upstream" BOOLEAN NOT NULL DEFAULT false;
