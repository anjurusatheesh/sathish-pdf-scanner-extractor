// frontend/components/FileUpload.js
import { useState } from 'react'
import axios from 'axios'

export default function FileUpload({ setExtractedText }) {
  const [file, setFile] = useState(null)

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!file) return

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      setExtractedText(response.data.extracted_text)
    } catch (error) {
      console.error('Error uploading file:', error)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileChange} accept=".pdf" />
      <button type="submit">Upload and Extract</button>
    </form>
  )
}