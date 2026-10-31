-- AlterTable
ALTER TABLE "EmbRouter_MCPServerTable" ADD COLUMN IF NOT EXISTS "allowed_tools" TEXT[] DEFAULT ARRAY[]::TEXT[];

