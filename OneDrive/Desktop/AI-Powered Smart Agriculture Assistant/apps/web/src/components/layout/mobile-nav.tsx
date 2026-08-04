"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, Camera, MessageSquare, CloudSun, Mic } from "lucide-react";
import { cn } from "@/lib/utils";

const mobileLinks = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { name: "Scanner", href: "/scanner", icon: Camera },
  { name: "AI Chat", href: "/assistant", icon: MessageSquare },
  { name: "Weather", href: "/weather", icon: CloudSun },
  { name: "Voice", href: "/voice", icon: Mic },
];

export function MobileNav() {
  const pathname = usePathname();

  return (
    <nav className="fixed bottom-0 left-0 z-40 flex h-16 w-full items-center justify-around border-t bg-background md:hidden">
      {mobileLinks.map((link) => {
        const Icon = link.icon;
        const isActive = pathname === link.href;
        return (
          <Link
            key={link.name}
            href={link.href}
            className={cn(
              "flex flex-col items-center justify-center gap-1 text-xs font-medium transition-colors hover:text-primary",
              isActive ? "text-primary" : "text-muted-foreground"
            )}
          >
            <Icon className="h-5 w-5" />
            {link.name}
          </Link>
        );
      })}
    </nav>
  );
}
