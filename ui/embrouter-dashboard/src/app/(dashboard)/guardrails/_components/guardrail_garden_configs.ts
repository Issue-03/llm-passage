export interface GuardrailPreset {
  provider: string;
  categoryName?: string;
  guardrailNameSuggestion: string;
  mode: string;
  defaultOn: boolean;
}

export const GUARDRAIL_PRESETS: Record<string, GuardrailPreset> = {
  // ── EmbRouter Content Filter: Content Categories ──
  cf_denied_financial: {
    provider: "EmbrouterContentFilter",
    categoryName: "denied_financial_advice",
    guardrailNameSuggestion: "Denied Financial Advice",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_denied_legal: {
    provider: "EmbrouterContentFilter",
    categoryName: "denied_legal_advice",
    guardrailNameSuggestion: "Denied Legal Advice",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_denied_medical: {
    provider: "EmbrouterContentFilter",
    categoryName: "denied_medical_advice",
    guardrailNameSuggestion: "Denied Medical Advice",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_denied_insults: {
    provider: "EmbrouterContentFilter",
    categoryName: "denied_insults",
    guardrailNameSuggestion: "Insults & Personal Attacks",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_harmful_violence: {
    provider: "EmbrouterContentFilter",
    categoryName: "harmful_violence",
    guardrailNameSuggestion: "Harmful Violence",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_harmful_self_harm: {
    provider: "EmbrouterContentFilter",
    categoryName: "harmful_self_harm",
    guardrailNameSuggestion: "Harmful Self-Harm",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_harmful_child_safety: {
    provider: "EmbrouterContentFilter",
    categoryName: "harmful_child_safety",
    guardrailNameSuggestion: "Harmful Child Safety",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_harmful_illegal_weapons: {
    provider: "EmbrouterContentFilter",
    categoryName: "harmful_illegal_weapons",
    guardrailNameSuggestion: "Harmful Illegal Weapons",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_bias_gender: {
    provider: "EmbrouterContentFilter",
    categoryName: "bias_gender",
    guardrailNameSuggestion: "Bias: Gender",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_bias_racial: {
    provider: "EmbrouterContentFilter",
    categoryName: "bias_racial",
    guardrailNameSuggestion: "Bias: Racial",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_bias_religious: {
    provider: "EmbrouterContentFilter",
    categoryName: "bias_religious",
    guardrailNameSuggestion: "Bias: Religious",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_bias_sexual_orientation: {
    provider: "EmbrouterContentFilter",
    categoryName: "bias_sexual_orientation",
    guardrailNameSuggestion: "Bias: Sexual Orientation",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_prompt_injection_jailbreak: {
    provider: "EmbrouterContentFilter",
    categoryName: "prompt_injection_jailbreak",
    guardrailNameSuggestion: "Prompt Injection: Jailbreak",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_prompt_injection_data_exfil: {
    provider: "EmbrouterContentFilter",
    categoryName: "prompt_injection_data_exfiltration",
    guardrailNameSuggestion: "Prompt Injection: Data Exfiltration",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_prompt_injection_sql: {
    provider: "EmbrouterContentFilter",
    categoryName: "prompt_injection_sql",
    guardrailNameSuggestion: "Prompt Injection: SQL",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_prompt_injection_malicious_code: {
    provider: "EmbrouterContentFilter",
    categoryName: "prompt_injection_malicious_code",
    guardrailNameSuggestion: "Prompt Injection: Malicious Code",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_prompt_injection_system_prompt: {
    provider: "EmbrouterContentFilter",
    categoryName: "prompt_injection_system_prompt",
    guardrailNameSuggestion: "Prompt Injection: System Prompt",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_toxic_abuse: {
    provider: "EmbrouterContentFilter",
    categoryName: "harm_toxic_abuse",
    guardrailNameSuggestion: "Toxic & Abusive Language",
    mode: "pre_call",
    defaultOn: false,
  },

  // ── EmbRouter Content Filter: Patterns & Keywords (no category) ──
  cf_patterns: {
    provider: "EmbrouterContentFilter",
    guardrailNameSuggestion: "Pattern Matching",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_keywords: {
    provider: "EmbrouterContentFilter",
    guardrailNameSuggestion: "Keyword Blocking",
    mode: "pre_call",
    defaultOn: false,
  },
  block_code_execution: {
    provider: "BlockCodeExecution",
    guardrailNameSuggestion: "Block Code Execution",
    mode: "pre_call",
    defaultOn: false,
  },
  cf_competitor_intent: {
    provider: "EmbrouterContentFilter",
    guardrailNameSuggestion: "Competitor Name Blocking",
    mode: "pre_call",
    defaultOn: false,
  },

  // ── Partner Guardrails ──
  presidio: {
    provider: "PresidioPII",
    guardrailNameSuggestion: "Presidio PII",
    mode: "pre_call",
    defaultOn: false,
  },
  bedrock: {
    provider: "Bedrock",
    guardrailNameSuggestion: "Bedrock Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  lakera: {
    provider: "Lakera",
    guardrailNameSuggestion: "Lakera",
    mode: "pre_call",
    defaultOn: false,
  },
  openai_moderation: {
    provider: "OpenaiModeration",
    guardrailNameSuggestion: "OpenAI Moderation",
    mode: "pre_call",
    defaultOn: false,
  },
  google_model_armor: {
    provider: "ModelArmor",
    guardrailNameSuggestion: "Google Cloud Model Armor",
    mode: "pre_call",
    defaultOn: false,
  },
  guardrails_ai: {
    provider: "GuardrailsAi",
    guardrailNameSuggestion: "Guardrails AI",
    mode: "pre_call",
    defaultOn: false,
  },
  zscaler: {
    provider: "ZscalerAiGuard",
    guardrailNameSuggestion: "Zscaler AI Guard",
    mode: "pre_call",
    defaultOn: false,
  },
  panw: {
    provider: "PanwPrismaAirs",
    guardrailNameSuggestion: "PANW Prisma AIRS",
    mode: "pre_call",
    defaultOn: false,
  },
  cisco_ai_defense: {
    provider: "CiscoAiDefense",
    guardrailNameSuggestion: "Cisco AI Defense",
    mode: "pre_call",
    defaultOn: false,
  },
  noma: {
    provider: "Noma",
    guardrailNameSuggestion: "Noma Security",
    mode: "pre_call",
    defaultOn: false,
  },
  aporia: {
    provider: "AporiaAi",
    guardrailNameSuggestion: "Aporia AI",
    mode: "pre_call",
    defaultOn: false,
  },
  aim: {
    provider: "Aim",
    guardrailNameSuggestion: "AIM Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  cato_networks: {
    provider: "Cato Networks",
    guardrailNameSuggestion: "Cato Networks Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  prompt_security: {
    provider: "PromptSecurity",
    guardrailNameSuggestion: "Prompt Security",
    mode: "pre_call",
    defaultOn: false,
  },
  lasso: {
    provider: "Lasso",
    guardrailNameSuggestion: "Lasso Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  pangea: {
    provider: "Pangea",
    guardrailNameSuggestion: "Pangea Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  enkryptai: {
    provider: "Enkryptai",
    guardrailNameSuggestion: "EnkryptAI",
    mode: "pre_call",
    defaultOn: false,
  },
  javelin: {
    provider: "Javelin",
    guardrailNameSuggestion: "Javelin Guardrails",
    mode: "pre_call",
    defaultOn: false,
  },
  pillar: {
    provider: "Pillar",
    guardrailNameSuggestion: "Pillar Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  akto: {
    provider: "Akto",
    guardrailNameSuggestion: "Akto Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  promptguard: {
    provider: "Promptguard",
    guardrailNameSuggestion: "PromptGuard",
    mode: "pre_call",
    defaultOn: false,
  },
  xecguard: {
    provider: "Xecguard",
    guardrailNameSuggestion: "XecGuard",
    mode: "pre_call",
    defaultOn: false,
  },
  deepkeep: {
    provider: "Deepkeep",
    guardrailNameSuggestion: "DeepKeep AI Firewall",
    mode: "pre_call",
    defaultOn: false,
  },
  repelloai: {
    provider: "Repelloai",
    guardrailNameSuggestion: "RepelloAI Argus",
    mode: "pre_call",
    defaultOn: false,
  },
  straiker: {
    provider: "Straiker",
    guardrailNameSuggestion: "Straiker Guardrail",
    mode: "pre_call",
    defaultOn: false,
  },
  alice: {
    provider: "Alice",
    guardrailNameSuggestion: "Alice",
    mode: "pre_call",
    defaultOn: false,
  },
  agent_365: {
    provider: "Agent365",
    guardrailNameSuggestion: "Microsoft Agent 365 Guardrail",
    mode: "pre_mcp_call",
    // MCP-only: default_on is the only activation path on the MCP hook
    defaultOn: true,
  },
  conduct: {
    provider: "Conduct",
    guardrailNameSuggestion: "Conduct Guard",
    mode: "pre_call",
    defaultOn: false,
  },
};
