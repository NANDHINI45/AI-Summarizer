# # from flask import Flask,request,jsonify
# # from flask_cors import CORS
# # from openai import OpenAI
# # from youtube_transcript_api import YouTubeTranscriptApi
# # import fitz
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()
# # client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # app=Flask(__name__)
# # CORS(app,origins="http://localhost:3000")

# # # def get_summary(prompt):
# # #     response=client.chat.completions.create(
# # #         model="gpt-3.5-turbo",
# # #         messages=[
# # #             {"role":"system","content":"You are a helpful assistant that summarizes content"},
# # #             {"role":"user","content":prompt}
# # #         ],

# # #         max_tokens=300
# # #     )
# # #     return response.choices[0].message.content
# # def get_summary(prompt):
# #     response = client.responses.create(
# #         model="gpt-4.1-mini",
# #         input=[
# #             {"role": "system", "content": "You are a helpful assistant that summarizes content"},
# #             {"role": "user", "content": prompt}
# #         ],
# #         max_output_tokens=300
# #     )

# #     return response.output[0].content[0].text

# # @app.route('/summarize/text',methods=['POST'])  
# # def summarize_text():
# #     data=request.get_json()
# #     text=data['text']
# #     prompt=f"Summarize the following text:\n{text}" 
# #     summary=get_summary(prompt)
# #     return jsonify({'summary':summary})

# # @app.route('/summarize/pdf',methods=['POST'])
# # def summarize_pdf():
# #     file=request.files['file']
# #     doc=fitz.open(stream=file.read(),filetype="pdf")
# #     text=""
# #     for page in doc:
# #         text+=page.get_text()
# #     prompt=f"Summarize the following pdf content:\n{text}"
# #     summary=get_summary(prompt)
# #     return jsonify({"summary":summary}) 


# # # @app.route('/summarize/youtube',methods=['POST'])
# # # def summarize_youtube():
# # #     data=request.get_json()
# # #     url=data['url']
# # #     video_id=url.split("v="[-1]) 
# # #     transcript=YoutubeTranscriptApi.get_transcript(video_id)
# # #     text="".join([t['text'] for t in transcript]) 
# # #     prompt=f"Summarize this youtube video transcript:\n{text}" 
# # #     summary=get_summary(prompt)
# # #     return jsonify({'summary':summary})
# # @app.route('/summarize/youtube', methods=['POST'])
# # def summarize_youtube():
# #     data = request.get_json()
# #     url = data['url']

# #     if "youtu.be" in url:
# #         video_id = url.split("/")[-1].split("?")[0]
# #     else:
# #         video_id = url.split("v=")[-1].split("&")[0]

# #     transcript = YouTubeTranscriptApi.get_transcript(video_id)
# #     text = " ".join([t['text'] for t in transcript])

# #     prompt = f"Summarize this YouTube video transcript:\n{text}"
# #     summary = get_summary(prompt)

# #     return jsonify({'summary': summary})

# # if __name__=='__main__':
# #     app.run(debug=True)    

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from google import genai
# from youtube_transcript_api import YouTubeTranscriptApi
# import fitz
# from dotenv import load_dotenv
# import os
# import re

# def extract_video_id(url):
#     patterns = [
#         r"v=([^&]+)",
#         r"youtu\.be/([^?&]+)",
#         r"shorts/([^?&]+)"
#     ]

#     for pattern in patterns:
#         match = re.search(pattern, url)
#         if match:
#             return match.group(1)

#     return None

# # -------------------- LOAD ENV --------------------
# print("YOUTUBE ROUTE LOADED")
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     print("❌ GEMINI_API_KEY not found")

# client = genai.Client(api_key=api_key)
# print("Available Models:")

# for m in client.models.list():
#     print(m.name)

# # -------------------- FLASK APP --------------------

# app = Flask(__name__)
# CORS(app)

# # -------------------- SUMMARY FUNCTION --------------------

# def get_summary(prompt):
#     try:
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=prompt
#         )
#         return response.text
#     except Exception as e:
#         print("🔥 Gemini Error:", e)
#         return "Error generating summary."

# # -------------------- TEXT ROUTE --------------------

# @app.route("/summarize/text", methods=["POST"])
# def summarize_text():
#     try:
#         data = request.get_json()
#         text = data.get("text", "")

#         if not text.strip():
#             return jsonify({"error": "Text is empty"}), 400

#         prompt = f"Summarize the following text clearly:\n{text[:4000]}"
#         summary = get_summary(prompt)

#         return jsonify({"summary": summary})

#     except Exception as e:
#         print("Text Error:", e)
#         return jsonify({"error": "Something went wrong"}), 500


# # -------------------- PDF ROUTE --------------------

# @app.route("/summarize/pdf", methods=["POST"])
# def summarize_pdf():
#     try:
#         if "file" not in request.files:
#             return jsonify({"error": "No file uploaded"}), 400

#         file = request.files["file"]
#         doc = fitz.open(stream=file.read(), filetype="pdf")

#         text = ""
#         for page in doc:
#             text += page.get_text()

#         if not text.strip():
#             return jsonify({"error": "No readable text found"}), 400

#         prompt = f"Summarize the following PDF content:\n{text[:4000]}"
#         summary = get_summary(prompt)

#         return jsonify({"summary": summary})

#     except Exception as e:
#         print("PDF Error:", e)
#         return jsonify({"error": "Something went wrong"}), 500


# # -------------------- YOUTUBE ROUTE --------------------

# # @app.route("/summarize/youtube", methods=["POST"])
# # def summarize_youtube():
# #     try:
# #         data = request.get_json()
# #         url = data.get("url", "")

# #         if not url.strip():
# #             return jsonify({"error": "URL is empty"}), 400

# #         if "youtu.be" in url:
# #             video_id = url.split("/")[-1].split("?")[0]
# #         else:
# #             video_id = url.split("v=")[-1].split("&")[0]

# #         transcript = YouTubeTranscriptApi().fetch(video_id)
# #         text = " ".join([t.text for t in transcript])

# #         prompt = f"Summarize this YouTube transcript:\n{text[:4000]}"
# #         summary = get_summary(prompt)

# #         return jsonify({"summary": summary})

# #     except Exception as e:
# #         print("YouTube Error:", e)
# #         return jsonify({"error": "Transcript not available"}), 500
# #---------
# # @app.route("/summarize/youtube", methods=["POST"])
# # def summarize_youtube():
# #     try:
# #         data = request.get_json()
# #         url = data.get("url", "")

# #         if not url.strip():
# #             return jsonify({"error": "URL is empty"}), 400

# #         # Extract video ID
# #         if "youtu.be" in url:
# #             video_id = url.split("/")[-1].split("?")[0]
# #         else:
# #             video_id = url.split("v=")[-1].split("&")[0]

# #         api = YouTubeTranscriptApi()

# #         # 🔥 Get transcript list (new API)
# #         transcript_list = api.list(video_id)

# #         transcript = None

# #         # Try English first
# #         try:
# #             transcript = transcript_list.find_transcript(["en"])
# #         except:
# #             # If English not available, use first available transcript
# #             transcript = next(iter(transcript_list))

# #         transcript_data = transcript.fetch()

# #         text = " ".join([item.text for item in transcript_data])

# #         prompt = f"""
# #         Summarize the following transcript in English:

# #         {text[:4000]}
# #         """

# #         summary = get_summary(prompt)

# #         return jsonify({"summary": summary})

# #     except Exception as e:
# #         print("🔥 YouTube Error:", e)
# #         return jsonify({
# #             "error": "This video does not allow transcript access or captions are unavailable."
# #         }), 400

# @app.route("/summarize/youtube", methods=["POST"])
# def summarize_youtube():
#     try:
#         data = request.get_json()
#         url = data.get("url", "").strip()

#         if not url:
#             return jsonify({"error": "URL is empty"}), 400

#         # 🔥 Extract Video ID (supports all formats)
#         video_id = extract_video_id(url)

#         if not video_id:
#             return jsonify({"error": "Invalid YouTube URL"}), 400

#         api = YouTubeTranscriptApi()

#         # 🔥 Get transcript list (new API style)
#         transcript_list = api.list(video_id)

#         try:
#             # Try English first
#             transcript = transcript_list.find_transcript(["en"])
#         except:
#             # If English not available, use first available language
#             transcript = next(iter(transcript_list))

#         transcript_data = transcript.fetch()

#         text = " ".join([item.text for item in transcript_data])

#         if not text.strip():
#             return jsonify({"error": "Transcript empty"}), 400

#         prompt = f"""
#         Summarize the following transcript in English:

#         {text[:4000]}
#         """

#         summary = get_summary(prompt)

#         return jsonify({"summary": summary})

#     except Exception as e:
#         print("🔥 YouTube Error:", e)
#         return jsonify({
#             "error": "This video does not allow transcript access or captions are unavailable."
#         }), 400
# # -------------------- RUN SERVER --------------------

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)


from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from youtube_transcript_api import YouTubeTranscriptApi
import fitz
from dotenv import load_dotenv
import os
import re

# -------------------- VIDEO ID EXTRACTOR --------------------

def extract_video_id(url):
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?&]+)",
        r"shorts/([^?&]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None

# -------------------- LOAD ENV --------------------

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

# -------------------- FLASK APP --------------------

app = Flask(__name__)
CORS(app)

# -------------------- SUMMARY FUNCTION --------------------

def get_summary(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("🔥 Gemini Error:", e)
        return "Error generating summary."

# -------------------- QUESTION GENERATION FUNCTION --------------------

def generate_questions(summary_text):
    try:
        prompt = f"""
        Based on the following summary, generate 5 meaningful study questions.

        Summary:
        {summary_text}

        Only return the questions in numbered format.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("🔥 Question Generation Error:", e)
        return "Error generating questions."

# -------------------- TEXT ROUTE --------------------

@app.route("/summarize/text", methods=["POST"])
def summarize_text():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "Text is empty"}), 400

        prompt = f"Summarize the following text clearly:\n{text[:4000]}"
        summary = get_summary(prompt)
        questions = generate_questions(summary)

        return jsonify({
            "summary": summary,
            "questions": questions
        })

    except Exception as e:
        print("Text Error:", e)
        return jsonify({"error": "Something went wrong"}), 500

# -------------------- PDF ROUTE --------------------

@app.route("/summarize/pdf", methods=["POST"])
def summarize_pdf():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        doc = fitz.open(stream=file.read(), filetype="pdf")

        text = ""
        for page in doc:
            text += page.get_text()

        if not text.strip():
            return jsonify({"error": "No readable text found"}), 400

        prompt = f"Summarize the following PDF content:\n{text[:4000]}"
        summary = get_summary(prompt)
        questions = generate_questions(summary)

        return jsonify({
            "summary": summary,
            "questions": questions
        })

    except Exception as e:
        print("PDF Error:", e)
        return jsonify({"error": "Something went wrong"}), 500

# -------------------- YOUTUBE ROUTE --------------------

@app.route("/summarize/youtube", methods=["POST"])
def summarize_youtube():
    try:
        data = request.get_json()
        url = data.get("url", "").strip()

        if not url:
            return jsonify({"error": "URL is empty"}), 400

        video_id = extract_video_id(url)

        if not video_id:
            return jsonify({"error": "Invalid YouTube URL"}), 400

        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        try:
            transcript = transcript_list.find_transcript(["en"])
        except:
            transcript = next(iter(transcript_list))

        transcript_data = transcript.fetch()
        text = " ".join([item.text for item in transcript_data])

        if not text.strip():
            return jsonify({"error": "Transcript empty"}), 400

        prompt = f"""
        Summarize the following transcript in English:

        {text[:4000]}
        """

        summary = get_summary(prompt)
        questions = generate_questions(summary)

        return jsonify({
            "summary": summary,
            "questions": questions
        })

    except Exception as e:
        print("🔥 YouTube Error:", e)
        return jsonify({
            "error": "This video does not allow transcript access or captions are unavailable."
        }), 400

# -------------------- RUN SERVER --------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)