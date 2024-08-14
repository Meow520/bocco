// 考える時間がある時用のページ

import { NextPage } from "next";
import React from "react";
import { QuizMain } from "@/components/features/quiz/QuizMain";
import data from "@/data/quiz.json";

type QuizProps = {
  params: { id: string };
};

const Quiz: NextPage<QuizProps> = ({ params }) => {
  const quiz = data["data"].filter((data) => data.id === params.id)[0];
  return (
    <div className="h-screen">
      <QuizMain quiz={quiz} status="playing" />
    </div>
  );
};

export default Quiz;
