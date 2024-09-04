"use client";
import axios from "axios";
import React, { useEffect } from "react";

export const CompleteMain = () => {
  useEffect(() => {
    const resData = window.localStorage.getItem("log");
    if (resData) {
      axios.post("/api/uploadLog", resData);
    }
  }, []);
  return (
    <div>
      <p className="text-center text-4xl">
        テストは終了です <br />
        画面はそのままで実験管理者に終了の旨をお知らせください
      </p>
    </div>
  );
};
