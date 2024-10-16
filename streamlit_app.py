import streamlit as st

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Digital Marketing"
)

# HTML code for embedding a digital marketing platform page
html_code = '''
<div class="bg-indigo-50">
  <header>
    <nav class="bg-indigo-50 border-zinc-200 px-4 lg:px-6 py-2.5">
      <div class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl">
        <a href="#" class="flex items-center"><span class="text-indigo-600 self-center text-xl font-semibold whitespace-nowrap">Digital Boost</span></a>
        <div class="flex items-center lg:order-2">
          <a href="#" class="text-zinc-800 hover:bg-zinc-50 focus:ring-4 focus:ring-zinc-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2">Log in</a
          ><a href="#" class="text-white bg-green-700 hover:bg-green-800 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2">Get Started</a
          ><button
            type="button"
            class="inline-flex items-center p-2 ml-1 text-sm text-zinc-500 rounded-lg lg:hidden hover:bg-zinc-100 focus:outline-none focus:ring-2 focus:ring-zinc-200"
            aria-controls="mobile-menu-2"
            aria-expanded="false"
          >
            <span class="sr-only">Open main menu</span
            ><svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path
                fill-rule="evenodd"
                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                clip-rule="evenodd"
              ></path></svg
            ><svg class="hidden w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>
        </div>
        <div class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1" id="mobile-menu-2">
          <ul class="flex flex-col mt-4 font-medium lg:flex-row lg:space-x-8 lg:mt-0">
            <li><a href="#" class="block py-2 pr-4 pl-3 hover:text-green-800 text-black rounded lg:bg-transparent lg:p-0" aria-current="page">Product</a></li>
            <li><a href="#" class="block py-2 pr-4 pl-3 hover:text-green-800 text-black rounded lg:bg-transparent lg:p-0" aria-current="page">Features</a></li>
            <li><a href="#" class="block py-2 pr-4 pl-3 hover:text-green-800 text-black rounded lg:bg-transparent lg:p-0" aria-current="page">Pricing</a></li>
            <li><a href="#" class="block py-2 pr-4 pl-3 hover:text-green-800 text-black rounded lg:bg-transparent lg:p-0" aria-current="page">Company</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <div class="relative isolate px-6 pt-14 lg:px-8">
    <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true"></div>
    <div class="mx-auto max-w-2xl py-10 sm:py-48 lg:py-10">
      <div class="text-center">
        <h1 class="text-4xl font-bold tracking-tight text-zinc-900 sm:text-6xl">Boost Your Online Presence</h1>
        <p class="mt-6 text-lg leading-8 text-zinc-600">Take your digital marketing to the next level with our all-in-one platform.</p>
        <div class="mt-10 flex items-center justify-center gap-x-6">
          <a
            href="#"
            class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >Get Started</a
          ><a href="#" class="text-sm font-semibold leading-6 text-zinc-900">Learn More<span aria-hidden="true">→</span></a>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="bg-indigo-600 py-10 sm:py-10">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:text-center">
      <h2 class="text-base font-semibold leading-7 text-indigo-200">Boost Your Marketing</h2>
      <p class="mt-2 text-3xl font-bold tracking-tight text-white sm:text-4xl">Powerful features to enhance your digital marketing efforts</p>
      <p class="mt-6 text-lg leading-8 text-indigo-200">Explore the key features that will help you succeed in the digital marketing landscape</p>
    </div>
    <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
      <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-white">Multi-Channel Marketing</dt>
          <dd class="mt-4 flex flex-auto flex-col text-base leading-7 text-indigo-200">
            <p class="flex-auto">Reach your audience across various digital channels</p>
            <p class="mt-6">
              <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-white">Analytics Dashboard</dt>
          <dd class="mt-4 flex flex-auto flex-col text-base leading-7 text-indigo-200">
            <p class="flex-auto">Track and analyze the performance of your marketing campaigns</p>
            <p class="mt-6">
              <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
        <div class="flex flex-col">
          <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-white">Automated Campaigns</dt>
          <dd class="mt-4 flex flex-auto flex-col text-base leading-7 text-indigo-200">
            <p class="flex-auto">Set up automated marketing campaigns to save time and increase efficiency</p>
            <p class="mt-6">
              <a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
            </p>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</div>
<div class="bg-white py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-4xl sm:text-center">
      <h2 class="text-base font-semibold leading-7 text-indigo-600">Choose Your Plan</h2>
      <p class="mt-2 text-4xl font-bold tracking-tight text-zinc-900 sm:text-5xl">Flexible Pricing Options</p>
    </div>
    <p class="mx-auto mt-6 max-w-2xl text-lg leading-8 text-zinc-600 sm:text-center">Select the plan that best fits your needs and budget</p>
    <div class="mt-20 flow-root">
      <div class="isolate -mt-16 grid max-w-sm grid-cols-1 gap-y-16 divide-y divide-zinc-100 sm:mx-auto lg:-mx-8 lg:mt-0 lg:max-w-none lg:grid-cols-3 lg:divide-x lg:divide-y-0 xl:-mx-4">
        <div class="pt-16 lg:px-8 lg:pt-0 xl:px-14">
          <h3 class="text-base font-semibold leading-7 text-zinc-900">Starter Plan</h3>
          <p class="mt-6 flex items-baseline gap-x-1">
            <span class="text-5xl font-bold tracking-tight text-zinc-900">$50</span><span class="text-sm font-semibold leading-6 text-zinc-600">/month</span>
          </p>
          <a
            href="#"
            class="mt-10 block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >Get started</a
          >
          <p class="mt-10 text-sm font-semibold leading-6 text-zinc-900">Ideal for small businesses</p>
          <ul role="list" class="mt-6 space-y-3 text-sm leading-6 text-zinc-600">
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Social Media Management
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Email Marketing Campaigns
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Basic Analytics Reporting
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Customer Support
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Limited Ad Campaigns
            </li>
          </ul>
        </div>
        <div class="pt-16 lg:px-8 lg:pt-0 xl:px-14">
          <h3 class="text-base font-semibold leading-7 text-zinc-900">Business Plan</h3>
          <p class="mt-6 flex items-baseline gap-x-1">
            <span class="text-5xl font-bold tracking-tight text-zinc-900">$100</span><span class="text-sm font-semibold leading-6 text-zinc-600">/month</span>
          </p>
          <a
            href="#"
            class="mt-10 block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >Get started</a
          >
          <p class="mt-10 text-sm font-semibold leading-6 text-zinc-900">Perfect for growing companies</p>
          <ul role="list" class="mt-6 space-y-3 text-sm leading-6 text-zinc-600">
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Advanced Social Media Strategies
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Customized Email Marketing Solutions
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Detailed Analytics Dashboard
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Priority Customer Support
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Expanded Ad Campaigns
            </li>
          </ul>
        </div>
        <div class="pt-16 lg:px-8 lg:pt-0 xl:px-14">
          <h3 class="text-base font-semibold leading-7 text-zinc-900">Enterprise Plan</h3>
          <p class="mt-6 flex items-baseline gap-x-1">
            <span class="text-5xl font-bold tracking-tight text-zinc-900">$200</span><span class="text-sm font-semibold leading-6 text-zinc-600">/month</span>
          </p>
          <a
            href="#"
            class="mt-10 block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >Get started</a
          >
          <p class="mt-10 text-sm font-semibold leading-6 text-zinc-900">Tailored for large corporations</p>
          <ul role="list" class="mt-6 space-y-3 text-sm leading-6 text-zinc-600">
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Dedicated Account Manager
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Personalized Marketing Strategies
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Comprehensive Analytics Suite
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >24/7 VIP Support
            </li>
            <li class="flex gap-x-3">
              <svg class="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg
              >Unlimited Ad Campaigns
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="bg-indigo-600">
  <div class="px-6 py-24 sm:px-6 sm:py-32 lg:px-8">
    <div class="mx-auto max-w-2xl text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl"><br />Take your digital marketing to the next level</h2>
      <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-indigo-200">Sign up now and start reaching more customers online</p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <a
          href="#"
          class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-indigo-600 shadow-sm hover:bg-indigo-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
          >Get started</a
        ><a href="#" class="text-sm font-semibold leading-6 text-white">Learn more <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</div>
<div class="bg-white">
  <div class="mx-auto max-w-7xl px-6 py-24 sm:pt-32 lg:px-8 lg:py-40">
    <div class="lg:grid lg:grid-cols-12 lg:gap-8">
      <div class="lg:col-span-5">
        <h2 class="text-2xl font-bold leading-10 tracking-tight text-zinc-900">Frequently asked questions</h2>
        <p class="mt-4 text-base leading-7 text-zinc-600">
          Can’t find the answer you’re looking for? Reach out to our
          <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">customer support</a>
          team.
        </p>
      </div>
      <div class="mt-10 lg:col-span-7 lg:mt-0">
        <dl class="space-y-10">
          <div>
            <dt class="text-base font-semibold leading-7 text-zinc-900">What is a digital marketing platform?</dt>
            <dd class="mt-2 text-base leading-7 text-zinc-600">
              A digital marketing platform is a software solution that helps businesses manage and execute their online marketing efforts across various channels such as social media, email, search
              engines, and websites.
            </dd>
          </div>
          <div>
            <dt class="text-base font-semibold leading-7 text-zinc-900">How can a digital marketing platform benefit my business?</dt>
            <dd class="mt-2 text-base leading-7 text-zinc-600">
              A digital marketing platform can help streamline your marketing efforts, improve targeting and personalization, track and analyze campaign performance, and ultimately drive better
              results and ROI for your business.
            </dd>
          </div>
          <div>
            <dt class="text-base font-semibold leading-7 text-zinc-900">What features should I look for in a digital marketing platform?</dt>
            <dd class="mt-2 text-base leading-7 text-zinc-600">
              Key features to look for in a digital marketing platform include multi-channel campaign management, analytics and reporting tools, automation capabilities, CRM integration, and
              personalization options.
            </dd>
          </div>
          <div>
            <dt class="text-base font-semibold leading-7 text-zinc-900">Is a digital marketing platform suitable for small businesses?</dt>
            <dd class="mt-2 text-base leading-7 text-zinc-600">
              Yes, digital marketing platforms come in various sizes and functionalities to cater to the needs of small businesses. They can help small businesses reach their target audience more
              effectively and efficiently.
            </dd>
          </div>
          <div>
            <dt class="text-base font-semibold leading-7 text-zinc-900">How do I choose the right digital marketing platform for my business?</dt>
            <dd class="mt-2 text-base leading-7 text-zinc-600">
              When choosing a digital marketing platform, consider factors such as your budget, business goals, target audience, required features, ease of use, and customer support. It&#x27;s also
              helpful to read reviews and get recommendations from other businesses.
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</div>
'''

# Display the HTML content in the Streamlit app
st.markdown(html_code, unsafe_allow_html=True)