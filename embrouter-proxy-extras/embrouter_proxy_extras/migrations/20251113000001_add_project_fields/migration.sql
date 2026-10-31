-- AlterTable: Add new fields to EmbRouter_ProjectTable
ALTER TABLE "EmbRouter_ProjectTable" ADD COLUMN IF NOT EXISTS "description" TEXT;
ALTER TABLE "EmbRouter_ProjectTable" ADD COLUMN IF NOT EXISTS "model_rpm_limit" JSONB NOT NULL DEFAULT '{}';
ALTER TABLE "EmbRouter_ProjectTable" ADD COLUMN IF NOT EXISTS "model_tpm_limit" JSONB NOT NULL DEFAULT '{}';

