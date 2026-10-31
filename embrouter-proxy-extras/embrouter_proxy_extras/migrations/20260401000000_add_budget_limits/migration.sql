-- AlterTable: add budget_limits column to EmbRouter_VerificationToken
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "budget_limits" JSONB;

-- AlterTable: add budget_limits column to EmbRouter_TeamTable
ALTER TABLE "EmbRouter_TeamTable" ADD COLUMN IF NOT EXISTS "budget_limits" JSONB;
