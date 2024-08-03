// テスト終了画面

import React from "react";

const Complete = () => {
  return (
    <div className="h-screen w-full flex items-center justify-center">
      <p className="text-center text-4xl">
        テストは終了です <br />
        画面はそのままで実験管理者に終了の旨をお知らせください
      </p>
    </div>
  );
};

export default Complete;
