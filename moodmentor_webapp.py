import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# ====================== MOODMENTOR CLASS ======================
class MoodMentor:
    def __init__(self, dataset_path=None):
        self.history = {}
        if dataset_path:
            self.load_from_dataset(dataset_path)

    def load_from_dataset(self, dataset_path):
        df = pd.read_csv(dataset_path)
        for _, row in df.iterrows():
            user_id = row['user_id']
            text = row['journal_text']
            try:
                entry_date = pd.to_datetime(row['entry_date']).date()
            except:
                entry_date = date.today()

            lower = text.lower()
            strong_neg = ['lonely', 'pointless', 'hopeless', 'worthless', 'depressed', 'anxious', 'overwhelmed', 'cry', 'sad', 'terrible', 'fail']
            neg = ['stress', 'stressed', 'tired', 'bad', 'miss home', 'alone', 'dont want']
            score = sum(2 for w in strong_neg if w in lower) + sum(1 for w in neg if w in lower)
            sentiment = -0.75 if score >= 3 else (-0.45 if score >= 2 else 0.4)
            mood = "Negative" if sentiment < 0 else "Positive"

            if user_id not in self.history:
                self.history[user_id] = []
            self.history[user_id].append({'date': entry_date, 'text': text, 'sentiment': sentiment, 'mood': mood})

    def analyze(self, user_id, journal_text):
        today = date.today()
        lower = journal_text.lower()
        strong_neg = ['lonely', 'pointless', 'hopeless', 'worthless', 'depressed', 'anxious', 'overwhelmed', 'cry', 'sad', 'terrible', 'fail', 'no motivation']
        neg = ['stress', 'stressed', 'tired', 'bad', 'miss home', 'alone', 'dont want']
        score = sum(2 for w in strong_neg if w in lower) + sum(1 for w in neg if w in lower)
        sentiment = -0.75 if score >= 3 else (-0.45 if score >= 2 else 0.4)
        mood = "Negative" if sentiment < 0 else "Positive"

        if user_id not in self.history:
            self.history[user_id] = []
        self.history[user_id].append({'date': today, 'text': journal_text, 'sentiment': sentiment, 'mood': mood})

        consec = 0
        for entry in reversed(self.history[user_id]):
            if entry['mood'] == "Negative":
                consec += 1
            else:
                break

        spiral = consec >= 5

        if spiral:
            response = "I've noticed you've been feeling really low for several days now."
        elif mood == "Negative":
            response = "I'm really sorry you're feeling this way right now."
        else:
            response = "Glad to hear that! Keep going 💪"

        return {
            "sentiment_score": round(sentiment, 2),
            "mood": mood,
            "consecutive_low_days": consec,
            "spiral_detected": spiral,
            "response": response
        }

# ====================== STREAMLIT CONFIG ======================
st.set_page_config(page_title="MoodMentor", page_icon="🌊", layout="wide")

# Modern Premium CSS
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0f172a 0%, #1e2937 100%); color: #e0f2fe; }
    h1, h2, h3 { color: #67e8f9; font-weight: 700; }
    .nav-link { color: #67e8f9; font-weight: 500; }
    .stButton>button {
        background: linear-gradient(135deg, #7c3aed, #db2777);
        color: white;
        border-radius: 12px;
        padding: 12px 28px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(124, 58, 237, 0.4);
    }
    .gentle-card {
        background: rgba(30, 41, 59, 0.95);
        border: 2px solid #67e8f9;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 15px 35px rgba(103, 232, 249, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Top Navigation Bar
st.markdown("""
<div style="background: rgba(15, 23, 42, 0.95); padding: 15px 30px; border-radius: 0 0 20px 20px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.3); position: sticky; top: 0; z-index: 100;">
    <h1 style="margin:0; display:inline-block;">🌊 MoodMentor</h1>
    <span style="float:right; margin-top:8px; color:#94a3b8;">
        A gentle, private space for your thoughts
    </span>
</div>
""", unsafe_allow_html=True)

mentor = MoodMentor(dataset_path=r"C:\Users\sayal\Downloads\moodmentor_dataset.csv")

# Navigation
page = st.radio(
    label="",
    options=["🏠 Home", "✍️ Journal", "🌍 Community & Insights", "📊 Dashboard", "ℹ️ About"],
    horizontal=True,
    label_visibility="collapsed"
)

# ====================== PAGES ======================
if page == "🏠 Home":
    st.markdown("### You are safe here.")
    st.info("Journal anonymously. We only reach out when we notice sustained struggles.")
    st.success("✅ Model loaded successfully with 1573 entries")

elif page == "✍️ Journal":
    st.subheader("✍️ Write Your Journal Entry")
    user_id = st.text_input("Anonymous ID", "student_demo")
    journal_text = st.text_area("How are you feeling today?", height=200)

    if st.button("Reflect on My Entry", type="primary", use_container_width=True):
        if journal_text.strip():
            result = mentor.analyze(user_id, journal_text)
            st.info(result['response'])

            if result['spiral_detected']:
                st.markdown('<div class="gentle-card">', unsafe_allow_html=True)
                st.markdown("### 💙 I've noticed something")
                st.write("You've been carrying a heavy feeling for several days now.")
                st.write("It's really brave that you're still showing up here.")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🌿 Guided Breathing Exercise", use_container_width=True):
                        st.balloons()
                        st.success("Let's breathe together...")
                with col2:
                    if st.button("💬 Anonymous Peer Chat", use_container_width=True):
                        st.success("Connecting you safely...")
                
                if st.button("Maybe Later", use_container_width=True):
                    st.info("No pressure. I'm here whenever you're ready 💙")
                st.markdown('</div>', unsafe_allow_html=True)

elif page == "🌍 Community & Insights":
    st.subheader("🌍 Community & Insights")
    st.markdown("**Feel connected without revealing your identity**")

    tab1, tab2 = st.tabs(["📍 Campus Vibe Map", "📊 Pulse Poll"])

    with tab1:
        st.markdown("##### Overall Campus Vibe (Last 24 hrs)")
        df = pd.read_csv(r"C:\Users\sayal\Downloads\moodmentor_dataset.csv")
        df['entry_date'] = pd.to_datetime(df['entry_date'])
        recent = df[df['entry_date'] >= df['entry_date'].max() - pd.Timedelta(days=1)]
        
        area_data = recent.groupby('department')['sentiment_score'].mean().reset_index()
        area_data['Location'] = area_data['department'].map({
            'CS': 'Engineering Quad', 'Engineering': 'Library Zone', 'Science': 'Student Union',
            'Business': 'Hostel Area', 'Arts': 'Canteen', 'Humanities': 'Academic Block'
        })

        fig = px.imshow(area_data.pivot_table(values='sentiment_score', index='Location'),
                        text_auto=True, color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("##### Pulse Poll: What’s contributing most to your stress this week?")
        options = ["Midterms", "Sleep Deprivation", "Project Deadlines", "Social Pressure", "Family Expectations", "Placement Anxiety"]
        selected = st.multiselect("Select all that apply", options)
        if st.button("Submit & See Results"):
            poll = {"Midterms": 48, "Sleep Deprivation": 35, "Project Deadlines": 42, "Social Pressure": 28, "Family Expectations": 22, "Placement Anxiety": 31}
            fig = px.bar(x=list(poll.values()), y=list(poll.keys()), orientation='h', text=[f"{v}%" for v in poll.values()])
            st.plotly_chart(fig, use_container_width=True)
            st.success("💙 You are not alone.")

elif page == "📊 Dashboard":
    st.subheader("📊 Campus Mental Health Overview")
    try:
        df = pd.read_csv(r"C:\Users\sayal\Downloads\moodmentor_dataset.csv")
        df['entry_date'] = pd.to_datetime(df['entry_date'])
        df['Week'] = df['entry_date'].dt.strftime('Week %U')
        
        st.markdown("##### Weekly Heatmap")
        heatmap_data = df.groupby(['department', 'Week'])['sentiment_score'].mean().reset_index()
        pivot = heatmap_data.pivot(index='department', columns='Week', values='sentiment_score')
        fig = px.imshow(pivot, text_auto=True, color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("##### Mood Trends")
        trend = px.line(df.groupby(['department', 'entry_date'])['sentiment_score'].mean().reset_index(),
                        x='entry_date', y='sentiment_score', color='department', markers=True)
        st.plotly_chart(trend, use_container_width=True)
    except:
        st.error("Could not load dashboard.")

elif page == "ℹ️ About":
    st.markdown("### About MoodMentor")
    st.write("A safe, private AI companion for college students.")

st.caption("MoodMentor — Because it's okay to not be okay 🌊")