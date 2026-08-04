"use client";

import React, { useState } from "react";
import { Mic } from "lucide-react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";

export default function VoicePage() {
  const [isListening, setIsListening] = useState(false);

  return (
    <div className="flex flex-col items-center justify-center h-[calc(100vh-8rem)] gap-8">
      <h1 className="text-3xl font-bold">Voice Assistant</h1>
      
      <motion.div 
        animate={{ scale: isListening ? 1.2 : 1 }}
        className="rounded-full bg-primary/20 p-10 cursor-pointer"
        onClick={() => setIsListening(!isListening)}
      >
        <Mic className="h-16 w-16 text-primary" />
      </motion.div>
      
      <p className="text-lg text-muted-foreground">
        {isListening ? "Listening..." : "Tap to speak"}
      </p>
    </div>
  );
}
