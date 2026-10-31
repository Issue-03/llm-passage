-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_SearchToolsTable" (
    "search_tool_id" TEXT NOT NULL,
    "search_tool_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "search_tool_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_SearchToolsTable_pkey" PRIMARY KEY ("search_tool_id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_SearchToolsTable_search_tool_name_key" ON "EmbRouter_SearchToolsTable"("search_tool_name");

