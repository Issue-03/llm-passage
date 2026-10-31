-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "total_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;

-- AlterTable
ALTER TABLE "EmbRouter_DeletedVerificationToken" ADD COLUMN IF NOT EXISTS "total_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0;
