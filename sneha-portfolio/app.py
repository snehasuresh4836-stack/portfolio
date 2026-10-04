import streamlit as st
import os

# Load external CSS
css_file = os.path.join(os.path.dirname(__file__), "style.css")

with open(css_file, "r") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Page configuration
st.set_page_config(
    page_title="Sneha | Python Developer",
    page_icon="💻",
    layout="wide"
)

# Navigation
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "About Me", "Skills", "Projects", "Education", "Internship", "Contact"]
)

# ---------------- HOME ----------------


if page == "Home":

    # Main hero section
    left, right = st.columns([1.8, 1], gap="large")

    with left:
        st.markdown(
            "<div style='padding-top: 60px;'>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h1 style='font-size: 48px; margin-bottom: 5px;'>"
            "Hi, I'm Sneha 👋"
            "</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='font-size: 28px; margin-top: 0;'>"
            "Aspiring Python Developer"
            "</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style='font-size: 18px; line-height: 1.7;'>
            BCA (Hons.) student passionate about Python, Data Science,
            Machine Learning, and Software Development.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style='font-size: 16px; line-height: 1.7;'>
            I enjoy building practical projects, learning new technologies,
            and improving my programming and problem-solving skills.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown(
            "<div style='text-align: center; padding-top: 25px;'>",
            unsafe_allow_html=True
        )

        st.image(
            "profile.jpeg",
            width=260
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # What I Do
    st.markdown(
        "<h2 style='text-align: left;'>🚀 What I Do</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            """
           <div class='skill-card'>
            <h3>🐍 Python Development</h3>
            <p>
            Developing Python programs and improving my programming skills.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='skill-card'>
            <h3>📊 Data Science & AI</h3>
            <p>
            Learning Data Science, Machine Learning, and Artificial Intelligence.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class='skill-card'>
            <h3>💻 Software Development</h3>
            <p>
            Building practical projects and developing software skills.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Career Goal
    st.markdown(
        "<h2 style='text-align: left;'>🎯 Career Goal</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class='career-goal'>
        <p style='font-size: 17px; line-height: 1.7; margin: 0;'>
        My goal is to become a skilled Python Developer and build a
        successful career in software development.
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )
        #------------cv-----------#
    st.markdown("---")

    st.subheader("📄 My CV")

    st.write(
        "You can download my CV to learn more about my education, skills, and projects."
)

    with open("cv.pdf", "rb") as pdf_file:
        cv_data = pdf_file.read()

        st.download_button(
        label="📥 Download CV",
        data=cv_data,
        file_name="Sneha_Suresh_CV.pdf",
        mime="application/pdf"
)
# ---------------- ABOUT ME ----------------

elif page == "About Me":

    st.title("👩‍💻 About Me")

    # Introduction
    st.subheader("Who I Am")

    st.write(
        "I am a BCA (Hons.) student with a strong interest in "
        "Python, Data Science, Artificial Intelligence, and "
        "Software Development."
    )

    st.write(
        "I enjoy learning new technologies, building practical "
        "projects, and improving my programming and problem-solving skills."
    )

    st.markdown("---")

    # Education
    st.subheader("🎓 Education")

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown(
            """
            <div class="skill-card">

            <h3>BCA (Hons.)</h3>

            <p>
            <strong>University</strong><br>
            University of Calicut
            </p>

            <p>
            <strong>College</strong><br>
            Ideal College for Advanced Studies, Kadakassery
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="skill-card">

            <h3>Programme Details</h3>

            <p>
            <strong>Programme</strong><br>
            FYUGP BCA (Hons.)
            </p>

            <p>
            <strong>Current Semester</strong><br>
            5th Semester
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Career Interests
    st.subheader("🎯 Career Interests")

    st.write(
        "My career interests include Python Development, "
        "Data Science, Artificial Intelligence, and Software Development."
    )
    # ---------------- SKILLS ----------------

elif page == "Skills":

    st.title("🛠️ Skills")

    st.write(
        "Here are the technical skills and tools I am currently "
        "learning and developing."
    )

    st.markdown("---")

    # Programming
    st.subheader("🐍 Programming")

    col1, col2, col3, col4 = st.columns(4, gap="large")

    with col1:
        st.markdown(
            """
            <div class="skill-card">
                <h3>🐍 Python</h3>
                <p>Programming and problem solving</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="skill-card">
                <h3>☕ Java</h3>
                <p>Programming fundamentals</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="skill-card">
                <h3>🗄️ SQL</h3>
                <p>Database fundamentals</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div class="skill-card">
                <h3>💻 C</h3>
                <p>Programming fundamentals</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Data & AI
    st.subheader("📊 Data & AI")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            """
            <div class="skill-card">
                <h3>📊 Data Science</h3>
                <p>Data analysis and visualization</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="skill-card">
                <h3>🤖 Machine Learning</h3>
                <p>ML concepts and practical projects</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="skill-card">
                <h3>🧠 NLP</h3>
                <p>Natural Language Processing</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Web Development
    st.subheader("🌐 Web Development")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
        """
        <div class="skill-card">
            <h3>🌐 HTML</h3>
            <p>Webpage structure</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col2:
        st.markdown(
        """
        <div class="skill-card">
            <h3>🎨 CSS</h3>
            <p>Webpage styling and design</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col3:
        st.markdown(
        """
        <div class="skill-card">
            <h3>⚡ JavaScript</h3>
            <p>Webpage functionality</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    # Tools
    st.subheader("🛠️ Tools")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
        """
        <div class="skill-card">
            <h3>💻 VS Code</h3>
            <p>Code development</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col2:
        st.markdown(
        """
        <div class="skill-card">
            <h3>🐙 GitHub</h3>
            <p>Code hosting and collaboration</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col3:
        st.markdown(
        """
        <div class="skill-card">
            <h3>🚀 Streamlit</h3>
            <p>Python web applications</p>
        </div>
        """,
        unsafe_allow_html=True
    )
        # ---------------- PROJECTS ----------------

elif page == "Projects":

    st.title("🚀 My Projects")

    st.write(
        "Here are some of my main projects created while learning "
        "Python, Data Science, Artificial Intelligence, and Web Development."
    )

    st.markdown("---")

    # Fake News Detection
    st.subheader("📰 Fake News Detection")

    st.markdown(
        """
        <div class="skill-card">
            <h3>Machine Learning & NLP Project</h3>
            <p>
            A machine learning project that classifies news as real or fake
            using Natural Language Processing, TF-IDF, and Logistic Regression.
            </p>
            <p><strong>Technologies:</strong> Python, Scikit-learn, NLP, Gradio</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🔗 View on GitHub",
        "https://github.com/snehasuresh4836-stack/fake-news-detection"
    )

    st.markdown("---")

    # AI Travel Planner
    st.subheader("✈️ AI Travel Planner")

    st.markdown(
        """
        <div class="skill-card">
            <h3>Generative AI Project</h3>
            <p>
            An AI-powered travel planner for students that creates personalized and
            budget-friendly travel itineraries based on user preferences.
            </p>
            <p><strong>Technologies:</strong> Python, Generative AI, Gradio, Hugging Face</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🔗 View on GitHub",
        "https://github.com/snehasuresh4836-stack/ai-travel-planner"
    )

    st.markdown("---")

    # E-Commerce Website
    st.subheader("🛒 E-Commerce Website")

    st.markdown(
        """
        <div class="skill-card">
            <h3>Web Development Project</h3>
            <p>
            My first e-commerce website project, created as part of my
            web development learning journey.
            </p>
            <p><strong>Technologies:</strong> HTML, CSS, JavaScript, React, Node JS</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🔗 View on GitHub",
        "https://github.com/snehasuresh4836-stack/sneha-ecommerce-website"
    )
    # ---------------- EDUCATION ----------------

elif page == "Education":

    st.title("🎓 Education")

    st.write(
        "My academic background and current educational journey."
    )

    st.markdown("---")

    # Main Education
    st.subheader("🎓 Bachelor of Computer Applications (Honours)")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.info(
            """
            **🏫 University**

            University of Calicut

            **🎓 Programme**

            FYUGP BCA (Hons.)
            """
        )

    with col2:
        st.info(
            """
            **🏛️ College**

            Ideal College for Advanced Studies, Kadakassery

            **📚 Current Semester**

            5th Semester
            """
        )

    st.markdown("---")

    # Academic Focus
    st.subheader("📚 Academic Focus")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### 🐍 Programming & Development")
        st.write("• Python")
        st.write("• C Programming")
        st.write("• Java")
        st.write("• SQL")
        st.write("• Web Development")

    with col2:
        st.markdown("### 🤖 Data & Computer Science")
        st.write("• Data Science")
        st.write("• Machine Learning")
        st.write("• Natural Language Processing")
        st.write("• Database Management")
        st.write("• Computer Architecture")

    st.markdown("---")

    # Current Learning
    st.subheader("🚀 Current Learning")

    st.success(
        "Currently focusing on Python Development, Data Science, "
        "Machine Learning, and Software Development."
    )
    # ---------------- INTERNSHIP----------------
elif page == "Internship":

    st.title("💼 Internship Experience")

    st.write(
        "My internship experience and the technologies I practiced."
    )

    st.markdown("---")

    st.subheader("🤖 AI & Robotics Internship")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.info(
            """
            🏢 **Cyber Square**

            **Location:** Hilite Business Park, Calicut

            **Focus:** AI, Robotics, Python & Data Science
            """
        )

    with col2:
        st.info(
            """
            📚 **Internship Learning**

            Practical learning through programming,
            data analysis, machine learning,
            and AI-related activities.
            """

        )

    st.markdown("---")

    st.subheader("🛠️ Technologies & Skills Practiced")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.info(
            """
            🐍 **Python & Data**

            • Python  
            • NumPy  
            • Pandas  
            • Data Analysis
            """
        )

    with col2:
        st.info(
            """
            🤖 **AI & Machine Learning**

            • Machine Learning  
            • Artificial Intelligence  
            • Data Visualization
            """
        )

    with col3:
        st.info(
            """
            📊 **Tools**

            • Power BI  
            • Orange AI  
            • Jupyter Notebook

            """
        )

    st.markdown("---")

    st.subheader("📜 Internship Certificate")

    st.write(
        "Certificate awarded for completing the AI & Robotics internship."
    )

    st.link_button(
        "📜 View Internship Certificate",
        "https://github.com/snehasuresh4836-stack/internship/blob/main/internship-certificate.jpeg"
    )
#------------------- CONTACT ----------------

elif page == "Contact":

    st.title("📩 Contact Me")

    st.write(
        "Feel free to connect with me for opportunities, collaboration, "
        "or professional discussions."
    )

    st.markdown("---")

    st.subheader("🔗 Let's Connect")

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.info(
            """
            📧 **Email**

            snehasuresh4836@gmail.com
            """
        )

        st.info(
            """
            💻 **GitHub**

            https://github.com/snehasuresh4836-stack
            """
        )

    with col2:

        st.info(
            """
            🔗 **LinkedIn**

            https://www.linkedin.com/in/sneha-k-7a784932b/
            """
        )

        st.info(
            """
            📍 **Location**

            Kerala, India
            """
        )

    st.markdown("---")

    st.subheader("🚀 Career Opportunities")

    st.success(
        "I am interested in internships, learning opportunities, "
        "and software development roles."
    )

    st.markdown("---")

    st.write(
        "Thank you for visiting my portfolio! 😊"
    )