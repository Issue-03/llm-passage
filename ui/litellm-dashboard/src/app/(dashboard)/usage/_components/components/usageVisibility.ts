// Usage page pieces hidden from the EmbRouter UI for now. Set a flag to true to bring it back.
export const USAGE_PAGE_VISIBILITY = {
  /** "MCP Server Activity" tab (MCP Servers is hidden from the sidebar). */
  mcpServerActivity: false,
  /** "Ask AI" button and its chat panel. */
  askAi: false,
  /** "Usage View" picker. Hidden, so the page always shows Global Usage (a non-admin's own usage). */
  viewSelect: false,
  /** Cost / Model Activity / Key Activity / Endpoint Activity tab strip. Hidden, so only Cost shows. */
  activityTabs: false,
  /** Spend by Provider "Show Zero Spend" / "Show Unknown" toggles. Hidden, so both stay off. */
  providerFilterToggles: false,
} as const;

/** "Usage View" options hidden from the picker; delete an entry to bring the view back. */
export const HIDDEN_USAGE_VIEWS: ReadonlySet<string> = new Set([
  "organization", // Organizations page is hidden
  "agent", // Agents / A2A are hidden
  "customer", // the Customers page is hidden
  "user-agent-activity",
]);
