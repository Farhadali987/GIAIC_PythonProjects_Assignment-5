import React from 'react';
import { WeatherCard, FarmOverview } from '@/components/dashboard/widgets';

export default function DashboardPage() {
  return (
    <div className="flex flex-col gap-6">
      <h1 className="text-3xl font-bold">Dashboard</h1>
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <WeatherCard />
        <FarmOverview />
        {/* Add more widgets here */}
      </div>
    </div>
  );
}
