"""
Passthrough table repositories.

Each repository centralizes access to a single Prisma table behind a ``table``
property, making the repository the one place that names the underlying table.
These are thin wrappers for tables that do not (yet) need domain-specific query
methods; richer repositories live in their own modules.
"""

from typing import TYPE_CHECKING, Any, Final, Generic

from embrouter.proxy.common_utils.config_sync_pubsub import wrap_table_actions_for_config_sync
from embrouter.repositories.prisma_protocols import RowT_co, TableActions

if TYPE_CHECKING:
    from prisma import models as prisma_models  # noqa: F401  # used by quoted base-class subscripts


class PrismaTableRepository(Generic[RowT_co]):
    """Base for repositories that expose a single Prisma table."""

    table_name: str

    def __init__(self, prisma_client: object, *, use_writer: bool = False) -> None:
        self._prisma_client = prisma_client
        self._use_writer = use_writer

    @property
    def prisma_client(self) -> Any:
        if self._prisma_client is None:
            raise RuntimeError("No DB Connected.")
        return self._prisma_client

    @property
    def table(self) -> TableActions[RowT_co]:
        actions: Final[TableActions[RowT_co]] = getattr(
            self.prisma_client.writer_db if self._use_writer else self.prisma_client.db, self.table_name
        )
        return wrap_table_actions_for_config_sync(actions=actions, table_name=self.table_name)


class PolicyRepository(PrismaTableRepository["prisma_models.EmbRouter_PolicyTable"]):
    table_name = "embrouter_policytable"


class AgentsRepository(PrismaTableRepository["prisma_models.EmbRouter_AgentsTable"]):
    table_name = "embrouter_agentstable"


class AgentIdentityRepository(PrismaTableRepository["prisma_models.EmbRouter_AgentIdentity"]):
    table_name = "embrouter_agentidentity"


class RetiredAgentIdentityRepository(PrismaTableRepository["prisma_models.EmbRouter_RetiredAgentIdentity"]):
    table_name = "embrouter_retiredagentidentity"


class VerifiedSubjectRepository(PrismaTableRepository["prisma_models.EmbRouter_VerifiedSubject"]):
    table_name = "embrouter_verifiedsubject"


class ObjectPermissionRepository(PrismaTableRepository["prisma_models.EmbRouter_ObjectPermissionTable"]):
    table_name = "embrouter_objectpermissiontable"


class GuardrailsRepository(PrismaTableRepository["prisma_models.EmbRouter_GuardrailsTable"]):
    table_name = "embrouter_guardrailstable"


class MCPServerRepository(PrismaTableRepository["prisma_models.EmbRouter_MCPServerTable"]):
    table_name = "embrouter_mcpservertable"


class ManagedObjectRepository(PrismaTableRepository["prisma_models.EmbRouter_ManagedObjectTable"]):
    table_name = "embrouter_managedobjecttable"


class OrganizationMembershipRepository(PrismaTableRepository["prisma_models.EmbRouter_OrganizationMembership"]):
    table_name = "embrouter_organizationmembership"


class SpendLogsRepository(PrismaTableRepository["prisma_models.EmbRouter_SpendLogs"]):
    table_name = "embrouter_spendlogs"


class BudgetWindowSpendRepository(PrismaTableRepository["prisma_models.EmbRouter_BudgetWindowSpend"]):
    table_name = "embrouter_budgetwindowspend"


class ClaudeCodePluginRepository(PrismaTableRepository["prisma_models.EmbRouter_ClaudeCodePluginTable"]):
    table_name = "embrouter_claudecodeplugintable"


class TeamMembershipRepository(PrismaTableRepository["prisma_models.EmbRouter_TeamMembership"]):
    table_name = "embrouter_teammembership"


class EndUserRepository(PrismaTableRepository["prisma_models.EmbRouter_EndUserTable"]):
    table_name = "embrouter_endusertable"


class ManagedVectorStoresRepository(PrismaTableRepository["prisma_models.EmbRouter_ManagedVectorStoresTable"]):
    table_name = "embrouter_managedvectorstorestable"


class MCPUserCredentialsRepository(PrismaTableRepository["prisma_models.EmbRouter_MCPUserCredentials"]):
    table_name = "embrouter_mcpusercredentials"


class MCPServerOAuthClientRepository(PrismaTableRepository["prisma_models.EmbRouter_MCPServerOAuthClient"]):
    table_name = "embrouter_mcpserveroauthclient"


class PromptRepository(PrismaTableRepository["prisma_models.EmbRouter_PromptTable"]):
    table_name = "embrouter_prompttable"


class TagRepository(PrismaTableRepository["prisma_models.EmbRouter_TagTable"]):
    table_name = "embrouter_tagtable"


class ModelAccessGroupBudgetRepository(PrismaTableRepository["prisma_models.EmbRouter_ModelAccessGroupBudgetTable"]):
    table_name = "embrouter_modelaccessgroupbudgettable"


class InvitationLinkRepository(PrismaTableRepository["prisma_models.EmbRouter_InvitationLink"]):
    table_name = "embrouter_invitationlink"


class JWTKeyMappingRepository(PrismaTableRepository["prisma_models.EmbRouter_JWTKeyMapping"]):
    table_name = "embrouter_jwtkeymapping"


class ManagedFileRepository(PrismaTableRepository["prisma_models.EmbRouter_ManagedFileTable"]):
    table_name = "embrouter_managedfiletable"


class MemoryRepository(PrismaTableRepository["prisma_models.EmbRouter_MemoryTable"]):
    table_name = "embrouter_memorytable"


class SearchToolsRepository(PrismaTableRepository["prisma_models.EmbRouter_SearchToolsTable"]):
    table_name = "embrouter_searchtoolstable"


class ConfigOverridesRepository(PrismaTableRepository["prisma_models.EmbRouter_ConfigOverrides"]):
    table_name = "embrouter_configoverrides"


class MCPToolsetRepository(PrismaTableRepository["prisma_models.EmbRouter_MCPToolsetTable"]):
    table_name = "embrouter_mcptoolsettable"


class ToolRepository(PrismaTableRepository["prisma_models.EmbRouter_ToolTable"]):
    table_name = "embrouter_tooltable"


class DeletedVerificationTokenRepository(PrismaTableRepository["prisma_models.EmbRouter_DeletedVerificationToken"]):
    table_name = "embrouter_deletedverificationtoken"


class WorkflowRunRepository(PrismaTableRepository["prisma_models.EmbRouter_WorkflowRun"]):
    table_name = "embrouter_workflowrun"


class ModelTableRepository(PrismaTableRepository["prisma_models.EmbRouter_ModelTable"]):
    table_name = "embrouter_modeltable"


class AccessGroupRepository(PrismaTableRepository["prisma_models.EmbRouter_AccessGroupTable"]):
    table_name = "embrouter_accessgrouptable"


class SSOConfigRepository(PrismaTableRepository["prisma_models.EmbRouter_SSOConfig"]):
    table_name = "embrouter_ssoconfig"


class UISettingsRepository(PrismaTableRepository["prisma_models.EmbRouter_UISettings"]):
    table_name = "embrouter_uisettings"


class DailyGuardrailMetricsRepository(PrismaTableRepository["prisma_models.EmbRouter_DailyGuardrailMetrics"]):
    table_name = "embrouter_dailyguardrailmetrics"


class DailyGuardrailUsageUnitsRepository(PrismaTableRepository["prisma_models.EmbRouter_DailyGuardrailUsageUnits"]):
    table_name = "embrouter_dailyguardrailusageunits"


class PolicyAttachmentRepository(PrismaTableRepository["prisma_models.EmbRouter_PolicyAttachmentTable"]):
    table_name = "embrouter_policyattachmenttable"


class TeamRepository(PrismaTableRepository["prisma_models.EmbRouter_TeamTable"]):
    table_name = "embrouter_teamtable"


class DeletedTeamRepository(PrismaTableRepository["prisma_models.EmbRouter_DeletedTeamTable"]):
    table_name = "embrouter_deletedteamtable"


class SkillsRepository(PrismaTableRepository["prisma_models.EmbRouter_SkillsTable"]):
    table_name = "embrouter_skillstable"


class CacheConfigRepository(PrismaTableRepository["prisma_models.EmbRouter_CacheConfig"]):
    table_name = "embrouter_cacheconfig"


class ManagedVectorStoreIndexRepository(PrismaTableRepository["prisma_models.EmbRouter_ManagedVectorStoreIndexTable"]):
    table_name = "embrouter_managedvectorstoreindextable"


class WorkflowMessageRepository(PrismaTableRepository["prisma_models.EmbRouter_WorkflowMessage"]):
    table_name = "embrouter_workflowmessage"


class DailyTagSpendRepository(PrismaTableRepository["prisma_models.EmbRouter_DailyTagSpend"]):
    table_name = "embrouter_dailytagspend"


class SpendLogToolIndexRepository(PrismaTableRepository["prisma_models.EmbRouter_SpendLogToolIndex"]):
    table_name = "embrouter_spendlogtoolindex"


class DailyToolSpendRepository(PrismaTableRepository["prisma_models.EmbRouter_DailyToolSpend"]):
    table_name = "embrouter_dailytoolspend"


class DailyModelUsageRepository(PrismaTableRepository["prisma_models.EmbRouter_DailyModelUsage"]):
    table_name = "embrouter_dailymodelusage"


class SpendLogGuardrailIndexRepository(PrismaTableRepository["prisma_models.EmbRouter_SpendLogGuardrailIndex"]):
    table_name = "embrouter_spendlogguardrailindex"


class UserNotificationsRepository(PrismaTableRepository["prisma_models.EmbRouter_UserNotifications"]):
    table_name = "embrouter_usernotifications"


class HealthCheckRepository(PrismaTableRepository["prisma_models.EmbRouter_HealthCheckTable"]):
    table_name = "embrouter_healthchecktable"


class DeprecatedVerificationTokenRepository(PrismaTableRepository["prisma_models.EmbRouter_DeprecatedVerificationToken"]):
    table_name = "embrouter_deprecatedverificationtoken"


class WorkflowEventRepository(PrismaTableRepository["prisma_models.EmbRouter_WorkflowEvent"]):
    table_name = "embrouter_workflowevent"


class DailyPolicyMetricsRepository(PrismaTableRepository["prisma_models.EmbRouter_DailyPolicyMetrics"]):
    table_name = "embrouter_dailypolicymetrics"


class AdaptiveRouterStateRepository(PrismaTableRepository["prisma_models.EmbRouter_AdaptiveRouterState"]):
    table_name = "embrouter_adaptiverouterstate"


class AuditLogRepository(PrismaTableRepository["prisma_models.EmbRouter_AuditLog"]):
    table_name = "embrouter_auditlog"


class AdaptiveRouterSessionRepository(PrismaTableRepository["prisma_models.EmbRouter_AdaptiveRouterSession"]):
    table_name = "embrouter_adaptiveroutersession"


class RetiredAgentRepository(PrismaTableRepository["prisma_models.EmbRouter_RetiredAgent"]):
    table_name = "embrouter_retiredagent"
