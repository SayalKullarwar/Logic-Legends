📝 Project Description
MoodMentor is a data-driven journaling companion designed for college students. Recognizing that students often avoid counseling due to social stigma, this tool allows for 100% anonymous emotional tracking. By utilizing Natural Language Processing (NLP), the system distinguishes between typical "bad days" and sustained "negative spirals," providing a bridge to professional help only when medically/statistically necessary.
🚩 Problem Statement
Traditional mental health outreach fails because it requires the student to take the first (and hardest) step.
 * Stigma: Students fear being labeled if seen entering a counseling center.
 * Lack of Self-Awareness: Many students don't realize their stress has become a chronic "negative spiral" until it's too late.
 * Action Gap: There is no "low-stakes" way to monitor mental health privately.
   
✨ Features and Functionality
 * Sentiment Tracking: Utilizes Lexicon-based NLP to assign a sentiment score (s) to daily journal entries.
 * Negative Spiral Detection: A temporal logic gate that flags users only if the rolling average sentiment remains below a threshold (e.g., s < -0.5) for more than 3 consecutive days.
 * Mood Trend Visualization: Generates time-series plots using Matplotlib to visualize emotional trajectories.
 * Anonymized Campus Heatmap: Aggregates sentiment data across simulated campus "zones" to create a mental health density map without identifying individual students.
 * Pulse Polls: Categorizes the most common stressors (e.g., Exams, Loneliness, Finance) through keyword extraction.
   
🛠 Tech Stack (ML-Focus)
 * Language: Python 3.12.0
 * Libraries: * Pandas & NumPy: For data manipulation and rolling window calculations.
   * Matplotlib / Seaborn: For generating the Mood Trend graphs and the Campus Heatmap.
     
🚀 Setup & Execution
 * Clone the Repository:
   git clone https://github.com/SayalKullarwar/Logic-Legends.git

 * Install Requirements:
   pip install pandas matplotlib seaborn 

 * Run the ML Pipeline:
   python moodmentor_webapp.py

📊 Sample Dataset (CSV Format)
The following is the structure of the mood_data.csv used for testing:
User_ID,Date,Journal_Entry,Sentiment_Score,Location,Stressor_Poll
STU_101,2026-03-10,"Feeling great after the gym.",0.8,Library,Fitness
STU_101,2026-03-11,"Missed my morning lecture, feeling behind.",-0.3,Dorm_A,Academics
STU_101,2026-03-12,"I can't seem to get anything right lately.",-0.7,Dorm_A,Social
STU_101,2026-03-13,"I feel completely isolated and overwhelmed.",-0.9,Dorm_A,Social

👥 Team Details
 * Sayal kullarwar
 * Rutuja balbudhe
 * Prachita Barapatre
 * Aryan pathan
   
🔮 Future Scope
 * Linguistic Shift Detection: Moving beyond simple sentiment to detect "Absolutist Thinking" (use of words like always, never, totally) which is a precursor to clinical depression.
 * Resource Recommendation Engine: Matching the specific detected stressor (e.g., "Financial Stress") with a specific campus resource (e.g., "Student Financial Aid Office").

 

 
