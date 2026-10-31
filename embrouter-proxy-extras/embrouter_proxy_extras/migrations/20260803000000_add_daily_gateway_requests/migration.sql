-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_DailyGatewayRequests" (
    "date" TEXT NOT NULL,
    "category" TEXT NOT NULL,
    "route" TEXT NOT NULL,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyGatewayRequests_pkey" PRIMARY KEY ("date","category","route")
);

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DailyGatewayRequests_date_idx" ON "EmbRouter_DailyGatewayRequests"("date");
