-- Add agent permission fields to EmbRouter_ObjectPermissionTable
ALTER TABLE "EmbRouter_ObjectPermissionTable" ADD COLUMN IF NOT EXISTS "agents" TEXT[] DEFAULT ARRAY[]::TEXT[];
ALTER TABLE "EmbRouter_ObjectPermissionTable" ADD COLUMN IF NOT EXISTS "agent_access_groups" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- Add agent_access_groups field to EmbRouter_AgentsTable  
ALTER TABLE "EmbRouter_AgentsTable" ADD COLUMN IF NOT EXISTS "agent_access_groups" TEXT[] DEFAULT ARRAY[]::TEXT[];

