-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_SpendLogs_startTime_request_id_idx" ON "EmbRouter_SpendLogs"("startTime", "request_id");
