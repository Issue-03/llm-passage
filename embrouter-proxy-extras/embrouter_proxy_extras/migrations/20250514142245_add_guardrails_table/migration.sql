-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_GuardrailsTable" (
    "guardrail_id" TEXT NOT NULL,
    "guardrail_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "guardrail_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_GuardrailsTable_pkey" PRIMARY KEY ("guardrail_id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_GuardrailsTable_guardrail_name_key" ON "EmbRouter_GuardrailsTable"("guardrail_name");

