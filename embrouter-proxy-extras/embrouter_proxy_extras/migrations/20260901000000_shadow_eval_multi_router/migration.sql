ALTER TABLE "EmbRouter_ShadowEvalJob" ADD COLUMN IF NOT EXISTS "router_names" TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[];

ALTER TABLE "EmbRouter_ShadowEvalAttempt" ADD COLUMN IF NOT EXISTS "router_name" TEXT;
