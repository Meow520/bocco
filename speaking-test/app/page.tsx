// スタート画面（ルート）

import React from "react";
import { LinkButton } from "@/components/elements/Button/LinkButton";

const Home = () => {
  return (
    <main className="min-h-screen flex justify-center items-center">
      <div className="">
        <div className="py-28">
          <h1 className="text-center text-4xl">English speaking test</h1>
        </div>
        <div className="py-28 flex">
          <div className="mx-auto">
            <LinkButton label="start" color="bg-gray-300" size="bg" path="/explanation/1" />
          </div>
        </div>
      </div>
    </main>
  );
};

export default Home;
