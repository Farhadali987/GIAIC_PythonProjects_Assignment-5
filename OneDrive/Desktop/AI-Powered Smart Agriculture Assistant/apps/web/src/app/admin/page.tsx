import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function AdminPage() {
  return (
    <div className="flex flex-col gap-6">
      <h1 className="text-3xl font-bold">Admin Panel</h1>
      
      <div className="grid md:grid-cols-3 gap-6">
        <Card>
          <CardHeader><CardTitle>Total Users</CardTitle></CardHeader>
          <CardContent><div className="text-2xl font-bold">1,234</div></CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Disease Reports</CardTitle></CardHeader>
          <CardContent><div className="text-2xl font-bold">89</div></CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>System Health</CardTitle></CardHeader>
          <CardContent><div className="text-2xl font-bold">Excellent</div></CardContent>
        </Card>
      </div>
    </div>
  );
}
