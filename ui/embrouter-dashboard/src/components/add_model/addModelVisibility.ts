// Add Model fields hidden from the EmbRouter UI for now. Set a flag to true to bring the field back.
export const ADD_MODEL_FIELD_VISIBILITY = {
  /** "Team-BYOK Model" switch: needs a LiteLLM Enterprise licence (premiumUser), so it can never be turned on here. */
  teamByokSwitch: false,
  /** "Attached Knowledge Bases (RAG)": the Vector Stores page is hidden, so there is nothing to pick. */
  knowledgeBases: false,
  /** Advanced Settings "Guardrails": the Guardrails page is hidden. */
  guardrails: false,
} as const;
