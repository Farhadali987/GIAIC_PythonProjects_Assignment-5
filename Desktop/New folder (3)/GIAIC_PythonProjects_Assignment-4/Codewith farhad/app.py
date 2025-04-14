import streamlit as st
import random
import time

def main():
    st.set_page_config(page_title="Snake, Water, Gun Game", page_icon="🎮", layout="centered")
    
    # Custom CSS for enhanced styling and animations
    st.markdown("""
        <style>
            @keyframes blink {
                0% {opacity: 1;}
                50% {opacity: 0.5;}
                100% {opacity: 1;}
            }
            .animated-title {
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                animation: blink 1.5s infinite;
                color: #FF5733;
                padding: 10px;
            }
            .stButton>button {
                background: linear-gradient(90deg, #4CAF50, #45a049);
                color: white;
                font-size: 22px;
                padding: 14px;
                border-radius: 12px;
                transition: 0.3s;
                width: 100%;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }
            .stButton>button:hover {
                background: linear-gradient(90deg, #45a049, #4CAF50);
                transform: scale(1.1);
            }
            .stRadio > div {
                font-size: 20px;
                font-weight: bold;
                padding: 10px;
                border: 2px solid #3498db;
                border-radius: 10px;
                background: #ecf0f1;
                transition: 0.3s;
                text-align: center;
            }
            .stRadio > div:hover {
                background: #d6eaf8;
            }
            .result-text {
                font-size: 26px;
                font-weight: bold;
                text-align: center;
                color: #3498db;
                animation: blink 1s infinite;
                padding: 15px;
                border-radius: 10px;
                background: #ecf0f1;
            }
            .choices-container {
                display: flex;
                justify-content: space-around;
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
                border-radius: 10px;
                background: #f9f9f9;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            @keyframes fadeIn {
                0% {opacity: 0;}
                100% {opacity: 1;}
            }
            .footer {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color: #555;
                margin-top: 20px;
                animation: fadeIn 2s ease-in-out;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='animated-title'>🎮 Snake, Water, Gun Game 🐍💧🔫</div>", unsafe_allow_html=True)
    
    choices = {"🐍 Snake": 1, "💧 Water": -1, "🔫 Gun": 0}
    reverse_choices = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}
    
    st.markdown("<div class='choices-container'>Choose one:</div>", unsafe_allow_html=True)
    user_choice = st.radio("", list(choices.keys()))
    
    if st.button("Play 🕹️"): 
        with st.spinner("Choosing... 🤔"):
            time.sleep(1.5)
        
        computer_choice = random.choice(list(choices.values()))
        user_value = choices[user_choice]
        
        st.markdown("<div class='choices-container'><b>You chose:</b> " + user_choice + "</div>", unsafe_allow_html=True)
        st.markdown("<div class='choices-container'><b>Computer chose:</b> " + reverse_choices[computer_choice] + "</div>", unsafe_allow_html=True)
        
        if computer_choice == user_value:
            st.markdown("<div class='result-text'>It's a draw! 🤝</div>", unsafe_allow_html=True)
        elif (computer_choice == -1 and user_value == 1) or \
             (computer_choice == 1 and user_value == 0) or \
             (computer_choice == 0 and user_value == -1):
            st.markdown("<div class='result-text' style='color: green;'>🎉 You win! 🏆</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-text' style='color: red;'>💀 You lose! Try again.</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='footer'>Made with ❤️ by Farhad Gul</div>", unsafe_allow_html=True)
            
if __name__ == "__main__":
    main()
