-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_DeprecatedVerificationToken" (
    "id" TEXT NOT NULL,
    "token" TEXT NOT NULL,
    "active_token_id" TEXT NOT NULL,
    "revoke_at" TIMESTAMP(3) NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_DeprecatedVerificationToken_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "EmbRouter_DeprecatedVerificationToken_token_key" ON "EmbRouter_DeprecatedVerificationToken"("token");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DeprecatedVerificationToken_token_revoke_at_idx" ON "EmbRouter_DeprecatedVerificationToken"("token", "revoke_at");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "EmbRouter_DeprecatedVerificationToken_revoke_at_idx" ON "EmbRouter_DeprecatedVerificationToken"("revoke_at");
