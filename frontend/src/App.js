// // // import React,{useState} from "react";
// // // import axios from 'axios'
// // // import logo from './logo.svg';
// // // import './App.css';

// // // function App() {
// // //   const [text,setText]=useStateQ("")
// // //   const [summary,setSummary]=useState("")
// // //   const [file,setFile]=useState(null)
// // //   const [youtubeURL,setyoutubeURL]=useState("")
// // //   const [mode,setMode]=useState('text')
// // //   const [loading,setLoading]=useState(false)

// // //   const handleSummarize=async()=>{
// // //     setLoading(true)
// // //     setSummary("")
// // //     try{
// // //       let res;
// // //       if (mode==="text"){
// // //         if(!text.trim()) return alert("Please Enter Some Text")
// // //           res=await axios.post("http://localhost:5000/summarize/text",{text})
// // //       }
// // //       else if (mode==="pdf"){
// // //         if(!file) return alert("Please Upload a PDF file")
// // //           const formData=new FormData()
// // //         formData.append("file",file)
// // //         res=await axios.post("http://localhost:5000/summarize/pdf",formData,{headers:{"Content-Type":"multipart/form-data"}})
// // //               }
// // //       else if (mode==='youtube')

// // //       if(!youtubeURL.trim()) return alert("Please Enter a Youtube URL")
// // //         res=await axios.post("http://localhost:5000/summarize/youtube",{url:youtubeURL,});
    
// // //         setSummary(res.data.summary)
// // //     }
// // //     catch(err){
// // //       console.error(err)
// // //       alert("Something went wrong")
// // //     }
// // //     setLoading(false)
// // //   }


// // //   return (
// // //     <div className="App">
// // //       <h1>AI Summarizer(Text,PDF and Youtube)</h1>
// // //       <div className="mode-buttons">
// // //         <button className={mode==="text"?"active":""} onClick={()=>setMode(text)}>
// // //           Text
// // //           </button>
// // //           <button className={mode==="pdf"?"active":""} onClick={()=>setMode(pdf)}>
// // //           PDF
// // //           </button>
// // //           <button className={mode==="youtube"?"active":""} onClick={()=>setMode(youtube)}>
// // //           Youtube
// // //           </button>
// // //       </div>

// // //       {mode=='text' && (
// // //         <textarea placeholder = "Paste yout text here..."
// // //         rows="10"
// // //         value = {text}
// // //         onChange={(e)=>setText(e.target.value)}></textarea>
// // //       )}

// // //       {mode=='pdf' && (
// // //         <input type="file"
// // //         accept="application/pdf"
// // //         onChange={(e)=>setFile(e.target.files[0])}></input>
// // //       )}

// // //       {mode=='youtube' && (
// // //         <input
// // //          type = "text"
// // //           placeholder = "Enter your Youtube video url here..."
// // //         rows="10"
// // //         value = {youtubeURL}
// // //         onChange={(e)=>setyoutubeURL(e.target.value)}></input>
// // //       )}
// // //       <button onClick={handleSummarize} disabled={loading}>
// // //        {loading?Summmarizing:Summarize}
// // //       </button>

// // //       {summary && 
// // //       (
// // //         <div className="summary">
// // //         <h2>Summary</h2>
// // //         <p>Summary</p>
// // //       )

// // //       }
// // //     </div>
// // //   );
// // // }

// // // export default App;
// // import React, { useState } from "react";
// // import axios from "axios";
// // import "./App.css";

// // function App() {
// //   const [text, setText] = useState("");
// //   const [summary, setSummary] = useState("");
// //   const [file, setFile] = useState(null);
// //   const [youtubeURL, setYoutubeURL] = useState("");
// //   const [mode, setMode] = useState("text");
// //   const [loading, setLoading] = useState(false);

// //   const handleSummarize = async () => {
// //     setLoading(true);
// //     setSummary("");

// //     try {
// //       let res;

// //       if (mode === "text") {
// //         if (!text.trim()) {
// //           alert("Please Enter Some Text");
// //           setLoading(false);
// //           return;
// //         }

// //         res = await axios.post("http://localhost:5000/summarize/text", {
// //           text,
// //         });
// //       }

// //       else if (mode === "pdf") {
// //         if (!file) {
// //           alert("Please Upload a PDF file");
// //           setLoading(false);
// //           return;
// //         }

// //         const formData = new FormData();
// //         formData.append("file", file);

// //         res = await axios.post(
// //           "http://localhost:5000/summarize/pdf",
// //           formData,
// //           {
// //             headers: { "Content-Type": "multipart/form-data" },
// //           }
// //         );
// //       }

// //       else if (mode === "youtube") {
// //         if (!youtubeURL.trim()) {
// //           alert("Please Enter a YouTube URL");
// //           setLoading(false);
// //           return;
// //         }

// //         res = await axios.post(
// //           "http://localhost:5000/summarize/youtube",
// //           { url: youtubeURL }
// //         );
// //       }

// //       setSummary(res.data.summary);
// //     } catch (err) {
// //       console.error(err);
// //       alert("Something went wrong");
// //     }

// //     setLoading(false);
// //   };

// //   return (
// //     <div className="App">
// //       <h1>AI Summarizer (Text, PDF and YouTube)</h1>

// //       <div className="mode-buttons">
// //         <button
// //           className={mode === "text" ? "active" : ""}
// //           onClick={() => setMode("text")}
// //         >
// //           Text
// //         </button>

// //         <button
// //           className={mode === "pdf" ? "active" : ""}
// //           onClick={() => setMode("pdf")}
// //         >
// //           PDF
// //         </button>

// //         <button
// //           className={mode === "youtube" ? "active" : ""}
// //           onClick={() => setMode("youtube")}
// //         >
// //           YouTube
// //         </button>
// //       </div>

// //       {mode === "text" && (
// //         <textarea
// //           placeholder="Paste your text here..."
// //           rows="10"
// //           value={text}
// //           onChange={(e) => setText(e.target.value)}
// //         />
// //       )}

// //       {mode === "pdf" && (
// //         <input
// //           type="file"
// //           accept="application/pdf"
// //           onChange={(e) => setFile(e.target.files[0])}
// //         />
// //       )}

// //       {mode === "youtube" && (
// //         <input
// //           type="text"
// //           placeholder="Enter your YouTube video URL here..."
// //           value={youtubeURL}
// //           onChange={(e) => setYoutubeURL(e.target.value)}
// //         />
// //       )}

// //       <button onClick={handleSummarize} disabled={loading}>
// //         {loading ? "Summarizing..." : "Summarize"}
// //       </button>

// //       {summary && (
// //         <div className="summary">
// //           <h2>Summary</h2>
// //           <p>{summary}</p>
// //         </div>
// //       )}
// //     </div>
// //   );
// // }

// // export default App;


// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [text, setText] = useState("");
//   const [summary, setSummary] = useState("");
//   const [file, setFile] = useState(null);
//   const [youtubeURL, setYoutubeURL] = useState("");
//   const [mode, setMode] = useState("text");
//   const [loading, setLoading] = useState(false);

//   const handleSummarize = async () => {
//     setLoading(true);
//     setSummary("");

//     try {
//       let res;

//       if (mode === "text") {
//         if (!text.trim()) {
//           alert("Please Enter Some Text");
//           setLoading(false);
//           return;
//         }

//         res = await axios.post("/summarize/text", { text });
//       }

//       else if (mode === "pdf") {
//         if (!file) {
//           alert("Please Upload a PDF file");
//           setLoading(false);
//           return;
//         }

//         const formData = new FormData();
//         formData.append("file", file);

//         res = await axios.post("/summarize/pdf", formData);
//       }

//       else if (mode === "youtube") {
//         if (!youtubeURL.trim()) {
//           alert("Please Enter a YouTube URL");
//           setLoading(false);
//           return;
//         }

//         res = await axios.post("/summarize/youtube", {
//           url: youtubeURL,
//         });
//       }

//       if (res.data.summary) {
//         setSummary(res.data.summary);
//       } else if (res.data.error) {
//         alert(res.data.error);
//       } else {
//         alert("Unexpected response from server");
//       }

//     } catch (err) {
//       console.error("Frontend Error:", err);
//       alert("Something went wrong");
//     }

//     setLoading(false);
//   };

//   return (
//     <div className="App">
//       <h1>AI Summarizer (Text, PDF and YouTube)</h1>

//       <div className="mode-buttons">
//         <button
//           className={mode === "text" ? "active" : ""}
//           onClick={() => setMode("text")}
//         >
//           Text
//         </button>

//         <button
//           className={mode === "pdf" ? "active" : ""}
//           onClick={() => setMode("pdf")}
//         >
//           PDF
//         </button>

//         <button
//           className={mode === "youtube" ? "active" : ""}
//           onClick={() => setMode("youtube")}
//         >
//           YouTube
//         </button>
//       </div>

//       {mode === "text" && (
//         <textarea
//           placeholder="Paste your text here..."
//           rows="10"
//           value={text}
//           onChange={(e) => setText(e.target.value)}
//         />
//       )}

//       {mode === "pdf" && (
//         <input
//           type="file"
//           accept="application/pdf"
//           onChange={(e) => setFile(e.target.files[0])}
//         />
//       )}

//       {mode === "youtube" && (
//         <input
//           type="text"
//           placeholder="Enter your YouTube video URL here..."
//           value={youtubeURL}
//           onChange={(e) => setYoutubeURL(e.target.value)}
//         />
//       )}

//       <button onClick={handleSummarize} disabled={loading}>
//         {loading ? "Summarizing..." : "Summarize"}
//       </button>

//       {summary && (
//         <div className="summary">
//           <h2>Summary</h2>
//           <p>{summary}</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;


import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [questions, setQuestions] = useState("");
  const [file, setFile] = useState(null);
  const [youtubeURL, setYoutubeURL] = useState("");
  const [mode, setMode] = useState("text");
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    setLoading(true);
    setSummary("");
    setQuestions("");

    try {
      let res;

      if (mode === "text") {
        if (!text.trim()) {
          alert("Please Enter Some Text");
          setLoading(false);
          return;
        }

        res = await axios.post("/summarize/text", { text });
      }

      else if (mode === "pdf") {
        if (!file) {
          alert("Please Upload a PDF file");
          setLoading(false);
          return;
        }

        const formData = new FormData();
        formData.append("file", file);

        res = await axios.post("/summarize/pdf", formData);
      }

      else if (mode === "youtube") {
        if (!youtubeURL.trim()) {
          alert("Please Enter a YouTube URL");
          setLoading(false);
          return;
        }

        res = await axios.post("/summarize/youtube", {
          url: youtubeURL,
        });
      }

      if (res.data.summary) {
        setSummary(res.data.summary);
        setQuestions(res.data.questions);   // 🔥 NEW
      } 
      else if (res.data.error) {
        alert(res.data.error);
      } 
      else {
        alert("Unexpected response from server");
      }

    } catch (err) {
      console.error("Frontend Error:", err);
      alert("Something went wrong");
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <h1>AI Summarizer (Text, PDF and YouTube)</h1>

      <div className="mode-buttons">
        <button
          className={mode === "text" ? "active" : ""}
          onClick={() => setMode("text")}
        >
          Text
        </button>

        <button
          className={mode === "pdf" ? "active" : ""}
          onClick={() => setMode("pdf")}
        >
          PDF
        </button>

        <button
          className={mode === "youtube" ? "active" : ""}
          onClick={() => setMode("youtube")}
        >
          YouTube
        </button>
      </div>

      {mode === "text" && (
        <textarea
          placeholder="Paste your text here..."
          rows="10"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      )}

      {mode === "pdf" && (
        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />
      )}

      {mode === "youtube" && (
        <input
          type="text"
          placeholder="Enter your YouTube video URL here..."
          value={youtubeURL}
          onChange={(e) => setYoutubeURL(e.target.value)}
        />
      )}

      <button onClick={handleSummarize} disabled={loading}>
        {loading ? "Summarizing..." : "Summarize"}
      </button>

      {summary && (
        <div className="summary">
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}

      {questions && (
        <div className="questions">
          <h2>Generated Questions</h2>
          <pre>{questions}</pre>
        </div>
      )}
    </div>
  );
}

export default App;