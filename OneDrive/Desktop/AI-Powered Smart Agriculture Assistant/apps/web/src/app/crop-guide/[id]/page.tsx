import React from "react";

export default async function CropDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  return (
    <div className="flex flex-col gap-6">
      <h1 className="text-3xl font-bold capitalize">{id} Guide</h1>
      <p className="text-muted-foreground">Detailed agricultural guide for {id}...</p>
    </div>
  );
}
