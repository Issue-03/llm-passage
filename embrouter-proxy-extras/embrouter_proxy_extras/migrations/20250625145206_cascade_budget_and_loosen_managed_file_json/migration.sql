-- DropForeignKey
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_TeamMembership_budget_id_fkey') THEN
        ALTER TABLE "EmbRouter_TeamMembership" DROP CONSTRAINT "EmbRouter_TeamMembership_budget_id_fkey";
    END IF;
END $$;

-- AlterTable
ALTER TABLE "EmbRouter_ManagedFileTable" ALTER COLUMN "file_object" DROP NOT NULL;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_TeamMembership_budget_id_fkey') THEN
        ALTER TABLE "EmbRouter_TeamMembership" ADD CONSTRAINT "EmbRouter_TeamMembership_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

