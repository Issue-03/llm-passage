-- AlterTable
ALTER TABLE "EmbRouter_DailyTagSpend" ALTER COLUMN "tag" DROP NOT NULL;

-- AlterTable
ALTER TABLE "EmbRouter_DailyTeamSpend" ALTER COLUMN "team_id" DROP NOT NULL;

-- AlterTable
ALTER TABLE "EmbRouter_DailyUserSpend" ALTER COLUMN "user_id" DROP NOT NULL;

