"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, Camera, MessageSquare, CloudSun, BookOpen, BarChart3, Mic, User, Settings, ShieldAlert } from "lucide-react";
import { cn } from "@/lib/utils"; // Assuming utils exist, or I might need to create them.

const sidebarLinks = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { name: "Disease Scanner", href: "/scanner", icon: Camera },
  { name: "AI Assistant", href: "/assistant", icon: MessageSquare },
  { name: "Weather", href: "/weather", icon: CloudSun },
  { name: "Crop Guide", href: "/crop-guide", icon: BookOpen },
  { name: "Market Prices", href: "/market", icon: BarChart3 },
  { name: "Voice Assistant", href: "/voice", icon: Mic },
  { name: "Profile", href: "/profile", icon: User },
  { name: "Settings", href: "/settings", icon: Settings },
  { name: "Admin", href: "/admin", icon: ShieldAlert },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="hidden h-screen w-64 flex-col border-r bg-background md:flex">
      <div className="flex h-16 items-center border-b px-6">
        <Link href="/" className="font-bold text-primary">KisanAI</Link>
      </div>
      <nav aria-label="Main Navigation" className="flex-1 overflow-y-auto p-4 space-y-1">
        {sidebarLinks.map((link) => {
          const Icon = link.icon;
          const isActive = pathname === link.href;
          return (
            <Link
              key={link.name}
              href={link.href}
              className={cn(
                "flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition-colors hover:bg-muted",
                isActive ? "bg-muted text-primary" : "text-muted-foreground"
              )}
            >
              <Icon className="h-4 w-4" />
              {link.name}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}
