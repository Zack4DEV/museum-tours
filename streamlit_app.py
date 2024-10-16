import streamlit as st

# Shared Tailwind CSS classes
BUTTON_CLASSES = "py-3 px-6 rounded-lg hover:bg-opacity-80 transition-colors"
GRID_CLASSES = "grid grid-cols-1 md:grid-cols-2 gap-6 mb-8"
TEXT_CENTER_CLASSES = "text-center"
TEXT_CLASSES = "text-xl font-semibold mb-6"

def marketing_expert_component():
    st.markdown('<div class="bg-background text-primary-foreground p-8 flex flex-col items-center justify-center">', unsafe_allow_html=True)
    st.markdown('<h1 class="text-4xl font-bold mb-4">Become A Marketing Expert</h1>', unsafe_allow_html=True)
    st.markdown('<p class="text-center mb-6 text-lg">Unlock Your Full Potential With Expert Guidance</p>', unsafe_allow_html=True)

    st.markdown(f'<div class="{GRID_CLASSES}">', unsafe_allow_html=True)
    st.markdown(f'<button class="bg-primary text-primary-foreground {BUTTON_CLASSES}">Get Started</button>', unsafe_allow_html=True)
    st.markdown(f'<button class="bg-primary text-primary-foreground {BUTTON_CLASSES}">Learn More</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<p class="{TEXT_CENTER_CLASSES} {TEXT_CLASSES}">Inspiring Creativity One Idea At A Time</p>', unsafe_allow_html=True)
    st.markdown('<p class="text-center mb-6">Transforming Creators into Storytelling Masters</p>', unsafe_allow_html=True)

    st.markdown(f'<div class="{GRID_CLASSES}">', unsafe_allow_html=True)
    st.markdown(f'<button class="bg-secondary text-secondary-foreground {BUTTON_CLASSES}">Learn More</button>', unsafe_allow_html=True)
    st.markdown(f'<button class="bg-secondary text-secondary-foreground {BUTTON_CLASSES}">Monthly Membership</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="text-center mt-6">Let\'s Build Your Digital Marketing Empire Now</p>', unsafe_allow_html=True)

    st.markdown(f'<div class="{GRID_CLASSES}">', unsafe_allow_html=True)
    st.markdown(f'<button class="bg-accent text-accent-foreground {BUTTON_CLASSES}">Join Now</button>', unsafe_allow_html=True)
    st.markdown(f'<button class="bg-accent text-accent-foreground {BUTTON_CLASSES}">Learn More</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="text-center mt-6">Check Out Our Contents</p>', unsafe_allow_html=True)
    st.markdown('<p class="text-center mb-6">Learn From The Experts</p>', unsafe_allow_html=True)

    st.markdown(f'<button class="bg-accent text-accent-foreground {BUTTON_CLASSES} mb-6">Stay In The Loop</button>', unsafe_allow_html=True)

    st.markdown('<form class="flex flex-col items-center mt-6">', unsafe_allow_html=True)
    st.markdown('<input type="email" placeholder="Enter your email" class="bg-input text-input placeholder-input p-2 rounded-md border border-border focus:outline-none focus:ring ring-ring transition-colors mb-2 w-full max-w-xs" />', unsafe_allow_html=True)
    st.markdown('<button type="submit" class="bg-primary text-primary-foreground py-2 px-4 rounded-md hover:bg-primary/80 transition-colors">Submit</button>', unsafe_allow_html=True)
    st.markdown('</form>', unsafe_allow_html=True)

    st.markdown('<p class="text-center mt-6 text-muted-foreground">All rights reserved</p>', unsafe_allow_html=True)
    st.markdown('<p class="text-center text-muted-foreground">Powered by</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Display the marketing expert component
marketing_expert_component()