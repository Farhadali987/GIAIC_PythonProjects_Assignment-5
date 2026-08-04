"use client";

import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Send, Mic, Paperclip, MessageSquare } from "lucide-react";

export default function AssistantPage() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! How can I help with your farm today?" },
  ]);

  return (
    <div className="flex h-[calc(100vh-8rem)] gap-4">
      {/* Sidebar - Chat History */}
      <Card className="w-64 p-4 hidden md:flex flex-col gap-2">
        <h2 className="font-semibold mb-4">Conversations</h2>
        <Button variant="ghost" className="justify-start"><MessageSquare className="mr-2 h-4 w-4" />Crop Health</Button>
      </Card>
      
      {/* Main Chat Window */}
      <Card className="flex-1 flex flex-col p-4">
        <div className="flex-1 overflow-y-auto mb-4 space-y-4">
          {messages.map((m, i) => (
            <div key={i} className={`p-3 rounded-lg ${m.role === 'assistant' ? 'bg-muted' : 'bg-primary text-primary-foreground self-end'}`}>
              {m.content}
            </div>
          ))}
        </div>
        <div className="flex gap-2">
          <Button variant="ghost" size="icon"><Paperclip className="h-5 w-5" /></Button>
          <input className="flex-1 rounded-md border p-2" placeholder="Ask about farming..." />
          <Button variant="ghost" size="icon"><Mic className="h-5 w-5" /></Button>
          <Button><Send className="h-4 w-4" /></Button>
        </div>
      </Card>
    </div>
  );
}
