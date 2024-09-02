// 説明（大問2）

import React from "react";
import { CountdownBar } from "@/components/elements/Bar/CountdownBarForExplain";
import { QuizBar } from "@/components/elements/Bar/QuizBar";
import { ExplanationMain } from "@/components/features/explanation/2/ExplanationMain";

const Explanation = () => {
  return (
    <div className="h-screen">
      <QuizBar currentNum={2} />
      <CountdownBar />
      <ExplanationMain />
    </div>
  );
};

export default Explanation;
