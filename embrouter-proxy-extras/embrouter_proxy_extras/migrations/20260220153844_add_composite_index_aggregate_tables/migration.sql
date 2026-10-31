-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyAgentSpend_agent_id_idx";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyEndUserSpend_end_user_id_idx";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyOrganizationSpend_organization_id_idx";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyTagSpend_tag_idx";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyTeamSpend_team_id_idx";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyUserSpend_user_id_idx";

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyAgentSpend_agent_id_date_idx" ON "EmbRouter_DailyAgentSpend"("agent_id", "date");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyEndUserSpend_end_user_id_date_idx" ON "EmbRouter_DailyEndUserSpend"("end_user_id", "date");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyOrganizationSpend_organization_id_date_idx" ON "EmbRouter_DailyOrganizationSpend"("organization_id", "date");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyTagSpend_tag_date_idx" ON "EmbRouter_DailyTagSpend"("tag", "date");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyTeamSpend_team_id_date_idx" ON "EmbRouter_DailyTeamSpend"("team_id", "date");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyUserSpend_user_id_date_idx" ON "EmbRouter_DailyUserSpend"("user_id", "date");

