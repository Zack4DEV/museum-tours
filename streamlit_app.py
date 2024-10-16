import streamlit as st

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Inventory Tracker"
)

# HTML code for embedding a digital marketing platform page
html_code = '''
<html lang="en">
<head>
    <!-- CSS for styling animations and general layout -->
    <style data-emotion="css-global">
        @-webkit-keyframes mui-auto-fill { from { display: block; } }
        @keyframes mui-auto-fill { from { display: block; } }
        @-webkit-keyframes mui-auto-fill-cancel { from { display: block; } }
        @keyframes mui-auto-fill-cancel { from { display: block; } }
    </style>
    <style data-emotion="css feqhe6">
        .css-feqhe6 {
            display: inline-flex;
            flex-direction: column;
            position: relative;
            min-width: 0;
            padding: 0;
            margin: 0;
            border: 0;
            vertical-align: top;
            width: 100%;
        }
    </style>
    <style data-emotion="css 1bewqcb">
        .css-1bewqcb {
            font-family: 'Poppins', Helvetica, sans-serif;
            font-weight: 400;
            font-size: 1rem;
            line-height: 1.4375em;
            color: rgba(0, 0, 0, 0.87);
            box-sizing: border-box;
            position: relative;
            cursor: text;
            display: inline-flex;
            align-items: center;
            width: 100%;
            border-radius: 8px;
            background-color: #FFFFFF;
        }
        .css-1bewqcb:hover .MuiOutlinedInput-notchedOutline {
            border-color: rgba(0, 0, 0, 0.87);
        }
        .css-1bewqcb.Mui-focused .MuiOutlinedInput-notchedOutline {
            border-color: #1976d2;
            border-width: 2px;
        }
    </style>

    <!-- Meta tags for SEO and responsiveness -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=contain, user-scalable=no">

    <!-- External stylesheet -->
    <link rel="stylesheet" href="https://beacons.ai/_next/static/css/cec9a5860a368e30.css" data-precedence="next">

    <!-- Page title and description -->
    <title>Digital Marketing Platform</title>
    <meta name="description" content="zack4dev's Website">

    <!-- Canonical and social meta tags -->
    <link rel="canonical" href="https://digital-marketing.streamlit.app/">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Digital Marketing Platform">
    <meta property="og:description" content="zack4dev's Website ,Digital marketing for influencers that can significantly optimize campaigns, streamline processes, and drive better results">
    <meta property="og:url" content="https://digital-marketing.streamlit.app">
    <meta property="og:site_name" content="Streamlit">

    <!-- Twitter card metadata -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Digital Marketing Platform">
    <meta name="twitter:description" content="zack4dev's Website ,Digital marketing for influencers that can significantly optimize campaigns, streamline processes, and drive better results">
</head>
<body>
    <div id="root">
        <div class="website-viewer relative h-full overflow-y-auto">
            <!-- Main content of the platform -->
            <h1>Digital Marketing Platform</h1>
            <p>Elevate Your Marketing Skills with Professional Insights</p>

            <!-- Links to actions -->
            <a href="https://digital-marketing.streamlit.app/">Get started</a>
            <a href="https://digital-marketing.streamlit.app/">Learn more</a>

            <!-- Footer section -->
            <footer>©2024 All Rights Reserved</footer>
        </div>
    </div>
</body>
</html>
'''

# Display the HTML content in the Streamlit app
st.markdown(html_code, unsafe_allow_html=True)
