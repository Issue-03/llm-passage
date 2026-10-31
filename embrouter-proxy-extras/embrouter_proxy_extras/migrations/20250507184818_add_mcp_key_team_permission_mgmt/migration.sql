-- AlterTable
ALTER TABLE "EmbRouter_OrganizationTable" ADD COLUMN IF NOT EXISTS "object_permission_id" TEXT;

-- AlterTable
ALTER TABLE "EmbRouter_TeamTable" ADD COLUMN IF NOT EXISTS "object_permission_id" TEXT;

-- AlterTable
ALTER TABLE "EmbRouter_UserTable" ADD COLUMN IF NOT EXISTS "object_permission_id" TEXT;

-- AlterTable
ALTER TABLE "EmbRouter_VerificationToken" ADD COLUMN IF NOT EXISTS "object_permission_id" TEXT;

-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_ObjectPermissionTable" (
    "object_permission_id" TEXT NOT NULL,
    "mcp_servers" TEXT[] DEFAULT ARRAY[]::TEXT[],

    CONSTRAINT "EmbRouter_ObjectPermissionTable_pkey" PRIMARY KEY ("object_permission_id")
);

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_OrganizationTable_object_permission_id_fkey') THEN
        ALTER TABLE "EmbRouter_OrganizationTable" ADD CONSTRAINT "EmbRouter_OrganizationTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_TeamTable_object_permission_id_fkey') THEN
        ALTER TABLE "EmbRouter_TeamTable" ADD CONSTRAINT "EmbRouter_TeamTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_UserTable_object_permission_id_fkey') THEN
        ALTER TABLE "EmbRouter_UserTable" ADD CONSTRAINT "EmbRouter_UserTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_VerificationToken_object_permission_id_fkey') THEN
        ALTER TABLE "EmbRouter_VerificationToken" ADD CONSTRAINT "EmbRouter_VerificationToken_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;

