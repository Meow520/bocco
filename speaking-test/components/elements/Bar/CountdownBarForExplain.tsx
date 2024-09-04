"use client";

import React, { FC } from "react";

type BarProps = {};

export const CountdownBar: FC<BarProps> = ({}) => {
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
          <p className="text-center text-2xl font-bold">説明中</p>
        </div>
      </div>
      {/* カウントダウンバーの部分 */}
      <div className="flex items-center w-[800px] bg-pink-100">
        <div className="h-4 w-[500px] bg-red-400"></div>
      </div>
      {/* 時間の表示 */}
      <div className="w-24 text-center">
        <p className="text-2xl font-bold">0 : 15</p>
      </div>
    </div>
  );
};

// カウントダウンバー（時間の表示）
// 使い方
// <CoundownBar
// />
