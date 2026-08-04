import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { CloudSun, Sprout, Activity, AlertTriangle } from 'lucide-react';

export const WeatherCard = () => (
  <Card>
    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
      <CardTitle className="text-sm font-medium">Weather</CardTitle>
      <CloudSun className="h-4 w-4 text-muted-foreground" />
    </CardHeader>
    <CardContent>
      <div className="text-2xl font-bold">28°C</div>
      <p className="text-xs text-muted-foreground">Sunny - 10% Rain chance</p>
    </CardContent>
  </Card>
);

export const FarmOverview = () => (
  <Card>
    <CardHeader>
      <CardTitle>Farm Overview</CardTitle>
    </CardHeader>
    <CardContent>
      <div className="text-3xl font-bold">45 Acres</div>
      <p className="text-sm text-muted-foreground">All crops healthy</p>
    </CardContent>
  </Card>
);
