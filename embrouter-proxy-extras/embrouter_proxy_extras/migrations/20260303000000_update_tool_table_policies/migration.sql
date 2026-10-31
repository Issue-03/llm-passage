-- Rename call_policy to input_policy (only if the old name still exists)
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'EmbRouter_ToolTable' AND column_name = 'call_policy') THEN
        ALTER TABLE "EmbRouter_ToolTable" RENAME COLUMN "call_policy" TO "input_policy";
    END IF;
END $$;

-- Add output_policy column
ALTER TABLE "EmbRouter_ToolTable" ADD COLUMN IF NOT EXISTS "output_policy" TEXT NOT NULL DEFAULT 'untrusted';

-- Add user_agent column
ALTER TABLE "EmbRouter_ToolTable" ADD COLUMN IF NOT EXISTS "user_agent" TEXT;

-- Add last_used_at column
ALTER TABLE "EmbRouter_ToolTable" ADD COLUMN IF NOT EXISTS "last_used_at" TIMESTAMP(3);

-- Drop old index on call_policy
DROP INDEX IF EXISTS "EmbRouter_ToolTable_call_policy_idx";

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_ToolTable_input_policy_idx" ON "EmbRouter_ToolTable"("input_policy");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_ToolTable_output_policy_idx" ON "EmbRouter_ToolTable"("output_policy");
