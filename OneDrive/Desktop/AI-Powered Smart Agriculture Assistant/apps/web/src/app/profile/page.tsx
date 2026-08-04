import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function ProfilePage() {
  return (
    <div className="flex flex-col gap-6 max-w-2xl">
      <h1 className="text-3xl font-bold">Profile</h1>
      <Card>
        <CardHeader><CardTitle>Personal Information</CardTitle></CardHeader>
        <CardContent>Form fields for name, contact, etc...</CardContent>
      </Card>
      <Card>
        <CardHeader><CardTitle>Farm Information</CardTitle></CardHeader>
        <CardContent>Form fields for location, size, crops...</CardContent>
      </Card>
    </div>
  );
}
