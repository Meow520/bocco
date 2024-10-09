"use client";

import React, { useState } from "react";
import { Button } from "@/components/elements/Button/Button";
import { LinkButton } from "@/components/elements/Button/LinkButton";

export const ExplanationMain = () => {
  const [num, setNum] = useState(1);
  const handleNum = () => {
    setNum(num + 1);
  };

  return (
    <div className="h-full">
      <div className="w-full py-32">
        <p className="text-4xl text-center">例題:</p>
        <p className="text-4xl text-center">It&apos;s been a long time. How have you been?</p>
      </div>
      {num > 0 && (
        <div className="w-60 absolute top-60 left-1/2 -translate-x-[570px]">
          <p className="text-red-500 text-2xl font-semibold text-center">
            現在の状況が
            <br />
            書かれます
            <br />
            (表示中、録音中など)
          </p>
        </div>
      )}
      {num > 1 && (
        <div className="w-60 absolute top-48 left-1/2 translate-x-[360px]">
          <p className="text-red-500 text-2xl font-semibold text-center">
            残り秒数が
            <br />
            表示されます
          </p>
        </div>
      )}
      {num > 2 && (
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 translate-y-12">
          <p className="text-red-500 text-2xl font-semibold text-center">
            文章が表示されます
            <br />
            左上のBoccoﾁｬﾝが「録音中」と表示されたら
            <br />
            文章を読み上げてください
            <br />
            制限時間は30秒です
          </p>
        </div>
      )}
      <div className="absolute bottom-6 right-6">
        {num > 2 ? (
          <div className="mr-0 ml-auto">
            <LinkButton label="start test" color="bg-gray-300 hover:bg-gray-200" size="bg" path="/quiz/1/thinking" />
          </div>
        ) : (
          <Button label="next" color="bg-gray-300 hover:bg-gray-200" size="bg" onClick={handleNum} />
        )}
      </div>
    </div>
  );
};
