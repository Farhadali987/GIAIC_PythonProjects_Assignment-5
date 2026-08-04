import React from "react";
import Link from "next/link";
import { Card, CardHeader, CardTitle } from "@/components/ui/card";

const crops = [
  { id: "wheat", name: "Wheat" },
  { id: "rice", name: "Rice" },
  { id: "cotton", name: "Cotton" },
  { id: "sugarcane", name: "Sugarcane" },
  { id: "maize", name: "Maize" },
];

export default function CropGuidePage() {
  return (
    <div className="flex flex-col gap-6">
      <h1 className="text-3xl font-bold">Crop Guide</h1>
      <div className="grid md:grid-cols-3 lg:grid-cols-4 gap-6">
        {crops.map((crop) => (
          <Link key={crop.id} href={`/crop-guide/${crop.id}`}>
            <Card className="hover:border-primary transition-colors">
              <CardHeader>
                <CardTitle>{crop.name}</CardTitle>
              </CardHeader>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
