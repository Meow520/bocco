"use client";

import Image from "next/image";
import React, { FC } from "react";
import { CountdownBar } from "@/components/elements/Bar/CountdownBar";
import { QuizBar } from "@/components/elements/Bar/QuizBar";

// .tsxは.tsファイルの中でhtmlを戻り値とする関数をexportする
type QuizMainProps = {
  quiz: {
    id: string;
    category: number;
    quiz?: string;
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
// export constを書かないと他のファイルで使えなくなる
// お名前:型<引数の型> = ({引数（型に書いているやつしか使えない）})　＝> {処理書いていく}
  const nextPath =
  // ===みっつつけるとifの時のイコール、?Trueの場合、:Falseの場合
    status === "thinking"  
      ? `/quiz/${quiz.id}`
      : quiz.next === "explanation"
        ? `/explanation/${quiz.category + 1}`
        : quiz.next === "complete"
          ? "complete"
          : `/quiz/${quiz.next}`;
  return (
    // 一個しか要素書いたらダメなので、divタグでくくる（中に要素入れるのはok)
    <div className="h-screen">
      <QuizBar currentNum={quiz.category} />
      <CountdownBar
        status={status === "quiz" ? "録音中" : "考え中"}
        timeLimit={status === "quiz" ? quiz.time : quiz.thinking ? quiz.thinking : 30}
        nextPath={nextPath}
      />
      {quiz.image && (
        // &&Trueの時だけの処理
        <div>
          <Image
          // /はpublicの中
            src={`/images/${quiz.image.path}`}
            priority
            width={quiz.image.width}
            height={quiz.image.height}
            alt="picture"
            className="mx-auto"
          />
        </div>
      )}
      {quiz.quiz&&(
          <div className={`${quiz.image?"":"py-40"}`}>
            <p className={`${quiz.image&&"py-4"} ${"text-center text-4xl"}`}>{quiz.quiz}</p>
          </div>
      )}
      
    </div>
  );
};
