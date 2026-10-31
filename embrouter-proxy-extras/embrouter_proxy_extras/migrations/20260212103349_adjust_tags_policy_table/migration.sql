-- AlterTable
ALTER TABLE "EmbRouter_PolicyAttachmentTable" ADD COLUMN IF NOT EXISTS "tags" TEXT[] DEFAULT ARRAY[]::TEXT[];

