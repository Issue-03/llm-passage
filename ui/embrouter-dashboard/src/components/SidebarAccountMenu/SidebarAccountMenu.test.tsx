import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { renderWithProviders, screen, waitFor } from "../../../tests/test-utils";
import SidebarAccountMenu from "./SidebarAccountMenu";

interface AuthMock {
  userId: string | null;
  userEmail: string | null;
  userRoleLabel: string;
  premiumUser: boolean;
  accessToken: string;
  loginMethod?: string | null;
}

let mockUseAuthorizedImpl: () => AuthMock = () => ({
  userId: "test-user-id",
  userEmail: "test@example.com",
  userRoleLabel: "Admin",
  premiumUser: false,
  accessToken: "test-token",
});

const mockRouterPush = vi.fn();

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: mockRouterPush }),
}));

vi.mock("@/app/(dashboard)/hooks/useAuthorized", () => ({
  default: () => mockUseAuthorizedImpl(),
}));

describe("SidebarAccountMenu", () => {
  const mockOnLogout = vi.fn();

  const getAccountTrigger = () => screen.getByRole("button", { name: /account menu/i });

  const openMenu = async (user: ReturnType<typeof userEvent.setup>) => {
    await user.click(getAccountTrigger());
    await waitFor(() => {
      expect(screen.getByTestId("sidebar-account-menu-panel")).toBeInTheDocument();
    });
  };

  beforeEach(() => {
    vi.clearAllMocks();
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
      accessToken: "test-token",
    });
  });

  it("should render the account trigger with initials", () => {
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);
    expect(getAccountTrigger()).toBeInTheDocument();
    expect(screen.getByText("TE")).toBeInTheDocument();
  });

  it("should render only the avatar (no name/role) when collapsed", () => {
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} collapsed />);
    expect(getAccountTrigger()).toBeInTheDocument();
    expect(screen.getByText("TE")).toBeInTheDocument();
    expect(screen.queryByText("Admin")).not.toBeInTheDocument();
    expect(screen.queryByText("test@example.com")).not.toBeInTheDocument();
  });

  it("shows a compact name trigger in the header placement", () => {
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} placement="header" />);
    expect(getAccountTrigger()).toBeInTheDocument();
    expect(screen.getByText("TE")).toBeInTheDocument();
    expect(screen.queryByText("Admin")).not.toBeInTheDocument();
  });

  it("should show email, user ID, and role when the menu is opened", async () => {
    const user = userEvent.setup();
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);

    await openMenu(user);

    expect(screen.getAllByText("test@example.com").length).toBeGreaterThan(0);
    expect(screen.getByText("test-user-id")).toBeInTheDocument();
    expect(screen.getAllByText("Admin").length).toBeGreaterThan(0);
  });

  it("shows no tier, version, decoration or preference switches", async () => {
    const user = userEvent.setup();
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);

    await openMenu(user);

    expect(screen.queryByText("Tier")).not.toBeInTheDocument();
    expect(screen.queryByText(/^v\d/)).not.toBeInTheDocument();
    expect(screen.queryByText("🌴")).not.toBeInTheDocument();
    expect(screen.queryByRole("switch")).not.toBeInTheDocument();
  });

  it("wires the email row to the shared copy button", async () => {
    const user = userEvent.setup();
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.defineProperty(navigator, "clipboard", { value: { writeText }, configurable: true });

    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);
    await openMenu(user);

    const copyButton = screen.getByRole("button", { name: "Copy email" });
    await user.click(copyButton);

    expect(writeText).toHaveBeenCalledWith("test@example.com");
    await waitFor(() => expect(copyButton.querySelector(".lucide-check")).toBeInTheDocument());
  });

  it("should call onLogout when logout is clicked", async () => {
    const user = userEvent.setup();
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);

    await openMenu(user);

    await user.click(screen.getByRole("button", { name: /logout/i }));

    expect(mockOnLogout).toHaveBeenCalledTimes(1);
  });

  it("should navigate to the change-password page for username/password sessions", async () => {
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
      accessToken: "test-token",
      loginMethod: "username_password",
    });
    const user = userEvent.setup();
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);

    await openMenu(user);

    await user.click(screen.getByRole("button", { name: /change password/i }));

    expect(mockRouterPush).toHaveBeenCalledWith(expect.stringContaining("change-password"));
  });

  it("should hide the change-password entry for SSO sessions", async () => {
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
      accessToken: "test-token",
      loginMethod: "sso",
    });
    const user = userEvent.setup();
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);

    await openMenu(user);

    expect(screen.queryByRole("button", { name: /change password/i })).not.toBeInTheDocument();
  });

  it("should show Account in the trigger for the default placeholder user id", () => {
    mockUseAuthorizedImpl = () => ({
      userId: "default_user_id",
      userEmail: null,
      userRoleLabel: "Admin",
      premiumUser: false,
      accessToken: "test-token",
    });
    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);
    expect(screen.getByText("Account")).toBeInTheDocument();
  });

  it("should display a dash when email is unavailable", async () => {
    const user = userEvent.setup();
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: null,
      userRoleLabel: "Admin",
      premiumUser: false,
      accessToken: "test-token",
    });

    renderWithProviders(<SidebarAccountMenu onLogout={mockOnLogout} />);

    await openMenu(user);

    expect(screen.getByText("-")).toBeInTheDocument();
  });
});
