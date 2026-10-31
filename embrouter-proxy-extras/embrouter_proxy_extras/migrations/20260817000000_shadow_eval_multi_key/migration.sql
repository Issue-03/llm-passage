ALTER TABLE "EmbRouter_ShadowEvalJob" ADD COLUMN IF NOT EXISTS "group_id" TEXT;

UPDATE "EmbRouter_ShadowEvalJob" SET "group_id" = "id" WHERE "group_id" IS NULL;

ALTER TABLE "EmbRouter_ShadowEvalJob" ALTER COLUMN "group_id" SET NOT NULL;

CREATE INDEX IF NOT EXISTS "EmbRouter_ShadowEvalJob_group_id_idx" ON "EmbRouter_ShadowEvalJob"("group_id");
