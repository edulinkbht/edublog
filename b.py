from flask import Flask

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduBlog - The Backstory of EduLink</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">
    
    <style>
        :root {
            /* Minimalist, professional grayscale palette */
            --accent-color: #C05636;
            --text-main: #1A1A1A;
            --text-muted: #666666;
            --text-faint: #999999;
            --bg-main: #FFFFFF;
            --bg-sidebar: #FDFCFB;
            --bg-navbar: #FFFFFF;
            --border-color: #EAEAEA;
            --blockquote-bg: #F9F9F9;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Merriweather', serif;
            color: var(--text-main);
            background-color: var(--bg-main);
            line-height: 1.8;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        a {
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 400;
        }

        a:hover {
            text-decoration: underline;
        }

        /* --- Navbar --- */
        .navbar {
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0;
            background-color: var(--bg-navbar);
            border-bottom: 1px solid var(--border-color);
            z-index: 10;
        }

        .navbar-left {
            display: flex;
            align-items: center;
            gap: 2rem;
            padding-left: 2rem;
        }

        .navbar-right {
            display: flex;
            align-items: center;
            height: 100%;
        }

        .navbar-right-links {
            display: flex;
            gap: 2rem;
            padding-right: 2rem;
        }

        .logo {
            font-weight: 900;
            font-size: 1.1rem;
            color: var(--text-main);
            text-decoration: none;
            letter-spacing: -0.01em;
        }

        .logo:hover {
            text-decoration: none;
        }

        .nav-links a {
            color: var(--text-muted);
            font-weight: 400;
            font-size: 0.9rem;
        }

        .nav-links a:hover {
            color: var(--text-main);
            text-decoration: none;
        }

        /* Aligned Search Wrapper */
        .search-wrapper {
            width: 250px;
            min-width: 250px;
            height: 100%;
            display: flex;
            align-items: center;
            border-left: 1px solid var(--border-color);
            padding: 0 1rem;
        }

        .search-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%; 
            background: #F5F5F5;
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            font-size: 0.85rem;
            color: var(--text-muted);
            cursor: pointer;
            border: 1px solid transparent;
            transition: border-color 0.2s ease;
        }

        .search-bar:hover {
            border-color: var(--border-color);
        }

        .shortcut-key {
            color: var(--text-faint);
            font-size: 0.75rem;
            font-family: sans-serif;
            border: 1px solid var(--border-color);
            padding: 1px 5px;
            border-radius: 4px;
            background: #FFFFFF;
        }

        /* --- Layout --- */
        .layout {
            display: flex;
            flex: 1;
            overflow: hidden;
        }

        .sidebar-left, .main-content, .sidebar-right {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        .sidebar-left::-webkit-scrollbar, 
        .main-content::-webkit-scrollbar, 
        .sidebar-right::-webkit-scrollbar {
            display: none;
        }

        /* --- Left Sidebar --- */
        .sidebar-left {
            width: 260px;
            min-width: 260px;
            background-color: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .menu {
            padding: 1.5rem 0;
        }

        .menu-group {
            margin-bottom: 1rem;
        }

        .menu-title {
            padding: 0.5rem 2rem;
            font-weight: 700;
            font-size: 0.85rem;
            color: var(--text-main);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: flex;
            justify-content: space-between;
            cursor: pointer;
        }

        .menu-item {
            padding: 0.3rem 2rem 0.3rem 2.5rem;
            font-size: 0.9rem;
            color: var(--text-muted);
            cursor: pointer;
            display: block;
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .menu-item:hover {
            color: var(--text-main);
            text-decoration: none;
        }

        .menu-item.active {
            color: var(--text-main);
            font-weight: 700;
        }

        .menu-item.active::before {
            content: "— ";
            color: var(--text-faint);
            margin-left: -1.2rem;
            position: absolute;
        }

        /* --- Main Content --- */
        .main-content {
            flex: 1;
            padding: 3rem 4rem;
            overflow-y: auto;
        }

        .content-inner {
            max-width: 720px;
            margin: 0 auto;
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 2rem;
            color: var(--text-main);
            letter-spacing: -0.02em;
            line-height: 1.2;
        }

        h2 {
            font-size: 1.5rem;
            font-weight: 700;
            margin: 2.5rem 0 1rem 0;
            color: var(--text-main);
        }

        .content-inner p {
            margin-bottom: 1.5rem;
            font-size: 1rem;
            color: #333333;
        }

        blockquote {
            background-color: var(--blockquote-bg);
            border-left: 4px solid var(--accent-color);
            padding: 1.5rem;
            margin: 2rem 0;
            font-style: italic;
            color: var(--text-muted);
            border-radius: 0 8px 8px 0;
        }

        /* Embedded Image Styling */
        .content-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 2rem 0 0.5rem 0;
            border: 1px solid var(--border-color);
            display: block;
            background-color: #F9F9F9;
        }

        .image-caption {
            font-size: 0.8rem !important;
            color: var(--text-faint) !important;
            text-align: center;
            margin-bottom: 2.5rem !important;
            font-family: sans-serif;
        }

        /* Container for profile pictures pair with a gap */
        .profile-row {
            display: flex;
            width: 100%;
            gap: 1.5rem;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .team-photo-pair-item {
            flex: 1; 
            height: 350px; 
            object-fit: cover; 
            display: block;
            border-radius: 8px; 
            border: 1px solid var(--border-color); 
            background-color: #F9F9F9;
        }

        /* Side-by-side Image and Text block for Genhub */
        .image-text-row {
            display: flex;
            gap: 2rem;
            align-items: center;
            margin: 2.5rem 0;
            background-color: var(--bg-sidebar);
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .image-text-row img {
            width: 280px;
            height: auto;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            object-fit: cover;
        }

        .image-text-row blockquote {
            margin: 0;
            border-left: none; /* remove standard blockquote line for this specific layout */
            padding: 0;
            background: transparent;
            font-size: 0.95rem;
        }

        strong {
            font-weight: 700;
            color: var(--text-main);
        }

        hr {
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 3rem 0;
        }

        /* --- Right Sidebar (TOC) --- */
        .sidebar-right {
            width: 250px;
            min-width: 250px;
            padding: 2.5rem 1.5rem;
            overflow-y: auto;
            border-left: 1px solid var(--border-color);
            background-color: var(--bg-sidebar);
        }

        .sidebar-right-title {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-faint);
            margin-bottom: 1rem;
            font-weight: 700;
        }

        .toc-list {
            list-style: none;
            font-size: 0.85rem;
        }

        .toc-list li {
            margin-bottom: 0.6rem;
        }

        .toc-list a {
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .toc-list a:hover {
            color: var(--text-main);
        }

        .toc-list a.active {
            color: var(--text-main);
            font-weight: 700;
        }

        /* --- Responsive Design --- */
        @media (max-width: 1024px) {
            .sidebar-right {
                display: none;
            }
            .search-wrapper {
                border-left: none;
            }
            .main-content {
                padding: 2rem;
            }
        }

        @media (max-width: 768px) {
            .sidebar-left {
                display: none;
            }
            .navbar-right-links {
                display: none;
            }
            .main-content {
                padding: 1.5rem;
            }
            h1 {
                font-size: 2rem;
            }
            .image-text-row {
                flex-direction: column;
            }
            .image-text-row img {
                width: 100%;
            }
        }
    </style>
</head>
<body>

    <header class="navbar">
        <div class="navbar-left">
            <a href="#" class="logo">EduBlog.</a>
        </div>
        <div class="navbar-right">
            <div class="nav-links navbar-right-links">
                <a href="#">v2.0</a>
                <a href="#">English</a>
            </div>
            <div class="search-wrapper">
                <div class="search-bar">
                    <span>Search</span>
                    <span class="shortcut-key">⌘ K</span>
                </div>
            </div>
        </div>
    </header>

    <div class="layout">
        
        <aside class="sidebar-left">
            <div class="menu">
                <div class="menu-group">
                    <a href="#" class="menu-item active">News & Updates</a>
                </div>
                
                <div class="menu-group">
                    <div class="menu-title">Platform</div>
                    <a href="#" class="menu-item">Development Logs</a>
                    <a href="#" class="menu-item">Security Patches</a>
                    <a href="#" class="menu-item">Frameworks</a>
                </div>

                <div class="menu-group">
                    <div class="menu-title">Community</div>
                    <a href="#" class="menu-item">Student Initiatives</a>
                    <a href="#" class="menu-item">Teacher Resources</a>
                </div>
            </div>
        </aside>

        <main class="main-content">
            <div class="content-inner">

                <h1>The Backstory of EduLink</h1>

                <p>Every major platform has an origin story, and EduLink is no different. What is today a cohesive educational tool initially started as a curious side project by <strong>Ngawang Tshogyal Phuentshok</strong>. Over the years, through trial, error, and iterations of completely different ideas, the vision for what we now know as EduLink gradually took form.</p>

                <h2 id="druk-brilliant">1. Druk Brilliant: The Playful Beginnings</h2>
                
                <p>Before any of the modern platforms took shape, there was <strong>Druk Brilliant</strong>. This was an idea from the founder when he was in 7th grade. It started as a playful environment, originally mimicking the school's design, to create a space for e-learning. Because he was just starting to experiment with web development, he added fun, interactive elements like game options and graphing tools.</p>
                
                <p>What started as playing around with "website things" became an opportunity to learn new technical skills. Druk Brilliant was created just for fun, started with Ngawang, Jamyang, Chencho Norbu, Karma Jangchuk, and Jigdral Namgyal.</p>

                <p>The early version of the site was constructed using <a href="https://www.w3schools.com/spaces/" target="_blank">w3spaces</a>. However, Druk Brilliant eventually ceased operation after w3schools discontinued certain services and blocked the website.</p>

                <img src="https://i.imghippo.com/files/xCZy1638AH.png" alt="Druk Brilliant Interface View 1" class="content-image">
                <img src="https://i.imghippo.com/files/UeR4105mBk.png" alt="Druk Brilliant Interface View 2" class="content-image">
                <p class="image-caption">Early interface concepts of Druk Brilliant</p>

                <h2 id="genhub">2. Genhub: The Generational Hub</h2>
                
                <p>Long before EduLink, the journey continued with an online code editor and social media platform known as <strong>Genhub (The Generational Hub)</strong>. Hosted on <a href="https://glitch.com" target="_blank">glitch.com</a>, Genhub allowed users to create websites easily without having to install external libraries, as everything was conveniently pre-installed.</p>
                
                <img src="https://i.imghippo.com/files/doG2043pM.png" alt="Genhub interface" class="content-image">
                <p class="image-caption">Early look at Genhub</p>

                <p>During this era, Genhub served as a testing ground for various services. It experimented with basic features like allowing users to post anonymously without an account, and even served as a promotional space for YouTube creators and school activities.</p> 

                <div class="image-text-row">
                    <img src="https://i.imghippo.com/files/veX5375Ca.jpg" alt="Genhub side project feature">
                    <div>
                        <blockquote>
                            "Genhub was his side project and I think that he was addicted to making websites, and I believed in his vision at that time as he inspired me to also grow and learn. I remember him adding my YouTube channel to this website in the sidebar."
                        </blockquote>
                    </div>
                </div>

                <p>Unfortunately, due to shifts in Glitch's economic model and hosting services, Genhub was discontinued, and the idea slowly faded.</p>

                <img src="https://i.imghippo.com/files/tEg2468EmI.png" alt="Genhub features" class="content-image">
                <p class="image-caption">Genhub in action before its closure</p>

                <h2 id="gravitas">3. Gravitas: The Learning Curve</h2>

                <p>Following the closure of Genhub, the founder pivoted to a new project titled <strong>Gravitas</strong>.</p>

                <img src="https://i.imghippo.com/files/vqkX6519jq.png" alt="Gravitas logo and early design" class="content-image">
                <p class="image-caption">Early branding for Gravitas</p>

                <p>Gravitas was initially built with the goal of fostering genuine connections and filtering out harmful content. It was during the development of this platform that Ngawang met his co-founder. Realizing they shared similar interests and visions, the two joined forces. As the founder noted, <em>"We share similar interests,"</em> which became the foundation of their collaborative workflow.</p>

                <img src="https://i.imghippo.com/files/RY6599aV.png" alt="Gravitas Code" class="content-image">
                <p class="image-caption">A glimpse into the codebase of Gravitas</p>

                <p>Interestingly, Gravitas was never publicly revealed. Hosted purely locally, only Sir Anith and Dasho Arun Kapur knew of its existence. It began primarily as an e-commerce shopping and generalized content platform—having absolutely no focus on education at the time. Due to a weak framework and poor security architecture, the app was prone to sudden crashes. There was a brief plan to host Gravitas on the school's servers, but this failed due to structural code issues. <a href="https://drive.google.com/drive/folders/1UNEPrOkov1nNxx6mbC-DHJOl8ukMpvJG?usp=sharing" target="_blank">The early codebase</a> still exists as a testament to those early struggles.</p>

                <img src="https://i.imghippo.com/files/aDTc3800wEg.png" alt="Early Gravitas Team Site" class="content-image">
                <p class="image-caption">The early team site for Gravitas</p>

                <p>Though Gravitas wasn't a commercial success, it was a massive learning experience. The turning point arrived when the team was given the opportunity to present their project to the <strong>DHI</strong> (Druk Holding and Investments) team. This pivotal presentation completely shifted their vision, leading them to rename and repurpose the entire platform.</p>

                <blockquote>
                    "Due to this conversation with the DHI team, I was able to learn new things and it made me more motivated to work on this project and focus on changemaking."
                </blockquote>

                <h2 id="edulink">4. EduLink Till the Present Day</h2>

                <p>With a renewed vision, the project was reborn as <strong>EduLink</strong>. The developer spent time experimenting with cloud services to construct a resilient backend, while the founder completely overhauled the product design, delivering a much more refined UI and UX.</p>
                
                <p>The core team engaged in extensive discussions to refine the platform's purpose. A massive leap forward occurred when the team secured an internship at <strong>IAC-Techpark</strong>. Working in a professional tech environment allowed them to significantly improve the website's functionality.</p>

                <div class="profile-row">
                    <img src="https://i.imghippo.com/files/Tpte7536KQ.png" alt="IAC Techpark Experience 1" class="team-photo-pair-item">
                    <img src="https://i.imghippo.com/files/ZW5008ek.png" alt="IAC Techpark Experience 2" class="team-photo-pair-item">
                </div>
                <p class="image-caption">The team working and learning during their IAC-Techpark internship</p>

                <blockquote>
                    "Due to the internship at the IAC I was able to learn new things and expand my social circle. Gratitude to Acho Yangsel's parents who supported us, and thanks to Acho Yangsel, Azhim Sonam P., and Azhim Dawa for guiding and giving us feedback."
                </blockquote>

                <p>Today, EduLink is heavily focused on growth. The team continues to improve their codebase, strengthen the framework, upgrade storage systems, and expand the services offered to students and educators.</p>

                <hr>

                <p><strong>In the next Publication:</strong> <em>EduLink and its growth</em>.</p>

            </div>
        </main>

        <aside class="sidebar-right">
            <div class="sidebar-right-title">On this page</div>
            <ul class="toc-list">
                <li><a href="#druk-brilliant" class="active">1. Druk Brilliant</a></li>
                <li><a href="#genhub">2. Genhub</a></li>
                <li><a href="#gravitas">3. Gravitas</a></li>
                <li><a href="#edulink">4. EduLink Present Day</a></li>
            </ul>
        </aside>

    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return html_content

if __name__ == '__main__':
    app.run(debug=True)