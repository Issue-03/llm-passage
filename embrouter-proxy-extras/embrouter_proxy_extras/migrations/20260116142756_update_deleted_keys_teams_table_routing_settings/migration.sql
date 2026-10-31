-- AlterTable
ALTER TABLE "EmbRouter_DeletedTeamTable" ADD COLUMN IF NOT EXISTS "router_settings" JSONB DEFAULT '{}';

-- AlterTable
ALTER TABLE "EmbRouter_DeletedVerificationToken" ADD COLUMN IF NOT EXISTS "router_settings" JSONB DEFAULT '{}';

