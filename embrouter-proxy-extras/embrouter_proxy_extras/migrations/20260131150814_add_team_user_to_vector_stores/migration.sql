-- AlterTable
ALTER TABLE "EmbRouter_ManagedVectorStoresTable"
    ADD COLUMN IF NOT EXISTS "team_id" TEXT,
    ADD COLUMN IF NOT EXISTS "user_id" TEXT;

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_ManagedVectorStoresTable_team_id_idx"
    ON "EmbRouter_ManagedVectorStoresTable"("team_id");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_ManagedVectorStoresTable_user_id_idx"
    ON "EmbRouter_ManagedVectorStoresTable"("user_id");

