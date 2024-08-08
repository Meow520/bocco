"use client";

import Image from "next/image";
import React from "react";
import { LinkButton } from "@/components/elements/Button/LinkButton";

export const ExplanationMain = () => {

  return (
    <div className="h-full">
      <div className="w-full">
        <p className="text-4xl text-center">例題:</p>
        {/* mx-auto: marginの横方向をautoにする→Image使った時に写真が中央に行くよ */}
        {/* py-4:paddingを縦方向に4（16px）入れる */}
        <Image src={"/images/2.png"} alt="picture" width={600} height={450} priority className="mx-auto py-4"/>
        <p className="text-4xl text-center">It&apos;s been a long time. How have you been?</p>
      </div>

        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 translate-y-32">
        {/* absolute=絶対位置, top/leftは要素の左上が指定された位置に行く（1/2だと画面の1/2)、-translateはマイナス方向に移動させる(x-1/2=要素のxに対する1/2、32とかはpx) */}
          <p className="text-red-500 text-2xl font-semibold text-center">
            左上のBoccoﾁｬﾝが「録音中」と表示されたら
            <br />
            文章と図に対して回答をしてください
            <br />
            制限時間は30秒です
          </p>
        </div>

      <div className="absolute bottom-6 right-6">
          <div className="mr-0 ml-auto">
            <LinkButton label="start test" color="bg-gray-300 hover:bg-gray-200" size="bg" path="/quiz/1" />
          </div>

      </div>
    </div>
  );
};
