import React from "react";

export default function CropDetailPage({ params }: { params: { id: string } }) {
  const { id } = React.use(params);
  
  return (
    <div className="flex flex-col gap-6">
      <h1 className="text-3xl font-bold capitalize">{id} Guide</h1>
      <p className="text-muted-foreground">Detailed agricultural guide for {id}...</p>
    </div>
  );
}
