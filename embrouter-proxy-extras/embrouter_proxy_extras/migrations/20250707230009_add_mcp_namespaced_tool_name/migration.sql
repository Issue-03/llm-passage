-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyTagSpend_tag_date_api_key_model_custom_llm_pro_key";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyTeamSpend_team_id_date_api_key_model_custom_ll_key";

-- DropIndex
DROP INDEX IF EXISTS "EmbRouter_DailyUserSpend_user_id_date_api_key_model_custom_ll_key";

-- AlterTable
ALTER TABLE "EmbRouter_DailyTagSpend" ADD COLUMN IF NOT EXISTS "mcp_namespaced_tool_name" TEXT,
ALTER COLUMN "model" DROP NOT NULL;

-- AlterTable
ALTER TABLE "EmbRouter_DailyTeamSpend" ADD COLUMN IF NOT EXISTS "mcp_namespaced_tool_name" TEXT,
ALTER COLUMN "model" DROP NOT NULL;

-- AlterTable
ALTER TABLE "EmbRouter_DailyUserSpend" ADD COLUMN IF NOT EXISTS "mcp_namespaced_tool_name" TEXT,
ALTER COLUMN "model" DROP NOT NULL;

-- AlterTable
ALTER TABLE "EmbRouter_SpendLogs" ADD COLUMN IF NOT EXISTS "mcp_namespaced_tool_name" TEXT;

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyTagSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyTagSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_DailyTagSpend_tag_date_api_key_model_custom_llm_pro_key" ON "EmbRouter_DailyTagSpend"("tag", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyTeamSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyTeamSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_DailyTeamSpend_team_id_date_api_key_model_custom_ll_key" ON "EmbRouter_DailyTeamSpend"("team_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyUserSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyUserSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_DailyUserSpend_user_id_date_api_key_model_custom_ll_key" ON "EmbRouter_DailyUserSpend"("user_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name");

