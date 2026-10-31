/*
  Warnings:

  - You are about to drop the column `spec_version` on the `EmbRouter_MCPServerTable` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "EmbRouter_MCPServerTable" DROP COLUMN IF EXISTS "spec_version";
