"use client";

import React from "react";
import { LinkButton } from "@/components/elements/Button/LinkButton";

export const ExplanationMain = () => {

  return (
    <div className="h-full">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
          <p className="text-red-500 text-2xl font-semibold text-center">
            左上のBoccoﾁｬﾝが「録音中」と表示されたら
            <br />
            流れてくる音声に対して回答をしてください
            <br />
        　　回答時間は15秒です
          </p>
        </div>

      <div className="absolute bottom-6 right-6">
          <div className="mr-0 ml-auto">
            <LinkButton label="start test" color="bg-gray-300 hover:bg-gray-200" size="bg" path="/quiz/21
            " />
          </div>

      </div>
    </div>
  );
};