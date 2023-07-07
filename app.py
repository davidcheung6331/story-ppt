import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Comic Book Presntation]",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.title('📖  :blue[ Comic Book Presntation]')
st.caption('story created by ChatGPT, illustration by MidJourney')
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSQjFg5sEM2Hdu8JnQnvb-YbU7xRB5l-FpDQ4s74IGFvhB--oZkJXBRz-NSxhEWIvZkmQwqEfPOGkeu/embed?start=true&loop=false&delayms=5000"
, height=580)



st.caption('story created by ChatGPT, illustration by MidJourney')
video_file = open('story-scripts.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
log = """
Following is a System Prompt of a story maker, you will generate the story by following requirement:
You are also an excellent storyteller and graphic novel author. Your primary job is to assist me in crafting a beautiful short story that will be turned into a graphic novel. The graphic novel will contain panels created with Midjourney.

INPUT VARIABLES:
{genre} = Comedy
{theme} = fat mouse catched by a Lazy family Man at garden
{pages} = 4

STORY:
Please come up with a short story based on {theme} that uses elements that are typical for {genre} stories. Provide me with a 3-4 sentence summary , store it in {plot}.

CHARACTER:
Please describe what each character looks like, how old they are, and what sort of clothes they are wearing.

SCENES, DIALOGUE & ACTION:
First break down the story into 12 scenes that would fit onto {pages} pages of a graphic novel.. Describe each scene in 20 words or less. Where suitable, please add brief dialogue that captures the essence of the scene. We will use this dialogue for speech bubbles in the graphic novel. Also describe the actions between characters such as look, talk, hug, hit, follow or any verb phase match the scene.




COVER PAGE IMAGE & TITLE;
Please come up with 3 suggestions for a title for the graphic novel.
Please also describe in 20 words or less what the cover image looks like.


OUTPUT:
please provide the content in this sequence : story,  character, scenes and dialogue , cover page image & title in English.
then  translate all above generated  content  into  traditional Chinese version following format:

English Version:
story,  character, scenes and dialogue , cover page image

Chinese Version:
story,  character, scenes and dialogue , cover page image

USER INPUT:
Example of user input format:
{genre:action, theme: fat mouse catched by a Lazy family Man at garden , pages:4}


"""


with st.expander("ChatGPT prompt for MidJourney"):
    st.code(log)
