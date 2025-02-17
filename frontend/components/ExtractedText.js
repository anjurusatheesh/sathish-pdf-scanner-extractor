// frontend/components/ExtractedText.js
export default function ExtractedText({ text }) {
    if (!text) return null
  
    return (
      <div>
        <h2>Extracted Text:</h2>
        <p>{text}</p>
      </div>
    )
  }