-- AlterTable
ALTER TABLE "EmbRouter_DeletedVerificationToken" ADD COLUMN IF NOT EXISTS "last_active" TIMESTAMP(3);

-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "last_active" TIMESTAMP(3);

