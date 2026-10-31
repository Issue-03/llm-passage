-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_SpendLogs_api_key_startTime_idx" ON "EmbRouter_SpendLogs"("api_key", "startTime");
