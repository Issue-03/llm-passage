-- AlterTable
ALTER TABLE "EmbRouter_DailyUserSpend" ADD COLUMN IF NOT EXISTS "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;

-- AlterTable
ALTER TABLE "EmbRouter_DailyOrganizationSpend" ADD COLUMN IF NOT EXISTS "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;

-- AlterTable
ALTER TABLE "EmbRouter_DailyEndUserSpend" ADD COLUMN IF NOT EXISTS "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;

-- AlterTable
ALTER TABLE "EmbRouter_DailyAgentSpend" ADD COLUMN IF NOT EXISTS "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;

-- AlterTable
ALTER TABLE "EmbRouter_DailyTeamSpend" ADD COLUMN IF NOT EXISTS "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;

-- AlterTable
ALTER TABLE "EmbRouter_DailyTagSpend" ADD COLUMN IF NOT EXISTS "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;
