-- AlterTable
ALTER TABLE "EmbRouter_TeamTable" ADD COLUMN IF NOT EXISTS "router_settings" JSONB DEFAULT '{}';

-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "router_settings" JSONB DEFAULT '{}';

