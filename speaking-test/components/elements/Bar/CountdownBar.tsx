"use client";

import { useRouter } from "next/navigation";
import React, { FC, useEffect } from "react";
import { useTimer } from "react-timer-hook";
import { TQuiz } from "@/types/type";

type BarProps = {
  status: string;
  timeLimit: number;
  isExplanation?: boolean;
  nextPath?: string;
  quiz?: TQuiz;
};

export const CountdownBar: FC<BarProps> = ({ status, timeLimit, isExplanation, nextPath, quiz }) => {
  const { totalSeconds } = useTimer({ expiryTimestamp: new Date(new Date().getTime() + timeLimit * 1000) });
  const router = useRouter();
  const logMessage = quiz ? `${status} ended: {CATEGORY: ${quiz.category}, QUIZ: ${quiz.id}}` : "";

  useEffect(() => {
    if (totalSeconds === 0) {
      if (nextPath) {
        router.push(nextPath);
      }
    }
  }, [logMessage, nextPath, router, status, totalSeconds]);

  return (
    <div className="flex justify-center items-center h-40">
      {/* Boccoの頭の部分 */}
      <div>
        {/* 問題進捗バーができたら数値を調整する */}
        <div className="w-6 absolute top-12 left-1/2 -translate-x-[402px] rotate-45">
          <div className="bg-red-600 w-6 h-6 rounded-full"></div>
          <div className="bg-bocco w-3 h-8 rounded-l-full"></div>
        </div>
        <div className="bg-bocco w-40 h-40 rounded-full flex justify-center items-center">
          <p className="text-center text-2xl font-bold">{status}</p>
        </div>
      </div>
      {/* カウントダウンバーの部分 */}
      <div className="flex items-center w-[800px] bg-pink-100">
        {isExplanation ? (
          <div className="h-4 w-[500px] bg-red-400"></div>
        ) : (
          <div className="h-4 bg-red-400" style={{ width: `${(totalSeconds / timeLimit) * 100}%` }}></div>
        )}
      </div>
      {/* 時間の表示 */}
      <div className="px-4">
        <p className="text-2xl font-bold">
          {isExplanation ? "0 : 15" : `${Math.floor(totalSeconds / 60)} : ${`${totalSeconds % 60}`.padStart(2, "0")}`}
        </p>
      </div>
    </div>
  );
};

// カウントダウンバー（時間の表示）
// 使い方
// <CoundownBar
// status = "準備中"
// timeLimit = {30} (sec)
// isExplanation (説明の時は必ずつける)
// />
