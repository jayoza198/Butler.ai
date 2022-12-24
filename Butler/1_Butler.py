import streamlit as st
import os
import openai
import time 
from bokeh.models.widgets import Div


st.set_page_config(page_title="AskMeThing")
openai.api_key = "api key"     
@st.cache(allow_output_mutation=True)
def get_mutable():
    return []

# import streamlit_theme as stt

# stt.set_theme({'primary': '#F63366'})
mutable_object = get_mutable()

engine_dis={'davinci':'''Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and content creative generation, Davinci is going to produce the best results. The trade-off with Davinci is that it costs more to use per API call and other engines are faster.\nAnother area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.''',
						'curie':'''Curie is extremely powerful, yet very fast. While Davinci is stronger when it comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment classification and summarization. Curie is also quite good at answering questions and performing Q&A and as a general service chatbot.''',
						'babbage':'''Babbage can perform straightforward tasks like simple classification. It’s also quite capable when it comes to Semantic Search ranking how well documents match up with search queries.''',
						'ada':'''Ada is usually the fastest model and can perform tasks like parsing text, address correction and certain kinds of classification tasks that don’t require too much nuance. Ada’s performance can often be improved by providing more context.'''}
st.header("AskMeAnything")

# print(list(engine_dis))
st.sidebar.subheader("Advance Options:")
se=st.sidebar.selectbox("Select Engine", options=list(engine_dis))
st.sidebar.info(engine_dis[se])
t=st.sidebar.slider("Max Tokens",min_value=1,value=100,max_value=250)
st.sidebar.write("\n\n"*5)

# st.sidebar.text("\n\n\n")
if st.sidebar.button('Github'):
    #js = "window.open('https://github.com/jainish-jain')"  # New tab or window
    js = "window.location.href = 'https://github.com/jainish-jain'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
if st.sidebar.button('LinkedIn'):
    #js = "window.open('https://github.com/jainish-jain')"  # New tab or window
    js = "window.location.href = 'https://www.linkedin.com/in/jainish-jain/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
if st.sidebar.button("Balloons"):
    st.balloons()
prompt_input=st.text_input("") 
# if st.checkbox("Show Advance Options:"):
#     engine_input=st.selectbox("Engine",['ada','babbage','curie','davinci'])

# st.text(prompt_input)
st.text("\n")
if st.button("Run") and prompt_input.strip()!="":
    if 'jainish' in prompt_input.lower():
        print(prompt_input)
        st.balloons()
        st.info("""Hello there, you found the developer of this application. I Jainish Jain a senior year undergrad student pursuing Bachelor of Technology major in Computer Science Engineering.""")
    else:
        response = openai.Completion.create(
            engine=se ,
            prompt="""I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: """+str(prompt_input)+"\nA:",
            temperature=0.05,
            max_tokens=t,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            best_of=3,
            stop=["\n"]
        )

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.009)
            my_bar.progress(percent_complete + 1)
        # with st.spinner('Wait for it...'):
        #     time.sleep(2)
        #print(response.choices[0].text!=" ",str(response.choices[0].text).strip())
        print(prompt_input)
        if (response.choices[0].text).strip()=="Unknown":
            st.error("Unknown")
            mutable_object.clear()
        elif str(response.choices[0].text).strip()!=" ":
            st.info(response.choices[0].text)
        else:
            st.error("Error\nTry again with hard refresh (Ctrl + F5)")
        # st.write(response)
        mutable_object.clear()