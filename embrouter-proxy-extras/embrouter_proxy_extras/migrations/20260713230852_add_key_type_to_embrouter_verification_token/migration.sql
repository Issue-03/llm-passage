-- AlterTable
ALTER TABLE "EmbRouter_DeletedVerificationToken" ADD COLUMN     "key_type" TEXT;

-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN     "key_type" TEXT;

