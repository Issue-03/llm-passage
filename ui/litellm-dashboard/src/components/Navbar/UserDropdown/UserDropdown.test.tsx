import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { renderWithProviders, screen, waitFor } from "../../../../tests/test-utils";
import UserDropdown from "./UserDropdown";

let mockUseAuthorizedImpl: () => {
  userId: string | null;
  userEmail: string | null;
  userRoleLabel: string;
  premiumUser: boolean;
  loginMethod?: string | null;
} = () => ({
  userId: "test-user-id",
  userEmail: "test@example.com",
  userRoleLabel: "Admin",
  premiumUser: false,
});

const mockRouterPush = vi.fn();

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: mockRouterPush }),
}));

vi.mock("@/app/(dashboard)/hooks/useAuthorized", () => ({
  default: () => mockUseAuthorizedImpl(),
}));

describe("UserDropdown", () => {
  const mockOnLogout = vi.fn();

  const getAccountTrigger = () => screen.getByRole("button", { name: /account menu/i });

  beforeEach(() => {
    vi.clearAllMocks();
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
    });
  });

  it("should render", () => {
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);
    expect(getAccountTrigger()).toBeInTheDocument();
  });

  it("should surface initials and account menu affordance", () => {
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);
    expect(getAccountTrigger()).toBeInTheDocument();
    expect(screen.getByText("TE")).toBeInTheDocument();
  });

  it("should show user email when dropdown is opened", async () => {
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      expect(screen.getAllByText("test@example.com").length).toBeGreaterThan(0);
    });
  });

  it("should show user ID when dropdown is opened", async () => {
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      expect(screen.getByText("test-user-id")).toBeInTheDocument();
    });
  });

  it("should show user role when dropdown is opened", async () => {
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      expect(screen.getAllByText("Admin").length).toBeGreaterThan(0);
    });
  });

  it("shows no tier badge or preference switches", async () => {
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    expect(await screen.findByTestId("user-dropdown-panel")).toBeInTheDocument();
    expect(screen.queryByText("Standard")).not.toBeInTheDocument();
    expect(screen.queryByText("Premium")).not.toBeInTheDocument();
    expect(screen.queryByRole("switch")).not.toBeInTheDocument();
  });

  it("should call onLogout when logout is clicked", async () => {
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      expect(screen.getAllByText("test@example.com").length).toBeGreaterThan(0);
    });

    await user.click(screen.getByText("Logout"));

    expect(mockOnLogout).toHaveBeenCalledTimes(1);
  });

  it("should navigate to the change-password page for username/password sessions", async () => {
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
      loginMethod: "username_password",
    });
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await user.click(await screen.findByText("Change Password"));

    expect(mockRouterPush).toHaveBeenCalledWith(expect.stringContaining("change-password"));
  });

  it("should hide the change-password entry for SSO sessions", async () => {
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
      loginMethod: "sso",
    });
    const user = userEvent.setup();
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      expect(screen.getAllByText("test@example.com").length).toBeGreaterThan(0);
    });

    expect(screen.queryByText("Change Password")).not.toBeInTheDocument();
  });

  it("should show Account in the trigger when user id is the default placeholder", () => {
    mockUseAuthorizedImpl = () => ({
      userId: "default_user_id",
      userEmail: null as any,
      userRoleLabel: "Admin",
      premiumUser: false,
    });
    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);
    expect(screen.getByText("Account")).toBeInTheDocument();
  });

  it("should display dash when user email is not available", async () => {
    const user = userEvent.setup();
    mockUseAuthorizedImpl = () => ({
      userId: "test-user-id",
      userEmail: null as any,
      userRoleLabel: "Admin",
      premiumUser: false,
    });

    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      expect(screen.getByText("-")).toBeInTheDocument();
    });
  });

  it("should display dash when user ID is not available", async () => {
    const user = userEvent.setup();
    mockUseAuthorizedImpl = () => ({
      userId: null as any,
      userEmail: "test@example.com",
      userRoleLabel: "Admin",
      premiumUser: false,
    });

    renderWithProviders(<UserDropdown onLogout={mockOnLogout} />);

    await user.click(getAccountTrigger());

    await waitFor(() => {
      const dashElements = screen.getAllByText("-");
      expect(dashElements.length).toBeGreaterThan(0);
    });
  });

});
