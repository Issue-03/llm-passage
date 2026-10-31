-- AlterTable
ALTER TABLE "EmbRouter_MCPServerTable" ADD COLUMN IF NOT EXISTS "available_on_public_internet" BOOLEAN NOT NULL DEFAULT false;

