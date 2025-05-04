import axios from 'axios';

export const analyzeLog = async (file: File | null, text: string | null) => {
  const formData = new FormData();
  if (file) {
    formData.append('file', file);
  } else if (text) {
    formData.append('text', text);
  }

  const response = await axios.post('/api/analyze/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  return response.data;
};
