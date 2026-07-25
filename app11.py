import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from gtts import gTTS

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Fluency Engine", layout="wide")

# --- IMAGE HANDLING ---
IMAGE_URL = "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=1200&auto=format&fit=crop"

def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# Function to generate audio bytes from text using gTTS
def text_to_speech_audio(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# --- SCREEN 1: LOGIN & WELCOME ---
if not st.session_state.logged_in:
    st.title("Welcome to Fluency Engine")
    st.write("Please enter your details to get started.")

    with st.form("user_info_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        submitted = st.form_submit_button("Enter App")

    if submitted:
        if name and email:
            st.session_state.logged_in = True
            st.session_state.user_name = name
            st.rerun()
        else:
            st.error("Please fill in both fields before continuing.")

# --- SCREEN 2: APP FLOW (POST-LOGIN) ---
else:
    st.title(f"Welcome, {st.session_state.user_name}!")

    # Navigation tabs for the app structure (updated to 17 tabs including Grammar 14)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17 = st.tabs([
        "🌟 Mission & Vision", 
        "📚 Grammar Lesson 1", 
        "✍️ Quiz Time 1", 
        "📚 Grammar Lesson 2", 
        "✍️ Quiz Time 2",
        "📚 Grammar Lesson 3",
        "📚 Grammar Lesson 4",
        "📚 Grammar Lesson 5",
        "📚 Grammar Lesson 6",
        "📚 Grammar Lesson 7",
        "📚 Grammar Lesson 8",
        "📚 Grammar Lesson 9",
        "📚 Grammar Lesson 10",
        "📚 Grammar Lesson 11",
        "📚 Grammar Lesson 12",
        "📚 Grammar Lesson 13",
        "📚 Grammar Lesson 14"
    ])

    # --- TAB 1: VISION & PURPOSE ---
    with tab1:
        col1, col2 = st.columns([2, 3]) 

        with col1:
            st.subheader("The Vision")
            image_obj = load_image_from_url(IMAGE_URL)
            if image_obj:
                st.image(image_obj, caption="Bridging the gap to confident speech.", use_column_width=True)
            else:
                st.warning("Image could not be loaded, but the purpose remains!")

        with col2:
            st.header("Our Mission & Purpose")
            st.markdown("""
            The purpose of this application is to bridge the critical gap between passive vocabulary and active, 
            confident speech, empowering learners to articulate complex thoughts with absolute precision and effortless spontaneity. 
            
            By moving beyond traditional rote memorization, the platform is engineered to immerse users in dynamic, 
            targeted practice that accelerates the transition from intermediate comprehension to an advanced, native-like command of spoken English. 
            
            Ultimately, it serves as a sophisticated digital environment designed to eliminate verbal hesitation, 
            refine natural linguistic patterns, and elevate daily communication to a seamless, professional standard.
            """)

    # --- TAB 2: GRAMMAR LESSON 1 ---
    with tab2:
        st.header("Grammar 1: Core Pronouns & Question Words")
        st.write("Explore foundational sentence structures comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        g_col1, g_col2 = st.columns(2)

        with g_col1:
            with st.container(border=True):
                st.markdown("### 1. THIS = ይህ")
                st.markdown("**English Example:**")
                st.info("This book is good.")
                st.markdown("**Amharic Translation:**")
                st.success("ይህ መጽሐፍ ጥሩ ነው።")

            with st.container(border=True):
                st.markdown("### 3. WHO = ማን")
                st.markdown("**English Example:**")
                st.info("Who is it? / Who is he/she?")
                st.markdown("**Amharic Translation:**")
                st.success("ማን ነው?")

        with g_col2:
            with st.container(border=True):
                st.markdown("### 2. THAT = ያ")
                st.markdown("**English Example:**")
                st.info("That house is big.")
                st.markdown("**Amharic Translation:**")
                st.success("ያ ቤት ትልቅ ነው።")

            with st.container(border=True):
                st.markdown("### 4. WHAT = ምን")
                st.markdown("**English Example:**")
                st.info("What do you want?")
                st.markdown("**Amharic Translation (Gender-Specific):**")
                st.success("ምን ፈልግሃለህ? *(Male)*\n\nምን ፈልግሻለሽ? *(Female)*")

    # --- TAB 3: QUIZ TIME 1 ---
    with tab3:
        st.header("Quiz Time 1: Comprehensive Translation Practice")
        st.write("Type your translation and press **Enter** to instantly reveal the English translation and listen to its pronunciation!")
        
        st.markdown("<br>", unsafe_allow_html=True)

        quiz_categories_1 = [
            ("Category 1: ይህ (This)", [
                ("ይህ መጽሐፍ የኔ ነው።", "This book is mine."),
                ("ይህ ምንድን ነው?", "What is this?"),
                ("ይህ በጣም ውብ ነው።", "This is very beautiful."),
                ("ይህ ምግብ ጣፋጭ ነው።", "This food is delicious."),
                ("ይህ ስልክ አዲስ ነው።", "This phone is new."),
                ("ይህ ቤት ትልቅ ነው።", "This house is big."),
                ("ይህ የእርስዎ ቁልፍ ነው?", "Is this your key?"),
                ("ይህ ስራ በጣም ከባድ ነው።", "This work is very hard."),
                ("ይህ ውሃ ቀዝቃዛ ነው።", "This water is cold."),
                ("ይህ ቀን በጣም ደስ የሚል ነው።", "This day is very pleasant.")
            ]),
            ("Category 2: ያ (That)", [
                ("ያ መጽሐፍ የኔ ነው።", "That book is mine."),
                ("ያ ምንድን ነው?", "What is that?"),
                ("ያ በጣም ውብ ነው።", "That is very beautiful."),
                ("ያ ምግብ ጣፋጭ ነው።", "That food is delicious."),
                ("ያ ስልክ አዲስ ነው።", "That phone is new."),
                ("ያ ቤት ትልቅ ነው።", "That house is big."),
                ("ያ የእርስዎ ቁልፍ ነው?", "Is that your key?"),
                ("ያ ስራ በጣም ከባድ ነው።", "That work is very hard."),
                ("ያ ውሃ ቀዝቃዛ ነው።", "That water is cold."),
                ("ያ ቀን በጣም ደስ የሚል ነበር።", "That day was very pleasant.")
            ]),
            ("Category 3: ማን (Who)", [
                ("ይህንን ያደረገው ማን ነው?", "Who did this?"),
                ("ማን መጣ?", "Who came?"),
                ("ይህ ስልክ የማን ነው?", "Whose phone is this?"),
                ("ማን ሊረዳኝ ይችላል?", "Who can help me?"),
                ("ማን ጋር እየተነጋገረህ ነው?", "Who are you talking to?"),
                ("ከእነሱ ጋር ማን ሄደ?", "Who went with them?"),
                ("ይህን የጻፈው ማን ነው?", "Who wrote this?"),
                ("በሩን አንኳኳው ማን ነው?", "Who knocked on the door?"),
                ("ነገ ማን ይመጣል?", "Who is coming tomorrow?"),
                ("እዚህ ያለውን ሰው ማን ያውቀዋል?", "Who knows the person here?")
            ]),
            ("Category 4: ምን (What)", [
                ("ይህ ምንድን ነው?", "What is this?"),
                ("ምን እየሰራህ ነው?", "What are you doing?"),
                ("ምን እንብላ?", "What shall we eat?"),
                ("ችግሩ ምንድን ነው?", "What is the problem?"),
                ("ምን ለማለት ፈልገሃል?", "What do you mean?"),
                ("ነገ ምን ታደርጋለህ?", "What will you do tomorrow?"),
                ("አስተያየትህ ምንድን ነው?", "What is your opinion?"),
                ("እሱን ለማድረግ ምን ያስፈልጋል?", "What is needed to do that?"),
                ("የምታወራው ስለ ምን ሠው ነው?", "What person are you talking about?"),
                ("በኋላ ምን እንድርግ?", "What shall we do later?")
            ])
        ]

        global_counter_1 = 1
        for cat_title, questions in quiz_categories_1:
            st.subheader(cat_title)
            for amharic_text, english_answer in questions:
                with st.container(border=True):
                    st.markdown(f"**Question {global_counter_1}**")
                    st.markdown(f"### 🇪🇹 {amharic_text}")
                    
                    user_input = st.text_input(f"Your English translation for Q{global_counter_1}:", key=f"user_ans_1_{global_counter_1}")
                    
                    if user_input:
                        st.markdown("**English translation is:**")
                        st.success(english_answer)
                        
                        st.markdown("🔊 **Listen to Pronunciation:**")
                        audio_data = text_to_speech_audio(english_answer)
                        st.audio(audio_data, format="audio/mp3")
                
                global_counter_1 += 1
            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 4: GRAMMAR LESSON 2 ---
    with tab4:
        st.header("Grammar 2: Prepositions & Quantifiers")
        st.write("Explore spatial prepositions and quantity expressions comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        g2_col1, g2_col2 = st.columns(2)

        with g2_col1:
            with st.container(border=True):
                st.markdown("### 1. IN = ውስጥ")
                st.markdown("**English Example:**")
                st.info("The book is in the house")
                st.markdown("**Amharic Translation:**")
                st.success("መጽሐፉ ቤት ውስጥ አለ።")

            with st.container(border=True):
                st.markdown("### 3. How many = ስንት")
                st.markdown("**Amharic Example:**")
                st.info("ስንት መጽሐፍ አሎት?")
                st.markdown("**English Translation:**")
                st.success("How many books do you have?")

        with g2_col2:
            with st.container(border=True):
                st.markdown("### 2. AT = (Location)")
                st.markdown("**English Example:**")
                st.info("She is at home.")
                st.markdown("**Amharic Translation:**")
                st.success("እሳ ቤት ነች።")

            with st.container(border=True):
                st.markdown("### 4. How much = ስንት")
                st.markdown("**Amharic Example:**")
                st.info("የዚህ ዋጋ ስንት ነው?")
                st.markdown("**English Translation:**")
                st.success("How much is this?")

    # --- TAB 5: QUIZ TIME 2 ---
    with tab5:
        st.header("Quiz Time 2: Prepositions & Location Translation Practice")
        st.write("Test your translation capabilities for **IN (ውስጥ)** and **AT (Location)** sentences. Type your translation and press **Enter** to reveal the English translation!")
        
        st.markdown("<br>", unsafe_allow_html=True)

        quiz_categories_2 = [
            ("Category 1: IN (ውስጥ)", [
                ("ድመቷ በቤቱ ውስጥ ትገኛለች።", "The cat is in the house."),
                ("ቁልፎቹ በኪሱ ውስጥ አሉ።", "The keys are in his pocket."),
                ("ሻይው በብርጭቆው ውስጥ ነው።", "The tea is in the glass."),
                ("ሰነዶቹ በፎልደሩ ውስጥ አሉ።", "The documents are in the folder."),
                ("አስተማሪው በክፍል ውስጥ አለ።", "The teacher is in the classroom."),
                ("እሱ በቢሮ ውስጥ እየሰራ ነው።", "He is working in the office."),
                ("አፖቹ በቅርጫቱ ውስጥ አሉ።", "The apples are in the basket."),
                ("መፅሐፉ በከረጢቱ ውስጥ ተቀምጧል።", "The book is placed in the bag."),
                ("ልጁ በኩሬው ውስጥ ይጫወታል።", "The boy plays in the puddle."),
                ("እሷ በገበያ ውስጥ ትገኛለች።", "She is in the market.")
            ]),
            ("Category 2: AT (Location)", [
                ("ቤት ነኝ።", "I am at home."),
                ("ሥራ ላይ ነኝ።", "I am at work."),
                ("ትምህርት ቤት ነኝ።", "I am at school."),
                ("በሩ ላይ ቆሜያለሁ።", "I am standing at the door."),
                ("ጠረጴዛው ላይ ተቀምጫለሁ።", "I am sitting at the table."),
                ("አውቶቡስ ማቆሚያ ላይ እየጠበኩ ነው።", "I am waiting at the bus stop."),
                ("ሆስፒታል ነኝ።", "I am at the hospital."),
                ("ዩኒቨርሲቲ ነኝ።", "I am at the university."),
                ("ፓርኩ ነኝ።", "I am at the park."),
                ("መኪና ማቆሚያ ላይ ነኝ።", "I am at the parking lot.")
            ])
        ]

        global_counter_2 = 1
        for cat_title, questions in quiz_categories_2:
            st.subheader(cat_title)
            for amharic_text, english_answer in questions:
                with st.container(border=True):
                    st.markdown(f"**Question {global_counter_2}**")
                    st.markdown(f"### 🇪🇹 {amharic_text}")
                    
                    user_input_2 = st.text_input(f"Your English translation for Q{global_counter_2}:", key=f"user_ans_2_{global_counter_2}")
                    
                    if user_input_2:
                        st.markdown("**English translation is:**")
                        st.success(english_answer)
                        
                        st.markdown("🔊 **Listen to Pronunciation:**")
                        audio_data = text_to_speech_audio(english_answer)
                        st.audio(audio_data, format="audio/mp3")
                
                global_counter_2 += 1
            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 6: GRAMMAR LESSON 3 ---
    with tab6:
        st.header("Grammar 3: Verb 'To Be' Sentence Structures")
        st.write("Master affirmative, negative, and interrogative sentence structures across all subject pronouns using a clear comparative layout.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        pronoun_data = [
            {
                "pronoun": "I (እኔ)",
                "affirmative_en": "I am a teacher",
                "affirmative_am": "እኔ መምህር ነኝ",
                "negative_en": "I am not a teacher",
                "negative_am": "እኔ መምህር አይደለሁም",
                "aff_q_en": "Am I a teacher?",
                "aff_q_am": "እኔ መምህር ነኝ?",
                "neg_q_en": "Am I not a teacher?",
                "neg_q_am": "እኔ መምህር አይደለሁም?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "affirmative_en": "You are a teacher",
                "affirmative_am": "አንተ/አንቺ መምህር ነህ/ነሽ",
                "negative_en": "You are not a teacher",
                "negative_am": "አንተ/አንቺ መምህር አይደለህም/አይደለሽም",
                "aff_q_en": "Are you a teacher?",
                "aff_q_am": "አንተ/አንቺ መምህር ነህ/ነሽ?",
                "neg_q_en": "Are you not a teacher?",
                "neg_q_am": "አንተ/አንቺ መምህር አይደለህም/አይደለሽም?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ)",
                "affirmative_en": "He/She is a teacher",
                "affirmative_am": "እሱ/እሷ መምህር ነው/ናት",
                "negative_en": "He/She is not a teacher",
                "negative_am": "እሱ/እሷ መምህር አይደለም/አይደለችም",
                "aff_q_en": "Is he/she a teacher?",
                "aff_q_am": "እሱ/እሷ መምህር ነው/ናት?",
                "neg_q_en": "Is he/she not a teacher?",
                "neg_q_am": "እሱ/እሷ መምህር አይደለም/አይደለችም?"
            },
            {
                "pronoun": "We (እኛ)",
                "affirmative_en": "We are teachers",
                "affirmative_am": "እኛ መምህራን ነን",
                "negative_en": "We are not teachers",
                "negative_am": "እኛ መምህራን አይደለንም",
                "aff_q_en": "Are we teachers?",
                "aff_q_am": "እኛ መምህራን ነን?",
                "neg_q_en": "Are we not teachers?",
                "neg_q_am": "እኛ መምህራን አይደለንም?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "affirmative_en": "You are teachers",
                "affirmative_am": "እናንተ መምህራን ናችሁ",
                "negative_en": "You are not teachers",
                "negative_am": "እናንተ መምህራን አይደላችሁም",
                "aff_q_en": "Are you teachers?",
                "aff_q_am": "እናንተ መምህራን ናችሁ?",
                "neg_q_en": "Are you not teachers?",
                "neg_q_am": "እናንተ መምህራን አይደላችሁም?"
            },
            {
                "pronoun": "They (እነሱ)",
                "affirmative_en": "They are teachers",
                "affirmative_am": "እነሱ መምህራን ናቸው",
                "negative_en": "They are not teachers",
                "negative_am": "እነሱ መምህራን አይደሉም",
                "aff_q_en": "Are they teachers?",
                "aff_q_am": "እነሱ መምህራን ናቸው?",
                "neg_q_en": "Are they not teachers?",
                "neg_q_am": "እነሱ መምህራን አይደሉም?"
            }
        ]

        for item in pronoun_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አዎንታዊ)")
                    st.info(item['affirmative_en'])
                    st.success(item['affirmative_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አዎንታዊ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['negative_en'])
                    st.success(item['negative_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 7: GRAMMAR LESSON 4 ---
    with tab7:
        st.header("Grammar 4: Present Continuous Tense ('To Be' + Verb-ing)")
        st.write("Master affirmative, negative, and interrogative continuous action structures across all subject pronouns using a clear comparative layout.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        continuous_data = [
            {
                "pronoun": "I (እኔ)",
                "affirmative_en": "I am coming",
                "affirmative_am": "እኔ እየመጣሁ ነው",
                "negative_en": "I am not coming",
                "negative_am": "እኔ እየመጣሁ አይደለም",
                "aff_q_en": "Am I coming?",
                "aff_q_am": "እኔ እየመጣሁ ነው?",
                "neg_q_en": "Am I not coming?",
                "neg_q_am": "እኔ እየመጣሁ አይደለም?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "affirmative_en": "You are coming",
                "affirmative_am": "አንተ/አንቺ እየመጣህ/እየመጣሽ ነው",
                "negative_en": "You are not coming",
                "negative_am": "አንተ/አንቺ እየመጣህ/እየመጣሽ አይደለም",
                "aff_q_en": "Are you coming?",
                "aff_q_am": "አንተ/አንቺ እየመጣህ/እየመጣሽ ነው?",
                "neg_q_en": "Are you not coming?",
                "neg_q_am": "አንተ/አንቺ እየመጣህ/እየመጣሽ አይደለም?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ)",
                "affirmative_en": "He/She is coming",
                "affirmative_am": "እሱ/እሷ እየመጣ/እየመጣች ነው",
                "negative_en": "He/She is not coming",
                "negative_am": "እሱ/እሷ እየመጣ/እየመጣች አይደለም",
                "aff_q_en": "Is he/she coming?",
                "aff_q_am": "እሱ/እሷ እየመጣ/እየመጣች ነው?",
                "neg_q_en": "Is he/she not coming?",
                "neg_q_am": "እሱ/እሷ እየመጣ/እየመጣች አይደለም?"
            },
            {
                "pronoun": "We (እኛ)",
                "affirmative_en": "We are coming",
                "affirmative_am": "እኛ እየመጣን ነው",
                "negative_en": "We are not coming",
                "negative_am": "እኛ እየመጣን አይደለም",
                "aff_q_en": "Are we coming?",
                "aff_q_am": "እኛ እየመጣን ነው?",
                "neg_q_en": "Are we not coming?",
                "neg_q_am": "እኛ እየመጣን አይደለም?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "affirmative_en": "You are coming",
                "affirmative_am": "እናንተ እየመጣችሁ ነው",
                "negative_en": "You are not coming",
                "negative_am": "እናንተ እየመጣችሁ አይደለም",
                "aff_q_en": "Are you coming?",
                "aff_q_am": "እናንተ እየመጣችሁ ነው?",
                "neg_q_en": "Are you not coming?",
                "neg_q_am": "እናንተ እየመጣችሁ አይደለም?"
            },
            {
                "pronoun": "They (እነሱ)",
                "affirmative_en": "They are coming",
                "affirmative_am": "እነሱ እየመጡ ናቸው",
                "negative_en": "They are not coming",
                "negative_am": "እነሱ እየመጡ አይደለም",
                "aff_q_en": "Are they coming?",
                "aff_q_am": "እነሱ እየመጡ ናቸው?",
                "neg_q_en": "Are they not coming?",
                "neg_q_am": "እነሱ እየመጡ አይደለም?"
            }
        ]

        for item in continuous_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አዎንታዊ)")
                    st.info(item['affirmative_en'])
                    st.success(item['affirmative_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አዎንታዊ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['negative_en'])
                    st.success(item['negative_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 8: GRAMMAR LESSON 5 ---
    with tab8:
        st.header("Grammar 5: Directional Prepositions (To / From)")
        st.write("Explore directional movement comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        g5_col1, g5_col2 = st.columns(2)

        with g5_col1:
            with st.container(border=True):
                st.markdown("### 1. TO = ወደ")
                st.markdown("**English Example:**")
                st.info("I am going to home.")
                st.markdown("**Amharic Translation:**")
                st.success("እኔ ወደ ቤት እየሄድኩ ነው")

        with g5_col2:
            with st.container(border=True):
                st.markdown("### 2. FROM = ከ")
                st.markdown("**English Example:**")
                st.info("I am coming from home.")
                st.markdown("**Amharic Translation:**")
                st.success("እኔ ከቤት እየመጣሁ ነው።")

    # --- TAB 9: GRAMMAR LESSON 6 ---
    with tab9:
        st.header("Grammar 6: Pronoun Forms, Possessives & Reflexives")
        st.write("Explore subjective pronouns, possessive adjectives, possessive pronouns, and reflexive pronouns comparing English and Amharic.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        pronoun_forms_data = [
            {
                "subject": "I (እኔ)",
                "poss_adj": "My (የእኔ)",
                "poss_pron": "Mine (የኔ)",
                "reflexive": "Myself (ራሴ)"
            },
            {
                "subject": "You (አንተ / አንቺ)",
                "poss_adj": "Your (የእርስዎ / የአንተ / የአንቺ)",
                "poss_pron": "Yours (ያንተ / ያንቺ / የእርስዎ)",
                "reflexive": "Yourself (ራስህን / ራስሽ)"
            },
            {
                "subject": "He (እሱ)",
                "poss_adj": "His (የእሱ)",
                "poss_pron": "His (የሱ)",
                "reflexive": "Himself (ራሱ)"
            },
            {
                "subject": "She (እሷ)",
                "poss_adj": "Her (የእሷ)",
                "poss_pron": "Hers (የሷ)",
                "reflexive": "Herself (ራሷ)"
            },
            {
                "subject": "It (እሱ/እሷ ለዕቃ)",
                "poss_adj": "Its (የእሱ/የእሷ)",
                "poss_pron": "— (—)",
                "reflexive": "Itself (ራሱ)"
            },
            {
                "subject": "We (እኛ)",
                "poss_adj": "Our (የእኛ)",
                "poss_pron": "Ours (የኛ)",
                "reflexive": "Ourselves (ራሳችን)"
            },
            {
                "subject": "You (እናንተ - Plural)",
                "poss_adj": "Your (የናንተ / የእርስዎን)",
                "poss_pron": "Yours (የናንተ / የእርስዎን)",
                "reflexive": "Yourselves (ራሳችሁ / ራስዎ)"
            },
            {
                "subject": "They (እነሱ)",
                "poss_adj": "Their (የእነሱ)",
                "poss_pron": "Theirs (የነሱ)",
                "reflexive": "Themselves (ራሳቸው)"
            }
        ]

        for item in pronoun_forms_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Subject: {item['subject']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### 📌 Possessive Adjective (ባለቤትነት ማሳያ ቅጽል)")
                    st.info(item['poss_adj'].split('(')[0].strip())
                    st.success(item['poss_adj'])
                    
                    st.markdown("##### 🏷️ Possessive Pronoun (ባለቤትነት ማሳያ ቅጽል ስም)")
                    st.info(item['poss_pron'].split('(')[0].strip())
                    st.success(item['poss_pron'])

                with col_b:
                    st.markdown("##### 🪞 Reflexive Pronoun (አንጸባራቂ ቅጽል ስም)")
                    st.info(item['reflexive'].split('(')[0].strip())
                    st.success(item['reflexive'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 10: GRAMMAR LESSON 7 (COMMANDS / JUSSIVE FORMS) ---
    with tab10:
        st.header("Grammar 7: Imperatives & Jussive Structures (Imperative & Permission/Request Forms)")
        st.write("Explore command and jussive structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_7_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "let me come",
                "aff_am": "ልምጣ",
                "neg_en": "let me not come",
                "neg_am": "አልምጣ",
                "aff_q_en": "should I come?",
                "aff_q_am": "ልምጣ ወይ? / ልምጣ?",
                "neg_q_en": "should I not come?",
                "neg_q_am": "አልምጣ ወይ? / አልምጣ?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "come",
                "aff_am": "ንዑ / ኑ",
                "neg_en": "don't come",
                "neg_am": "አትምጡ (ወይም ኑ/አትምጡ)",
                "aff_q_en": "—",
                "aff_q_am": "—",
                "neg_q_en": "—",
                "neg_q_am": "—"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ / እሱ)",
                "aff_en": "let him/her come",
                "aff_am": "ይምጣ / ትምጣ",
                "neg_en": "let him/her not come",
                "neg_am": "አትምጣ / አይምጣ",
                "aff_q_en": "should he/she come?",
                "aff_q_am": "ይምጣ ወይ?",
                "neg_q_en": "should he/she not come?",
                "neg_q_am": "አትምጣ ወይ?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "let us come",
                "aff_am": "እንምጣ / እንሂድ (እንምጣ)",
                "neg_en": "let us not come",
                "neg_am": "አንምጣ",
                "aff_q_en": "should we come?",
                "aff_q_am": "እንምጣ ወይ? / እንምጣ?",
                "neg_q_en": "should we not come?",
                "neg_q_am": "አንምጣ ወይ? / አንምጣ?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "come",
                "aff_am": "ኑ",
                "neg_en": "don't come",
                "neg_am": "አትምጡ",
                "aff_q_en": "—",
                "aff_q_am": "—",
                "neg_q_en": "—",
                "neg_q_am": "—"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "let them come",
                "aff_am": "ይምጡ",
                "neg_en": "let them not come",
                "neg_am": "አይምጡ",
                "aff_q_en": "should they come?",
                "aff_q_am": "ይምጡ ወይ?",
                "neg_q_en": "should they not come?",
                "neg_q_am": "አይምጡ ወይ?"
            }
        ]

        for item in grammar_7_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 11: GRAMMAR LESSON 8 (SIMPLE PAST TENSE) ---
    with tab11:
        st.header("Grammar 8: Simple Past Tense ('To Come' Paradigms)")
        st.write("Explore simple past tense sentence structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_8_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "came",
                "aff_am": "መጣሁ",
                "neg_en": "didn't come",
                "neg_am": "አልመጣሁም",
                "aff_q_en": "did I come?",
                "aff_q_am": "መጣሁ?",
                "neg_q_en": "didn't I come?",
                "neg_q_am": "አልመጣሁም?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "came",
                "aff_am": "መጣህ / መጣሽ",
                "neg_en": "didn't come",
                "neg_am": "አልመጣህም / አልመጣሽም",
                "aff_q_en": "did you come?",
                "aff_q_am": "መጣህ / መጣሽ?",
                "neg_q_en": "didn't you come?",
                "neg_q_am": "አልመጣህም / አልመጣሽም?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ / እሱ)",
                "aff_en": "came",
                "aff_am": "መጣ / መጣች",
                "neg_en": "didn't come",
                "neg_am": "አልመጣም / አልመጣችም",
                "aff_q_en": "did he/she/it come?",
                "aff_q_am": "መጣ / መጣች?",
                "neg_q_en": "didn't he/she/it come?",
                "neg_q_am": "አልመጣም / አልመጣችም?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "came",
                "aff_am": "መጣን",
                "neg_en": "didn't come",
                "neg_am": "አልመጣንም",
                "aff_q_en": "did we come?",
                "aff_q_am": "መጣን?",
                "neg_q_en": "didn't we come?",
                "neg_q_am": "አልመጣንም?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "came",
                "aff_am": "መጣችሁ",
                "neg_en": "didn't come",
                "neg_am": "አልመጣችሁም",
                "aff_q_en": "did you come?",
                "aff_q_am": "መጣችሁ?",
                "neg_q_en": "didn't you come?",
                "neg_q_am": "አልመጣችሁም?"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "came",
                "aff_am": "መጡ",
                "neg_en": "didn't come",
                "neg_am": "አልመጡም",
                "aff_q_en": "did they come?",
                "aff_q_am": "መጡ?",
                "neg_q_en": "didn't they come?",
                "neg_q_am": "አልመጡም?"
            }
        ]

        for item in grammar_8_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 12: GRAMMAR LESSON 9 (PAST STATE - 'TO BE SICK') ---
    with tab12:
        st.header("Grammar 9: Past State Tense ('To Be Sick' Paradigms)")
        st.write("Explore past state sentence structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_9_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "I was sick",
                "aff_am": "ታምሜ ነበር",
                "neg_en": "I wasn't sick",
                "neg_am": "አልታመምኩም ነበር",
                "aff_q_en": "was I sick?",
                "aff_q_am": "ታምሜ ነበር?",
                "neg_q_en": "wasn't I sick?",
                "neg_q_am": "አልታመምኩም ነበር?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "you were sick",
                "aff_am": "ታመህ / ታመሽ ነበር",
                "neg_en": "you weren't sick",
                "neg_am": "አልታመምክም / አልታመምሽም ነበር",
                "aff_q_en": "were you sick?",
                "aff_q_am": "ታመህ / ታመሽ ነበር?",
                "neg_q_en": "weren't you sick?",
                "neg_q_am": "አልታመምክም / አልታመምሽም ነበር?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ / እሱ)",
                "aff_en": "he/she/it was sick",
                "aff_am": "ታሞ / ታማ ነበር",
                "neg_en": "he/she/it wasn't sick",
                "neg_am": "አልታመመም / አልታመመችም ነበር",
                "aff_q_en": "was he/she/it sick?",
                "aff_q_am": "ታሞ / ታማ ነበር?",
                "neg_q_en": "wasn't he/she/it sick?",
                "neg_q_am": "አልታመመም / አልታመመችም ነበር?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "we were sick",
                "aff_am": "ታመን ነበር",
                "neg_en": "we weren't sick",
                "neg_am": "አልታመምንም ነበር",
                "aff_q_en": "were we sick?",
                "aff_q_am": "ታመን ነበር?",
                "neg_q_en": "weren't we sick?",
                "neg_q_am": "አልታመምንም ነበር?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "you were sick",
                "aff_am": "ታማችሁ ነበር",
                "neg_en": "you weren't sick",
                "neg_am": "አልታመምችሁም ነበር",
                "aff_q_en": "were you sick?",
                "aff_q_am": "ታማችሁ ነበር?",
                "neg_q_en": "weren't you sick?",
                "neg_q_am": "አልታመምችሁም ነበር?"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "they were sick",
                "aff_am": "ታመው ነበር",
                "neg_en": "they weren't sick",
                "neg_am": "አልታመሙም ነበር",
                "aff_q_en": "were they sick?",
                "aff_q_am": "ታመው ነበር?",
                "neg_q_en": "weren't they sick?",
                "neg_q_am": "አልታመሙም ነበር?"
            }
        ]

        for item in grammar_9_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 13: GRAMMAR LESSON 10 (SIMPLE FUTURE TENSE - 'TO COME') ---
    with tab13:
        st.header("Grammar 10: Simple Future Tense ('To Come' Paradigms)")
        st.write("Explore simple future tense sentence structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_10_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "I will come",
                "aff_am": "እመጣለሁ",
                "neg_en": "I won't come",
                "neg_am": "አልመጣም",
                "aff_q_en": "will I come?",
                "aff_q_am": "እመጣለሁ?",
                "neg_q_en": "won't I come?",
                "neg_q_am": "አልመጣም?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "you will come",
                "aff_am": "ትመጣለህ / ትመጣለሽ",
                "neg_en": "you won't come",
                "neg_am": "አልመጣም / አልመጣሽም (አትመጣም / አትመጣሽም)",
                "aff_q_en": "will you come?",
                "aff_q_am": "ትመጣለህ / ትመጣለሽ?",
                "neg_q_en": "won't you come?",
                "neg_q_am": "አትመጣም / አትመጣሽም?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ / እሱ)",
                "aff_en": "he/she/it will come",
                "aff_am": "ይመጣል / ትመጣለች",
                "neg_en": "he/she/it won't come",
                "neg_am": "አይመጣም / አትመጣም",
                "aff_q_en": "will he/she/it come?",
                "aff_q_am": "ይመጣል / ትመጣለች?",
                "neg_q_en": "won't he/she/it come?",
                "neg_q_am": "አይመጣም / አትመጣም?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "we will come",
                "aff_am": "እንመጣለን",
                "neg_en": "we won't come",
                "neg_am": "አልመጣም (አንመጣም)",
                "aff_q_en": "will we come?",
                "aff_q_am": "እንመጣለን?",
                "neg_q_en": "won't we come?",
                "neg_q_am": "አንመጣም?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "you will come",
                "aff_am": "ትመጣላችሁ",
                "neg_en": "you won't come",
                "neg_am": "አትመጡም",
                "aff_q_en": "will you come?",
                "aff_q_am": "ትመጣላችሁ?",
                "neg_q_en": "won't you come?",
                "neg_q_am": "አትመጡም?"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "they will come",
                "aff_am": "ይመጣሉ",
                "neg_en": "they won't come",
                "neg_am": "አይመጡም",
                "aff_q_en": "will they come?",
                "aff_q_am": "ይመጣሉ?",
                "neg_q_en": "won't they come?",
                "neg_q_am": "አይመጡም?"
            }
        ]

        for item in grammar_10_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 14: GRAMMAR LESSON 11 (SIMPLE FUTURE STATE - 'TO BE HAPPY') ---
    with tab14:
        st.header("Grammar 11: Simple Future State ('To Be Happy' Paradigms)")
        st.write("Explore simple future state sentence structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_11_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "I will be happy",
                "aff_am": "ደስተኛ እሆናለሁ",
                "neg_en": "I won't be happy",
                "neg_am": "ደስተኛ አልሆንም",
                "aff_q_en": "will I be happy?",
                "aff_q_am": "ደስተኛ እሆናለሁ?",
                "neg_q_en": "won't I be happy?",
                "neg_q_am": "ደስተኛ አልሆንም?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "you will be happy",
                "aff_am": "ደስተኛ ትሆናለህ / ትሆናለሽ",
                "neg_en": "you won't be happy",
                "neg_am": "ደስተኛ አትሆንም / አትሆኚም",
                "aff_q_en": "will you be happy?",
                "aff_q_am": "ደስተኛ ትሆናለህ / ትሆናለሽ?",
                "neg_q_en": "won't you be happy?",
                "neg_q_am": "ደስተኛ አትሆንም / አትሆኚም?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ / እሱ)",
                "aff_en": "he/she/it will be happy",
                "aff_am": "ደስተኛ ይሆናል / ትሆናለች",
                "neg_en": "he/she/it won't be happy",
                "neg_am": "ደስተኛ አይሆንም / አትሆንም",
                "aff_q_en": "will he/she/it be happy?",
                "aff_q_am": "ደስተኛ ይሆናል / ትሆናለች?",
                "neg_q_en": "won't he/she/it be happy?",
                "neg_q_am": "ደስተኛ አይሆንም / አትሆንም?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "we will be happy",
                "aff_am": "ደስተኛ እንሆናለን",
                "neg_en": "we won't be happy",
                "neg_am": "ደስተኛ አንሆንም",
                "aff_q_en": "will we be happy?",
                "aff_q_am": "ደስተኛ እንሆናለን?",
                "neg_q_en": "won't we be happy?",
                "neg_q_am": "ደስተኛ አንሆንም?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "you will be happy",
                "aff_am": "ደስተኛ ትሆናላችሁ",
                "neg_en": "you won't be happy",
                "neg_am": "ደስተኛ አትሆኑም",
                "aff_q_en": "will you be happy?",
                "aff_q_am": "ደስተኛ ትሆናላችሁ?",
                "neg_q_en": "won't you be happy?",
                "neg_q_am": "ደስተኛ አትሆኑም?"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "they will be happy",
                "aff_am": "ደስተኛ ይሆናሉ",
                "neg_en": "they won't be happy",
                "neg_am": "ደስተኛ አይሆኑም",
                "aff_q_en": "will they be happy?",
                "aff_q_am": "ደስተኛ ይሆናሉ?",
                "neg_q_en": "won't they be happy?",
                "neg_q_am": "ደስተኛ አይሆኑም?"
            }
        ]

        for item in grammar_11_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 15: GRAMMAR LESSON 12 (SIMPLE PRESENT TENSE - 'TO SPEAK') ---
    with tab15:
        st.header("Grammar 12: Simple Present Tense ('To Speak' Paradigms)")
        st.write("Explore simple present tense sentence structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_12_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "I speak",
                "aff_am": "እናገራለሁ",
                "neg_en": "I don't speak",
                "neg_am": "አላወራም (አይናገርም)",
                "aff_q_en": "do I speak?",
                "aff_q_am": "እናገራለሁ ?",
                "neg_q_en": "don't I speak?",
                "neg_q_am": "አላወራም ?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "you speak",
                "aff_am": "ትናገራለህ / ትናገራለሽ",
                "neg_en": "you don't speak",
                "neg_am": "አትናገርም / አትናገሪም",
                "aff_q_en": "do you speak?",
                "aff_q_am": "ትናገራለህ/ትናገራለሽ ?",
                "neg_q_en": "don't you speak?",
                "neg_q_am": "አትናገርም/አትናገሪም ?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ)",
                "aff_en": "he/she/it speaks",
                "aff_am": "ይናገራል / ትናገራለች",
                "neg_en": "he/she/it doesn't speak",
                "neg_am": "አይናገርም / አትናገርም",
                "aff_q_en": "does he/she/it speak?",
                "aff_q_am": "ይናገራል/ትናገራለች ወይ?",
                "neg_q_en": "doesn't he/she/it speak?",
                "neg_q_am": "አይናገርም/አትናገርም ?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "we speak",
                "aff_am": "እንናገራለን",
                "neg_en": "we don't speak",
                "neg_am": "አንናገርም",
                "aff_q_en": "do we speak?",
                "aff_q_am": "እንናገራለን ?",
                "neg_q_en": "don't we speak?",
                "neg_q_am": "አንናገርም ?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "you speak",
                "aff_am": "ትናገራላችሁ",
                "neg_en": "you don't speak",
                "neg_am": "አትናገሩም",
                "aff_q_en": "do you speak?",
                "aff_q_am": "ትናገራላችሁ ?",
                "neg_q_en": "don't you speak?",
                "neg_q_am": "አትናገሩም ?"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "they speak",
                "aff_am": "ይናገራሉ",
                "neg_en": "they don't speak",
                "neg_am": "አይናገሩም",
                "aff_q_en": "do they speak?",
                "aff_q_am": "ይናገራሉ ?",
                "neg_q_en": "don't they speak?",
                "neg_q_am": "አይናገሩም ?"
            }
        ]

        for item in grammar_12_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 16: GRAMMAR LESSON 13 (MODAL VERB 'CAN') ---
    with tab16:
        st.header("Grammar 13: Modal Verb 'Can' Paradigms")
        st.write("Explore modal verb 'can' sentence structures (Affirmative, Negative, Affirmative Question, Negative Question) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_13_data = [
            {
                "pronoun": "I (እኔ)",
                "aff_en": "I can",
                "aff_am": "እችላለሁ",
                "neg_en": "I can't",
                "neg_am": "አልችልም",
                "aff_q_en": "can I?",
                "aff_q_am": "እችላለሁ ?",
                "neg_q_en": "can't I?",
                "neg_q_am": "አልችልም ?"
            },
            {
                "pronoun": "You (አንተ / አንቺ)",
                "aff_en": "you can",
                "aff_am": "ትችላለህ / ትችላለሽ",
                "neg_en": "you can't",
                "neg_am": "አትችልም / አትችዪም",
                "aff_q_en": "can you?",
                "aff_q_am": "ትችላለህ/ትችላለሽ ?",
                "neg_q_en": "can't you?",
                "neg_q_am": "አትችልም/አትችዪም ?"
            },
            {
                "pronoun": "He / She / It (እሱ / እሷ / እሱ)",
                "aff_en": "he/she/it can",
                "aff_am": "ይችላል / ትችላለች",
                "neg_en": "he/she/it can't",
                "neg_am": "አይችልም / አትችልም",
                "aff_q_en": "can he/she/it?",
                "aff_q_am": "ይችላል/ትችላለች ?",
                "neg_q_en": "can't he/she/it?",
                "neg_q_am": "አይችልም/አትችልም ?"
            },
            {
                "pronoun": "We (እኛ)",
                "aff_en": "we can",
                "aff_am": "እንችላለን",
                "neg_en": "we can't",
                "neg_am": "አንችልም",
                "aff_q_en": "can we?",
                "aff_q_am": "እንችላለን ?",
                "neg_q_en": "can't we?",
                "neg_q_am": "አንችልም ?"
            },
            {
                "pronoun": "You (እናንተ - Plural)",
                "aff_en": "you can",
                "aff_am": "ትችላላችሁ",
                "neg_en": "you can't",
                "neg_am": "አትችሉም",
                "aff_q_en": "can you?",
                "aff_q_am": "ትችላላችሁ ?",
                "neg_q_en": "can't you?",
                "neg_q_am": "አትችሉም ?"
            },
            {
                "pronoun": "They (እነሱ)",
                "aff_en": "they can",
                "aff_am": "ይችላሉ",
                "neg_en": "they can't",
                "neg_am": "አይችሉም",
                "aff_q_en": "can they?",
                "aff_q_am": "ይችላሉ ?",
                "neg_q_en": "can't they?",
                "neg_q_am": "አይችሉም ?"
            }
        ]

        for item in grammar_13_data:
            with st.container(border=True):
                st.markdown(f"### 👤 Pronoun: {item['pronoun']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("##### ➕ Affirmative (አረጋጋጭ)")
                    st.info(item['aff_en'])
                    st.success(item['aff_am'])
                    
                    st.markdown("##### ❓ Affirmative Question (አረጋጋጭ ጥያቄ)")
                    st.info(item['aff_q_en'])
                    st.success(item['aff_q_am'])

                with col_b:
                    st.markdown("##### ➖ Negative (አሉታዊ)")
                    st.info(item['neg_en'])
                    st.success(item['neg_am'])
                    
                    st.markdown("##### ❓ Negative Question (አሉታዊ ጥያቄ)")
                    st.info(item['neg_q_en'])
                    st.success(item['neg_q_am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB 17: GRAMMAR LESSON 14 (MODAL & ADVANCED STRUCTURES) ---
    with tab17:
        st.header("Grammar 14: Modal Expressions & Advanced Structures")
        st.write("Explore polite requests (Can I, May I, Could you), participle clauses (Having + V3), and prepositional modifiers (Without + V1+ing) comparing English and Amharic translation patterns.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        grammar_14_items = [
            {
                "title": "1. CAN I",
                "en": "Can I open the window?",
                "am": "መስኮቱን መክፈት እችላለው?"
            },
            {
                "title": "2. MAY I",
                "en": "May I open the window?",
                "am": "መስኮቱን ልክፈተው?"
            },
            {
                "title": "3. COULD YOU",
                "en": "Could you open the window?",
                "am": "መስኮቱን ልትከፍተው ትችላለህ?"
            },
            {
                "title": "4. HAVING + V3",
                "en": "Having eaten the food, he slept.",
                "am": "ምግቡን በልቶ ተኛ።"
            },
            {
                "title": "5. WITHOUT + V1+ING",
                "en": "He took the test without studying. (Or: Without studying, he took the test.)",
                "am": "ሳያጠና ፈተናውን ወሰደ።"
            }
        ]

        for item in grammar_14_items:
            with st.container(border=True):
                st.markdown(f"### {item['title']}")
                st.markdown("**English Example:**")
                st.info(item['en'])
                st.markdown("**Amharic Translation:**")
                st.success(item['am'])

            st.markdown("<br>", unsafe_allow_html=True)

    # --- GLOBAL LOGOUT BUTTON AT THE BOTTOM ---
    st.divider()
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()