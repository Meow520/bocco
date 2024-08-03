"use client";

import Image from "next/image";
import React, { FC } from "react";
import { CountdownBar } from "@/components/elements/Bar/CountdownBar";
import { QuizBar } from "@/components/elements/Bar/QuizBar";

type QuizMainProps = {
  quiz: {
    id: string;
    category: number;
    quiz: string;
    time: number;
    thinking?: number;
    image?: {
      path: string;
      width: number;
      height: number;
    };
    next: string;
  };
  status: "thinking" | "quiz";
};

export const QuizMain: FC<QuizMainProps> = ({ quiz, status }) => {
  const nextPath =
    status === "thinking"
      ? `/quiz/${quiz.id}`
      : quiz.next === "explanation"
        ? `/explanation/${quiz.category + 1}`
        : quiz.next === "complete"
          ? "complete"
          : `/quiz/${quiz.next}`;
  return (
    <div className="h-screen">
      <QuizBar currentNum={quiz.category} />
      <CountdownBar
        status={status === "quiz" ? "録音中" : "考え中"}
        timeLimit={status === "quiz" ? quiz.time : quiz.thinking ? quiz.thinking : 30}
        nextPath={nextPath}
      />
      {quiz.image ? (
        <div>
          <Image
            src={`/images/${quiz.image.path}`}
            width={quiz.image.width}
            height={quiz.image.height}
            alt="picture"
            className="mx-auto"
          />
          <p className="text-center text-4xl py-4">{quiz.quiz}</p>
        </div>
      ) : (
        <div className="py-40">
          <p className="text-center text-4xl">{quiz.quiz}</p>
        </div>
      )}
    </div>
  );
};
