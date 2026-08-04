"use client";

import React from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ArrowRight, Leaf, ShieldCheck, Zap, Users } from "lucide-react";

export default function Home() {
  const features = [
    { title: "Smart Disease Detection", icon: ShieldCheck, desc: "AI-powered scanner for instant crop health diagnosis." },
    { title: "Real-time Weather Insights", icon: CloudSun, desc: "Hyper-local weather forecasts and agricultural planning." },
    { title: "Yield Optimization", icon: Zap, desc: "Data-driven recommendations for maximum production." },
    { title: "Community Connection", icon: Users, desc: "Collaborate with experts and fellow farmers." },
  ];

  return (
    <div className="flex flex-col gap-20 pb-20">
      {/* Hero Section */}
      <motion.section
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="flex flex-col items-center justify-center text-center pt-20"
      >
        <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6">
          Cultivating the Future with <span className="text-primary">KisanAI</span>
        </h1>
        <p className="text-xl text-muted-foreground max-w-2xl mb-10">
          Your AI-powered assistant for sustainable, intelligent, and profitable farming.
        </p>
        <div className="flex gap-4">
          <Button size="lg" className="rounded-full px-8 text-lg">Get Started</Button>
          <Button size="lg" variant="outline" className="rounded-full px-8 text-lg">Learn More</Button>
        </div>
      </motion.section>

      {/* Features Section */}
      <section className="container">
        <h2 className="text-3xl font-bold text-center mb-12">Empowering Your Farm</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, i) => {
            const Icon = feature.icon;
            return (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                viewport={{ once: true }}
              >
                <Card className="h-full hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <div className="mb-4 rounded-full bg-primary/10 w-12 h-12 flex items-center justify-center">
                      <Icon className="text-primary h-6 w-6" />
                    </div>
                    <CardTitle>{feature.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground">{feature.desc}</p>
                  </CardContent>
                </Card>
              </motion.div>
            );
          })}
        </div>
      </section>
    </div>
  );
}

// Icon placeholder to avoid error until I import properly
function CloudSun(props: any) {
  return <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="M20 12h2"/><path d="m19.07 4.93-1.41 1.41"/><path d="M15.947 12.65a4 4 0 0 0-5.925-4.128"/><path d="M13 22H7a5 5 0 1 1 4.9-6H13a3 3 0 0 1 0 6Z"/></svg>
}
