-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_ProjectTable" (
    "project_id" TEXT NOT NULL,
    "project_alias" TEXT,
    "team_id" TEXT,
    "budget_id" TEXT,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "models" TEXT[],
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "blocked" BOOLEAN NOT NULL DEFAULT false,
    "object_permission_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_ProjectTable_pkey" PRIMARY KEY ("project_id")
);

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_ProjectTable_team_id_fkey') THEN
        ALTER TABLE "EmbRouter_ProjectTable" ADD CONSTRAINT "EmbRouter_ProjectTable_team_id_fkey" FOREIGN KEY ("team_id") REFERENCES "EmbRouter_TeamTable"("team_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_ProjectTable_budget_id_fkey') THEN
        ALTER TABLE "EmbRouter_ProjectTable" ADD CONSTRAINT "EmbRouter_ProjectTable_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_ProjectTable_object_permission_id_fkey') THEN
        ALTER TABLE "EmbRouter_ProjectTable" ADD CONSTRAINT "EmbRouter_ProjectTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

-- AlterTable: Add project_id to EmbRouter_VerificationToken
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "project_id" TEXT;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_VerificationToken_project_id_fkey') THEN
        ALTER TABLE "EmbRouter_VerificationToken" ADD CONSTRAINT "EmbRouter_VerificationToken_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "EmbRouter_ProjectTable"("project_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

