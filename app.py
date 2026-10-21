import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

st.set_page_config(page_title="Webcam Stream", page_icon="📷")

st.title("Live Webcam Stream")
st.write("This app uses WebRTC to stream your local camera feed straight to the browser.")

# We add a public STUN server so it works properly if you deploy it online
# rtc_config = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )

# Launch the webcam streamer
webrtc_streamer(
    key="webcam-stream",
    # rtc_configuration=rtc_config,
    media_stream_constraints={"video": True, "audio": False} # Set audio to True if you want sound
)