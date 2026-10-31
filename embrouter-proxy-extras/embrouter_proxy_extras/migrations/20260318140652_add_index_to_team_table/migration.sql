-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_TeamTable_organization_id_idx" ON "EmbRouter_TeamTable"("organization_id");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_TeamTable_team_alias_idx" ON "EmbRouter_TeamTable"("team_alias");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_TeamTable_created_at_idx" ON "EmbRouter_TeamTable"("created_at");

