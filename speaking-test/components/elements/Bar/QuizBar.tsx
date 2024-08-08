import React, { FC } from "react";

type QuizBarProps = {
  currentNum: number;
};

export const QuizBar: FC<QuizBarProps> = ({ currentNum }) => {
  return (
    <div className="flex justify-center items-start h-16">
      <div
        className={`${currentNum === 1 ? "bg-red-300" : "bg-gray-300 text-gray-500"} ${"w-60 h-full text-3xl flex items-center justify-center"}`}
      >
        <p>大問1</p>
      </div>
      <div
        className={`${currentNum === 2 ? "bg-red-300" : "bg-gray-300 text-gray-500"} ${"w-60 h-full text-3xl flex items-center justify-center"}`}
      >
        <p>大問2</p>
      </div>
      <div
        className={`${currentNum === 3 ? "bg-red-300" : "bg-gray-300 text-gray-500"} ${"w-60 h-full text-3xl flex items-center justify-center"}`}
      >
        <p>大問3</p>
      </div>
    </div>
  );
};

// クイズバー（問題の進捗を表すバー）
// <QuizBar
// currentNum = {1} (1 or 2 or 3)
// />
