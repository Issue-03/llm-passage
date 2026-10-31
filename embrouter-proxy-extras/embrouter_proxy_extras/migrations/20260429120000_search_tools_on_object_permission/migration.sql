-- Search tool allowlists live on EmbRouter_ObjectPermissionTable (with agents, MCP, vector stores).
ALTER TABLE "EmbRouter_ObjectPermissionTable" ADD COLUMN IF NOT EXISTS "search_tools" TEXT[] DEFAULT ARRAY[]::TEXT[];
