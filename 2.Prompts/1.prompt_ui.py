from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt

model = ChatOllama(model="llama3")

st.title("Ollama Chat Model")
st.header("Interact with the Llama3 Model")


paper_input = st.selectbox("Select Research Paper" , ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners" , "Diffusion Models Beat GANs on Image Synthesis" , "Neural Ordinary Differential Equations"])

style_input = st.selectbox("Select Explanation Style" , ["Beginner-Friendly", "Technical", "Concise Summary" , "Detailed Analysis" , "Visual Explanation" , "Mathematical"])

length_input = st.selectbox("Select Explanation Length" , ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (6+ paragraphs)"])



template = PromptTemplate(template = """
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.""" ,
 input_variables=["paper_input", "style_input", "length_input"])


#template = load_prompt("2.Prompts/research_paper_summary_template.json")



#fill the prompt template with user inputs
prompt =template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})



if st.button("Search"):
    result = model.invoke(prompt)
    st.write(result.content)


# if st.button("Search"):
#     chain = template | model
#     result = chain.invoke(({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# }))
#     st.write(result.content)    


