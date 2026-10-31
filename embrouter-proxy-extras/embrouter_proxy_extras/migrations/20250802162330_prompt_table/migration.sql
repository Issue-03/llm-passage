-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_PromptTable" (
    "id" TEXT NOT NULL,
    "prompt_id" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "prompt_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_PromptTable_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_PromptTable_prompt_id_key" ON "EmbRouter_PromptTable"("prompt_id");

