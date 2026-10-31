-- AlterTable
ALTER TABLE "EmbRouter_AgentsTable" ADD COLUMN IF NOT EXISTS "access_group_ids" TEXT[] DEFAULT ARRAY[]::TEXT[];
