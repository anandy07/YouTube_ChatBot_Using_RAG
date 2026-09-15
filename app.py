import streamlit as st

from src.youtube import get_video_id, get_transcript
from src.rag import create_vector_store
from src.llm import answer_question


st.set_page_config(
    page_title="YouTube Chatbot",
    page_icon="🎥"
)

st.title("🎥 YouTube Chatbot")
st.write("Ask questions about any YouTube video.")

# Session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "video_id" not in st.session_state:
    st.session_state.video_id = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# YouTube URL
youtube_url = st.text_input(
    "YouTube Video URL",
    placeholder="Paste YouTube URL here..."
)


# Process video
if st.button("Process Video"):

    if not youtube_url:
        st.warning("Please enter a YouTube URL.")

    else:
        video_id = get_video_id(youtube_url)

        if not video_id:
            st.error("Invalid YouTube URL.")

        else:
            try:
                with st.spinner("Processing video..."):

                    transcript = get_transcript(video_id)

                    if not transcript:
                        st.error("Transcript not found.")
                    else:
                        vector_store = create_vector_store(transcript)

                        st.session_state.vector_store = vector_store
                        st.session_state.video_id = video_id
                        st.session_state.chat_history = []

                        st.success("Video processed successfully!")

            except Exception as e:
                st.error(f"Error processing video: {e}")


# Show video
if st.session_state.video_id:

    st.video(
        f"https://www.youtube.com/watch?v={st.session_state.video_id}"
    )

    st.divider()

    st.subheader("Ask a Question")

    question = st.text_input(
        "Your Question",
        placeholder="What is this video about?"
    )

    if st.button("Ask AI"):

        if not question:
            st.warning("Please enter a question.")

        else:
            try:
                with st.spinner("Thinking..."):

                    answer = answer_question(
                        st.session_state.vector_store,
                        question
                    )

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

            except Exception as e:
                st.error(f"Error generating answer: {e}")
