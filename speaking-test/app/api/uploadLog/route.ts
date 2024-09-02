import fs from "node:fs/promises";
import { revalidatePath } from "next/cache";
import { NextResponse } from "next/server";

export async function POST(req: Request) {
  let Data;
  try {
    const formData = await req.formData();
    for (let value of formData.entries()) {
      Data = value;
    }
    if (Data) {
        const outputData = Data[0].toString();
        const date = new Date().toLocaleString().replaceAll(/[/,:]/g, "_").replace(/\s+/g, "")
        const filename = `${process.cwd()}/public/log/log_${date}.json`
        await fs.writeFile(filename, outputData);
    }

    // const file = formData.get("file") as File;
    // const arrayBuffer = await file.arrayBuffer();
    // const buffer = new Uint8Array(arrayBuffer);

    revalidatePath("/");

    return NextResponse.json({ status: "success" });
  } catch (e) {
    console.error(e);
    return NextResponse.json({ status: "fail", error: e });
  }
}
