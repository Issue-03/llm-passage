-- CreateTable
CREATE TABLE "EmbRouter_WorkflowRun" (
    "run_id" TEXT NOT NULL,
    "session_id" TEXT NOT NULL,
    "workflow_type" TEXT NOT NULL,
    "status" TEXT NOT NULL DEFAULT 'pending',
    "created_by" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "input" JSONB,
    "output" JSONB,
    "metadata" JSONB,

    CONSTRAINT "EmbRouter_WorkflowRun_pkey" PRIMARY KEY ("run_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_WorkflowEvent" (
    "event_id" TEXT NOT NULL,
    "run_id" TEXT NOT NULL,
    "event_type" TEXT NOT NULL,
    "step_name" TEXT NOT NULL,
    "sequence_number" INTEGER NOT NULL,
    "data" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_WorkflowEvent_pkey" PRIMARY KEY ("event_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_WorkflowMessage" (
    "message_id" TEXT NOT NULL,
    "run_id" TEXT NOT NULL,
    "role" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "sequence_number" INTEGER NOT NULL,
    "session_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_WorkflowMessage_pkey" PRIMARY KEY ("message_id")
);

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_WorkflowRun_session_id_key" ON "EmbRouter_WorkflowRun"("session_id");

-- CreateIndex
CREATE INDEX "EmbRouter_WorkflowRun_workflow_type_status_idx" ON "EmbRouter_WorkflowRun"("workflow_type", "status");

-- CreateIndex
CREATE INDEX "EmbRouter_WorkflowRun_session_id_idx" ON "EmbRouter_WorkflowRun"("session_id");

-- CreateIndex
CREATE INDEX "EmbRouter_WorkflowRun_created_at_idx" ON "EmbRouter_WorkflowRun"("created_at");

-- CreateIndex
CREATE INDEX "EmbRouter_WorkflowRun_created_by_idx" ON "EmbRouter_WorkflowRun"("created_by");

-- CreateIndex
CREATE INDEX "EmbRouter_WorkflowEvent_run_id_idx" ON "EmbRouter_WorkflowEvent"("run_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_WorkflowEvent_run_id_sequence_number_key" ON "EmbRouter_WorkflowEvent"("run_id", "sequence_number");

-- CreateIndex
CREATE INDEX "EmbRouter_WorkflowMessage_run_id_idx" ON "EmbRouter_WorkflowMessage"("run_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_WorkflowMessage_run_id_sequence_number_key" ON "EmbRouter_WorkflowMessage"("run_id", "sequence_number");

-- AddForeignKey
ALTER TABLE "EmbRouter_WorkflowEvent" ADD CONSTRAINT "EmbRouter_WorkflowEvent_run_id_fkey" FOREIGN KEY ("run_id") REFERENCES "EmbRouter_WorkflowRun"("run_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_WorkflowMessage" ADD CONSTRAINT "EmbRouter_WorkflowMessage_run_id_fkey" FOREIGN KEY ("run_id") REFERENCES "EmbRouter_WorkflowRun"("run_id") ON DELETE RESTRICT ON UPDATE CASCADE;

