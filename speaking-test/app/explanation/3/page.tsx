// 説明（大問3）

import React from 'react'
import { CountdownBar } from '@/components/elements/Bar/CountdownBar'
import { QuizBar } from '@/components/elements/Bar/QuizBar'
import { ExplanationMain } from '@/components/features/explanation/3/ExplanationMain'

const Explanation = () => {
  return (
    <div className='h-screen'>
        <QuizBar currentNum={3} />
        <CountdownBar status='説明中' timeLimit={30} isExplanation />
        <ExplanationMain />
    </div>
  )
}

export default Explanation