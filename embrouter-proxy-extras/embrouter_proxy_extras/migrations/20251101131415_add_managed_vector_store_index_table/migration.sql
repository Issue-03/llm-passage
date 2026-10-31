-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_ManagedVectorStoreIndexTable" (
    "id" TEXT NOT NULL,
    "index_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "index_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ManagedVectorStoreIndexTable_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_ManagedVectorStoreIndexTable_index_name_key" ON "EmbRouter_ManagedVectorStoreIndexTable"("index_name");

