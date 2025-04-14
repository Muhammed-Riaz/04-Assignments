# import time 
# import winsound 

# def Countdwon(seconds):

#   while seconds > 0:
   
#    mins , secs = divmod(seconds,60)

#    timer = f"{mins:02d} : {secs:02d}"

#    time.sleep(1)

#    print(timer , end="\r")

#    seconds -= 1

#   print("⏰ Time's up!") 
#   winsound.Beep(1000, 2000)  
 

# user_input = int(input("Enter second"))
# Countdwon(user_input)
  



# import time
# import streamlit as st

# # Streamlit Web App
# def countdown_timer(seconds):
#     st.title("⏳ Countdown Timer")
#     timer_placeholder = st.empty()  # Placeholder for timer text

#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)
#         timer_placeholder.markdown(f"## ⏰ {mins:02d}:{secs:02d}")  # Update UI
#         time.sleep(1)  # Wait for 1 second
#         seconds -= 1  # Decrease countdown

#     timer_placeholder.markdown("## 🎉 Time's up!")  # Final message

#     # Play Beep Sound in Web (Using HTML + JavaScript)
#     st.markdown(
#         """
#         <audio autoplay>
#         <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
#         </audio>
#         """,
#         unsafe_allow_html=True,
#     )

# # Streamlit UI
# seconds = st.number_input("Enter Countdown Time (seconds):", min_value=1, value=20)
# if st.button("Start Countdown"):
#     countdown_timer(seconds)
