export type TQuiz = {
  id: string;
  category: number;
  quiz?: string;
  time: number;
  thinking?: number;
  image?: {
    path: string;
    width: number;
    height: number;
  };
  audio?: { audioPath: string; duration: number };
  next: string;
};
