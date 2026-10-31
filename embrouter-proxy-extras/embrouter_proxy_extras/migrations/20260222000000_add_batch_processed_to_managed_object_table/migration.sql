-- Add batch_processed column to EmbRouter_ManagedObjectTable
-- Set to true by CheckBatchCost after cost has been computed for a completed batch
ALTER TABLE "EmbRouter_ManagedObjectTable" ADD COLUMN IF NOT EXISTS "batch_processed" BOOLEAN NOT NULL DEFAULT false;
