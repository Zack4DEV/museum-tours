import streamlit as st

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Inventory Tracker",
    page_icon=":shopping_bags:",
)

# HTML code for embedding a digital marketing platform page
html_code = '''
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
		<script src="https://unpkg.com/unlazy@0.11.3/dist/unlazy.with-hashing.iife.js" defer init></script>
		<script type="text/javascript">
			window.tailwind.config = {
				darkMode: ['class'],
				theme: {
					extend: {
						colors: {
							border: 'hsl(var(--border))',
							input: 'hsl(var(--input))',
							ring: 'hsl(var(--ring))',
							background: 'hsl(var(--background))',
							foreground: 'hsl(var(--foreground))',
							primary: {
								DEFAULT: 'hsl(var(--primary))',
								foreground: 'hsl(var(--primary-foreground))'
							},
							secondary: {
								DEFAULT: 'hsl(var(--secondary))',
								foreground: 'hsl(var(--secondary-foreground))'
							},
							destructive: {
								DEFAULT: 'hsl(var(--destructive))',
								foreground: 'hsl(var(--destructive-foreground))'
							},
							muted: {
								DEFAULT: 'hsl(var(--muted))',
								foreground: 'hsl(var(--muted-foreground))'
							},
							accent: {
								DEFAULT: 'hsl(var(--accent))',
								foreground: 'hsl(var(--accent-foreground))'
							},
							popover: {
								DEFAULT: 'hsl(var(--popover))',
								foreground: 'hsl(var(--popover-foreground))'
							},
							card: {
								DEFAULT: 'hsl(var(--card))',
								foreground: 'hsl(var(--card-foreground))'
							},
						},
					}
				}
			}
		</script>
		<style type="text/tailwindcss">
			@layer base {
				:root {
					--background: 0 0% 100%;
--foreground: 240 10% 3.9%;
--card: 0 0% 100%;
--card-foreground: 240 10% 3.9%;
--popover: 0 0% 100%;
--popover-foreground: 240 10% 3.9%;
--primary: 240 5.9% 10%;
--primary-foreground: 0 0% 98%;
--secondary: 240 4.8% 95.9%;
--secondary-foreground: 240 5.9% 10%;
--muted: 240 4.8% 95.9%;
--muted-foreground: 240 3.8% 46.1%;
--accent: 240 4.8% 95.9%;
--accent-foreground: 240 5.9% 10%;
--destructive: 0 84.2% 60.2%;
--destructive-foreground: 0 0% 98%;
--border: 240 5.9% 90%;
--input: 240 5.9% 90%;
--ring: 240 5.9% 10%;
--radius: 0.5rem;
				}
				.dark {
					--background: 240 10% 3.9%;
--foreground: 0 0% 98%;
--card: 240 10% 3.9%;
--card-foreground: 0 0% 98%;
--popover: 240 10% 3.9%;
--popover-foreground: 0 0% 98%;
--primary: 0 0% 98%;
--primary-foreground: 240 5.9% 10%;
--secondary: 240 3.7% 15.9%;
--secondary-foreground: 0 0% 98%;
--muted: 240 3.7% 15.9%;
--muted-foreground: 240 5% 64.9%;
--accent: 240 3.7% 15.9%;
--accent-foreground: 0 0% 98%;
--destructive: 0 62.8% 30.6%;
--destructive-foreground: 0 0% 98%;
--border: 240 3.7% 15.9%;
--input: 240 3.7% 15.9%;
--ring: 240 4.9% 83.9%;
				}
			}
		</style>
  </head>
  <body>
    <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charSet="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=contain, user-scalable=no"/>
        <link rel="preload" as="image" href="https://cdn.beacons.ai/images/beacons_assets/made-with-beacons.png"/>
        <link rel="stylesheet" href="https://beacons.ai/_next/static/css/cec9a5860a368e30.css" data-precedence="next"/>
        <link rel="stylesheet" href="https://beacons.ai/_next/static/css/fca59e7c5ca010dc.css" data-precedence="next"/>
        <link rel="stylesheet" href="https://beacons.ai/_next/static/css/f1c1b11210d202b4.css" data-precedence="next"/>
        <link rel="stylesheet" href="https://beacons.ai/_next/static/css/5077ce94dd45ae31.css" data-precedence="next"/>
        <link rel="stylesheet" href="https://beacons.ai/_next/static/css/c0b8703e7d1ef173.css" data-precedence="next"/>
        <link rel="stylesheet" href="https://beacons.ai/_next/static/css/2f4f14aec8c88745.css" data-precedence="next"/>
        <link rel="preload" as="script" fetchPriority="low" href="https://beacons.ai/_next/static/chunks/webpack-df60ad87447b8a2c.js"/>
        <script src="https://beacons.ai/_next/static/chunks/9d13b1b8-8148a511ac2ab10e.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/4582-d5f30fa55e73be04.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/main-app-d13a94f2396cd32d.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/6829-cf90ca5e0c9467e4.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/app/layout-6e722cc4c3da36c7.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/6844-d4e8b0889c382aef.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/9384-746ea90a90b977aa.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/app/error-7a557e1d05c36e52.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/app/global-error-af0cbd177542a539.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/c0ee81ba-8f034ff5772dd4db.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/5723-c2750a8c7e4aae0d.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/8003-7f358badc18bf9d8.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/3127-e2fe3afb7cb8b6fe.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/4924-eeeac8bb749d9773.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/7541-543c748d472a4a78.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/7199-6143064827efc080.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/4979-7e851e19f6480f7c.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/3501-1d6c6587445cf6b2.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/8690-0e74dee08771593e.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/3188-468ee9e55546b510.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/3225-a74d33bc44e72678.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/8675-0a62a0f90af3bad6.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/8763-4c577172c476b725.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/2813-ec85ccadedbdd0ed.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/3843-33c67a0771d0bd85.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/9400-977472b9c535a150.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/6872-4ab6a36d6c8f14c2.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/4210-fc8b8200c29c2843.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/8970-4a0fc2d7846c70ab.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/9481-c3ee1e9a4c5e61e0.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/1293-d4c274ea16e41539.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/7231-403a8af3a243447c.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/6858-40e5aaabb32aeb3e.js" async></script>
        <script src="https://beacons.ai/_next/static/chunks/app/user_website_domain/%5BbeaconsUsername%5D/websites/%5Bversion%5D/%5BuserWebsiteId%5D/%5B%5B...pageSlugs%5D%5D/page-4b5f4bfa1dabf2c5.js" async></script>
        <link href="/splashscreens/iphone5_splash.png" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/iphone6_splash.png" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/iphoneplus_splash.png" media="(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/iphonex_splash.png" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/iphonexr_splash.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/iphonexsmax_splash.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/ipad_splash.png" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/ipadpro1_splash.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/ipadpro3_splash.png" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <link href="/splashscreens/ipadpro2_splash.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>
        <meta name="theme-color" content="#000000"/>
        <title>Digital Marketing</title>
        <meta name="description" content="zack4dev&#x27;s Website"/>
        <link rel="manifest" href="/manifest.json" crossorigin="use-credentials"/>
        <meta name="robots" content="index, follow"/>
        <meta name="fb:app_id" content="3294868390539011"/>
        <link rel="canonical" href="https://beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516/undefined"/>
        <meta name="apple-mobile-web-app-capable" content="yes"/>
        <meta name="apple-mobile-web-app-title" content="Beacons"/>
        <meta name="apple-mobile-web-app-status-bar-style" content="default"/>
        <meta property="og:title" content="Digital Marketing"/>
        <meta property="og:description" content="zack4dev&#x27;s Website"/>
        <meta property="og:url" content="https://beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516/undefined"/>
        <meta property="og:site_name" content="Beacons"/>
        <meta property="og:image" content="https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482"/>
        <meta property="og:image:width" content="600"/>
        <meta property="og:image:height" content="600"/>
        <meta name="twitter:card" content="summary_large_image"/>
        <meta name="twitter:creator" content="zack4dev"/>
        <meta name="twitter:title" content="Digital Marketing"/>
        <meta name="twitter:description" content="zack4dev&#x27;s Website"/>
        <meta name="twitter:image" content="https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482"/>
        <link rel="shortcut icon" href="/favicon.ico"/>
        <link rel="icon" href="/favicon.ico"/>
        <link rel="apple-touch-icon" href="/favicon.ico"/>
        <script src="https://beacons.ai/_next/static/chunks/polyfills-78c92fac7aa8fdd8.js" noModule></script>
        <style id="__jsx-undefined">
            @import url(https://fonts.googleapis.com/css?family=Poppins:400|Merriweather:400&display=swap); #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 {
                font-family: Poppins, sans-serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 h1 {
                font-family: Merriweather, serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 h2 {
                font-family: Merriweather, serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 h3 {
                font-family: Merriweather, serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .website-button {
                font-family: Merriweather, serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .nav-link {
                font-family: Merriweather, serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 h4 {
                font-family: Merriweather, serif;
                font-weight: 400;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .website-button {
                border-radius: 24px !important;
                border-width: 4px !important;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c {
                color: #00473e;
                background-color: #faae2b;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .website-button.primary {
                color: #f2f7f5;
                background-color: #00473e;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .website-button.secondary {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .seated-event-link1 {
                color: #f2f7f5;
                background-color: #00473e;
                border-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .seated-event-link1:hover {
                color: #f2f7f5;
                background-color: #00473e;
                border-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .seated-follow-link {
                color: #00473e;
                background-color: #f2f7f5;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .seated-follow-link:hover {
                color: #f2f7f5;
                background-color: #00473e;
                border-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .seated-events-table {
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-c .seated-event-row {
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b {
                color: #f2f7f5;
                background-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .website-button.primary {
                color: #00473e;
                background-color: #faae2b;
                border-color: #faae2b;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .website-button.secondary {
                color: #f2f7f5;
                background-color: #00473e;
                border-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .seated-event-link1 {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .seated-event-link1:hover {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .seated-follow-link {
                color: #faae2b;
                background-color: #00473e;
                border-color: #faae2b;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .seated-follow-link:hover {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .seated-events-table {
                border-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-b .seated-event-row {
                border-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a {
                color: #00473e;
                background-color: #f2f7f5;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .website-button.primary {
                color: #00473e;
                background-color: #faae2b;
                border-color: #faae2b;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .website-button.secondary {
                color: #00473e;
                background-color: #f2f7f5;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .seated-event-link1 {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .seated-event-link1:hover {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .seated-follow-link {
                color: #faae2b;
                background-color: #00473e;
                border-color: #faae2b;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .seated-follow-link:hover {
                color: #00473e;
                background-color: #faae2b;
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .seated-events-table {
                border-color: #00473e;
            }

            #website-viewer-a9934823-5188-40da-953e-79f51b5c0516 .subpalette-a .seated-event-row {
                border-color: #00473e;
            }
        </style>
    </head>
    <body>
        <beacons-tag></beacons-tag>
        <div id="root">
            <div class="previewer website-viewer relative h-full overflow-y-auto" id="website-viewer-a9934823-5188-40da-953e-79f51b5c0516">
                <div class="text fixed bottom-4 left-4 z-30 rounded-8 bg-gray-200 px-4 py-2 font-poppins preview-mobile:right-4">
                    <div class="text-md-bold">This is a preview of your website</div>
                    <div>Your website is not published yet</div>
                </div>
                <div class>
                    <div class="absolute top-0 z-30 w-full">
                        <div>
                            <div class="website-viewer-menu subpalette-b box-border flex w-full items-center justify-between px-2 preview-desktop:px-4 !bg-transparent" style="padding-top:8px;padding-bottom:8px">
                                <div class="flex items-center" style="min-width:none;height:40px">
                                    <a class="w-full" style="text-decoration:none;color:inherit" tabindex="0" role="button" href="/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516">
                                        <h1 style="font-size:24px">Digital Marketing</h1>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-b hero-block-container flex justify-center outline-transparent" style="padding-bottom:50px;padding-top:122px;background-image:url(https://images.unsplash.com/photo-1564463836146-4e30522c2984?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjE0Nzh8&amp;ixlib=rb-4.0.3);background-size:cover;background-position:center">
                        <div aria-label="viewer-overlay" class="absolute inset-0 opacity-30 bg-black"></div>
                        <div class="hero-block-layout-3 website-side-padding relative box-border flex w-full text-center" style="max-width:1440px;min-height:640px;text-align:center">
                            <div class="w-full preview-mobile:self-center preview-desktop:self-center">
                                <h1 class="website-display-2 w-full">Become a digital marketing expert</h1>
                                <div class="!mt-3">
                                    <h4 class="website-subheading-1 w-full">Unlock Your Potential with Expert Guidance</h4>
                                </div>
                                <div class="flex w-full gap-4 mt-6" style="justify-content:center">
                                    <a class="website-button primary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" aria-label="hero-block-button Get started" rel="noopener noreferrer" target="_blank" href="https://beacons.ai">
                                        <div class="flex items-center">Get started</div>
                                    </a>
                                    <a class="website-button secondary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" aria-label="hero-block-button Learn more" rel="noopener noreferrer" target="_blank" href="https://beacons.ai">
                                        <div class="flex items-center">Learn more</div>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a content-block-container flex justify-center outline-transparent" style="padding-bottom:24px;padding-top:24px">
                        <div class="content-block box-border flex grow justify-between overflow-hidden px-0 preview-mobile:flex-col website-side-padding" style="max-width:1440px">
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:0;padding-right:0">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a content-block-container flex justify-center outline-transparent" style="padding-bottom:100px;padding-top:100px">
                        <div class="content-block box-border flex grow justify-between overflow-hidden px-0 preview-mobile:flex-col website-side-padding" style="max-width:1440px">
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:0;padding-right:48px;flex-basis:25%">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <br>
                                </div>
                            </div>
                            <div class="shrink preview-desktop:px-9 preview-desktop:py-2 preview-mobile:py-9">
                                <div class="preview-desktop:h-full preview-desktop:w-px preview-mobile:h-px preview-mobile:w-full" style="background-color:#194d33"></div>
                            </div>
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:30px;padding-top:30px;padding-left:48px;padding-right:48px;flex-basis:50%">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <h1 align="center">Inspiring creativity, one idea at a time.</h1>
                                    <p align="center">Transforming creators into storytelling masters. Join me on the journey to unleash your creativity and captivate your audience.</p>
                                </div>
                            </div>
                            <div class="shrink preview-desktop:px-9 preview-desktop:py-2 preview-mobile:py-9">
                                <div class="preview-desktop:h-full preview-desktop:w-px preview-mobile:h-px preview-mobile:w-full" style="background-color:#194d33"></div>
                            </div>
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:48px;padding-right:0;flex-basis:25%">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a content-block-container flex justify-center outline-transparent" style="padding-bottom:24px;padding-top:24px">
                        <div class="content-block box-border flex grow justify-between overflow-hidden px-0 preview-mobile:flex-col website-side-padding" style="max-width:1440px">
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:0;padding-right:0">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-b hero-block-container flex justify-center outline-transparent" style="padding-bottom:41px;padding-top:33px;background-image:url(https://images.unsplash.com/photo-1503407768185-30e0f283410a?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjIzNjB8&amp;ixlib=rb-4.0.3);background-size:cover;background-position:center">
                        <div aria-label="viewer-overlay" class="absolute inset-0 opacity-30 bg-black"></div>
                        <div class="hero-block-layout-4 website-side-padding relative box-border flex w-full" style="max-width:1440px;min-height:640px;text-align:left">
                            <div class="w-full preview-mobile:self-center preview-desktop:self-center">
                                <h1 class="website-heading-1 w-full">Ready to Elevate Your Marketing Skills?</h1>
                                <div class="flex gap-4 mt-6" style="justify-content:flex-start">
                                    <a class="website-button primary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" aria-label="hero-block-button Let&#x27;s get started!" rel="noopener noreferrer" target="_blank" href="https://beacons.ai">
                                        <div class="flex items-center">Let &#x27;s get started!</div>
                                    </a>
                                    <a class="website-button secondary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" aria-label="hero-block-button Learn more" rel="noopener noreferrer" target="_blank" href="https://beacons.ai">
                                        <div class="flex items-center">Learn more</div>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a content-block-container flex justify-center outline-transparent" style="padding-bottom:24px;padding-top:24px">
                        <div class="content-block box-border flex grow justify-between overflow-hidden px-0 preview-mobile:flex-col website-side-padding" style="max-width:1440px">
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:24px;padding-top:24px;padding-left:0;padding-right:0">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a content-block-container flex justify-center outline-transparent" style="padding-bottom:100px;padding-top:100px">
                        <div class="content-block box-border flex grow justify-between overflow-hidden px-0 preview-mobile:flex-col website-side-padding" style="max-width:1440px">
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:0;padding-right:48px;flex-basis:33%">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <h3 align="center">
                                        <strong>Beginner’s Guide</strong>
                                    </h3>
                                    <p align="center">
                                        <strong>Free</strong>
                                    </p>
                                    <br>
                                    <p align="center">Get started with expert advice, a comprehensive to-do list, and valuable resources to guide you along the way.</p>
                                </div>
                            </div>
                            <div class="shrink preview-desktop:px-9 preview-desktop:py-2 preview-mobile:py-9">
                                <div class="preview-desktop:h-full preview-desktop:w-px preview-mobile:h-px preview-mobile:w-full" style="background-color:black"></div>
                            </div>
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:48px;padding-right:48px;flex-basis:33%">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <h3 align="center">
                                        <strong>Starter Park</strong>
                                    </h3>
                                    <p align="center">
                                        <strong>$19</strong>
                                    </p>
                                    <br>
                                    <p align="center">Unlock a comprehensive package featuring expert marketing tips, a social posting calendar, and essential tools to fuel your success.</p>
                                </div>
                            </div>
                            <div class="shrink preview-desktop:px-9 preview-desktop:py-2 preview-mobile:py-9">
                                <div class="preview-desktop:h-full preview-desktop:w-px preview-mobile:h-px preview-mobile:w-full" style="background-color:black"></div>
                            </div>
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:48px;padding-right:0;flex-basis:33%">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <h3 align="center">
                                        <strong>Monthly Membership</strong>
                                    </h3>
                                    <p align="center">
                                        <strong>$39/mo</strong>
                                    </p>
                                    <br>
                                    <p align="center">Gain monthly entry to our expanding collection of classes, training programs, and personalized one-on-one coaching sessions.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a content-block-container flex justify-center outline-transparent" style="padding-bottom:78px;padding-top:24px">
                        <div class="content-block box-border flex grow justify-between overflow-hidden px-0 preview-mobile:flex-col website-side-padding" style="max-width:1440px">
                            <div class="flex grow self-stretch preview-mobile:!px-2" style="padding-bottom:0px;padding-top:0px;padding-left:0;padding-right:0">
                                <div class="rich-text-html relative grow outline outline-2 -outline-offset-2 preview-mobile:min-w-0 preview-mobile:self-center outline-transparent preview-desktop:self-center">
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-b hero-block-container flex justify-center outline-transparent" style="padding-bottom:24px;padding-top:24px;background-image:url(https://images.unsplash.com/photo-1537218764248-06f18c55f006?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjMxOTZ8&amp;ixlib=rb-4.0.3);background-size:cover;background-position:center">
                        <div aria-label="viewer-overlay" class="absolute inset-0 opacity-30 bg-black"></div>
                        <div class="hero-block-layout-3 website-side-padding relative box-border flex w-full text-center" style="max-width:1440px;min-height:640px;text-align:center">
                            <div class="w-full preview-mobile:self-center preview-desktop:self-center">
                                <h1 class="website-heading-1 w-full">Let &#x27;s build your digital marketing empire together</h1>
                                <div class="flex w-full gap-4 mt-6" style="justify-content:center">
                                    <a class="website-button primary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" aria-label="hero-block-button Join now" rel="noopener noreferrer" target="_blank" href="https://beacons.ai">
                                        <div class="flex items-center">Join now</div>
                                    </a>
                                    <a class="website-button secondary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" aria-label="hero-block-button Learn more" rel="noopener noreferrer" target="_blank" href="https://beacons.ai">
                                        <div class="flex items-center">Learn more</div>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="preview-mobile:hidden">
                        <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a youtube-block-container-desktop outline-transparent" style="padding-bottom:184px;padding-top:135px">
                            <div class="relative mx-auto box-border" style="max-width:1440px website-side-padding;text-align:center">
                                <h1 class="website-heading-1 w-full">Check out our content</h1>
                                <div class="!mt-3">
                                    <h4 class="website-subheading-2 w-full">Learn from the experts</h4>
                                </div>
                                <div class="mt-12">
                                    <div class="mx-auto" style="width:100%">
                                        <div class="grid grid-cols-3" style="gap:24px">
                                            <div class="youtube-block-item aspect-video grow overflow-hidden">
                                                <div class="max-h-screen w-full">
                                                    <div style="width:600px">
                                                        <div role="button" tabindex="0" class="cursor-pointer YoutubePlayer_lazy-youtube-player__GTswb" style="background-image:url(https://img.youtube.com/vi/O1YntbDxqcM/mqdefault.jpg);width:100%;height:100%" aria-label="Youtube Embed">
                                                            <div class="YoutubePlayer_play-button__o_Dt1"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="youtube-block-item aspect-video grow overflow-hidden">
                                                <div class="max-h-screen w-full">
                                                    <div style="width:600px">
                                                        <div role="button" tabindex="0" class="cursor-pointer YoutubePlayer_lazy-youtube-player__GTswb" style="background-image:url(https://img.youtube.com/vi/obFvKftbhKM/mqdefault.jpg);width:100%;height:100%" aria-label="Youtube Embed">
                                                            <div class="YoutubePlayer_play-button__o_Dt1"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="youtube-block-item aspect-video grow overflow-hidden">
                                                <div class="max-h-screen w-full">
                                                    <div style="width:600px">
                                                        <div role="button" tabindex="0" class="cursor-pointer YoutubePlayer_lazy-youtube-player__GTswb" style="background-image:url(https://img.youtube.com/vi/3FPfEjPmRks/mqdefault.jpg);width:100%;height:100%" aria-label="Youtube Embed">
                                                            <div class="YoutubePlayer_play-button__o_Dt1"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="preview-desktop:hidden">
                        <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-a youtube-block-container-mobile outline-transparent" style="padding-bottom:184px;padding-top:135px">
                            <div class="relative mx-auto box-border" style="max-width:1440px website-side-padding;text-align:center">
                                <h1 class="website-heading-1 w-full">Check out our content</h1>
                                <div class="!mt-3">
                                    <h4 class="website-subheading-2 w-full">Learn from the experts</h4>
                                </div>
                                <div class="mt-12">
                                    <div class="mx-auto" style="width:100%">
                                        <div class="grid grid-cols-2" style="gap:16px">
                                            <div class="youtube-block-item aspect-video grow overflow-hidden">
                                                <div class="max-h-screen w-full">
                                                    <div style="width:600px">
                                                        <div role="button" tabindex="0" class="cursor-pointer YoutubePlayer_lazy-youtube-player__GTswb" style="background-image:url(https://img.youtube.com/vi/O1YntbDxqcM/mqdefault.jpg);width:100%;height:100%" aria-label="Youtube Embed">
                                                            <div class="YoutubePlayer_play-button__o_Dt1"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="youtube-block-item aspect-video grow overflow-hidden">
                                                <div class="max-h-screen w-full">
                                                    <div style="width:600px">
                                                        <div role="button" tabindex="0" class="cursor-pointer YoutubePlayer_lazy-youtube-player__GTswb" style="background-image:url(https://img.youtube.com/vi/obFvKftbhKM/mqdefault.jpg);width:100%;height:100%" aria-label="Youtube Embed">
                                                            <div class="YoutubePlayer_play-button__o_Dt1"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="mx-auto" style="margin-top:16px;width:calc(100% - 16px)">
                                            <div class="mx-auto flex" style="gap:16px;width:calc(50% + 0px)">
                                                <div class="youtube-block-item aspect-video grow overflow-hidden">
                                                    <div class="max-h-screen w-full">
                                                        <div style="width:600px">
                                                            <div role="button" tabindex="0" class="cursor-pointer YoutubePlayer_lazy-youtube-player__GTswb" style="background-image:url(https://img.youtube.com/vi/3FPfEjPmRks/mqdefault.jpg);width:100%;height:100%" aria-label="Youtube Embed">
                                                                <div class="YoutubePlayer_play-button__o_Dt1"></div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative outline outline-2 -outline-offset-2 website-block subpalette-b email-block-container text-center outline-transparent" style="padding-bottom:120px;padding-top:120px;background-image:url(https://images.unsplash.com/photo-1529866147017-1b4508a0485d?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjI5NTF8&amp;ixlib=rb-4.0.3);background-size:cover;background-position:center">
                        <div aria-label="viewer-overlay" class="absolute inset-0 opacity-30 bg-black"></div>
                        <div class="website-side-padding relative mx-auto box-border py-0.5" style="max-width:1440px;text-align:center">
                            <h1 class="website-heading-1 w-full">Stay in the Loop</h1>
                            <div class="!mt-3">
                                <h4 class="website-subheading-2 w-full">Subscribe to get my monthly newsletter</h4>
                            </div>
                            <div class="mt-12">
                                <div class="mx-auto w-full gap-3 grid preview-desktop:grid-cols-2" style="max-width:732px">
                                    <div class="grow">
                                        <div class="flex gap-3">
                                            <style data-emotion="css feqhe6">
                                                .css-feqhe6 {
                                                    display: -webkit-inline-box;
                                                    display: -webkit-inline-flex;
                                                    display: -ms-inline-flexbox;
                                                    display: inline-flex;
                                                    -webkit-flex-direction: column;
                                                    -ms-flex-direction: column;
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
                                            <div class="MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-feqhe6">
                                                <style data-emotion="css-global 1prfaxn">
                                                    @-webkit-keyframes mui-auto-fill {
                                                        from {
                                                            display: block;
                                                        }
                                                    }

                                                    @keyframes mui-auto-fill {
                                                        from {
                                                            display: block;
                                                        }
                                                    }

                                                    @-webkit-keyframes mui-auto-fill-cancel {
                                                        from {
                                                            display: block;
                                                        }
                                                    }

                                                    @keyframes mui-auto-fill-cancel {
                                                        from {
                                                            display: block;
                                                        }
                                                    }
                                                </style>
                                                <style data-emotion="css 1bewqcb">
                                                    .css-1bewqcb {
                                                        font-family: 'Poppins',Helvetica,sans-serif;
                                                        font-weight: 400;
                                                        font-size: 1rem;
                                                        line-height: 1.4375em;
                                                        color: rgba(0, 0, 0, 0.87);
                                                        box-sizing: border-box;
                                                        position: relative;
                                                        cursor: text;
                                                        display: -webkit-inline-box;
                                                        display: -webkit-inline-flex;
                                                        display: -ms-inline-flexbox;
                                                        display: inline-flex;
                                                        -webkit-align-items: center;
                                                        -webkit-box-align: center;
                                                        -ms-flex-align: center;
                                                        align-items: center;
                                                        width: 100%;
                                                        position: relative;
                                                        border-radius: 8px;
                                                        overflow: hidden;
                                                        background-color: #FFFFFF;
                                                        font-weight: 400;
                                                    }

                                                    .css-1bewqcb.Mui-disabled {
                                                        color: rgba(0, 0, 0, 0.38);
                                                        cursor: default;
                                                    }

                                                    .css-1bewqcb:hover .MuiOutlinedInput-notchedOutline {
                                                        border-color: rgba(0, 0, 0, 0.87);
                                                    }

                                                    @media (hover: none) {
                                                        .css-1bewqcb:hover .MuiOutlinedInput-notchedOutline {
                                                            border-color:rgba(0, 0, 0, 0.23);
                                                        }
                                                    }

                                                    .css-1bewqcb.Mui-focused .MuiOutlinedInput-notchedOutline {
                                                        border-color: #1976d2;
                                                        border-width: 2px;
                                                    }

                                                    .css-1bewqcb.Mui-error .MuiOutlinedInput-notchedOutline {
                                                        border-color: #d32f2f;
                                                    }

                                                    .css-1bewqcb.Mui-disabled .MuiOutlinedInput-notchedOutline {
                                                        border-color: rgba(0, 0, 0, 0.26);
                                                    }

                                                    .css-1bewqcb fieldset {
                                                        border-color: #E0E0E0!important;
                                                        border-width: 1px!important;
                                                    }

                                                    .css-1bewqcb.Mui-focused fieldset {
                                                        border-color: #1C1C1C!important;
                                                        border-width: 1px!important;
                                                    }

                                                    .css-1bewqcb.Mui-error fieldset {
                                                        border-color: #B00020!important;
                                                        border-width: 1px!important;
                                                    }

                                                    .css-1bewqcb.Mui-disabled {
                                                        border-color: #1C1C1C!important;
                                                        color: #9E9E9E;
                                                    }
                                                </style>
                                                <div class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl css-1bewqcb">
                                                    <style data-emotion="css 1x5jdmq">
                                                        .css-1x5jdmq {
                                                            font: inherit;
                                                            letter-spacing: inherit;
                                                            color: currentColor;
                                                            padding: 4px 0 5px;
                                                            border: 0;
                                                            box-sizing: content-box;
                                                            background: none;
                                                            height: 1.4375em;
                                                            margin: 0;
                                                            -webkit-tap-highlight-color: transparent;
                                                            display: block;
                                                            min-width: 0;
                                                            width: 100%;
                                                            -webkit-animation-name: mui-auto-fill-cancel;
                                                            animation-name: mui-auto-fill-cancel;
                                                            -webkit-animation-duration: 10ms;
                                                            animation-duration: 10ms;
                                                            padding: 16.5px 14px;
                                                        }

                                                        .css-1x5jdmq::-webkit-input-placeholder {
                                                            color: currentColor;
                                                            opacity: 0.42;
                                                            -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                            transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        }

                                                        .css-1x5jdmq::-moz-placeholder {
                                                            color: currentColor;
                                                            opacity: 0.42;
                                                            -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                            transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        }

                                                        .css-1x5jdmq:-ms-input-placeholder {
                                                            color: currentColor;
                                                            opacity: 0.42;
                                                            -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                            transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        }

                                                        .css-1x5jdmq::-ms-input-placeholder {
                                                            color: currentColor;
                                                            opacity: 0.42;
                                                            -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                            transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        }

                                                        .css-1x5jdmq:focus {
                                                            outline: 0;
                                                        }

                                                        .css-1x5jdmq:invalid {
                                                            box-shadow: none;
                                                        }

                                                        .css-1x5jdmq::-webkit-search-decoration {
                                                            -webkit-appearance: none;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq::-webkit-input-placeholder {
                                                            opacity: 0!important;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq::-moz-placeholder {
                                                            opacity: 0!important;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:-ms-input-placeholder {
                                                            opacity: 0!important;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq::-ms-input-placeholder {
                                                            opacity: 0!important;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus::-webkit-input-placeholder {
                                                            opacity: 0.42;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus::-moz-placeholder {
                                                            opacity: 0.42;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus:-ms-input-placeholder {
                                                            opacity: 0.42;
                                                        }

                                                        label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus::-ms-input-placeholder {
                                                            opacity: 0.42;
                                                        }

                                                        .css-1x5jdmq.Mui-disabled {
                                                            opacity: 1;
                                                            -webkit-text-fill-color: rgba(0, 0, 0, 0.38);
                                                        }

                                                        .css-1x5jdmq:-webkit-autofill {
                                                            -webkit-animation-duration: 5000s;
                                                            animation-duration: 5000s;
                                                            -webkit-animation-name: mui-auto-fill;
                                                            animation-name: mui-auto-fill;
                                                        }

                                                        .css-1x5jdmq:-webkit-autofill {
                                                            border-radius: inherit;
                                                        }
                                                    </style>
                                                    <input aria-invalid="false" id=":R1avml9j7rrrrrrqja:" placeholder="Full name" type="text" class="MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq" value/>
                                                    <style data-emotion="css 19w1uun">
                                                        .css-19w1uun {
                                                            border-color: rgba(0, 0, 0, 0.23);
                                                        }
                                                    </style>
                                                    <style data-emotion="css igs3ac">
                                                        .css-igs3ac {
                                                            text-align: left;
                                                            position: absolute;
                                                            bottom: 0;
                                                            right: 0;
                                                            top: -5px;
                                                            left: 0;
                                                            margin: 0;
                                                            padding: 0 8px;
                                                            pointer-events: none;
                                                            border-radius: inherit;
                                                            border-style: solid;
                                                            border-width: 1px;
                                                            overflow: hidden;
                                                            min-width: 0%;
                                                            border-color: rgba(0, 0, 0, 0.23);
                                                        }
                                                    </style>
                                                    <fieldset aria-hidden="true" class="MuiOutlinedInput-notchedOutline css-igs3ac">
                                                        <style data-emotion="css ihdtdm">
                                                            .css-ihdtdm {
                                                                float: unset;
                                                                width: auto;
                                                                overflow: hidden;
                                                                padding: 0;
                                                                line-height: 11px;
                                                                -webkit-transition: width 150ms cubic-bezier(0.0, 0, 0.2, 1) 0ms;
                                                                transition: width 150ms cubic-bezier(0.0, 0, 0.2, 1) 0ms;
                                                            }
                                                        </style>
                                                        <legend class="css-ihdtdm">
                                                            <span class="notranslate">​</span>
                                                        </legend>
                                                    </fieldset>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="grow">
                                        <style data-emotion="css feqhe6">
                                            .css-feqhe6 {
                                                display: -webkit-inline-box;
                                                display: -webkit-inline-flex;
                                                display: -ms-inline-flexbox;
                                                display: inline-flex;
                                                -webkit-flex-direction: column;
                                                -ms-flex-direction: column;
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
                                        <div class="MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-feqhe6">
                                            <style data-emotion="css-global 1prfaxn">
                                                @-webkit-keyframes mui-auto-fill {
                                                    from {
                                                        display: block;
                                                    }
                                                }

                                                @keyframes mui-auto-fill {
                                                    from {
                                                        display: block;
                                                    }
                                                }

                                                @-webkit-keyframes mui-auto-fill-cancel {
                                                    from {
                                                        display: block;
                                                    }
                                                }

                                                @keyframes mui-auto-fill-cancel {
                                                    from {
                                                        display: block;
                                                    }
                                                }
                                            </style>
                                            <style data-emotion="css 1bewqcb">
                                                .css-1bewqcb {
                                                    font-family: 'Poppins',Helvetica,sans-serif;
                                                    font-weight: 400;
                                                    font-size: 1rem;
                                                    line-height: 1.4375em;
                                                    color: rgba(0, 0, 0, 0.87);
                                                    box-sizing: border-box;
                                                    position: relative;
                                                    cursor: text;
                                                    display: -webkit-inline-box;
                                                    display: -webkit-inline-flex;
                                                    display: -ms-inline-flexbox;
                                                    display: inline-flex;
                                                    -webkit-align-items: center;
                                                    -webkit-box-align: center;
                                                    -ms-flex-align: center;
                                                    align-items: center;
                                                    width: 100%;
                                                    position: relative;
                                                    border-radius: 8px;
                                                    overflow: hidden;
                                                    background-color: #FFFFFF;
                                                    font-weight: 400;
                                                }

                                                .css-1bewqcb.Mui-disabled {
                                                    color: rgba(0, 0, 0, 0.38);
                                                    cursor: default;
                                                }

                                                .css-1bewqcb:hover .MuiOutlinedInput-notchedOutline {
                                                    border-color: rgba(0, 0, 0, 0.87);
                                                }

                                                @media (hover: none) {
                                                    .css-1bewqcb:hover .MuiOutlinedInput-notchedOutline {
                                                        border-color:rgba(0, 0, 0, 0.23);
                                                    }
                                                }

                                                .css-1bewqcb.Mui-focused .MuiOutlinedInput-notchedOutline {
                                                    border-color: #1976d2;
                                                    border-width: 2px;
                                                }

                                                .css-1bewqcb.Mui-error .MuiOutlinedInput-notchedOutline {
                                                    border-color: #d32f2f;
                                                }

                                                .css-1bewqcb.Mui-disabled .MuiOutlinedInput-notchedOutline {
                                                    border-color: rgba(0, 0, 0, 0.26);
                                                }

                                                .css-1bewqcb fieldset {
                                                    border-color: #E0E0E0!important;
                                                    border-width: 1px!important;
                                                }

                                                .css-1bewqcb.Mui-focused fieldset {
                                                    border-color: #1C1C1C!important;
                                                    border-width: 1px!important;
                                                }

                                                .css-1bewqcb.Mui-error fieldset {
                                                    border-color: #B00020!important;
                                                    border-width: 1px!important;
                                                }

                                                .css-1bewqcb.Mui-disabled {
                                                    border-color: #1C1C1C!important;
                                                    color: #9E9E9E;
                                                }
                                            </style>
                                            <div class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl css-1bewqcb">
                                                <style data-emotion="css 1x5jdmq">
                                                    .css-1x5jdmq {
                                                        font: inherit;
                                                        letter-spacing: inherit;
                                                        color: currentColor;
                                                        padding: 4px 0 5px;
                                                        border: 0;
                                                        box-sizing: content-box;
                                                        background: none;
                                                        height: 1.4375em;
                                                        margin: 0;
                                                        -webkit-tap-highlight-color: transparent;
                                                        display: block;
                                                        min-width: 0;
                                                        width: 100%;
                                                        -webkit-animation-name: mui-auto-fill-cancel;
                                                        animation-name: mui-auto-fill-cancel;
                                                        -webkit-animation-duration: 10ms;
                                                        animation-duration: 10ms;
                                                        padding: 16.5px 14px;
                                                    }

                                                    .css-1x5jdmq::-webkit-input-placeholder {
                                                        color: currentColor;
                                                        opacity: 0.42;
                                                        -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                    }

                                                    .css-1x5jdmq::-moz-placeholder {
                                                        color: currentColor;
                                                        opacity: 0.42;
                                                        -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                    }

                                                    .css-1x5jdmq:-ms-input-placeholder {
                                                        color: currentColor;
                                                        opacity: 0.42;
                                                        -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                    }

                                                    .css-1x5jdmq::-ms-input-placeholder {
                                                        color: currentColor;
                                                        opacity: 0.42;
                                                        -webkit-transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                        transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
                                                    }

                                                    .css-1x5jdmq:focus {
                                                        outline: 0;
                                                    }

                                                    .css-1x5jdmq:invalid {
                                                        box-shadow: none;
                                                    }

                                                    .css-1x5jdmq::-webkit-search-decoration {
                                                        -webkit-appearance: none;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq::-webkit-input-placeholder {
                                                        opacity: 0!important;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq::-moz-placeholder {
                                                        opacity: 0!important;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:-ms-input-placeholder {
                                                        opacity: 0!important;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq::-ms-input-placeholder {
                                                        opacity: 0!important;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus::-webkit-input-placeholder {
                                                        opacity: 0.42;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus::-moz-placeholder {
                                                        opacity: 0.42;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus:-ms-input-placeholder {
                                                        opacity: 0.42;
                                                    }

                                                    label[data-shrink=false]+.MuiInputBase-formControl .css-1x5jdmq:focus::-ms-input-placeholder {
                                                        opacity: 0.42;
                                                    }

                                                    .css-1x5jdmq.Mui-disabled {
                                                        opacity: 1;
                                                        -webkit-text-fill-color: rgba(0, 0, 0, 0.38);
                                                    }

                                                    .css-1x5jdmq:-webkit-autofill {
                                                        -webkit-animation-duration: 5000s;
                                                        animation-duration: 5000s;
                                                        -webkit-animation-name: mui-auto-fill;
                                                        animation-name: mui-auto-fill;
                                                    }

                                                    .css-1x5jdmq:-webkit-autofill {
                                                        border-radius: inherit;
                                                    }
                                                </style>
                                                <input aria-invalid="false" id=":Rivml9j7rrrrrrqja:" placeholder="Email" type="text" class="MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq" value/>
                                                <style data-emotion="css 19w1uun">
                                                    .css-19w1uun {
                                                        border-color: rgba(0, 0, 0, 0.23);
                                                    }
                                                </style>
                                                <style data-emotion="css igs3ac">
                                                    .css-igs3ac {
                                                        text-align: left;
                                                        position: absolute;
                                                        bottom: 0;
                                                        right: 0;
                                                        top: -5px;
                                                        left: 0;
                                                        margin: 0;
                                                        padding: 0 8px;
                                                        pointer-events: none;
                                                        border-radius: inherit;
                                                        border-style: solid;
                                                        border-width: 1px;
                                                        overflow: hidden;
                                                        min-width: 0%;
                                                        border-color: rgba(0, 0, 0, 0.23);
                                                    }
                                                </style>
                                                <fieldset aria-hidden="true" class="MuiOutlinedInput-notchedOutline css-igs3ac">
                                                    <style data-emotion="css ihdtdm">
                                                        .css-ihdtdm {
                                                            float: unset;
                                                            width: auto;
                                                            overflow: hidden;
                                                            padding: 0;
                                                            line-height: 11px;
                                                            -webkit-transition: width 150ms cubic-bezier(0.0, 0, 0.2, 1) 0ms;
                                                            transition: width 150ms cubic-bezier(0.0, 0, 0.2, 1) 0ms;
                                                        }
                                                    </style>
                                                    <legend class="css-ihdtdm">
                                                        <span class="notranslate">​</span>
                                                    </legend>
                                                </fieldset>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-span-full flex justify-center">
                                        <button class="website-button primary title-sm no-underline outline-none flex items-center relative px-3 cursor-pointer border-solid" style="height:56px;letter-spacing:-0.012em" type="button">
                                            <div class="flex items-center">Submit</div>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col gap-2 text-center website-block subpalette-a website-footer" style="background-color:#f2f7f5;color:#00473e;padding-bottom:48px;padding-top:48px">
                        <div class="flex items-center justify-center"></div>
                        <div class="flex items-center justify-center gap-3"></div>
                        <div>©2024 All Rights Reserved</div>
                        <div role="button" tabindex="0" class="cursor-pointer">Powered by Beacons</div>
                    </div>
                    <div class="z-30 fixed bottom-2 right-4">
                        <a href="https://beacons.ai/?referral_type=footer_logo&amp;referring_user=zack4dev&amp;utm_medium=self_referral&amp;utm_campaign=zack4dev&amp;utm_content=website_footer_logo&amp;utm_source=bUnknown" rel="noopener noreferrer" target="_blank">
                            <img class="h-10 w-[165px]" src="https://cdn.beacons.ai/images/beacons_assets/made-with-beacons.png" alt="Made with Beacons"/>
                        </a>
                    </div>
                </div>
            </div>
            <script type="application/ld+json">
                {
                    "@context": "https://schema.org/",
                    "@type": "WebPage",
                    "name": "Digital Marketing",
                    "url": "https://beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516/undefined",
                    "sameAs": [
                    ],
                    "description": "zack4dev's Website",
                    "image": "https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482",
                    "identifier": "zack4dev",
                    "alternateName": "@zack4dev Beacons Profile",
                    "significantLink": "",
                    "isPartOf": "https://beacons.ai",
                    "thumbnailUrl": "https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482"
                }</script>
        </div>
        <script src="https://beacons.ai/_next/static/chunks/webpack-df60ad87447b8a2c.js" async></script>
        <script>
            (self.__next_f = self.__next_f || []).push([0]);
            self.__next_f.push([2, null])
        </script>
        <script>
            self.__next_f.push([1, "1:HL[\"https://beacons.ai/_next/static/css/cec9a5860a368e30.css\",\"style\"]\n2:HL[\"https://beacons.ai/_next/static/css/fca59e7c5ca010dc.css\",\"style\"]\n3:HL[\"https://beacons.ai/_next/static/css/f1c1b11210d202b4.css\",\"style\"]\n4:HL[\"https://beacons.ai/_next/static/css/5077ce94dd45ae31.css\",\"style\"]\n5:HL[\"https://beacons.ai/_next/static/css/c0b8703e7d1ef173.css\",\"style\"]\n6:HL[\"https://beacons.ai/_next/static/css/2f4f14aec8c88745.css\",\"style\"]\n"])
        </script>
        <script>
            self.__next_f.push([1, "7:I[11523,[],\"\"]\na:I[30311,[],\"\"]\nf:I[17482,[],\"\"]\n10:I[45993,[\"6829\",\"static/chunks/6829-cf90ca5e0c9467e4.js\",\"3185\",\"static/chunks/app/layout-6e722cc4c3da36c7.js\"],\"default\"]\n11:I[25136,[\"6829\",\"static/chunks/6829-cf90ca5e0c9467e4.js\",\"3185\",\"static/chunks/app/layout-6e722cc4c3da36c7.js\"],\"SSRGlobalsProvider\"]\n12:I[35339,[\"6844\",\"static/chunks/6844-d4e8b0889c382aef.js\",\"9384\",\"static/chunks/9384-746ea90a90b977aa.js\",\"7601\",\"static/chunks/app/error-7a557e1d05c36e52.js\"],\"default\"]\n13:I[60579,[\"6829\",\"static/chunks/6829-cf90ca5e0c9467e4.js\",\"3185\",\"static/chunks/app/layout-6e722cc4c3da36c7.js\"],\"VersionCheck\"]\n15:I[8185,[\"6844\",\"static/chunks/6844-d4e8b0889c382aef.js\",\"9384\",\"static/chunks/9384-746ea90a90b977aa.js\",\"6470\",\"static/chunks/app/global-error-af0cbd177542a539.js\"],\"default\"]\nb:[\"beaconsUsername\",\"zack4dev\",\"d\"]\nc:[\"version\",\"draft\",\"d\"]\nd:[\"userWebsiteId\",\"a9934823-5188-40da-953e-79f51b5c0516\",\"d\"]\ne:[\"pageSlugs\",\"\",\"oc\"]\n16:[]\n"])
        </script>
        <script>
            self.__next_f.push([1, "0:[[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"https://beacons.ai/_next/static/css/cec9a5860a368e30.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}],[\"$\",\"link\",\"1\",{\"rel\":\"stylesheet\",\"href\":\"https://beacons.ai/_next/static/css/fca59e7c5ca010dc.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}],[\"$\",\"link\",\"2\",{\"rel\":\"stylesheet\",\"href\":\"https://beacons.ai/_next/static/css/f1c1b11210d202b4.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]],[\"$\",\"$L7\",null,{\"buildId\":\"hxpLhAFH4mcGmp52Gui12\",\"assetPrefix\":\"https://beacons.ai\",\"initialCanonicalUrl\":\"/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516\",\"initialTree\":[\"\",{\"children\":[\"user_website_domain\",{\"children\":[[\"beaconsUsername\",\"zack4dev\",\"d\"],{\"children\":[\"websites\",{\"children\":[[\"version\",\"draft\",\"d\"],{\"children\":[[\"userWebsiteId\",\"a9934823-5188-40da-953e-79f51b5c0516\",\"d\"],{\"children\":[[\"pageSlugs\",\"\",\"oc\"],{\"children\":[\"__PAGE__\",{}]}]}]}]}]}]}]},\"$undefined\",\"$undefined\",true],\"initialSeedData\":[\"\",{\"children\":[\"user_website_domain\",{\"children\":[[\"beaconsUsername\",\"zack4dev\",\"d\"],{\"children\":[\"websites\",{\"children\":[[\"version\",\"draft\",\"d\"],{\"children\":[[\"userWebsiteId\",\"a9934823-5188-40da-953e-79f51b5c0516\",\"d\"],{\"children\":[[\"pageSlugs\",\"\",\"oc\"],{\"children\":[\"__PAGE__\",{},[[\"$L8\",\"$L9\"],null],null]},[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"user_website_domain\",\"children\",\"$b\",\"children\",\"websites\",\"children\",\"$c\",\"children\",\"$d\",\"children\",\"$e\",\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"https://beacons.ai/_next/static/css/5077ce94dd45ae31.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}],[\"$\",\"link\",\"1\",{\"rel\":\"stylesheet\",\"href\":\"https://beacons.ai/_next/static/css/c0b8703e7d1ef173.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}],[\"$\",\"link\",\"2\",{\"rel\":\"stylesheet\",\"href\":\"https://beacons.ai/_next/static/css/2f4f14aec8c88745.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]]}],null]},[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"user_website_domain\",\"children\",\"$b\",\"children\",\"websites\",\"children\",\"$c\",\"children\",\"$d\",\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}],null]},[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"user_website_domain\",\"children\",\"$b\",\"children\",\"websites\",\"children\",\"$c\",\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}],null]},[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"user_website_domain\",\"children\",\"$b\",\"children\",\"websites\",\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}],null]},[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"user_website_domain\",\"children\",\"$b\",\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}],null]},[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"user_website_domain\",\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}],null]},[[\"$\",\"html\",null,{\"lang\":\"en\",\"children\":[[\"$\",\"head\",null,{\"children\":[[\"$\",\"link\",null,{\"href\":\"/splashscreens/iphone5_splash.png\",\"media\":\"(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/iphone6_splash.png\",\"media\":\"(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/iphoneplus_splash.png\",\"media\":\"(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/iphonex_splash.png\",\"media\":\"(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/iphonexr_splash.png\",\"media\":\"(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/iphonexsmax_splash.png\",\"media\":\"(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/ipad_splash.png\",\"media\":\"(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/ipadpro1_splash.png\",\"media\":\"(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/ipadpro3_splash.png\",\"media\":\"(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}],[\"$\",\"link\",null,{\"href\":\"/splashscreens/ipadpro2_splash.png\",\"media\":\"(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)\",\"rel\":\"apple-touch-startup-image\"}]]}],[\"$\",\"body\",null,{\"children\":[[\"$\",\"beacons-tag\",null,{}],[\"$\",\"div\",null,{\"id\":\"root\",\"children\":[\"$\",\"$L10\",null,{\"children\":[\"$\",\"$L11\",null,{\"value\":{\"hostname\":\"website.beacons.ai\",\"pathname\":\"/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516\",\"href\":\"https://website.beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0\",\"referrer\":null,\"socialReferrer\":\"direct\",\"languages\":[\"en-US\",\"en\",\"fr\"],\"preferredLanguage\":\"en-US\"},\"children\":[\"$\",\"$La\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\"],\"error\":\"$12\",\"errorStyles\":[],\"errorScripts\":[],\"template\":[\"$\",\"$Lf\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":[[\"$\",\"title\",null,{\"children\":\"404: This page could not be found.\"}],[\"$\",\"div\",null,{\"style\":{\"fontFamily\":\"system-ui,\\\"Segoe UI\\\",Roboto,Helvetica,Arial,sans-serif,\\\"Apple Color Emoji\\\",\\\"Segoe UI Emoji\\\"\",\"height\":\"100vh\",\"textAlign\":\"center\",\"display\":\"flex\",\"flexDirection\":\"column\",\"alignItems\":\"center\",\"justifyContent\":\"center\"},\"children\":[\"$\",\"div\",null,{\"children\":[[\"$\",\"style\",null,{\"dangerouslySetInnerHTML\":{\"__html\":\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\"}}],[\"$\",\"h1\",null,{\"className\":\"next-error-h1\",\"style\":{\"display\":\"inline-block\",\"margin\":\"0 20px 0 0\",\"padding\":\"0 23px 0 0\",\"fontSize\":24,\"fontWeight\":500,\"verticalAlign\":\"top\",\"lineHeight\":\"49px\"},\"children\":\"404\"}],[\"$\",\"div\",null,{\"style\":{\"display\":\"inline-block\"},\"children\":[\"$\",\"h2\",null,{\"style\":{\"fontSize\":14,\"fontWeight\":400,\"lineHeight\":\"49px\",\"margin\":0},\"children\":\"This page could not be found.\"}]}]]}]}]],\"notFoundStyles\":[],\"styles\":null}]}]}]}],[\"$\",\"$L13\",null,{}]]}]]}],null],null],\"couldBeIntercepted\":false,\"initialHead\":[null,\"$L14\"],\"globalErrorComponent\":\"$15\",\"missingSlots\":\"$W16\"}]]\n"])
        </script>
        <script>
            self.__next_f.push([1, "17:I[37182,[\"2214\",\"static/chunks/c0ee81ba-8f034ff5772dd4db.js\",\"5723\",\"static/chunks/5723-c2750a8c7e4aae0d.js\",\"8003\",\"static/chunks/8003-7f358badc18bf9d8.js\",\"6829\",\"static/chunks/6829-cf90ca5e0c9467e4.js\",\"3127\",\"static/chunks/3127-e2fe3afb7cb8b6fe.js\",\"4924\",\"static/chunks/4924-eeeac8bb749d9773.js\",\"7541\",\"static/chunks/7541-543c748d472a4a78.js\",\"7199\",\"static/chunks/7199-6143064827efc080.js\",\"4979\",\"static/chunks/4979-7e851e19f6480f7c.js\",\"3501\",\"static/chunks/3501-1d6c6587445cf6b2.js\",\"8690\",\"static/chunks/8690-0e74dee08771593e.js\",\"3188\",\"static/chunks/3188-468ee9e55546b510.js\",\"3225\",\"static/chunks/3225-a74d33bc44e72678.js\",\"6844\",\"static/chunks/6844-d4e8b0889c382aef.js\",\"8675\",\"static/chunks/8675-0a62a0f90af3bad6.js\",\"8763\",\"static/chunks/8763-4c577172c476b725.js\",\"2813\",\"static/chunks/2813-ec85ccadedbdd0ed.js\",\"3843\",\"static/chunks/3843-33c67a0771d0bd85.js\",\"9384\",\"static/chunks/9384-746ea90a90b977aa.js\",\"9400\",\"static/chunks/9400-977472b9c535a150.js\",\"6872\",\"static/chunks/6872-4ab6a36d6c8f14c2.js\",\"4210\",\"static/chunks/4210-fc8b8200c29c2843.js\",\"8970\",\"static/chunks/8970-4a0fc2d7846c70ab.js\",\"9481\",\"static/chunks/9481-c3ee1e9a4c5e61e0.js\",\"1293\",\"static/chunks/1293-d4c274ea16e41539.js\",\"7231\",\"static/chunks/7231-403a8af3a243447c.js\",\"6858\",\"static/chunks/6858-40e5aaabb32aeb3e.js\",\"5610\",\"static/chunks/app/user_website_domain/%5BbeaconsUsername%5D/websites/%5Bversion%5D/%5BuserWebsiteId%5D/%5B%5B...pageSlugs%5D%5D/page-4b5f4bfa1dabf2c5.js\"],\"UserWebsiteClientRoot\"]\n"])
        </script>
        <script>
            self.__next_f.push([1, "9:[[\"$\",\"$L17\",null,{\"websiteParams\":{\"beaconsUsername\":\"zack4dev\",\"userWebsiteId\":\"a9934823-5188-40da-953e-79f51b5c0516\",\"version\":\"draft\",\"pageSlug\":\"$undefined\"},\"websiteDocument\":{\"dirty\":false,\"beacons_username\":\"zack4dev\",\"user_website_id\":\"a9934823-5188-40da-953e-79f51b5c0516\",\"draft\":{\"padding_between_columns\":48,\"pages\":{\"homepage\":{\"blocks\":{\"19111b00-9543-4ec2-8d5c-096f52c45ac6\":{\"secondary_button_text\":\"Learn more\",\"background_image_url\":\"https://images.unsplash.com/photo-1564463836146-4e30522c2984?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjE0Nzh8\u0026ixlib=rb-4.0.3\",\"is_secondary_button_visible\":true,\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Become a digital marketing expert\",\"image_url\":\"https://cdn.beacons.ai/user_content/W60VEikH0QdIZosLjiilxFxgfEI3/referenced_images/f9f998f2-2f22-4624-ae8f-55f0d5e70476__website__a9934823-5188-40da-953e-79f51b5c0516__hero__homepage__19111b00-9543-4ec2-8d5c-096f52c45ac6__5ee2ab31-2628-4503-acd2-1ad987e93f49.png?t=1729038160355\",\"vertical_alignment\":\"center\",\"padding_top\":50,\"text_alignment\":\"center\",\"is_subheading_visible\":true,\"primary_button_url\":\"https://beacons.ai\",\"display_name\":\"Hero\",\"type\":\"hero\",\"layout\":\"hero_3\",\"background_image_filter\":\"dark\",\"secondary_button_url\":\"https://beacons.ai\",\"primary_button_text\":\"Get started\",\"is_heading_visible\":true,\"padding_bottom\":50,\"is_image_video_visible\":false,\"is_primary_button_visible\":true,\"subheading\":\"Unlock Your Potential with Expert Guidance\"},\"ae0abc94-932c-4589-b6ea-6b75fe3297b6\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"27d43cf8-f9f8-437f-81ce-b2a2c0d5db09\":{\"vertical_alignment\":\"center\",\"padding_top\":30,\"padding_bottom\":30,\"type\":\"rich_text\",\"content\":\"\u003ch1 align=\\\"center\\\"\u003eInspiring creativity, one idea at a time.\u003c/h1\u003e\u003cp align=\\\"center\\\"\u003eTransforming creators into storytelling masters. Join me on the journey to unleash your creativity and captivate your audience.\u003c/p\u003e\"},\"432d8ff3-4d59-4250-b5f4-bec01857e75b\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"},\"fca85151-746b-445a-854e-4b8fb178f9eb\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"column_separator_color\":\"#194d33\",\"padding_top\":100,\"column_separator\":\"line\",\"display_name\":\"Content\",\"padding_bottom\":100,\"type\":\"content\",\"column_layout\":\"three_column_25_50_25\",\"column_order\":[\"432d8ff3-4d59-4250-b5f4-bec01857e75b\",\"27d43cf8-f9f8-437f-81ce-b2a2c0d5db09\",\"fca85151-746b-445a-854e-4b8fb178f9eb\"]},\"51ce8c55-70af-4bdc-b42e-f6ac0aeaefea\":{\"subpalette\":\"a\",\"visible\":true,\"is_mobile_stacked\":false,\"heading\":\"Check out our content\",\"padding_top\":135,\"text_alignment\":\"center\",\"video_text_alignment\":\"left\",\"videos\":[{\"subtitle\":\"Check out this video!\",\"id\":\"e85b7f77-b476-4ad8-9aad-e7b7914a1823\",\"title\":\"YouTube Video 2\",\"url\":\"https://www.youtube.com/embed/O1YntbDxqcM\"},{\"subtitle\":\"Check out this video!\",\"id\":\"8bd05769-a7cc-4022-abaa-7dc8fae90841\",\"title\":\"YouTube Video 1\",\"url\":\"https://www.youtube.com/embed/obFvKftbhKM\"},{\"subtitle\":\"Check out this video!\",\"id\":\"ffae8ba8-01f5-4c3d-971d-403246dcd58a\",\"title\":\"YouTube Video 3\",\"url\":\"https://www.youtube.com/embed/3FPfEjPmRks\"}],\"display_name\":\"YouTube\",\"type\":\"youtube\",\"layout\":\"three_column\",\"padding_bottom\":184,\"subheading\":\"Learn from the experts\"},\"77169c0c-ed50-424e-aa2b-a5a28ff383fc\":{\"background_image_url\":\"https://images.unsplash.com/photo-1529866147017-1b4508a0485d?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjI5NTF8\u0026ixlib=rb-4.0.3\",\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Stay in the Loop\",\"submit_text\":\"Submit\",\"padding_top\":120,\"text_alignment\":\"center\",\"display_name\":\"Email\",\"type\":\"email\",\"background_image_filter\":\"dark\",\"shown_fields\":[\"name\",\"email\"],\"success_message\":\"Submitted!\",\"padding_bottom\":120,\"subheading\":\"Subscribe to get my monthly newsletter\"},\"e3fc14da-d83c-4823-9cfa-eb6d3bbe87e8\":{\"secondary_button_text\":\"Learn more\",\"background_image_url\":\"https://images.unsplash.com/photo-1537218764248-06f18c55f006?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjMxOTZ8\u0026ixlib=rb-4.0.3\",\"is_secondary_button_visible\":true,\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Let's build your digital marketing empire together\",\"image_url\":\"https://cdn.beacons.ai/user_content/W60VEikH0QdIZosLjiilxFxgfEI3/referenced_images/e3fc14da-d83c-4823-9cfa-eb6d3bbe87e8.png?t=1729038166861\",\"vertical_alignment\":\"center\",\"padding_top\":24,\"text_alignment\":\"center\",\"is_subheading_visible\":true,\"primary_button_url\":\"https://beacons.ai\",\"display_name\":\"Hero\",\"type\":\"hero\",\"heading_size\":\"md\",\"layout\":\"hero_3\",\"background_image_filter\":\"dark\",\"secondary_button_url\":\"https://beacons.ai\",\"primary_button_text\":\"Join now\",\"is_heading_visible\":true,\"padding_bottom\":24,\"is_primary_button_visible\":true,\"subheading\":\"\"},\"2ac4a72d-0a23-4d40-b2ea-ea5d99c4b16a\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"cd4d4a37-731f-4c78-aab2-c1e793f8715e\":{\"vertical_alignment\":\"center\",\"padding_top\":24,\"padding_bottom\":24,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":24,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"cd4d4a37-731f-4c78-aab2-c1e793f8715e\"]},\"56e06028-6578-45dd-b75f-648b70ffd1d5\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"c4150711-4943-4479-a24a-dbd1530d0b06\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":24,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"c4150711-4943-4479-a24a-dbd1530d0b06\"]},\"e31b7aec-64c9-4e40-8b66-66302d986ebc\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"c4288dd9-c55e-4d04-a97e-513eea45bd73\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":24,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"c4288dd9-c55e-4d04-a97e-513eea45bd73\"]},\"d301d1f2-fa00-4129-a736-31a2338a34c0\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"822dfe72-e92d-4846-95e5-43b47166abb4\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003ch3 align=\\\"center\\\"\u003e\u003cstrong\u003eBeginner’s Guide\u003c/strong\u003e\u003c/h3\u003e\u003cp align=\\\"center\\\"\u003e\u003cstrong\u003eFree\u003c/strong\u003e\u003c/p\u003e\u003cbr\u003e\u003cp align=\\\"center\\\"\u003eGet started with expert advice, a comprehensive to-do list, and valuable resources to guide you along the way.\u003c/p\u003e\"},\"3e2cfa9a-120c-4911-938f-e172c515af9e\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003ch3 align=\\\"center\\\"\u003e\u003cstrong\u003eMonthly Membership\u003c/strong\u003e\u003c/h3\u003e\u003cp align=\\\"center\\\"\u003e\u003cstrong\u003e$39/mo\u003c/strong\u003e\u003c/p\u003e\u003cbr\u003e\u003cp align=\\\"center\\\"\u003eGain monthly entry to our expanding collection of classes, training programs, and personalized one-on-one coaching sessions.\u003c/p\u003e\"},\"d343187a-4ed8-40ae-829b-53f763e2a93c\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003ch3 align=\\\"center\\\"\u003e\u003cstrong\u003eStarter Park\u003c/strong\u003e\u003c/h3\u003e\u003cp align=\\\"center\\\"\u003e\u003cstrong\u003e$19\u003c/strong\u003e\u003c/p\u003e\u003cbr\u003e\u003cp align=\\\"center\\\"\u003eUnlock a comprehensive package featuring expert marketing tips, a social posting calendar, and essential tools to fuel your success.\u003c/p\u003e\"}},\"padding_top\":100,\"column_separator\":\"line\",\"display_name\":\"Content\",\"padding_bottom\":100,\"type\":\"content\",\"column_layout\":\"three_column_33_33_33\",\"column_order\":[\"822dfe72-e92d-4846-95e5-43b47166abb4\",\"d343187a-4ed8-40ae-829b-53f763e2a93c\",\"3e2cfa9a-120c-4911-938f-e172c515af9e\"]},\"d083c312-756e-4520-802d-414fb791bec8\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"cd539c37-6586-401d-a1c3-2a1211fd3f23\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":78,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"cd539c37-6586-401d-a1c3-2a1211fd3f23\"]},\"648aa440-fceb-4a50-ace2-a0451d0840b6\":{\"secondary_button_text\":\"Learn more\",\"background_image_url\":\"https://images.unsplash.com/photo-1503407768185-30e0f283410a?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjIzNjB8\u0026ixlib=rb-4.0.3\",\"is_secondary_button_visible\":true,\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Ready to Elevate Your Marketing Skills?\",\"image_url\":\"https://cdn.beacons.ai/user_content/W60VEikH0QdIZosLjiilxFxgfEI3/referenced_images/stock-images__website__a9934823-5188-40da-953e-79f51b5c0516__hero__homepage__648aa440-fceb-4a50-ace2-a0451d0840b6__fc06da65-bc56-4e8a-b7c4-e05cc7333a58.jpg?t=1729038154481\",\"vertical_alignment\":\"center\",\"padding_top\":33,\"text_alignment\":\"left\",\"is_subheading_visible\":true,\"primary_button_url\":\"https://beacons.ai\",\"display_name\":\"Hero\",\"type\":\"hero\",\"heading_size\":\"md\",\"layout\":\"hero_4_large_bottom_text\",\"background_image_filter\":\"dark\",\"secondary_button_url\":\"https://beacons.ai\",\"primary_button_text\":\"Let's get started!\",\"is_heading_visible\":true,\"subheading_size\":\"lg\",\"padding_bottom\":41,\"is_primary_button_visible\":true,\"subheading\":\"\"}},\"name\":\"Home\",\"block_order\":[\"19111b00-9543-4ec2-8d5c-096f52c45ac6\",\"e31b7aec-64c9-4e40-8b66-66302d986ebc\",\"ae0abc94-932c-4589-b6ea-6b75fe3297b6\",\"56e06028-6578-45dd-b75f-648b70ffd1d5\",\"648aa440-fceb-4a50-ace2-a0451d0840b6\",\"2ac4a72d-0a23-4d40-b2ea-ea5d99c4b16a\",\"d301d1f2-fa00-4129-a736-31a2338a34c0\",\"d083c312-756e-4520-802d-414fb791bec8\",\"e3fc14da-d83c-4823-9cfa-eb6d3bbe87e8\",\"51ce8c55-70af-4bdc-b42e-f6ac0aeaefea\",\"77169c0c-ed50-424e-aa2b-a5a28ff383fc\"],\"slug\":\"home\"}},\"menu_bar\":{\"logo_type\":\"text\",\"is_transparent\":true,\"subpalette\":\"b\",\"logo_image_url\":\"\",\"logo_size\":\"small\",\"show_socials\":true,\"logo_text\":\"Digital Marketing\"},\"page_order\":[{\"page_id\":\"homepage\",\"visible\":false,\"type\":\"single\"}],\"design\":{\"body_font_weight\":400,\"body_font\":\"Poppins\",\"preset_palette_name\":\"Tropical Green\",\"heading_font\":\"Merriweather\",\"button_corner_radius\":24,\"button_thickness\":4,\"heading_font_weight\":400,\"subheading_font\":\"Merriweather\",\"subheading_font_weight\":400},\"name\":\"Digital Marketing\",\"home_page_id\":\"homepage\"},\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"has_ever_been_published\":false,\"last_published_at\":\"Wed Oct 16 2024 01:22:46 GMT+0100 (GMT+01:00)\",\"live\":{\"padding_between_columns\":48,\"pages\":{\"homepage\":{\"blocks\":{\"19111b00-9543-4ec2-8d5c-096f52c45ac6\":{\"secondary_button_text\":\"Learn more\",\"background_image_url\":\"https://images.unsplash.com/photo-1564463836146-4e30522c2984?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjE0Nzh8\u0026ixlib=rb-4.0.3\",\"is_secondary_button_visible\":true,\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Become a digital marketing expert\",\"image_url\":\"https://cdn.beacons.ai/user_content/W60VEikH0QdIZosLjiilxFxgfEI3/referenced_images/f9f998f2-2f22-4624-ae8f-55f0d5e70476__website__a9934823-5188-40da-953e-79f51b5c0516__hero__homepage__19111b00-9543-4ec2-8d5c-096f52c45ac6__5ee2ab31-2628-4503-acd2-1ad987e93f49.png?t=1729038160355\",\"vertical_alignment\":\"center\",\"padding_top\":50,\"text_alignment\":\"center\",\"is_subheading_visible\":true,\"primary_button_url\":\"https://beacons.ai\",\"display_name\":\"Hero\",\"type\":\"hero\",\"layout\":\"hero_3\",\"background_image_filter\":\"dark\",\"secondary_button_url\":\"https://beacons.ai\",\"primary_button_text\":\"Get started\",\"is_heading_visible\":true,\"padding_bottom\":50,\"is_image_video_visible\":false,\"is_primary_button_visible\":true,\"subheading\":\"Unlock Your Potential with Expert Guidance\"},\"ae0abc94-932c-4589-b6ea-6b75fe3297b6\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"27d43cf8-f9f8-437f-81ce-b2a2c0d5db09\":{\"vertical_alignment\":\"center\",\"padding_top\":30,\"padding_bottom\":30,\"type\":\"rich_text\",\"content\":\"\u003ch1 align=\\\"center\\\"\u003eInspiring creativity, one idea at a time.\u003c/h1\u003e\u003cp align=\\\"center\\\"\u003eTransforming creators into storytelling masters. Join me on the journey to unleash your creativity and captivate your audience.\u003c/p\u003e\"},\"432d8ff3-4d59-4250-b5f4-bec01857e75b\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"},\"fca85151-746b-445a-854e-4b8fb178f9eb\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"column_separator_color\":\"#194d33\",\"padding_top\":100,\"column_separator\":\"line\",\"display_name\":\"Content\",\"padding_bottom\":100,\"type\":\"content\",\"column_layout\":\"three_column_25_50_25\",\"column_order\":[\"432d8ff3-4d59-4250-b5f4-bec01857e75b\",\"27d43cf8-f9f8-437f-81ce-b2a2c0d5db09\",\"fca85151-746b-445a-854e-4b8fb178f9eb\"]},\"51ce8c55-70af-4bdc-b42e-f6ac0aeaefea\":{\"subpalette\":\"a\",\"visible\":true,\"is_mobile_stacked\":false,\"heading\":\"Check out our content\",\"padding_top\":135,\"text_alignment\":\"center\",\"video_text_alignment\":\"left\",\"videos\":[{\"subtitle\":\"Check out this video!\",\"id\":\"e85b7f77-b476-4ad8-9aad-e7b7914a1823\",\"title\":\"YouTube Video 2\",\"url\":\"https://www.youtube.com/embed/O1YntbDxqcM\"},{\"subtitle\":\"Check out this video!\",\"id\":\"8bd05769-a7cc-4022-abaa-7dc8fae90841\",\"title\":\"YouTube Video 1\",\"url\":\"https://www.youtube.com/embed/obFvKftbhKM\"},{\"subtitle\":\"Check out this video!\",\"id\":\"ffae8ba8-01f5-4c3d-971d-403246dcd58a\",\"title\":\"YouTube Video 3\",\"url\":\"https://www.youtube.com/embed/3FPfEjPmRks\"}],\"display_name\":\"YouTube\",\"type\":\"youtube\",\"layout\":\"three_column\",\"padding_bottom\":184,\"subheading\":\"Learn from the experts\"},\"77169c0c-ed50-424e-aa2b-a5a28ff383fc\":{\"background_image_url\":\"https://images.unsplash.com/photo-1529866147017-1b4508a0485d?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjI5NTF8\u0026ixlib=rb-4.0.3\",\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Stay in the Loop\",\"submit_text\":\"Submit\",\"padding_top\":120,\"text_alignment\":\"center\",\"display_name\":\"Email\",\"type\":\"email\",\"background_image_filter\":\"dark\",\"shown_fields\":[\"name\",\"email\"],\"success_message\":\"Submitted!\",\"padding_bottom\":120,\"subheading\":\"Subscribe to get my monthly newsletter\"},\"e3fc14da-d83c-4823-9cfa-eb6d3bbe87e8\":{\"secondary_button_text\":\"Learn more\",\"background_image_url\":\"https://images.unsplash.com/photo-1537218764248-06f18c55f006?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjMxOTZ8\u0026ixlib=rb-4.0.3\",\"is_secondary_button_visible\":true,\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Let's build your digital marketing empire together\",\"image_url\":\"https://cdn.beacons.ai/user_content/W60VEikH0QdIZosLjiilxFxgfEI3/referenced_images/e3fc14da-d83c-4823-9cfa-eb6d3bbe87e8.png?t=1729038166861\",\"vertical_alignment\":\"center\",\"padding_top\":24,\"text_alignment\":\"center\",\"is_subheading_visible\":true,\"primary_button_url\":\"https://beacons.ai\",\"display_name\":\"Hero\",\"type\":\"hero\",\"heading_size\":\"md\",\"layout\":\"hero_3\",\"background_image_filter\":\"dark\",\"secondary_button_url\":\"https://beacons.ai\",\"primary_button_text\":\"Join now\",\"is_heading_visible\":true,\"padding_bottom\":24,\"is_primary_button_visible\":true,\"subheading\":\"\"},\"2ac4a72d-0a23-4d40-b2ea-ea5d99c4b16a\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"cd4d4a37-731f-4c78-aab2-c1e793f8715e\":{\"vertical_alignment\":\"center\",\"padding_top\":24,\"padding_bottom\":24,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":24,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"cd4d4a37-731f-4c78-aab2-c1e793f8715e\"]},\"56e06028-6578-45dd-b75f-648b70ffd1d5\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"c4150711-4943-4479-a24a-dbd1530d0b06\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":24,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"c4150711-4943-4479-a24a-dbd1530d0b06\"]},\"e31b7aec-64c9-4e40-8b66-66302d986ebc\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"c4288dd9-c55e-4d04-a97e-513eea45bd73\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":24,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"c4288dd9-c55e-4d04-a97e-513eea45bd73\"]},\"d301d1f2-fa00-4129-a736-31a2338a34c0\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"822dfe72-e92d-4846-95e5-43b47166abb4\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003ch3 align=\\\"center\\\"\u003e\u003cstrong\u003eBeginner’s Guide\u003c/strong\u003e\u003c/h3\u003e\u003cp align=\\\"center\\\"\u003e\u003cstrong\u003eFree\u003c/strong\u003e\u003c/p\u003e\u003cbr\u003e\u003cp align=\\\"center\\\"\u003eGet started with expert advice, a comprehensive to-do list, and valuable resources to guide you along the way.\u003c/p\u003e\"},\"3e2cfa9a-120c-4911-938f-e172c515af9e\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003ch3 align=\\\"center\\\"\u003e\u003cstrong\u003eMonthly Membership\u003c/strong\u003e\u003c/h3\u003e\u003cp align=\\\"center\\\"\u003e\u003cstrong\u003e$39/mo\u003c/strong\u003e\u003c/p\u003e\u003cbr\u003e\u003cp align=\\\"center\\\"\u003eGain monthly entry to our expanding collection of classes, training programs, and personalized one-on-one coaching sessions.\u003c/p\u003e\"},\"d343187a-4ed8-40ae-829b-53f763e2a93c\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003ch3 align=\\\"center\\\"\u003e\u003cstrong\u003eStarter Park\u003c/strong\u003e\u003c/h3\u003e\u003cp align=\\\"center\\\"\u003e\u003cstrong\u003e$19\u003c/strong\u003e\u003c/p\u003e\u003cbr\u003e\u003cp align=\\\"center\\\"\u003eUnlock a comprehensive package featuring expert marketing tips, a social posting calendar, and essential tools to fuel your success.\u003c/p\u003e\"}},\"padding_top\":100,\"column_separator\":\"line\",\"display_name\":\"Content\",\"padding_bottom\":100,\"type\":\"content\",\"column_layout\":\"three_column_33_33_33\",\"column_order\":[\"822dfe72-e92d-4846-95e5-43b47166abb4\",\"d343187a-4ed8-40ae-829b-53f763e2a93c\",\"3e2cfa9a-120c-4911-938f-e172c515af9e\"]},\"d083c312-756e-4520-802d-414fb791bec8\":{\"full_width\":false,\"subpalette\":\"a\",\"visible\":true,\"columns\":{\"cd539c37-6586-401d-a1c3-2a1211fd3f23\":{\"vertical_alignment\":\"center\",\"padding_top\":0,\"padding_bottom\":0,\"type\":\"rich_text\",\"content\":\"\u003cbr\u003e\"}},\"padding_top\":24,\"column_separator\":\"none\",\"display_name\":\"Content\",\"padding_bottom\":78,\"type\":\"content\",\"column_layout\":\"free\",\"column_order\":[\"cd539c37-6586-401d-a1c3-2a1211fd3f23\"]},\"648aa440-fceb-4a50-ace2-a0451d0840b6\":{\"secondary_button_text\":\"Learn more\",\"background_image_url\":\"https://images.unsplash.com/photo-1503407768185-30e0f283410a?ixid=M3wxMTAwMjh8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTExNjIzNjB8\u0026ixlib=rb-4.0.3\",\"is_secondary_button_visible\":true,\"subpalette\":\"b\",\"visible\":true,\"heading\":\"Ready to Elevate Your Marketing Skills?\",\"image_url\":\"https://cdn.beacons.ai/user_content/W60VEikH0QdIZosLjiilxFxgfEI3/referenced_images/stock-images__website__a9934823-5188-40da-953e-79f51b5c0516__hero__homepage__648aa440-fceb-4a50-ace2-a0451d0840b6__fc06da65-bc56-4e8a-b7c4-e05cc7333a58.jpg?t=1729038154481\",\"vertical_alignment\":\"center\",\"padding_top\":33,\"text_alignment\":\"left\",\"is_subheading_visible\":true,\"primary_button_url\":\"https://beacons.ai\",\"display_name\":\"Hero\",\"type\":\"hero\",\"heading_size\":\"md\",\"layout\":\"hero_4_large_bottom_text\",\"background_image_filter\":\"dark\",\"secondary_button_url\":\"https://beacons.ai\",\"primary_button_text\":\"Let's get started!\",\"is_heading_visible\":true,\"subheading_size\":\"lg\",\"padding_bottom\":41,\"is_primary_button_visible\":true,\"subheading\":\"\"}},\"name\":\"Home\",\"block_order\":[\"19111b00-9543-4ec2-8d5c-096f52c45ac6\",\"e31b7aec-64c9-4e40-8b66-66302d986ebc\",\"ae0abc94-932c-4589-b6ea-6b75fe3297b6\",\"56e06028-6578-45dd-b75f-648b70ffd1d5\",\"648aa440-fceb-4a50-ace2-a0451d0840b6\",\"2ac4a72d-0a23-4d40-b2ea-ea5d99c4b16a\",\"d301d1f2-fa00-4129-a736-31a2338a34c0\",\"d083c312-756e-4520-802d-414fb791bec8\",\"e3fc14da-d83c-4823-9cfa-eb6d3bbe87e8\",\"51ce8c55-70af-4bdc-b42e-f6ac0aeaefea\",\"77169c0c-ed50-424e-aa2b-a5a28ff383fc\"],\"slug\":\"home\"}},\"menu_bar\":{\"logo_type\":\"text\",\"is_transparent\":true,\"subpalette\":\"b\",\"logo_image_url\":\"\",\"logo_size\":\"small\",\"show_socials\":true,\"logo_text\":\"Digital Marketing\"},\"page_order\":[{\"page_id\":\"homepage\",\"visible\":false,\"type\":\"single\"}],\"design\":{\"body_font_weight\":400,\"body_font\":\"Poppins\",\"preset_palette_name\":\"Tropical Green\",\"heading_font\":\"Merriweather\",\"button_corner_radius\":24,\"button_thickness\":4,\"heading_font_weight\":400,\"subheading_font\":\"Merriweather\",\"subheading_font_weight\":400},\"name\":\"Digital Marketing\",\"home_page_id\":\"homepage\"},\"status\":\"primary\"},\"profileInfoDocument\":{\"verified\":false,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"beacons_username\":\"zack4dev\",\"pages\":[{\"page_id\":\"home\",\"page_title\":\"home\",\"display\":true}],\"subscription_plan_ids\":[],\"page_appearance\":{\"button\":{\"background_color\":\"#1F2125\",\"hover_background_color\":\"#FEFEFE\"},\"components\":{\"theme\":\"round\",\"opacity\":\"\"},\"background\":{\"type\":\"solid\",\"background_color1\":\"#101010\"},\"header\":{\"size\":\"big\",\"color\":\"#ffffff\",\"text\":\"#ffffff\",\"type\":\"full\"},\"links\":{\"border_color\":true},\"text\":{\"color\":\"#FEFEFE\",\"link_text_color\":\"#FEFEFE\",\"header_text_color\":\"#FEFEFE\",\"font_family\":\"Poppins, sans-serif\",\"hover_color\":\"#101010\"},\"card\":{\"background_color\":\"#1F2125\"}},\"25b3ec42-e38b-46f9-a62d-52ddb1b484f0\":{\"onboarding_completed\":true,\"block_type\":\"links\",\"display\":true,\"description\":\"\",\"link_outline\":true,\"links\":[{\"display\":true,\"is_suspended\":null,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"id\":\"d6951f3a-c3b0-4d47-a323-71098ea25001\",\"title\":\"elhatimizakaria.link\",\"url\":\"https://elhatimizakaria.link\"},{\"display\":true,\"is_suspended\":null,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"id\":\"b2c0e8e6-eb98-49a9-be77-db8ecb8f182f\",\"title\":\"Instagram\",\"url\":\"https://www.instagram.com/zack4dev/\",\"picture\":\"instagram;source=beacons\"},{\"display\":true,\"is_suspended\":null,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"id\":\"ed786667-2114-43b9-a93a-18f0c2570709\",\"title\":\"Twitter\",\"url\":\"https://www.twitter.com/zeh4dev/\",\"picture\":\"twitter;source=beacons\"},{\"display\":true,\"is_suspended\":null,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"id\":\"4b06b925-fec6-4217-b254-bebdc5ef333b\",\"title\":\"YouTube\",\"url\":\"https://www.youtube.com/@Zeh4DEV\",\"picture\":\"youtube;source=beacons\"},{\"display\":true,\"is_suspended\":null,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"id\":\"c54fa04d-6ae1-4d05-9dd4-05561b4a0293\",\"title\":\"Make your own Beacons page\",\"url\":\"https://beacons.ai/signup?c=zack4dev\",\"picture\":\"beacons;source=beacons\"}],\"headline\":\"\"},\"page_layout\":[{\"block_id\":\"8e6a20bd-98b0-4632-a9dd-df60999b55df\"},{\"block_id\":\"25b3ec42-e38b-46f9-a62d-52ddb1b484f0\"},{\"block_id\":\"2c8c2d95-e2fb-4d1f-ade1-c4d7b204f6b4\"},{\"block_id\":\"d83e5d6d-9d8c-4690-8dc0-6bc42c9568e0\"}],\"profile_picture_url\":\"https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482\",\"931ed7b4-7f66-4c0c-beac-f55499e87ba4\":{\"block_type\":\"header\",\"header_color\":\"#ffffff\",\"header_layout\":\"portrait\",\"social_links\":{\"email\":\"Zackelhat@gmail.com\"},\"display\":true,\"header_size\":\"big\",\"header_type\":\"full\"},\"a94b1dd6-a7d8-4a31-b8cb-6552bbefcb02\":{\"onboarding_completed\":true,\"block_type\":\"links\",\"display\":true,\"description\":\"\",\"link_outline\":true,\"links\":[{\"subtitle\":\"Use this link to get $20 credit!\",\"display\":true,\"is_suspended\":null,\"firebase_uid\":\"W60VEikH0QdIZosLjiilxFxgfEI3\",\"id\":\"430beccd-7dcf-489b-aafa-2f0dd8b3f1a7\",\"title\":\"Make your own Beacons page\",\"picture\":\"beacons;source=beacons\",\"url\":\"https://beacons.ai/signup?c=zack4dev\"}],\"headline\":\"\"},\"a09b8562-531b-4ae9-85f7-ac3da3ab5aa0\":{\"mailchimp\":null,\"block_type\":\"email\",\"form_style\":\"card\",\"submit_text\":\"Subscribe\",\"success_message\":\"Submitted!\",\"display\":true,\"description\":\"\",\"placeholder_text\":\"\",\"email_destination\":\"beacons\"},\"ff08db80-ca89-4660-b7e6-8ca8224b5ae9\":{\"store_title\":\"Shop my products\",\"block_type\":\"store\",\"one_column_image_aspect_ratio\":\"3:2\",\"collapse_style\":\"exposed\",\"display\":true,\"store_items\":[],\"layout_type\":\"leftImageRightText\",\"store_subtitle\":\"\"},\"8e6a20bd-98b0-4632-a9dd-df60999b55df\":{\"block_type\":\"header\",\"header_color\":\"#ffffff\",\"header_layout\":\"portrait\",\"social_links\":{\"youtube\":\"https://www.youtube.com/@Zeh4DEV\",\"twitter\":\"zeh4dev\",\"instagram\":\"zack4dev\"},\"display\":true,\"header_profile_picture_color1\":\"#ffffff\",\"header_size\":\"big\",\"header_profile_picture_border\":\"solid\",\"header_type\":\"full\",\"header_banner_image\":\"\",\"header_profile_picture_border_radius\":100,\"header_bio\":\"Software Developer, enthusiast with DevOps ,CI and CD.\"},\"2c8c2d95-e2fb-4d1f-ade1-c4d7b204f6b4\":{\"mailchimp\":null,\"block_type\":\"email\",\"form_style\":\"card\",\"submit_text\":\"Subscribe\",\"success_message\":\"Submitted!\",\"description\":\"\",\"placeholder_text\":\"\",\"email_destination\":\"beacons\",\"show_name_field\":false,\"show_city_field\":false,\"show_birthdate_field\":false,\"legal_enabled\":false,\"zapier_webhook_url\":\"\",\"substack_url\":\"\",\"show_postal_code_field\":false,\"show_phone_number_field\":false,\"show_first_name_field\":true,\"legal_url\":\"\",\"thumbnail_image_url\":\"\",\"show_custom_field\":false,\"show_name_fields\":\"first_name\",\"information_type\":null,\"show_location_fields\":\"\",\"display\":false,\"is_notifications_enabled\":false,\"redirect_page_id\":null,\"show_email_field\":true,\"show_region_field\":false,\"show_address_line_2_field\":false,\"show_country_field\":false,\"show_address_line_1_field\":false,\"collapse_style\":\"exposed\",\"name_field_text\":\"Full name\",\"form_order\":[\"name\",\"email\",\"phone_number\",\"location\",\"birthdate\",\"custom\"],\"show_last_name_field\":false,\"custom_field_text\":\"\",\"legal_text\":\"\"},\"d83e5d6d-9d8c-4690-8dc0-6bc42c9568e0\":{\"store_title\":\"Shop my products\",\"block_type\":\"store\",\"one_column_image_aspect_ratio\":\"3:2\",\"collapse_style\":\"exposed\",\"store_items\":[],\"layout_type\":\"leftImageRightText\",\"store_subtitle\":\"\",\"display\":false}},\"sessionToken\":\"gAAAAABnDweOCq9AS8AHSD9Ap0dYB2ZBD_JhfVNSTTbiGY8RagEHVwXzNAOaCbFeDMj-Qsy8VERwPqVX9xJepfdscUW7wPstkz9upppknK2Hjy2wmtBNvhryhgbygKw2GluAHNIK-EbEVEiRqFvpA91D_WhX6wllLaP7Ruf31V-ZkO55XhbHYNAMkN5S_XZ0C6ftqKtUyH9wj6FjIHtWJrm_TEzOOeUX3jyZWJT92NU_Vvbm3jeVQC5kGJD-3ePAns8TFeVbszQv\"}],[\"$\",\"script\",null,{\"type\":\"application/ld+json\",\"dangerouslySetInnerHTML\":{\"__html\":\"{\\\"@context\\\":\\\"https://schema.org/\\\",\\\"@type\\\":\\\"WebPage\\\",\\\"name\\\":\\\"Digital Marketing\\\",\\\"url\\\":\\\"https://beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516/undefined\\\",\\\"sameAs\\\":[],\\\"description\\\":\\\"zack4dev's Website\\\",\\\"image\\\":\\\"https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482\\\",\\\"identifier\\\":\\\"zack4dev\\\",\\\"alternateName\\\":\\\"@zack4dev Beacons Profile\\\",\\\"significantLink\\\":\\\"\\\",\\\"isPartOf\\\":\\\"https://beacons.ai\\\",\\\"thumbnailUrl\\\":\\\"https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482\\\"}\"}}]]\n"])
        </script>
        <script>
            self.__next_f.push([1, "14:[[\"$\",\"meta\",\"0\",{\"name\":\"viewport\",\"content\":\"width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=contain, user-scalable=no\"}],[\"$\",\"meta\",\"1\",{\"name\":\"theme-color\",\"content\":\"#000000\"}],[\"$\",\"meta\",\"2\",{\"charSet\":\"utf-8\"}],[\"$\",\"title\",\"3\",{\"children\":\"Digital Marketing\"}],[\"$\",\"meta\",\"4\",{\"name\":\"description\",\"content\":\"zack4dev's Website\"}],[\"$\",\"link\",\"5\",{\"rel\":\"manifest\",\"href\":\"/manifest.json\",\"crossOrigin\":\"use-credentials\"}],[\"$\",\"meta\",\"6\",{\"name\":\"robots\",\"content\":\"index, follow\"}],[\"$\",\"meta\",\"7\",{\"name\":\"fb:app_id\",\"content\":\"3294868390539011\"}],[\"$\",\"link\",\"8\",{\"rel\":\"canonical\",\"href\":\"https://beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516/undefined\"}],[\"$\",\"meta\",\"9\",{\"name\":\"apple-mobile-web-app-capable\",\"content\":\"yes\"}],[\"$\",\"meta\",\"10\",{\"name\":\"apple-mobile-web-app-title\",\"content\":\"Beacons\"}],[\"$\",\"meta\",\"11\",{\"name\":\"apple-mobile-web-app-status-bar-style\",\"content\":\"default\"}],[\"$\",\"meta\",\"12\",{\"property\":\"og:title\",\"content\":\"Digital Marketing\"}],[\"$\",\"meta\",\"13\",{\"property\":\"og:description\",\"content\":\"zack4dev's Website\"}],[\"$\",\"meta\",\"14\",{\"property\":\"og:url\",\"content\":\"https://beacons.ai/zack4dev/websites/draft/a9934823-5188-40da-953e-79f51b5c0516/undefined\"}],[\"$\",\"meta\",\"15\",{\"property\":\"og:site_name\",\"content\":\"Beacons\"}],[\"$\",\"meta\",\"16\",{\"property\":\"og:image\",\"content\":\"https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482\"}],[\"$\",\"meta\",\"17\",{\"property\":\"og:image:width\",\"content\":\"600\"}],[\"$\",\"meta\",\"18\",{\"property\":\"og:image:height\",\"content\":\"600\"}],[\"$\",\"meta\",\"19\",{\"name\":\"twitter:card\",\"content\":\"summary_large_image\"}],[\"$\",\"meta\",\"20\",{\"name\":\"twitter:creator\",\"content\":\"zack4dev\"}],[\"$\",\"meta\",\"21\",{\"name\":\"twitter:title\",\"content\":\"Digital Marketing\"}],[\"$\",\"meta\",\"22\",{\"name\":\"twitter:description\",\"content\":\"zack4dev's Website\"}],[\"$\",\"meta\",\"23\",{\"name\":\"twitter:image\",\"content\":\"https://cdn.beacons.ai/profile_pictures/youtube/zack4dev?q=1728940091.2651482\"}],[\"$\",\"link\",\"24\",{\"rel\":\"shortcut icon\",\"href\":\"/favicon.ico\"}],[\"$\",\"link\",\"25\",{\"rel\":\"icon\",\"href\":\"/favicon.ico\"}],[\"$\",\"link\",\"26\",{\"rel\":\"apple-touch-icon\",\"href\":\"/favicon.ico\"}]]\n"])
        </script>
        <script>
            self.__next_f.push([1, "8:null\n"])
        </script>
        <script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"rayId":"8d33e6d7d8570c3c","serverTiming":{"name":{"cfExtPri":true,"cfL4":true,"cfSpeedBrain":true,"cfCacheStatus":true}},"version":"2024.10.1","token":"190d103813884531a3fca79b339a91c2"}' crossorigin="anonymous"></script>
    </body>
</html>

  </body>
</html>
'''

# Display the HTML content in the Streamlit app
st.markdown(html_code, unsafe_allow_html=True)
