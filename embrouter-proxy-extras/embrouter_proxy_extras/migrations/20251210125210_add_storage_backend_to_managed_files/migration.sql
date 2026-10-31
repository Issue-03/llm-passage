-- AlterTable
ALTER TABLE "EmbRouter_ManagedFileTable" ADD COLUMN IF NOT EXISTS "storage_backend" TEXT;
ALTER TABLE "EmbRouter_ManagedFileTable" ADD COLUMN IF NOT EXISTS "storage_url" TEXT;

