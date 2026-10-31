// Login page pieces hidden from the EmbRouter UI for now. Set a flag to true to bring it back.
export const LOGIN_PAGE_VISIBILITY = {
  /** The "Login with SSO" button. */
  ssoButton: false,
  /** The "Default Credentials" info card (admin / MASTER_KEY hint and docs link). */
  defaultCredentialsHint: false,
} as const;
