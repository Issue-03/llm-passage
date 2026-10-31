-- CreateTable
CREATE TABLE "EmbRouter_ProxyWorkerHeartbeat" (
    "worker_id" TEXT NOT NULL,
    "hostname" TEXT NOT NULL,
    "started_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "last_heartbeat_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_ProxyWorkerHeartbeat_pkey" PRIMARY KEY ("worker_id")
);
