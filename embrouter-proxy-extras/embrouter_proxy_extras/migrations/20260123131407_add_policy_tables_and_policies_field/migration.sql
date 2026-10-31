-- AlterTable
ALTER TABLE "EmbRouter_DeletedTeamTable" ADD COLUMN IF NOT EXISTS "policies" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- AlterTable
ALTER TABLE "EmbRouter_DeletedVerificationToken" ADD COLUMN IF NOT EXISTS "policies" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- AlterTable
ALTER TABLE "EmbRouter_TeamTable" ADD COLUMN IF NOT EXISTS "policies" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- AlterTable
ALTER TABLE "EmbRouter_UserTable" ADD COLUMN IF NOT EXISTS "policies" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "policies" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_PolicyTable" (
    "policy_id" TEXT NOT NULL,
    "policy_name" TEXT NOT NULL,
    "inherit" TEXT,
    "description" TEXT,
    "guardrails_add" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "guardrails_remove" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "condition" JSONB DEFAULT '{}',
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_PolicyTable_pkey" PRIMARY KEY ("policy_id")
);

-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_PolicyAttachmentTable" (
    "attachment_id" TEXT NOT NULL,
    "policy_name" TEXT NOT NULL,
    "scope" TEXT,
    "teams" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "keys" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "models" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_PolicyAttachmentTable_pkey" PRIMARY KEY ("attachment_id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_PolicyTable_policy_name_key" ON "EmbRouter_PolicyTable"("policy_name");

