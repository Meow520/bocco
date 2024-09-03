"use client";

import Image from "next/image";
import React, { FC, useEffect, useRef, useState } from "react";
import { IoVolumeHigh } from "react-icons/io5";
import { CountdownBar } from "@/components/elements/Bar/CountdownBar";
import { QuizBar } from "@/components/elements/Bar/QuizBar";
import { TLog, TLogs, TQuiz } from "@/types/type";

type QuizMainProps = {
  quiz: TQuiz;
  status: "thinking" | "quiz" | "playing";
};

type AudioPlayAudioProps = {
  audioUrl: string;
};

// 自動再生用の要素を戻り値にもつ
const AutoPlayAudio: React.FC<AudioPlayAudioProps> = ({ audioUrl }) => {
  const audioRef = useRef<HTMLAudioElement>(null);

  useEffect(() => {
    if (audioUrl && audioRef.current) {
      audioRef.current.play();
    }
  }, [audioUrl]);

  return (
    <audio ref={audioRef} controls>
      <source src={`/audios/${audioUrl}`} type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  );
};

// .tsxは.tsファイルの中でhtmlを戻り値とする関数をexportする
export const QuizMain: FC<QuizMainProps> = ({ quiz, status }) => {
  const [logs, setLogs] = useState<TLogs>([]);
  const categoryToString: string = quiz.category.toString();
  const log: TLog = { time: new Date().toLocaleString(), quiz: quiz.id, category: categoryToString, status: status };
  useEffect(() => {
    let logsData: TLogs;
    const resData = window.localStorage.getItem("log");
    logsData = resData && JSON.parse(resData);
    logsData.push(log);
    setLogs([...logs, ...logsData]);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  // export constを書かないと他のファイルで使えなくなる
  // お名前:型<引数の型> = ({引数（型に書いているやつしか使えない）})　＝> {処理書いていく}
  const nextPath =
    // ===みっつつけるとifの時のイコール、?Trueの場合、:Falseの場合
    status === "thinking" || status === "playing"
      ? `/quiz/${quiz.id}`
      : quiz.next === "explanation"
        ? `/explanation/${quiz.category + 1}`
        : quiz.next === "complete"
          ? "/complete"
          : `/quiz/${quiz.next}`;

  return (
    // 一個しか要素書いたらダメなので、divタグでくくる（中に要素入れるのはok)
    <div className="h-screen">
      <QuizBar currentNum={quiz.category} />
      <CountdownBar
        status={status === "thinking" ? "考え中" : status === "playing" ? "再生中" : "録音中"}
        timeLimit={
          status === "thinking" && quiz.thinking
            ? quiz.thinking
            : status === "playing" && quiz.audio
              ? quiz.audio.duration
              : quiz.time
        }
        nextPath={nextPath}
        quiz={quiz}
        logsData={logs}
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
      {quiz.quiz && (
        <div className={`${quiz.image ? "" : "py-40"}`}>
          <p className={`${quiz.image && "py-4"} ${"text-center text-4xl"}`}>{quiz.quiz}</p>
        </div>
      )}
      {quiz.audio && (
        <div>
          {status === "playing" && (
            <div className="invisible">
              <AutoPlayAudio audioUrl={quiz.audio.audioPath} />
            </div>
          )}
          <div className="text-gray-600 flex items-center justify-center">
            <IoVolumeHigh className="w-[400px] h-[400px]" />
          </div>
        </div>
      )}
    </div>
  );
};
