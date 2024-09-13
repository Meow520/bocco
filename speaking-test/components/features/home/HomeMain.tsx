"use client";
import React, { useEffect } from "react";
import { LinkButton } from "@/components/elements/Button/LinkButton";

export const HomeMain = () => {
  const log = 
  [{quiz: "home",category:"-", status: "-", time: new Date().toLocaleString()}];
  const logMessage = JSON.stringify(log)
  useEffect(() => {
    window.localStorage.setItem("log", logMessage);
  }, [logMessage]);
  return (
    <div className="">
      <div className="py-28">
        <h1 className="text-center text-4xl">English speaking test</h1>
      </div>
      <div className="py-28 flex">
        <div className="mx-auto">
          <LinkButton label="start" color="bg-gray-300 hover:bg-gray-200" size="bg" path="/explanation/1" />
        </div>
      </div>
    </div>
  );
};
