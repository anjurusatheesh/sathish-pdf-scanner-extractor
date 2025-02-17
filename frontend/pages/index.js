// frontend/pages/index.js
import { useState } from 'react'
import FileUpload from '../components/FileUpload'
import ExtractedText from '../components/ExtractedText'

export default function Home() {
  const [extractedText, setExtractedText] = useState('')

  return (
    <div>
      <h1>PDF Scanner and Extractor</h1>
      <FileUpload setExtractedText={setExtractedText} />
      <ExtractedText text={extractedText} />
    </div>
  )
}