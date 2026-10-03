import { afterEach, describe, expect, it, vi } from "vitest";
import { act, fireEvent, render, screen } from "@testing-library/react";
import { DashboardHeader } from "./DashboardHeader";

const { mockUsePluginMode, mockUseUISettings, state } = vi.hoisted(() => {
  const state = {
    plugins: [] as { name: string; display_name: string; url: string }[],
    enableChatUI: false,
    pathname: "/ui/logs",
  };
  return {
    state,
    mockUsePluginMode: vi.fn(() => ({ mode: "ai-gateway", setMode: vi.fn(), plugins: state.plugins })),
    mockUseUISettings: vi.fn(() => ({ data: { values: { enable_chat_ui: state.enableChatUI } } })),
  };
});

vi.mock("@/contexts/PluginModeContext", () => ({ usePluginMode: mockUsePluginMode }));
vi.mock("@/app/(dashboard)/hooks/uiSettings/useUISettings", () => ({ useUISettings: mockUseUISettings }));
vi.mock("next/navigation", () => ({ usePathname: () => state.pathname }));
vi.mock("@/hooks/useWorker", () => ({ useWorker: () => ({ isControlPlane: false, selectedWorker: null }) }));
vi.mock("@/components/Navbar/WorkerDropdown/WorkerDropdown", () => ({ default: () => null }));

describe("DashboardHeader breadcrumb", () => {
  afterEach(() => {
    state.plugins = [];
    state.enableChatUI = false;
    state.pathname = "/ui/logs";
  });

  it("titles the breadcrumb from the current route, not from a sidebar page id", () => {
    state.pathname = "/ui/models-and-endpoints";
    render(<DashboardHeader />);

    expect(screen.getByText("Models + Endpoints")).toBeInTheDocument();
  });

  it("titles the dashboard root as Virtual Keys", () => {
    state.pathname = "/ui/";
    render(<DashboardHeader />);

    expect(screen.getByText("Virtual Keys")).toBeInTheDocument();
  });

  it("roots the breadcrumb in the AI Gateway selector (with a Chat option) and drops the static section crumb when the selector is available", async () => {
    state.enableChatUI = true;
    render(<DashboardHeader showViewSwitcher />);

    expect(screen.getByText("Logs")).toBeInTheDocument();
    expect(screen.queryByText("Observability")).not.toBeInTheDocument();

    const selector = screen.getByRole("button", { name: /AI Gateway/i });
    act(() => {
      fireEvent.click(selector);
    });
    expect(await screen.findByText("Chat")).toBeInTheDocument();
  });

  it("keeps the AI Gateway selector at the root even when there is nothing to switch to (discovery)", () => {
    render(<DashboardHeader showViewSwitcher />);

    expect(screen.getByRole("button", { name: /AI Gateway/i })).toBeInTheDocument();
    expect(screen.getByText("Logs")).toBeInTheDocument();
    expect(screen.queryByText("Observability")).not.toBeInTheDocument();
  });

  it("hides the AI Gateway app switcher by default and shows only the page title", () => {
    state.enableChatUI = true;
    render(<DashboardHeader />);

    expect(screen.getByText("Logs")).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /AI Gateway/i })).not.toBeInTheDocument();
  });

  it("leaves docs, blog, community links and notifications out of the toolbar", () => {
    const { container } = render(<DashboardHeader />);

    expect(screen.queryByRole("link", { name: "Docs" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /blog/i })).not.toBeInTheDocument();
    expect(screen.queryByRole("group", { name: "Community links" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Notifications" })).not.toBeInTheDocument();
    expect(container.querySelectorAll('[data-slot="separator"][data-orientation="vertical"]')).toHaveLength(0);
  });
});
