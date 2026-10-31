-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_SSOConfig" (
    "id" TEXT NOT NULL DEFAULT 'sso_config',
    "sso_settings" JSONB NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_SSOConfig_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE IF NOT EXISTS "EmbRouter_CacheConfig" (
    "id" TEXT NOT NULL DEFAULT 'cache_config',
    "cache_settings" JSONB NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_CacheConfig_pkey" PRIMARY KEY ("id")
);

