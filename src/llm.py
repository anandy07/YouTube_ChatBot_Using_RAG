from langchain_groq import ChatGroq

from langchain_core.prompts import (
    PromptTemplate
)

from dotenv import load_dotenv


# Load environment variables
load_dotenv()


def answer_question(
    vector_store,
    question
):
    """
    Retrieve relevant transcript chunks
    and generate an answer using Groq.
    """

    # Retrieve relevant documents

    documents = vector_store.similarity_search(
        question,
        k=4
    )

    # Create context

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Groq LLM

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0
    )

    # Prompt

    prompt = PromptTemplate(
        template="""
You are a helpful YouTube video assistant.

Your job is to answer the user's question
using ONLY the provided video transcript.

Rules:

1. Use only the provided context.
2. Do not make up information.
3. If the answer is not available in the
   context, say:

"I couldn't find that information in the video."

4. Give a clear and concise answer.

Video Transcript Context:

{context}

User Question:

{question}

Answer:
""",

        input_variables=[
            "context",
            "question"
        ]
    )

    # Create final prompt

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    # Generate response

    response = llm.invoke(
        final_prompt
    )


    return response.content