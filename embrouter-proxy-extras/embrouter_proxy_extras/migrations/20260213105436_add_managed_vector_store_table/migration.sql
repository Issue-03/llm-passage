-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_ManagedVectorStoreTable" (
    "id" TEXT NOT NULL,
    "unified_resource_id" TEXT NOT NULL,
    "resource_object" JSONB,
    "model_mappings" JSONB NOT NULL,
    "flat_model_resource_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "storage_backend" TEXT,
    "storage_url" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ManagedVectorStoreTable_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_ManagedVectorStoreTable_unified_resource_id_key" ON "EmbRouter_ManagedVectorStoreTable"("unified_resource_id");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_ManagedVectorStoreTable_unified_resource_id_idx" ON "EmbRouter_ManagedVectorStoreTable"("unified_resource_id");
