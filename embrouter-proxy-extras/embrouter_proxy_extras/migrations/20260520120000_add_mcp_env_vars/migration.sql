-- AlterTable: add admin-configured env_vars to MCP server table
ALTER TABLE "EmbRouter_MCPServerTable" ADD COLUMN IF NOT EXISTS "env_vars" JSONB DEFAULT '[]';

-- CreateTable: per-user env var values for MCP servers
CREATE TABLE IF NOT EXISTS "EmbRouter_MCPUserEnvVars" (
    "id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "server_id" TEXT NOT NULL,
    "values_b64" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_MCPUserEnvVars_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_MCPUserEnvVars_user_id_server_id_key" ON "EmbRouter_MCPUserEnvVars"("user_id", "server_id");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_MCPUserEnvVars_user_id_idx" ON "EmbRouter_MCPUserEnvVars"("user_id");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_MCPUserEnvVars_server_id_idx" ON "EmbRouter_MCPUserEnvVars"("server_id");
