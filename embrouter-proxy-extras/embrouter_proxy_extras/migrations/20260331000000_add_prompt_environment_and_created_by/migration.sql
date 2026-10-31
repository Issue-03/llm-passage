-- AlterTable
ALTER TABLE "EmbRouter_PromptTable" ADD COLUMN "environment" TEXT NOT NULL DEFAULT 'development';
ALTER TABLE "EmbRouter_PromptTable" ADD COLUMN "created_by" TEXT;

-- DropIndex (old unique constraint)
DROP INDEX IF EXISTS "EmbRouter_PromptTable_prompt_id_version_key";

-- CreateIndex (new unique constraint)
CREATE UNIQUE INDEX "EmbRouter_PromptTable_prompt_id_version_environment_key" ON "EmbRouter_PromptTable"("prompt_id", "version", "environment");

-- CreateIndex (new composite index)
CREATE INDEX "EmbRouter_PromptTable_prompt_id_environment_idx" ON "EmbRouter_PromptTable"("prompt_id", "environment");
