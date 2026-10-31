-- CreateEnum
CREATE TYPE "JobStatus" AS ENUM ('ACTIVE', 'INACTIVE');

-- CreateTable
CREATE TABLE "EmbRouter_BudgetTable" (
    "budget_id" TEXT NOT NULL,
    "max_budget" DOUBLE PRECISION,
    "soft_budget" DOUBLE PRECISION,
    "max_parallel_requests" INTEGER,
    "tpm_limit" BIGINT,
    "rpm_limit" BIGINT,
    "tpd_limit" BIGINT,
    "model_max_budget" JSONB,
    "budget_duration" TEXT,
    "budget_reset_at" TIMESTAMP(3),
    "allowed_models" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "temp_budget_increase" DOUBLE PRECISION,
    "temp_budget_expiry" TIMESTAMP(3),
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_BudgetTable_pkey" PRIMARY KEY ("budget_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_CredentialsTable" (
    "credential_id" TEXT NOT NULL,
    "credential_name" TEXT NOT NULL,
    "credential_values" JSONB NOT NULL,
    "credential_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_CredentialsTable_pkey" PRIMARY KEY ("credential_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ProxyModelTable" (
    "model_id" TEXT NOT NULL,
    "model_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "model_info" JSONB,
    "blocked" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_ProxyModelTable_pkey" PRIMARY KEY ("model_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_AgentsTable" (
    "agent_id" TEXT NOT NULL,
    "agent_name" TEXT NOT NULL,
    "embrouter_params" JSONB,
    "agent_card_params" JSONB NOT NULL,
    "static_headers" JSONB DEFAULT '{}',
    "extra_headers" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "kill_switch" JSONB,
    "agent_access_groups" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_group_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "object_permission_id" TEXT,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "identity_managed" BOOLEAN NOT NULL DEFAULT false,
    "enabled" BOOLEAN NOT NULL DEFAULT true,
    "execution_mode" TEXT NOT NULL DEFAULT 'autonomous',
    "tpm_limit" INTEGER,
    "rpm_limit" INTEGER,
    "session_tpm_limit" INTEGER,
    "session_rpm_limit" INTEGER,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_AgentsTable_pkey" PRIMARY KEY ("agent_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_AgentIdentity" (
    "agent_id" TEXT NOT NULL,
    "active" BOOLEAN NOT NULL DEFAULT true,
    "provider" TEXT NOT NULL,
    "issuer" TEXT NOT NULL,
    "tenant_id" TEXT NOT NULL,
    "client_id" TEXT NOT NULL,
    "service_principal_id" TEXT,
    "required_roles" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "required_scopes" TEXT[] DEFAULT ARRAY['user_impersonation']::TEXT[],
    "revision" TEXT NOT NULL,
    "last_authenticated_at" TIMESTAMP(3),

    CONSTRAINT "EmbRouter_AgentIdentity_pkey" PRIMARY KEY ("agent_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_RetiredAgentIdentity" (
    "binding_id" TEXT NOT NULL,
    "agent_id" TEXT,
    "provider" TEXT NOT NULL,
    "issuer" TEXT NOT NULL,
    "tenant_id" TEXT NOT NULL,
    "client_id" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_RetiredAgentIdentity_pkey" PRIMARY KEY ("binding_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_RetiredAgent" (
    "original_agent_id" TEXT NOT NULL,
    "retired_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_RetiredAgent_pkey" PRIMARY KEY ("original_agent_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_VerifiedSubject" (
    "subject_id" TEXT NOT NULL,
    "issuer" TEXT NOT NULL,
    "tenant_id" TEXT NOT NULL,
    "oid" TEXT NOT NULL,
    "kind" TEXT NOT NULL DEFAULT 'human',
    "user_id" TEXT,
    "verified_via" TEXT NOT NULL DEFAULT 'sso_interactive',
    "verified_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_VerifiedSubject_pkey" PRIMARY KEY ("subject_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_OrganizationTable" (
    "organization_id" TEXT NOT NULL,
    "organization_alias" TEXT NOT NULL,
    "budget_id" TEXT NOT NULL,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "models" TEXT[],
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "object_permission_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_OrganizationTable_pkey" PRIMARY KEY ("organization_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ModelTable" (
    "id" SERIAL NOT NULL,
    "aliases" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_ModelTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_TeamTable" (
    "team_id" TEXT NOT NULL,
    "team_alias" TEXT,
    "organization_id" TEXT,
    "object_permission_id" TEXT,
    "admins" TEXT[],
    "members" TEXT[],
    "members_with_roles" JSONB NOT NULL DEFAULT '{}',
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "max_budget" DOUBLE PRECISION,
    "soft_budget" DOUBLE PRECISION,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "models" TEXT[],
    "max_parallel_requests" INTEGER,
    "tpm_limit" BIGINT,
    "rpm_limit" BIGINT,
    "tpd_limit" BIGINT,
    "budget_duration" TEXT,
    "budget_reset_at" TIMESTAMP(3),
    "blocked" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "model_max_budget" JSONB NOT NULL DEFAULT '{}',
    "router_settings" JSONB DEFAULT '{}',
    "team_member_permissions" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_group_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "policies" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "default_team_member_models" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "budget_limits" JSONB,
    "model_id" INTEGER,
    "allow_team_guardrail_config" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "EmbRouter_TeamTable_pkey" PRIMARY KEY ("team_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ProjectTable" (
    "project_id" TEXT NOT NULL,
    "project_alias" TEXT,
    "description" TEXT,
    "team_id" TEXT,
    "budget_id" TEXT,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "models" TEXT[],
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "model_rpm_limit" JSONB NOT NULL DEFAULT '{}',
    "model_tpm_limit" JSONB NOT NULL DEFAULT '{}',
    "blocked" BOOLEAN NOT NULL DEFAULT false,
    "object_permission_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_ProjectTable_pkey" PRIMARY KEY ("project_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DeletedTeamTable" (
    "id" TEXT NOT NULL,
    "team_id" TEXT NOT NULL,
    "team_alias" TEXT,
    "organization_id" TEXT,
    "object_permission_id" TEXT,
    "admins" TEXT[],
    "members" TEXT[],
    "members_with_roles" JSONB NOT NULL DEFAULT '{}',
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "max_budget" DOUBLE PRECISION,
    "soft_budget" DOUBLE PRECISION,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "models" TEXT[],
    "max_parallel_requests" INTEGER,
    "tpm_limit" BIGINT,
    "rpm_limit" BIGINT,
    "tpd_limit" BIGINT,
    "budget_duration" TEXT,
    "budget_reset_at" TIMESTAMP(3),
    "blocked" BOOLEAN NOT NULL DEFAULT false,
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "model_max_budget" JSONB NOT NULL DEFAULT '{}',
    "router_settings" JSONB DEFAULT '{}',
    "team_member_permissions" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_group_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "policies" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "model_id" INTEGER,
    "allow_team_guardrail_config" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMP(3),
    "updated_at" TIMESTAMP(3),
    "deleted_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_by" TEXT,
    "deleted_by_api_key" TEXT,
    "embrouter_changed_by" TEXT,

    CONSTRAINT "EmbRouter_DeletedTeamTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_UserTable" (
    "user_id" TEXT NOT NULL,
    "user_alias" TEXT,
    "team_id" TEXT,
    "sso_user_id" TEXT,
    "organization_id" TEXT,
    "object_permission_id" TEXT,
    "password" TEXT,
    "password_reset_required" BOOLEAN,
    "last_breach_check_at" TIMESTAMP(3),
    "teams" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "user_role" TEXT,
    "max_budget" DOUBLE PRECISION,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "user_email" TEXT,
    "models" TEXT[],
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "max_parallel_requests" INTEGER,
    "tpm_limit" BIGINT,
    "rpm_limit" BIGINT,
    "budget_duration" TEXT,
    "budget_reset_at" TIMESTAMP(3),
    "allowed_cache_controls" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "policies" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "model_max_budget" JSONB NOT NULL DEFAULT '{}',
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_UserTable_pkey" PRIMARY KEY ("user_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ObjectPermissionTable" (
    "object_permission_id" TEXT NOT NULL,
    "mcp_servers" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "mcp_access_groups" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "mcp_tool_permissions" JSONB,
    "vector_stores" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "agents" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "agent_access_groups" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "models" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "blocked_tools" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "mcp_toolsets" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "search_tools" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "mcp_tool_search_enabled" BOOLEAN,
    "skills" TEXT[] DEFAULT ARRAY[]::TEXT[],

    CONSTRAINT "EmbRouter_ObjectPermissionTable_pkey" PRIMARY KEY ("object_permission_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_MCPServerTable" (
    "server_id" TEXT NOT NULL,
    "server_name" TEXT,
    "alias" TEXT,
    "description" TEXT,
    "instructions" TEXT,
    "url" TEXT,
    "spec_path" TEXT,
    "transport" TEXT NOT NULL DEFAULT 'sse',
    "auth_type" TEXT,
    "credentials" JSONB DEFAULT '{}',
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,
    "mcp_info" JSONB DEFAULT '{}',
    "mcp_access_groups" TEXT[],
    "allowed_tools" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "tool_name_to_display_name" JSONB DEFAULT '{}',
    "tool_name_to_description" JSONB DEFAULT '{}',
    "pinned_tools" JSONB DEFAULT '{}',
    "extra_headers" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "static_headers" JSONB DEFAULT '{}',
    "env_vars" JSONB DEFAULT '[]',
    "status" TEXT DEFAULT 'unknown',
    "last_health_check" TIMESTAMP(3),
    "health_check_error" TEXT,
    "command" TEXT,
    "args" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "env" JSONB DEFAULT '{}',
    "issuer" TEXT,
    "authorization_url" TEXT,
    "token_url" TEXT,
    "registration_url" TEXT,
    "oauth2_flow" TEXT,
    "token_exchange_endpoint" TEXT,
    "audience" TEXT,
    "subject_token_type" TEXT,
    "token_exchange_profile" TEXT,
    "allow_all_keys" BOOLEAN NOT NULL DEFAULT false,
    "available_on_public_internet" BOOLEAN NOT NULL DEFAULT true,
    "delegate_auth_to_upstream" BOOLEAN NOT NULL DEFAULT false,
    "oauth_passthrough" BOOLEAN NOT NULL DEFAULT false,
    "dcr_bridge" BOOLEAN,
    "per_server_oauth_discovery" BOOLEAN NOT NULL DEFAULT false,
    "is_byok" BOOLEAN NOT NULL DEFAULT false,
    "byok_description" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "byok_api_key_help_url" TEXT,
    "source_url" TEXT,
    "timeout" DOUBLE PRECISION,
    "max_concurrent_requests" INTEGER,
    "approval_status" TEXT DEFAULT 'active',
    "submitted_by" TEXT,
    "submitted_at" TIMESTAMP(3),
    "reviewed_at" TIMESTAMP(3),
    "review_notes" TEXT,

    CONSTRAINT "EmbRouter_MCPServerTable_pkey" PRIMARY KEY ("server_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_MCPToolsetTable" (
    "toolset_id" TEXT NOT NULL,
    "toolset_name" TEXT NOT NULL,
    "description" TEXT,
    "tools" JSONB NOT NULL DEFAULT '[]',
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_MCPToolsetTable_pkey" PRIMARY KEY ("toolset_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_MCPUserCredentials" (
    "id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "server_id" TEXT NOT NULL,
    "credential_b64" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_MCPUserCredentials_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_MCPUserEnvVars" (
    "id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "server_id" TEXT NOT NULL,
    "values_b64" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_MCPUserEnvVars_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_MCPServerOAuthClient" (
    "server_id" TEXT NOT NULL,
    "credentials" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_MCPServerOAuthClient_pkey" PRIMARY KEY ("server_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_SSOIdentityAssertion" (
    "user_id" TEXT NOT NULL,
    "assertion_b64" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_SSOIdentityAssertion_pkey" PRIMARY KEY ("user_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_VerificationToken" (
    "token" TEXT NOT NULL,
    "key_name" TEXT,
    "key_alias" TEXT,
    "soft_budget_cooldown" BOOLEAN NOT NULL DEFAULT false,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "total_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "expires" TIMESTAMP(3),
    "models" TEXT[],
    "aliases" JSONB NOT NULL DEFAULT '{}',
    "config" JSONB NOT NULL DEFAULT '{}',
    "router_settings" JSONB DEFAULT '{}',
    "user_id" TEXT,
    "team_id" TEXT,
    "agent_id" TEXT,
    "project_id" TEXT,
    "permissions" JSONB NOT NULL DEFAULT '{}',
    "max_parallel_requests" INTEGER,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "blocked" BOOLEAN,
    "tpm_limit" BIGINT,
    "rpm_limit" BIGINT,
    "tpd_limit" BIGINT,
    "max_budget" DOUBLE PRECISION,
    "budget_duration" TEXT,
    "budget_reset_at" TIMESTAMP(3),
    "allowed_cache_controls" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "allowed_routes" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "key_type" TEXT,
    "policies" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_group_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "model_max_budget" JSONB NOT NULL DEFAULT '{}',
    "budget_fallbacks" JSONB NOT NULL DEFAULT '{}',
    "budget_id" TEXT,
    "organization_id" TEXT,
    "object_permission_id" TEXT,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,
    "settings_updated_at" TIMESTAMP(3),
    "last_active" TIMESTAMP(3),
    "rotation_count" INTEGER DEFAULT 0,
    "auto_rotate" BOOLEAN DEFAULT false,
    "rotation_interval" TEXT,
    "last_rotation_at" TIMESTAMP(3),
    "key_rotation_at" TIMESTAMP(3),
    "budget_limits" JSONB,

    CONSTRAINT "EmbRouter_VerificationToken_pkey" PRIMARY KEY ("token")
);

-- CreateTable
CREATE TABLE "EmbRouter_JWTKeyMapping" (
    "id" TEXT NOT NULL,
    "jwt_issuer" TEXT NOT NULL DEFAULT '',
    "jwt_claim_name" TEXT NOT NULL,
    "jwt_claim_value" TEXT NOT NULL,
    "token" TEXT NOT NULL,
    "description" TEXT,
    "is_active" BOOLEAN NOT NULL DEFAULT true,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_JWTKeyMapping_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DeprecatedVerificationToken" (
    "id" TEXT NOT NULL,
    "token" TEXT NOT NULL,
    "active_token_id" TEXT NOT NULL,
    "revoke_at" TIMESTAMP(3) NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_DeprecatedVerificationToken_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DeletedVerificationToken" (
    "id" TEXT NOT NULL,
    "token" TEXT NOT NULL,
    "key_name" TEXT,
    "key_alias" TEXT,
    "soft_budget_cooldown" BOOLEAN NOT NULL DEFAULT false,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "total_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "expires" TIMESTAMP(3),
    "models" TEXT[],
    "aliases" JSONB NOT NULL DEFAULT '{}',
    "config" JSONB NOT NULL DEFAULT '{}',
    "user_id" TEXT,
    "team_id" TEXT,
    "agent_id" TEXT,
    "project_id" TEXT,
    "permissions" JSONB NOT NULL DEFAULT '{}',
    "max_parallel_requests" INTEGER,
    "metadata" JSONB NOT NULL DEFAULT '{}',
    "blocked" BOOLEAN,
    "tpm_limit" BIGINT,
    "rpm_limit" BIGINT,
    "tpd_limit" BIGINT,
    "max_budget" DOUBLE PRECISION,
    "budget_duration" TEXT,
    "budget_reset_at" TIMESTAMP(3),
    "allowed_cache_controls" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "allowed_routes" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "key_type" TEXT,
    "policies" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_group_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "model_spend" JSONB NOT NULL DEFAULT '{}',
    "model_max_budget" JSONB NOT NULL DEFAULT '{}',
    "budget_fallbacks" JSONB NOT NULL DEFAULT '{}',
    "router_settings" JSONB DEFAULT '{}',
    "budget_id" TEXT,
    "organization_id" TEXT,
    "object_permission_id" TEXT,
    "created_at" TIMESTAMP(3),
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3),
    "updated_by" TEXT,
    "settings_updated_at" TIMESTAMP(3),
    "last_active" TIMESTAMP(3),
    "rotation_count" INTEGER DEFAULT 0,
    "auto_rotate" BOOLEAN DEFAULT false,
    "rotation_interval" TEXT,
    "last_rotation_at" TIMESTAMP(3),
    "key_rotation_at" TIMESTAMP(3),
    "deleted_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_by" TEXT,
    "deleted_by_api_key" TEXT,
    "embrouter_changed_by" TEXT,

    CONSTRAINT "EmbRouter_DeletedVerificationToken_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_EndUserTable" (
    "user_id" TEXT NOT NULL,
    "alias" TEXT,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "allowed_model_region" TEXT,
    "default_model" TEXT,
    "budget_id" TEXT,
    "object_permission_id" TEXT,
    "blocked" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "EmbRouter_EndUserTable_pkey" PRIMARY KEY ("user_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ModelAccessGroupBudgetTable" (
    "access_group_name" TEXT NOT NULL,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "budget_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ModelAccessGroupBudgetTable_pkey" PRIMARY KEY ("access_group_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_TagTable" (
    "tag_name" TEXT NOT NULL,
    "description" TEXT,
    "models" TEXT[],
    "model_info" JSONB,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "budget_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_TagTable_pkey" PRIMARY KEY ("tag_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_Config" (
    "param_name" TEXT NOT NULL,
    "param_value" JSONB,
    "last_run_at" TIMESTAMP(3),
    "reload_revision" BIGINT NOT NULL DEFAULT 0,

    CONSTRAINT "EmbRouter_Config_pkey" PRIMARY KEY ("param_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_SpendLogs" (
    "request_id" TEXT NOT NULL,
    "call_type" TEXT NOT NULL,
    "api_key" TEXT NOT NULL DEFAULT '',
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "total_tokens" INTEGER NOT NULL DEFAULT 0,
    "prompt_tokens" INTEGER NOT NULL DEFAULT 0,
    "completion_tokens" INTEGER NOT NULL DEFAULT 0,
    "startTime" TIMESTAMP(3) NOT NULL,
    "endTime" TIMESTAMP(3) NOT NULL,
    "request_duration_ms" INTEGER,
    "completionStartTime" TIMESTAMP(3),
    "model" TEXT NOT NULL DEFAULT '',
    "model_id" TEXT DEFAULT '',
    "model_group" TEXT DEFAULT '',
    "custom_llm_provider" TEXT DEFAULT '',
    "api_base" TEXT DEFAULT '',
    "user" TEXT DEFAULT '',
    "metadata" JSONB DEFAULT '{}',
    "cache_hit" TEXT DEFAULT '',
    "cache_key" TEXT DEFAULT '',
    "request_tags" JSONB DEFAULT '[]',
    "team_id" TEXT,
    "organization_id" TEXT,
    "end_user" TEXT,
    "requester_ip_address" TEXT,
    "messages" JSONB DEFAULT '{}',
    "response" JSONB DEFAULT '{}',
    "session_id" TEXT,
    "status" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "billing_agent_id" TEXT,
    "agent_id" TEXT,
    "proxy_server_request" JSONB DEFAULT '{}',
    "embrouter_call_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_SpendLogs_pkey" PRIMARY KEY ("request_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_BudgetWindowSpend" (
    "entity_type" TEXT NOT NULL,
    "entity_id" TEXT NOT NULL,
    "window_duration" TEXT NOT NULL,
    "window_start" TIMESTAMP(3) NOT NULL,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_BudgetWindowSpend_pkey" PRIMARY KEY ("entity_type","entity_id","window_duration")
);

-- CreateTable
CREATE TABLE "EmbRouter_ErrorLogs" (
    "request_id" TEXT NOT NULL,
    "startTime" TIMESTAMP(3) NOT NULL,
    "endTime" TIMESTAMP(3) NOT NULL,
    "api_base" TEXT NOT NULL DEFAULT '',
    "model_group" TEXT NOT NULL DEFAULT '',
    "embrouter_model_name" TEXT NOT NULL DEFAULT '',
    "model_id" TEXT NOT NULL DEFAULT '',
    "request_kwargs" JSONB NOT NULL DEFAULT '{}',
    "exception_type" TEXT NOT NULL DEFAULT '',
    "exception_string" TEXT NOT NULL DEFAULT '',
    "status_code" TEXT NOT NULL DEFAULT '',

    CONSTRAINT "EmbRouter_ErrorLogs_pkey" PRIMARY KEY ("request_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_UserNotifications" (
    "request_id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "models" TEXT[],
    "justification" TEXT NOT NULL,
    "status" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_UserNotifications_pkey" PRIMARY KEY ("request_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_TeamMembership" (
    "user_id" TEXT NOT NULL,
    "team_id" TEXT NOT NULL,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "total_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "budget_id" TEXT,

    CONSTRAINT "EmbRouter_TeamMembership_pkey" PRIMARY KEY ("user_id","team_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_OrganizationMembership" (
    "user_id" TEXT NOT NULL,
    "organization_id" TEXT NOT NULL,
    "user_role" TEXT,
    "spend" DOUBLE PRECISION DEFAULT 0.0,
    "budget_id" TEXT,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_OrganizationMembership_pkey" PRIMARY KEY ("user_id","organization_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_InvitationLink" (
    "id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "is_accepted" BOOLEAN NOT NULL DEFAULT false,
    "accepted_at" TIMESTAMP(3),
    "expires_at" TIMESTAMP(3) NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL,
    "created_by" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT NOT NULL,

    CONSTRAINT "EmbRouter_InvitationLink_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_AuditLog" (
    "id" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "changed_by" TEXT NOT NULL DEFAULT '',
    "changed_by_api_key" TEXT NOT NULL DEFAULT '',
    "action" TEXT NOT NULL,
    "table_name" TEXT NOT NULL,
    "object_id" TEXT NOT NULL,
    "before_value" JSONB,
    "updated_values" JSONB,

    CONSTRAINT "EmbRouter_AuditLog_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyUserSpend" (
    "id" TEXT NOT NULL,
    "user_id" TEXT,
    "date" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyUserSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyGlobalSpend" (
    "id" TEXT NOT NULL,
    "date" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyGlobalSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyOrganizationSpend" (
    "id" TEXT NOT NULL,
    "organization_id" TEXT,
    "date" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyOrganizationSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyEndUserSpend" (
    "id" TEXT NOT NULL,
    "end_user_id" TEXT,
    "date" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyEndUserSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyAgentSpend" (
    "id" TEXT NOT NULL,
    "agent_id" TEXT,
    "date" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyAgentSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyTeamSpend" (
    "id" TEXT NOT NULL,
    "team_id" TEXT,
    "date" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "ptu_flat_cost" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyTeamSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyTagSpend" (
    "id" TEXT NOT NULL,
    "request_id" TEXT,
    "tag" TEXT,
    "date" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "model" TEXT,
    "model_group" TEXT,
    "custom_llm_provider" TEXT,
    "mcp_namespaced_tool_name" TEXT,
    "endpoint" TEXT,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_read_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "cache_creation_input_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_saved_tokens" BIGINT NOT NULL DEFAULT 0,
    "compression_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "gateway_injected_caching_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "autorouter_savings_spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "api_requests" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "total_response_time_ms" BIGINT NOT NULL DEFAULT 0,
    "timed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyTagSpend_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ProxyWorkerHeartbeat" (
    "worker_id" TEXT NOT NULL,
    "hostname" TEXT NOT NULL,
    "started_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "last_heartbeat_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_ProxyWorkerHeartbeat_pkey" PRIMARY KEY ("worker_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_CronJob" (
    "cronjob_id" TEXT NOT NULL,
    "pod_id" TEXT NOT NULL,
    "status" "JobStatus" NOT NULL DEFAULT 'INACTIVE',
    "last_updated" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "ttl" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_CronJob_pkey" PRIMARY KEY ("cronjob_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ManagedFileTable" (
    "id" TEXT NOT NULL,
    "unified_file_id" TEXT NOT NULL,
    "file_object" JSONB,
    "model_mappings" JSONB NOT NULL,
    "flat_model_file_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "storage_backend" TEXT,
    "storage_url" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "team_id" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ManagedFileTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ManagedObjectTable" (
    "id" TEXT NOT NULL,
    "unified_object_id" TEXT NOT NULL,
    "model_object_id" TEXT NOT NULL,
    "file_object" JSONB NOT NULL,
    "file_purpose" TEXT NOT NULL,
    "status" TEXT,
    "batch_processed" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "team_id" TEXT,
    "org_id" TEXT,
    "api_key" TEXT,
    "request_tags" JSONB DEFAULT '[]',
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ManagedObjectTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ManagedFileContentTable" (
    "id" TEXT NOT NULL,
    "content" BYTEA NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_ManagedFileContentTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ManagedVectorStoreTable" (
    "id" TEXT NOT NULL,
    "unified_resource_id" TEXT NOT NULL,
    "resource_object" JSONB,
    "model_mappings" JSONB NOT NULL,
    "flat_model_resource_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "storage_backend" TEXT,
    "storage_url" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "team_id" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ManagedVectorStoreTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ManagedVectorStoresTable" (
    "vector_store_id" TEXT NOT NULL,
    "custom_llm_provider" TEXT NOT NULL,
    "vector_store_name" TEXT,
    "vector_store_description" TEXT,
    "vector_store_metadata" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "embrouter_credential_name" TEXT,
    "embrouter_params" JSONB,
    "team_id" TEXT,
    "user_id" TEXT,

    CONSTRAINT "EmbRouter_ManagedVectorStoresTable_pkey" PRIMARY KEY ("vector_store_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_GuardrailsTable" (
    "guardrail_id" TEXT NOT NULL,
    "guardrail_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "guardrail_info" JSONB,
    "team_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "status" TEXT NOT NULL DEFAULT 'active',
    "submitted_at" TIMESTAMP(3),
    "reviewed_at" TIMESTAMP(3),

    CONSTRAINT "EmbRouter_GuardrailsTable_pkey" PRIMARY KEY ("guardrail_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyGuardrailMetrics" (
    "guardrail_id" TEXT NOT NULL,
    "date" TEXT NOT NULL,
    "requests_evaluated" BIGINT NOT NULL DEFAULT 0,
    "passed_count" BIGINT NOT NULL DEFAULT 0,
    "blocked_count" BIGINT NOT NULL DEFAULT 0,
    "flagged_count" BIGINT NOT NULL DEFAULT 0,
    "avg_score" DOUBLE PRECISION,
    "avg_latency_ms" DOUBLE PRECISION,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyGuardrailMetrics_pkey" PRIMARY KEY ("guardrail_id","date")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyGuardrailUsageUnits" (
    "guardrail_id" TEXT NOT NULL,
    "date" TEXT NOT NULL,
    "team_id" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "usage_unit" TEXT NOT NULL,
    "units" BIGINT NOT NULL DEFAULT 0,
    "cost" DOUBLE PRECISION,
    "untracked_units" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyGuardrailUsageUnits_pkey" PRIMARY KEY ("guardrail_id","date","team_id","api_key","usage_unit")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyPolicyMetrics" (
    "policy_id" TEXT NOT NULL,
    "date" TEXT NOT NULL,
    "requests_evaluated" BIGINT NOT NULL DEFAULT 0,
    "passed_count" BIGINT NOT NULL DEFAULT 0,
    "blocked_count" BIGINT NOT NULL DEFAULT 0,
    "flagged_count" BIGINT NOT NULL DEFAULT 0,
    "avg_score" DOUBLE PRECISION,
    "avg_latency_ms" DOUBLE PRECISION,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyPolicyMetrics_pkey" PRIMARY KEY ("policy_id","date")
);

-- CreateTable
CREATE TABLE "EmbRouter_SpendLogGuardrailIndex" (
    "request_id" TEXT NOT NULL,
    "guardrail_id" TEXT NOT NULL,
    "policy_id" TEXT,
    "start_time" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_SpendLogGuardrailIndex_pkey" PRIMARY KEY ("request_id","guardrail_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_SpendLogToolIndex" (
    "request_id" TEXT NOT NULL,
    "tool_name" TEXT NOT NULL,
    "start_time" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_SpendLogToolIndex_pkey" PRIMARY KEY ("request_id","tool_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyToolSpend" (
    "date" TEXT NOT NULL,
    "tool_name" TEXT NOT NULL,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "total_tokens" BIGINT NOT NULL DEFAULT 0,
    "request_count" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyToolSpend_pkey" PRIMARY KEY ("date","tool_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyModelUsage" (
    "date" TEXT NOT NULL,
    "model_group" TEXT NOT NULL,
    "model" TEXT NOT NULL,
    "custom_llm_provider" TEXT NOT NULL,
    "task_type" TEXT NOT NULL,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    "prompt_tokens" BIGINT NOT NULL DEFAULT 0,
    "completion_tokens" BIGINT NOT NULL DEFAULT 0,
    "request_count" BIGINT NOT NULL DEFAULT 0,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyModelUsage_pkey" PRIMARY KEY ("date","model_group","model","custom_llm_provider","task_type")
);

-- CreateTable
CREATE TABLE "EmbRouter_DailyGatewayRequests" (
    "date" TEXT NOT NULL,
    "category" TEXT NOT NULL,
    "route" TEXT NOT NULL,
    "successful_requests" BIGINT NOT NULL DEFAULT 0,
    "failed_requests" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_DailyGatewayRequests_pkey" PRIMARY KEY ("date","category","route")
);

-- CreateTable
CREATE TABLE "EmbRouter_PromptTable" (
    "id" TEXT NOT NULL,
    "prompt_id" TEXT NOT NULL,
    "version" INTEGER NOT NULL DEFAULT 1,
    "environment" TEXT NOT NULL DEFAULT 'development',
    "created_by" TEXT,
    "embrouter_params" JSONB NOT NULL,
    "prompt_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_PromptTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_HealthCheckTable" (
    "health_check_id" TEXT NOT NULL,
    "model_name" TEXT NOT NULL,
    "model_id" TEXT,
    "status" TEXT NOT NULL,
    "healthy_count" INTEGER NOT NULL DEFAULT 0,
    "unhealthy_count" INTEGER NOT NULL DEFAULT 0,
    "error_message" TEXT,
    "response_time_ms" DOUBLE PRECISION,
    "details" JSONB,
    "checked_by" TEXT,
    "checked_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_HealthCheckTable_pkey" PRIMARY KEY ("health_check_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_SearchToolsTable" (
    "search_tool_id" TEXT NOT NULL,
    "search_tool_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "search_tool_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_SearchToolsTable_pkey" PRIMARY KEY ("search_tool_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_SSOConfig" (
    "id" TEXT NOT NULL DEFAULT 'sso_config',
    "sso_settings" JSONB NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_SSOConfig_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ManagedVectorStoreIndexTable" (
    "id" TEXT NOT NULL,
    "index_name" TEXT NOT NULL,
    "embrouter_params" JSONB NOT NULL,
    "index_info" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ManagedVectorStoreIndexTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_CacheConfig" (
    "id" TEXT NOT NULL DEFAULT 'cache_config',
    "cache_settings" JSONB NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_CacheConfig_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_UISettings" (
    "id" TEXT NOT NULL DEFAULT 'ui_settings',
    "ui_settings" JSONB NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_UISettings_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ConfigOverrides" (
    "config_type" TEXT NOT NULL,
    "config_value" JSONB NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "EmbRouter_ConfigOverrides_pkey" PRIMARY KEY ("config_type")
);

-- CreateTable
CREATE TABLE "EmbRouter_SkillsTable" (
    "skill_id" TEXT NOT NULL,
    "display_title" TEXT,
    "description" TEXT,
    "instructions" TEXT,
    "source" TEXT NOT NULL DEFAULT 'custom',
    "latest_version" TEXT,
    "file_content" BYTEA,
    "file_name" TEXT,
    "file_type" TEXT,
    "metadata" JSONB DEFAULT '{}',
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_SkillsTable_pkey" PRIMARY KEY ("skill_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_PolicyTable" (
    "policy_id" TEXT NOT NULL,
    "policy_name" TEXT NOT NULL,
    "version_number" INTEGER NOT NULL DEFAULT 1,
    "version_status" TEXT NOT NULL DEFAULT 'production',
    "parent_version_id" TEXT,
    "is_latest" BOOLEAN NOT NULL DEFAULT true,
    "published_at" TIMESTAMP(3),
    "production_at" TIMESTAMP(3),
    "inherit" TEXT,
    "description" TEXT,
    "guardrails_add" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "guardrails_remove" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "condition" JSONB DEFAULT '{}',
    "pipeline" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_PolicyTable_pkey" PRIMARY KEY ("policy_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_PolicyAttachmentTable" (
    "attachment_id" TEXT NOT NULL,
    "policy_name" TEXT NOT NULL,
    "scope" TEXT,
    "teams" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "keys" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "models" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "tags" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "priority" INTEGER,
    "is_default" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_PolicyAttachmentTable_pkey" PRIMARY KEY ("attachment_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ToolTable" (
    "tool_id" TEXT NOT NULL,
    "tool_name" TEXT NOT NULL,
    "origin" TEXT,
    "input_policy" TEXT NOT NULL DEFAULT 'untrusted',
    "output_policy" TEXT NOT NULL DEFAULT 'untrusted',
    "call_count" INTEGER NOT NULL DEFAULT 0,
    "assignments" JSONB DEFAULT '{}',
    "key_hash" TEXT,
    "team_id" TEXT,
    "key_alias" TEXT,
    "user_agent" TEXT,
    "last_used_at" TIMESTAMP(3),
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_ToolTable_pkey" PRIMARY KEY ("tool_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_AccessGroupTable" (
    "access_group_id" TEXT NOT NULL,
    "access_group_name" TEXT NOT NULL,
    "description" TEXT,
    "access_model_names" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_mcp_server_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "access_agent_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "assigned_team_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "assigned_key_ids" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_AccessGroupTable_pkey" PRIMARY KEY ("access_group_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ClaudeCodePluginTable" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "version" TEXT,
    "description" TEXT,
    "manifest_json" TEXT,
    "files_json" TEXT DEFAULT '{}',
    "enabled" BOOLEAN NOT NULL DEFAULT true,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,

    CONSTRAINT "EmbRouter_ClaudeCodePluginTable_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_MemoryTable" (
    "memory_id" TEXT NOT NULL,
    "key" TEXT NOT NULL,
    "value" TEXT NOT NULL,
    "metadata" JSONB,
    "user_id" TEXT,
    "team_id" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_by" TEXT,

    CONSTRAINT "EmbRouter_MemoryTable_pkey" PRIMARY KEY ("memory_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_AdaptiveRouterState" (
    "router_name" TEXT NOT NULL,
    "request_type" TEXT NOT NULL,
    "model_name" TEXT NOT NULL,
    "alpha" DOUBLE PRECISION NOT NULL,
    "beta" DOUBLE PRECISION NOT NULL,
    "total_samples" INTEGER NOT NULL DEFAULT 0,
    "last_updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_AdaptiveRouterState_pkey" PRIMARY KEY ("router_name","request_type","model_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_AdaptiveRouterSession" (
    "session_id" TEXT NOT NULL,
    "router_name" TEXT NOT NULL,
    "model_name" TEXT NOT NULL,
    "classified_type" TEXT NOT NULL,
    "misalignment_count" INTEGER NOT NULL DEFAULT 0,
    "stagnation_count" INTEGER NOT NULL DEFAULT 0,
    "disengagement_count" INTEGER NOT NULL DEFAULT 0,
    "satisfaction_count" INTEGER NOT NULL DEFAULT 0,
    "failure_count" INTEGER NOT NULL DEFAULT 0,
    "loop_count" INTEGER NOT NULL DEFAULT 0,
    "exhaustion_count" INTEGER NOT NULL DEFAULT 0,
    "last_user_content" TEXT,
    "last_assistant_content" TEXT,
    "tool_call_history" JSONB NOT NULL DEFAULT '[]',
    "pending_tool_calls" JSONB NOT NULL DEFAULT '{}',
    "turn_count" INTEGER NOT NULL DEFAULT 0,
    "last_processed_turn" INTEGER NOT NULL DEFAULT -1,
    "clean_credit_awarded" BOOLEAN NOT NULL DEFAULT false,
    "terminal_status" INTEGER,
    "last_activity_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_AdaptiveRouterSession_pkey" PRIMARY KEY ("session_id","router_name","model_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_AutoRouterBaselineComparison" (
    "scope" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "session_id" TEXT NOT NULL,
    "router_name" TEXT NOT NULL,
    "initial_equivalent" BOOLEAN NOT NULL,
    "revision" BIGINT NOT NULL DEFAULT 0,
    "published_revision" BIGINT NOT NULL DEFAULT 0,
    "history" TEXT,
    "attempted_at" TIMESTAMP(3),
    "retired" BOOLEAN NOT NULL DEFAULT false,
    "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_AutoRouterBaselineComparison_pkey" PRIMARY KEY ("scope")
);

-- CreateTable
CREATE TABLE "EmbRouter_AutoRouterBaselineObservation" (
    "request_id" TEXT NOT NULL,
    "scope" TEXT NOT NULL,
    "started_at" DOUBLE PRECISION NOT NULL,
    "revision" BIGINT NOT NULL,
    "data" TEXT NOT NULL,
    "publication" TEXT,
    "conflicted" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "EmbRouter_AutoRouterBaselineObservation_pkey" PRIMARY KEY ("request_id")
);

-- CreateTable
CREATE TABLE "EmbRouter_AutoRouterSession" (
    "api_key" TEXT NOT NULL,
    "session_id" TEXT NOT NULL,
    "router_name" TEXT NOT NULL,
    "router_type" TEXT NOT NULL,
    "first_turn_at" TIMESTAMP(3) NOT NULL,
    "last_turn_at" TIMESTAMP(3) NOT NULL,
    "last_model" TEXT NOT NULL,
    "models" JSONB NOT NULL DEFAULT '{}',
    "turns" INTEGER NOT NULL DEFAULT 0,
    "unordered_turns" INTEGER NOT NULL DEFAULT 0,
    "covered_turns" INTEGER NOT NULL DEFAULT 0,
    "cache_hits" INTEGER NOT NULL DEFAULT 0,
    "same_model_turns" INTEGER NOT NULL DEFAULT 0,
    "same_model_hits" INTEGER NOT NULL DEFAULT 0,
    "first_visit_turns" INTEGER NOT NULL DEFAULT 0,
    "first_visit_hits" INTEGER NOT NULL DEFAULT 0,
    "return_turns" INTEGER NOT NULL DEFAULT 0,
    "return_hits" INTEGER NOT NULL DEFAULT 0,
    "return_expired_misses" INTEGER NOT NULL DEFAULT 0,
    "return_within_ttl_misses" INTEGER NOT NULL DEFAULT 0,
    "ttl_5m_turns" INTEGER NOT NULL DEFAULT 0,
    "ttl_1h_turns" INTEGER NOT NULL DEFAULT 0,
    "total_tokens" BIGINT NOT NULL DEFAULT 0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "saved_spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "savings_estimated_turns" INTEGER NOT NULL DEFAULT 0,
    "savings_estimated_actual_spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "savings_estimated_saved_spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "savings_estimated_baseline_models" JSONB NOT NULL DEFAULT '{}',
    "classifier_cost" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "classifier_cost_recorded_turns" INTEGER NOT NULL DEFAULT 0,
    "tier_turns" JSONB NOT NULL DEFAULT '{}',
    "baseline_models" JSONB NOT NULL DEFAULT '{}',

    CONSTRAINT "EmbRouter_AutoRouterSession_pkey" PRIMARY KEY ("api_key","session_id","router_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_AutoRouterUserSession" (
    "user_id" TEXT NOT NULL,
    "api_key" TEXT NOT NULL,
    "session_id" TEXT NOT NULL,
    "router_name" TEXT NOT NULL,
    "router_type" TEXT NOT NULL,
    "first_turn_at" TIMESTAMP(3) NOT NULL,
    "last_turn_at" TIMESTAMP(3) NOT NULL,
    "last_model" TEXT NOT NULL,
    "models" JSONB NOT NULL DEFAULT '{}',
    "turns" INTEGER NOT NULL DEFAULT 0,
    "unordered_turns" INTEGER NOT NULL DEFAULT 0,
    "covered_turns" INTEGER NOT NULL DEFAULT 0,
    "cache_hits" INTEGER NOT NULL DEFAULT 0,
    "same_model_turns" INTEGER NOT NULL DEFAULT 0,
    "same_model_hits" INTEGER NOT NULL DEFAULT 0,
    "first_visit_turns" INTEGER NOT NULL DEFAULT 0,
    "first_visit_hits" INTEGER NOT NULL DEFAULT 0,
    "return_turns" INTEGER NOT NULL DEFAULT 0,
    "return_hits" INTEGER NOT NULL DEFAULT 0,
    "return_expired_misses" INTEGER NOT NULL DEFAULT 0,
    "return_within_ttl_misses" INTEGER NOT NULL DEFAULT 0,
    "ttl_5m_turns" INTEGER NOT NULL DEFAULT 0,
    "ttl_1h_turns" INTEGER NOT NULL DEFAULT 0,
    "total_tokens" BIGINT NOT NULL DEFAULT 0,
    "spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "saved_spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "savings_estimated_turns" INTEGER NOT NULL DEFAULT 0,
    "savings_estimated_actual_spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "savings_estimated_saved_spend" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "savings_estimated_baseline_models" JSONB NOT NULL DEFAULT '{}',
    "classifier_cost" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "classifier_cost_recorded_turns" INTEGER NOT NULL DEFAULT 0,
    "tier_turns" JSONB NOT NULL DEFAULT '{}',
    "baseline_models" JSONB NOT NULL DEFAULT '{}',

    CONSTRAINT "EmbRouter_AutoRouterUserSession_pkey" PRIMARY KEY ("user_id","api_key","session_id","router_name")
);

-- CreateTable
CREATE TABLE "EmbRouter_ShadowEvalJob" (
    "id" TEXT NOT NULL,
    "group_id" TEXT NOT NULL,
    "target_type" TEXT NOT NULL DEFAULT 'key',
    "target_id" TEXT NOT NULL,
    "router_name" TEXT NOT NULL,
    "router_names" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "models" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "direction" TEXT NOT NULL DEFAULT 'forward',
    "baseline_model" TEXT,
    "judge_model" TEXT NOT NULL,
    "shadow_percentage" DOUBLE PRECISION NOT NULL,
    "max_turns" INTEGER NOT NULL,
    "max_budget" DOUBLE PRECISION,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by" TEXT,
    "ends_at" TIMESTAMP(3) NOT NULL,
    "stopped_at" TIMESTAMP(3),
    "stopped_by" TEXT,

    CONSTRAINT "EmbRouter_ShadowEvalJob_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ShadowEvalAttempt" (
    "id" TEXT NOT NULL,
    "job_id" TEXT NOT NULL,
    "request_id" TEXT NOT NULL,
    "outcome" TEXT NOT NULL,
    "router_name" TEXT,
    "tier" TEXT,
    "real_model" TEXT,
    "shadow_model" TEXT,
    "confidence" DOUBLE PRECISION,
    "judge_cost" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "shadow_cost" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "real_cost" DOUBLE PRECISION,
    "real_classifier_cost" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "shadow_classifier_cost" DOUBLE PRECISION NOT NULL DEFAULT 0,
    "real_cache_hit" BOOLEAN NOT NULL DEFAULT false,
    "error" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "EmbRouter_ShadowEvalAttempt_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EmbRouter_ShadowEvalFunnel" (
    "job_id" TEXT NOT NULL,
    "not_sampled" INTEGER NOT NULL DEFAULT 0,
    "unjudgeable" INTEGER NOT NULL DEFAULT 0,
    "shed" INTEGER NOT NULL DEFAULT 0,
    "withheld" INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT "EmbRouter_ShadowEvalFunnel_pkey" PRIMARY KEY ("job_id")
);

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
CREATE UNIQUE INDEX "EmbRouter_CredentialsTable_credential_name_key" ON "EmbRouter_CredentialsTable"("credential_name");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_AgentsTable_agent_name_key" ON "EmbRouter_AgentsTable"("agent_name");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_AgentIdentity_provider_tenant_id_client_id_key" ON "EmbRouter_AgentIdentity"("provider", "tenant_id", "client_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_AgentIdentity_issuer_service_principal_id_key" ON "EmbRouter_AgentIdentity"("issuer", "service_principal_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_RetiredAgentIdentity_provider_tenant_id_client_id_key" ON "EmbRouter_RetiredAgentIdentity"("provider", "tenant_id", "client_id");

-- CreateIndex
CREATE INDEX "EmbRouter_VerifiedSubject_user_id_idx" ON "EmbRouter_VerifiedSubject"("user_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_VerifiedSubject_issuer_tenant_id_oid_key" ON "EmbRouter_VerifiedSubject"("issuer", "tenant_id", "oid");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_TeamTable_model_id_key" ON "EmbRouter_TeamTable"("model_id");

-- CreateIndex
CREATE INDEX "EmbRouter_TeamTable_organization_id_idx" ON "EmbRouter_TeamTable"("organization_id");

-- CreateIndex
CREATE INDEX "EmbRouter_TeamTable_team_alias_idx" ON "EmbRouter_TeamTable"("team_alias");

-- CreateIndex
CREATE INDEX "EmbRouter_TeamTable_created_at_idx" ON "EmbRouter_TeamTable"("created_at");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedTeamTable_team_id_idx" ON "EmbRouter_DeletedTeamTable"("team_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedTeamTable_deleted_at_idx" ON "EmbRouter_DeletedTeamTable"("deleted_at");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedTeamTable_organization_id_idx" ON "EmbRouter_DeletedTeamTable"("organization_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedTeamTable_team_alias_idx" ON "EmbRouter_DeletedTeamTable"("team_alias");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedTeamTable_created_at_idx" ON "EmbRouter_DeletedTeamTable"("created_at");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_UserTable_sso_user_id_key" ON "EmbRouter_UserTable"("sso_user_id");

-- CreateIndex
CREATE INDEX "EmbRouter_MCPServerTable_approval_status_idx" ON "EmbRouter_MCPServerTable"("approval_status");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_MCPToolsetTable_toolset_name_key" ON "EmbRouter_MCPToolsetTable"("toolset_name");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_MCPUserCredentials_user_id_server_id_key" ON "EmbRouter_MCPUserCredentials"("user_id", "server_id");

-- CreateIndex
CREATE INDEX "EmbRouter_MCPUserEnvVars_user_id_idx" ON "EmbRouter_MCPUserEnvVars"("user_id");

-- CreateIndex
CREATE INDEX "EmbRouter_MCPUserEnvVars_server_id_idx" ON "EmbRouter_MCPUserEnvVars"("server_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_MCPUserEnvVars_user_id_server_id_key" ON "EmbRouter_MCPUserEnvVars"("user_id", "server_id");

-- CreateIndex
CREATE INDEX "EmbRouter_VerificationToken_user_id_team_id_idx" ON "EmbRouter_VerificationToken"("user_id", "team_id");

-- CreateIndex
CREATE INDEX "EmbRouter_VerificationToken_team_id_idx" ON "EmbRouter_VerificationToken"("team_id");

-- CreateIndex
CREATE INDEX "EmbRouter_VerificationToken_budget_reset_at_expires_idx" ON "EmbRouter_VerificationToken"("budget_reset_at", "expires");

-- CreateIndex
CREATE INDEX "EmbRouter_JWTKeyMapping_jwt_issuer_jwt_claim_name_jwt_claim_idx" ON "EmbRouter_JWTKeyMapping"("jwt_issuer", "jwt_claim_name", "jwt_claim_value", "is_active");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_JWTKeyMapping_jwt_issuer_jwt_claim_name_jwt_claim_key" ON "EmbRouter_JWTKeyMapping"("jwt_issuer", "jwt_claim_name", "jwt_claim_value");

-- CreateIndex
CREATE INDEX "EmbRouter_DeprecatedVerificationToken_token_revoke_at_idx" ON "EmbRouter_DeprecatedVerificationToken"("token", "revoke_at");

-- CreateIndex
CREATE INDEX "EmbRouter_DeprecatedVerificationToken_revoke_at_idx" ON "EmbRouter_DeprecatedVerificationToken"("revoke_at");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DeprecatedVerificationToken_token_key" ON "EmbRouter_DeprecatedVerificationToken"("token");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_token_idx" ON "EmbRouter_DeletedVerificationToken"("token");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_deleted_at_idx" ON "EmbRouter_DeletedVerificationToken"("deleted_at");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_user_id_idx" ON "EmbRouter_DeletedVerificationToken"("user_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_team_id_idx" ON "EmbRouter_DeletedVerificationToken"("team_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_organization_id_idx" ON "EmbRouter_DeletedVerificationToken"("organization_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_key_alias_idx" ON "EmbRouter_DeletedVerificationToken"("key_alias");

-- CreateIndex
CREATE INDEX "EmbRouter_DeletedVerificationToken_created_at_idx" ON "EmbRouter_DeletedVerificationToken"("created_at");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogs_startTime_idx" ON "EmbRouter_SpendLogs"("startTime");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogs_startTime_request_id_idx" ON "EmbRouter_SpendLogs"("startTime", "request_id");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogs_end_user_idx" ON "EmbRouter_SpendLogs"("end_user");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogs_session_id_idx" ON "EmbRouter_SpendLogs"("session_id");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogs_embrouter_call_id_idx" ON "EmbRouter_SpendLogs"("embrouter_call_id");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogs_api_key_startTime_idx" ON "EmbRouter_SpendLogs"("api_key", "startTime");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_OrganizationMembership_user_id_organization_id_key" ON "EmbRouter_OrganizationMembership"("user_id", "organization_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyUserSpend_date_idx" ON "EmbRouter_DailyUserSpend"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyUserSpend_user_id_date_idx" ON "EmbRouter_DailyUserSpend"("user_id", "date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyUserSpend_api_key_idx" ON "EmbRouter_DailyUserSpend"("api_key");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyUserSpend_model_idx" ON "EmbRouter_DailyUserSpend"("model");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyUserSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyUserSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyUserSpend_endpoint_idx" ON "EmbRouter_DailyUserSpend"("endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyUserSpend_user_id_date_api_key_model_custom__key" ON "EmbRouter_DailyUserSpend"("user_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyGlobalSpend_date_idx" ON "EmbRouter_DailyGlobalSpend"("date");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyGlobalSpend_date_model_model_group_custom_ll_key" ON "EmbRouter_DailyGlobalSpend"("date", "model", "model_group", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyOrganizationSpend_date_idx" ON "EmbRouter_DailyOrganizationSpend"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyOrganizationSpend_organization_id_date_idx" ON "EmbRouter_DailyOrganizationSpend"("organization_id", "date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyOrganizationSpend_api_key_idx" ON "EmbRouter_DailyOrganizationSpend"("api_key");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyOrganizationSpend_model_idx" ON "EmbRouter_DailyOrganizationSpend"("model");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyOrganizationSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyOrganizationSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyOrganizationSpend_endpoint_idx" ON "EmbRouter_DailyOrganizationSpend"("endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyOrganizationSpend_organization_id_date_api_k_key" ON "EmbRouter_DailyOrganizationSpend"("organization_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyEndUserSpend_date_idx" ON "EmbRouter_DailyEndUserSpend"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyEndUserSpend_end_user_id_date_idx" ON "EmbRouter_DailyEndUserSpend"("end_user_id", "date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyEndUserSpend_api_key_idx" ON "EmbRouter_DailyEndUserSpend"("api_key");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyEndUserSpend_model_idx" ON "EmbRouter_DailyEndUserSpend"("model");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyEndUserSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyEndUserSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyEndUserSpend_endpoint_idx" ON "EmbRouter_DailyEndUserSpend"("endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyEndUserSpend_end_user_id_date_api_key_model__key" ON "EmbRouter_DailyEndUserSpend"("end_user_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyAgentSpend_date_idx" ON "EmbRouter_DailyAgentSpend"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyAgentSpend_agent_id_date_idx" ON "EmbRouter_DailyAgentSpend"("agent_id", "date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyAgentSpend_api_key_idx" ON "EmbRouter_DailyAgentSpend"("api_key");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyAgentSpend_model_idx" ON "EmbRouter_DailyAgentSpend"("model");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyAgentSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyAgentSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyAgentSpend_endpoint_idx" ON "EmbRouter_DailyAgentSpend"("endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyAgentSpend_agent_id_date_api_key_model_custo_key" ON "EmbRouter_DailyAgentSpend"("agent_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTeamSpend_date_idx" ON "EmbRouter_DailyTeamSpend"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTeamSpend_team_id_date_idx" ON "EmbRouter_DailyTeamSpend"("team_id", "date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTeamSpend_api_key_idx" ON "EmbRouter_DailyTeamSpend"("api_key");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTeamSpend_model_idx" ON "EmbRouter_DailyTeamSpend"("model");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTeamSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyTeamSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTeamSpend_endpoint_idx" ON "EmbRouter_DailyTeamSpend"("endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyTeamSpend_team_id_date_api_key_model_custom__key" ON "EmbRouter_DailyTeamSpend"("team_id", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTagSpend_date_idx" ON "EmbRouter_DailyTagSpend"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTagSpend_tag_date_idx" ON "EmbRouter_DailyTagSpend"("tag", "date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTagSpend_api_key_idx" ON "EmbRouter_DailyTagSpend"("api_key");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTagSpend_model_idx" ON "EmbRouter_DailyTagSpend"("model");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTagSpend_mcp_namespaced_tool_name_idx" ON "EmbRouter_DailyTagSpend"("mcp_namespaced_tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyTagSpend_endpoint_idx" ON "EmbRouter_DailyTagSpend"("endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_DailyTagSpend_tag_date_api_key_model_custom_llm_p_key" ON "EmbRouter_DailyTagSpend"("tag", "date", "api_key", "model", "custom_llm_provider", "mcp_namespaced_tool_name", "endpoint");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ManagedFileTable_unified_file_id_key" ON "EmbRouter_ManagedFileTable"("unified_file_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedFileTable_unified_file_id_idx" ON "EmbRouter_ManagedFileTable"("unified_file_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedFileTable_team_id_created_at_idx" ON "EmbRouter_ManagedFileTable"("team_id", "created_at" DESC);

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ManagedObjectTable_unified_object_id_key" ON "EmbRouter_ManagedObjectTable"("unified_object_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ManagedObjectTable_model_object_id_key" ON "EmbRouter_ManagedObjectTable"("model_object_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedObjectTable_unified_object_id_idx" ON "EmbRouter_ManagedObjectTable"("unified_object_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedObjectTable_model_object_id_idx" ON "EmbRouter_ManagedObjectTable"("model_object_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedObjectTable_team_id_created_at_idx" ON "EmbRouter_ManagedObjectTable"("team_id", "created_at" DESC);

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ManagedVectorStoreTable_unified_resource_id_key" ON "EmbRouter_ManagedVectorStoreTable"("unified_resource_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedVectorStoreTable_unified_resource_id_idx" ON "EmbRouter_ManagedVectorStoreTable"("unified_resource_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedVectorStoreTable_team_id_created_at_idx" ON "EmbRouter_ManagedVectorStoreTable"("team_id", "created_at" DESC);

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedVectorStoresTable_team_id_idx" ON "EmbRouter_ManagedVectorStoresTable"("team_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ManagedVectorStoresTable_user_id_idx" ON "EmbRouter_ManagedVectorStoresTable"("user_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_GuardrailsTable_guardrail_name_key" ON "EmbRouter_GuardrailsTable"("guardrail_name");

-- CreateIndex
CREATE INDEX "EmbRouter_GuardrailsTable_status_idx" ON "EmbRouter_GuardrailsTable"("status");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyGuardrailMetrics_date_idx" ON "EmbRouter_DailyGuardrailMetrics"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyGuardrailMetrics_guardrail_id_idx" ON "EmbRouter_DailyGuardrailMetrics"("guardrail_id");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyGuardrailUsageUnits_date_idx" ON "EmbRouter_DailyGuardrailUsageUnits"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyPolicyMetrics_date_idx" ON "EmbRouter_DailyPolicyMetrics"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyPolicyMetrics_policy_id_idx" ON "EmbRouter_DailyPolicyMetrics"("policy_id");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogGuardrailIndex_guardrail_id_start_time_idx" ON "EmbRouter_SpendLogGuardrailIndex"("guardrail_id", "start_time");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogGuardrailIndex_policy_id_start_time_idx" ON "EmbRouter_SpendLogGuardrailIndex"("policy_id", "start_time");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogToolIndex_tool_name_start_time_idx" ON "EmbRouter_SpendLogToolIndex"("tool_name", "start_time");

-- CreateIndex
CREATE INDEX "EmbRouter_SpendLogToolIndex_start_time_idx" ON "EmbRouter_SpendLogToolIndex"("start_time");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyModelUsage_date_idx" ON "EmbRouter_DailyModelUsage"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyModelUsage_model_group_idx" ON "EmbRouter_DailyModelUsage"("model_group");

-- CreateIndex
CREATE INDEX "EmbRouter_DailyGatewayRequests_date_idx" ON "EmbRouter_DailyGatewayRequests"("date");

-- CreateIndex
CREATE INDEX "EmbRouter_PromptTable_prompt_id_environment_idx" ON "EmbRouter_PromptTable"("prompt_id", "environment");

-- CreateIndex
CREATE INDEX "EmbRouter_PromptTable_prompt_id_idx" ON "EmbRouter_PromptTable"("prompt_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_PromptTable_prompt_id_version_environment_key" ON "EmbRouter_PromptTable"("prompt_id", "version", "environment");

-- CreateIndex
CREATE INDEX "EmbRouter_HealthCheckTable_model_name_idx" ON "EmbRouter_HealthCheckTable"("model_name");

-- CreateIndex
CREATE INDEX "EmbRouter_HealthCheckTable_checked_at_idx" ON "EmbRouter_HealthCheckTable"("checked_at");

-- CreateIndex
CREATE INDEX "EmbRouter_HealthCheckTable_status_idx" ON "EmbRouter_HealthCheckTable"("status");

-- CreateIndex
CREATE INDEX "EmbRouter_HealthCheckTable_model_id_model_name_checked_at_idx" ON "EmbRouter_HealthCheckTable"("model_id", "model_name", "checked_at" DESC);

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_SearchToolsTable_search_tool_name_key" ON "EmbRouter_SearchToolsTable"("search_tool_name");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ManagedVectorStoreIndexTable_index_name_key" ON "EmbRouter_ManagedVectorStoreIndexTable"("index_name");

-- CreateIndex
CREATE INDEX "EmbRouter_PolicyTable_policy_name_version_status_idx" ON "EmbRouter_PolicyTable"("policy_name", "version_status");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_PolicyTable_policy_name_version_number_key" ON "EmbRouter_PolicyTable"("policy_name", "version_number");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ToolTable_tool_name_key" ON "EmbRouter_ToolTable"("tool_name");

-- CreateIndex
CREATE INDEX "EmbRouter_ToolTable_input_policy_idx" ON "EmbRouter_ToolTable"("input_policy");

-- CreateIndex
CREATE INDEX "EmbRouter_ToolTable_output_policy_idx" ON "EmbRouter_ToolTable"("output_policy");

-- CreateIndex
CREATE INDEX "EmbRouter_ToolTable_team_id_idx" ON "EmbRouter_ToolTable"("team_id");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_AccessGroupTable_access_group_name_key" ON "EmbRouter_AccessGroupTable"("access_group_name");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_ClaudeCodePluginTable_name_key" ON "EmbRouter_ClaudeCodePluginTable"("name");

-- CreateIndex
CREATE UNIQUE INDEX "EmbRouter_MemoryTable_key_key" ON "EmbRouter_MemoryTable"("key");

-- CreateIndex
CREATE INDEX "EmbRouter_MemoryTable_user_id_idx" ON "EmbRouter_MemoryTable"("user_id");

-- CreateIndex
CREATE INDEX "EmbRouter_MemoryTable_team_id_idx" ON "EmbRouter_MemoryTable"("team_id");

-- CreateIndex
CREATE INDEX "idx_adaptive_router_session_activity" ON "EmbRouter_AdaptiveRouterSession"("last_activity_at");

-- CreateIndex
CREATE INDEX "idx_autorouter_baseline_scope" ON "EmbRouter_AutoRouterBaselineComparison"("api_key", "session_id", "router_name");

-- CreateIndex
CREATE INDEX "idx_autorouter_baseline_updated" ON "EmbRouter_AutoRouterBaselineComparison"("updated_at");

-- CreateIndex
CREATE INDEX "idx_autorouter_baseline_event_order" ON "EmbRouter_AutoRouterBaselineObservation"("scope", "started_at", "request_id");

-- CreateIndex
CREATE INDEX "idx_autorouter_baseline_event_revision" ON "EmbRouter_AutoRouterBaselineObservation"("scope", "revision", "started_at");

-- CreateIndex
CREATE INDEX "idx_autorouter_session_last_turn" ON "EmbRouter_AutoRouterSession"("last_turn_at");

-- CreateIndex
CREATE INDEX "idx_autorouter_user_session_last_turn" ON "EmbRouter_AutoRouterUserSession"("last_turn_at");

-- CreateIndex
CREATE INDEX "idx_autorouter_user_session_user_last_turn" ON "EmbRouter_AutoRouterUserSession"("user_id", "last_turn_at");

-- CreateIndex
CREATE INDEX "EmbRouter_ShadowEvalJob_group_id_idx" ON "EmbRouter_ShadowEvalJob"("group_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ShadowEvalJob_target_type_target_id_idx" ON "EmbRouter_ShadowEvalJob"("target_type", "target_id");

-- CreateIndex
CREATE INDEX "EmbRouter_ShadowEvalJob_created_at_idx" ON "EmbRouter_ShadowEvalJob"("created_at");

-- CreateIndex
CREATE INDEX "EmbRouter_ShadowEvalAttempt_job_id_idx" ON "EmbRouter_ShadowEvalAttempt"("job_id");

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
ALTER TABLE "EmbRouter_AgentsTable" ADD CONSTRAINT "EmbRouter_AgentsTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_AgentIdentity" ADD CONSTRAINT "EmbRouter_AgentIdentity_agent_id_fkey" FOREIGN KEY ("agent_id") REFERENCES "EmbRouter_AgentsTable"("agent_id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_RetiredAgentIdentity" ADD CONSTRAINT "EmbRouter_RetiredAgentIdentity_agent_id_fkey" FOREIGN KEY ("agent_id") REFERENCES "EmbRouter_AgentsTable"("agent_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_VerifiedSubject" ADD CONSTRAINT "EmbRouter_VerifiedSubject_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "EmbRouter_UserTable"("user_id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_OrganizationTable" ADD CONSTRAINT "EmbRouter_OrganizationTable_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_OrganizationTable" ADD CONSTRAINT "EmbRouter_OrganizationTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_TeamTable" ADD CONSTRAINT "EmbRouter_TeamTable_organization_id_fkey" FOREIGN KEY ("organization_id") REFERENCES "EmbRouter_OrganizationTable"("organization_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_TeamTable" ADD CONSTRAINT "EmbRouter_TeamTable_model_id_fkey" FOREIGN KEY ("model_id") REFERENCES "EmbRouter_ModelTable"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_TeamTable" ADD CONSTRAINT "EmbRouter_TeamTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_ProjectTable" ADD CONSTRAINT "EmbRouter_ProjectTable_team_id_fkey" FOREIGN KEY ("team_id") REFERENCES "EmbRouter_TeamTable"("team_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_ProjectTable" ADD CONSTRAINT "EmbRouter_ProjectTable_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_ProjectTable" ADD CONSTRAINT "EmbRouter_ProjectTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_UserTable" ADD CONSTRAINT "EmbRouter_UserTable_organization_id_fkey" FOREIGN KEY ("organization_id") REFERENCES "EmbRouter_OrganizationTable"("organization_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_UserTable" ADD CONSTRAINT "EmbRouter_UserTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_VerificationToken" ADD CONSTRAINT "EmbRouter_VerificationToken_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_VerificationToken" ADD CONSTRAINT "EmbRouter_VerificationToken_organization_id_fkey" FOREIGN KEY ("organization_id") REFERENCES "EmbRouter_OrganizationTable"("organization_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_VerificationToken" ADD CONSTRAINT "EmbRouter_VerificationToken_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "EmbRouter_ProjectTable"("project_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_VerificationToken" ADD CONSTRAINT "EmbRouter_VerificationToken_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_JWTKeyMapping" ADD CONSTRAINT "EmbRouter_JWTKeyMapping_token_fkey" FOREIGN KEY ("token") REFERENCES "EmbRouter_VerificationToken"("token") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_EndUserTable" ADD CONSTRAINT "EmbRouter_EndUserTable_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_EndUserTable" ADD CONSTRAINT "EmbRouter_EndUserTable_object_permission_id_fkey" FOREIGN KEY ("object_permission_id") REFERENCES "EmbRouter_ObjectPermissionTable"("object_permission_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_ModelAccessGroupBudgetTable" ADD CONSTRAINT "EmbRouter_ModelAccessGroupBudgetTable_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_TagTable" ADD CONSTRAINT "EmbRouter_TagTable_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_TeamMembership" ADD CONSTRAINT "EmbRouter_TeamMembership_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_OrganizationMembership" ADD CONSTRAINT "EmbRouter_OrganizationMembership_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "EmbRouter_UserTable"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_OrganizationMembership" ADD CONSTRAINT "EmbRouter_OrganizationMembership_organization_id_fkey" FOREIGN KEY ("organization_id") REFERENCES "EmbRouter_OrganizationTable"("organization_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_OrganizationMembership" ADD CONSTRAINT "EmbRouter_OrganizationMembership_budget_id_fkey" FOREIGN KEY ("budget_id") REFERENCES "EmbRouter_BudgetTable"("budget_id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_InvitationLink" ADD CONSTRAINT "EmbRouter_InvitationLink_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "EmbRouter_UserTable"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_InvitationLink" ADD CONSTRAINT "EmbRouter_InvitationLink_created_by_fkey" FOREIGN KEY ("created_by") REFERENCES "EmbRouter_UserTable"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_InvitationLink" ADD CONSTRAINT "EmbRouter_InvitationLink_updated_by_fkey" FOREIGN KEY ("updated_by") REFERENCES "EmbRouter_UserTable"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_WorkflowEvent" ADD CONSTRAINT "EmbRouter_WorkflowEvent_run_id_fkey" FOREIGN KEY ("run_id") REFERENCES "EmbRouter_WorkflowRun"("run_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "EmbRouter_WorkflowMessage" ADD CONSTRAINT "EmbRouter_WorkflowMessage_run_id_fkey" FOREIGN KEY ("run_id") REFERENCES "EmbRouter_WorkflowRun"("run_id") ON DELETE RESTRICT ON UPDATE CASCADE;


-- Not expressible in schema.prisma; carried over by hand from the pre-squash migrations.

-- ShadowEvalJob arrays are NOT NULL (20260901000000_shadow_eval_multi_router, 20260904000000_shadow_eval_model_scope)
ALTER TABLE "EmbRouter_ShadowEvalJob" ALTER COLUMN "router_names" SET NOT NULL;
ALTER TABLE "EmbRouter_ShadowEvalJob" ALTER COLUMN "models" SET NOT NULL;

-- Case-insensitive email lookups (20260108_add_user_email_lower_idx)
CREATE INDEX "EmbRouter_UserTable_user_email_lower_idx" ON "EmbRouter_UserTable"(LOWER("user_email"));

-- One active shadow eval per target and direction (20260831000000_shadow_eval_typed_targets)
CREATE UNIQUE INDEX "EmbRouter_ShadowEvalJob_one_active_per_target_direction"
    ON "EmbRouter_ShadowEvalJob"("target_type", "target_id", "direction") WHERE "stopped_at" IS NULL;

-- Baseline comparisons waiting to be published (20260915010000_add_autorouter_baseline_state)
CREATE INDEX "idx_autorouter_baseline_dirty"
    ON "EmbRouter_AutoRouterBaselineComparison" ("attempted_at", "updated_at", "scope")
    WHERE NOT "retired" AND "revision" <> "published_revision";
