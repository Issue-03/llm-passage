-- AlterTable
ALTER TABLE "EmbRouter_BudgetTable" ADD COLUMN IF NOT EXISTS "tpd_limit" BIGINT;

-- AlterTable
ALTER TABLE "EmbRouter_TeamTable" ADD COLUMN IF NOT EXISTS "tpd_limit" BIGINT;

-- AlterTable
ALTER TABLE "EmbRouter_DeletedTeamTable" ADD COLUMN IF NOT EXISTS "tpd_limit" BIGINT;

-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "tpd_limit" BIGINT;

-- AlterTable
ALTER TABLE "EmbRouter_DeletedVerificationToken" ADD COLUMN IF NOT EXISTS "tpd_limit" BIGINT;
