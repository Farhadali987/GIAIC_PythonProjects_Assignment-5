"use client";

import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Camera, Upload, Loader2, ImageIcon } from "lucide-react";
import { motion } from "framer-motion";

export default function ScannerPage() {
  const [image, setImage] = useState<string | null>(null);
  const [isScanning, setIsScanning] = useState(false);
  const [result, setResult] = useState<string | null>(null);

  const handleScan = () => {
    setIsScanning(true);
    setResult(null);
    setTimeout(() => {
      setIsScanning(false);
      setResult("Healthy crop detected.");
    }, 3000);
  };

  return (
    <div className="flex flex-col gap-6 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold">Disease Scanner</h1>
      <Card>
        <CardHeader>
          <CardTitle>Upload or Capture Image</CardTitle>
        </CardHeader>
        <CardContent className="flex flex-col gap-4">
          <div className="border-2 border-dashed rounded-lg p-10 flex flex-col items-center justify-center gap-4 text-muted-foreground">
            {image ? (
              <img src={image} alt="Preview" className="max-h-64 rounded-md" />
            ) : (
              <>
                <Upload className="h-10 w-10" />
                <p>Drag & drop or click to upload</p>
                <Button variant="outline"><Camera className="mr-2 h-4 w-4" /> Camera</Button>
              </>
            )}
          </div>
          <Button onClick={handleScan} disabled={!image || isScanning}>
            {isScanning ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : "Scan Crop"}
          </Button>
          {result && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="p-4 bg-primary/10 rounded-md">
              <p className="font-semibold">{result}</p>
            </motion.div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
