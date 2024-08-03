"use client";

import React, { FC } from "react";

type ButtonProps = {
  label: string;
  color: string;
  size: "bg" | "sm";
  type?: "submit" | "reset" | "button";
  disabled?: boolean;
  form?: string;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
};

export const Button: FC<ButtonProps> = ({ label, color, size, type, disabled, form, onClick }) => {
  const className = `${color} ${size === "bg" ? "w-[200px] h-[80px] text-3xl" : "w-[120px] h-[48px] text-xl"} ${"items-center rounded-md px-4 py-2"}`;
  return (
    <button className={className} type={type} disabled={disabled} form={form} onClick={onClick}>
      {label}
    </button>
  );
};

// ノーマルボタン
// 使い方
// <Button
//  label = "Start"
//  color="bg-blue-500 text-white"
//  type="submit"  (submit or button or reset) 設定しなくてもいい
//  onClick={()=>console.log("start")} 設定しなくてもいい
//  size="bg" (bg or sm)
// />
