-- AlterTable
ALTER TABLE "EmbRouter_ObjectPermissionTable" ADD COLUMN IF NOT EXISTS "models" TEXT[] DEFAULT ARRAY[]::TEXT[];

