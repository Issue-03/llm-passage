-- DropForeignKey
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_JWTKeyMapping_token_fkey') THEN
        ALTER TABLE "EmbRouter_JWTKeyMapping" DROP CONSTRAINT "EmbRouter_JWTKeyMapping_token_fkey";
    END IF;
END $$;

-- AddForeignKey
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'EmbRouter_JWTKeyMapping_token_fkey') THEN
        ALTER TABLE "EmbRouter_JWTKeyMapping" ADD CONSTRAINT "EmbRouter_JWTKeyMapping_token_fkey" FOREIGN KEY ("token") REFERENCES "EmbRouter_VerificationToken"("token") ON DELETE CASCADE ON UPDATE CASCADE;
    END IF;
END $$;
