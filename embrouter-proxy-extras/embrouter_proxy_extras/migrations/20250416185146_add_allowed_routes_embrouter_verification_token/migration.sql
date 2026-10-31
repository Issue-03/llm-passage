-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "allowed_routes" TEXT[] DEFAULT ARRAY[]::TEXT[];

