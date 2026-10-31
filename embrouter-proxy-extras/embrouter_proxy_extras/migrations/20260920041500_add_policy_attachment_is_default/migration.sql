ALTER TABLE "EmbRouter_PolicyAttachmentTable" ADD COLUMN IF NOT EXISTS "is_default" BOOLEAN NOT NULL DEFAULT false;
