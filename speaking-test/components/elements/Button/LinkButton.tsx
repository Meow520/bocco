"use client";

import Link from "next/link";
import React, { FC } from "react";

type LinkButtonProps = {
  label: string;
  color: string;
  size: "bg" | "sm";
  type?: "submit" | "reset" | "button";
  disabled?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  path: string;
};

export const LinkButton: FC<LinkButtonProps> = ({ label, color, size, type, disabled, onClick, path }) => {
  const className = `${color} ${size === "bg" ? "w-[200px] h-[80px] text-4xl" : "w-[120px] h-[48px] text-xl"} ${"items-center rounded-md px-4 py-2"}`;
  return (
    <Link href={path} as={path} className={`${disabled ? "pointer-events-none" : ""}`}>
      <button className={className} type={type} disabled={disabled} onClick={onClick}>
        {label}
      </button>
    </Link>
  );
};

// リンクボタン（ページの遷移がある場合に使う）
// 使い方
// <LinkButton
//  label = "Start"
//  color="bg-blue-500 text-white"
//  type="submit"  (submit or button or reset) 設定しなくてもいい
//  onClick={()=>console.log("start")} 設定しなくてもいい
//  size="bg" (bg or sm)
//  ref="/abc"
// />
