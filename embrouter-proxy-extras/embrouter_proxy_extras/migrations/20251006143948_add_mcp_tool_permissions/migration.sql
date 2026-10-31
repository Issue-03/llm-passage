-- AlterTable
ALTER TABLE "EmbRouter_ObjectPermissionTable" ADD COLUMN IF NOT EXISTS "mcp_tool_permissions" JSONB;

