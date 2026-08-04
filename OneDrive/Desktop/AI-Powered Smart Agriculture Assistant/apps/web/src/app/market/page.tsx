import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function MarketPage() {
  return (
    <div className="flex flex-col gap-6">
      <h1 className="text-3xl font-bold">Market Prices</h1>
      
      <div className="grid md:grid-cols-3 gap-6">
        <Card>
          <CardHeader><CardTitle>Price Trends</CardTitle></CardHeader>
          <CardContent className="h-48 flex items-center justify-center text-muted-foreground bg-muted rounded-md">
            Chart Placeholder
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Top Crops</CardTitle></CardHeader>
          <CardContent>List of crops...</CardContent>
        </Card>
      </div>
    </div>
  );
}
