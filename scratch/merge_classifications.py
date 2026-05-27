import json

# Dream classifications
dream_ai = [
  {
    "filename": "12-Weeks Year Framework.md",
    "relative_path": "Dream/12-Weeks Year Framework.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "A three-month goal-setting schedule utilizes a one-month preservation buffer for the final deadline rush. Gameplans and sub-milestones partition major deliverables to track project momentum.",
    "confidence": "high"
  },
  {
    "filename": "22 lessons in 22 years.md",
    "relative_path": "Dream/22 lessons in 22 years.md",
    "category": "3 RESOURCES/Happiness",
    "summary": "Twenty-two personal guidelines outline principles for parental empathy, critical thinking, and social connections. Active habits include daily journaling, photo documentation, and a self-forgiveness process for emotional inventory management.",
    "confidence": "high"
  },
  {
    "filename": "48 Laws of Power.md",
    "relative_path": "Dream/48 Laws of Power.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Forty-eight interpersonal strategies outline methods for establishing workplace authority and managing professional reputations. Explicit instructions detail tactics like hiding operational intentions, speaking concisely, and leveraging enemy alliances.",
    "confidence": "high"
  },
  {
    "filename": "_Focus.md",
    "relative_path": "Dream/_Focus.md",
    "category": "2 ACTIONS",
    "summary": "An operational dashboard integrates daily composer productivity rules with task lists for violin practice, video production, and Excalidraw diagrams. Index links map target folders for happiness, study strategies, and productivity improvement.",
    "confidence": "high"
  },
  {
    "filename": "Career Advices.md",
    "relative_path": "Dream/Career Advices.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Career strategy guidelines prioritize apprenticing under successful corporations before launching new business ventures. First-principles analysis and high iteration rates drive employee development and organizational problem-solving.",
    "confidence": "high"
  },
  {
    "filename": "CHANGES.md",
    "relative_path": "Dream/CHANGES.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "A morning routine protocol outlines guidelines for waking up at 4:30 AM through early sleep schedules and technology-free exercise. Dopamine management strategies leverage hyper-focus on passion projects to mitigate ADHD constraints.",
    "confidence": "high"
  },
  {
    "filename": "Cheat Code.md",
    "relative_path": "Dream/Cheat Code.md",
    "category": "3 RESOURCES/How To Study",
    "summary": "Behavioral protocols list physiological interventions like box breathing, cold-water facial immersion, and post-study naps. An exam preparation framework details skimming strategies and practice question retrieval to accelerate learning.",
    "confidence": "high"
  },
  {
    "filename": "Delusion.md",
    "relative_path": "Dream/Delusion.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "A psychological analysis translates Carl Jung's definition of delusions as manifestations of the unconscious mind. The text compares these cognitive phenomena to dreams and details their integration into therapeutic models.",
    "confidence": "high"
  },
  {
    "filename": "Flow.md",
    "relative_path": "Dream/Flow.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "A mental performance model maps the five-stage cycle from struggle and cognitive release to flow and recovery. Active recovery protocols specify saunas, ice baths, and sleep to restore metabolic baselines.",
    "confidence": "high"
  },
  {
    "filename": "How to get PERFECT GRADES as a GAMER (How to Success in 2 different Domains at the same time).md",
    "relative_path": "Dream/How to get PERFECT GRADES as a GAMER (How to Success in 2 different Domains at the same time).md",
    "category": "3 RESOURCES/How To Study",
    "summary": "A student-gamer discipline protocol mandates a strict 6:00 PM curfew on competitive gaming to protect sleep quality. Single-day context blocks allocate cognitive energy to either intensive academic study or high-performance gaming.",
    "confidence": "high"
  },
  {
    "filename": "Improve your critical inquiry skills.md",
    "relative_path": "Dream/Improve your critical inquiry skills.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Cognitive bias checks and logical fallacies form the core of critical thinking methods. Analysis of multi-variable scenarios guides decision-making and prevents premature conclusions.",
    "confidence": "high"
  },
  {
    "filename": "Learn 10x Faster Starting Tonight.md",
    "relative_path": "Dream/Learn 10x Faster Starting Tonight.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Active recall testing and distraction reduction serve as the primary mechanics for short-term memory optimization. Daily endurance training and scheduled rest periods facilitate long-term memory retention.",
    "confidence": "high"
  },
  {
    "filename": "Make Any Conversation More Fun and Fulfilling.md",
    "relative_path": "Dream/Make Any Conversation More Fun and Fulfilling.md",
    "category": "3 RESOURCES/How To",
    "summary": "Open-ended questions and reflective responses extend conversation durations. Active summarization and emotional labeling improve mutual understanding between speakers.",
    "confidence": "high"
  },
  {
    "filename": "Philopsophy that brought me back to life.md",
    "relative_path": "Dream/Philopsophy that brought me back to life.md",
    "category": "3 RESOURCES/Happiness",
    "summary": "Definitions of identity rely on observable behavioral patterns rather than abstract essences. Scientific observation describes functional behaviors rather than fundamental existence.",
    "confidence": "high"
  },
  {
    "filename": "Possitive Though.md",
    "relative_path": "Dream/Possitive Though.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Optimal sleep hygiene and daily task reflection increase focus during study sessions. Pomodoro timers and single-goal focus limit decision fatigue and prevent task abandonment.",
    "confidence": "high"
  },
  {
    "filename": "Productivity Note.md",
    "relative_path": "Dream/Productivity Note.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Focus cycles of ninety minutes leverage natural human energy peaks for maximum efficiency. The DSRP framework provides cognitive mapping patterns.",
    "confidence": "high"
  },
  {
    "filename": "PROKLEM.md",
    "relative_path": "Dream/PROKLEM.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "A checklist tracks resolved habits such as doom scrolling and poor morning exercise routines. Cross-references link to personal reflection files on positive thinking.",
    "confidence": "high"
  },
  {
    "filename": "Question to Ask My Self.md",
    "relative_path": "Dream/Question to Ask My Self.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "Structured prompts guide self-reflection on past decisions, life purpose, and personal ambitions. Dialogues explore identity, competitive drives, and behavioral changes.",
    "confidence": "high"
  },
  {
    "filename": "Riddle.md",
    "relative_path": "Dream/Riddle.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "An ethical dilemma presents a scenario involving a dying lady, a life-saving friend, and a dream partner. The puzzle evaluates decision-making logic and moral prioritization during recruitment.",
    "confidence": "high"
  },
  {
    "filename": "Secret History Work.md",
    "relative_path": "Dream/Secret History Work.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "Economic history analysis outlines the consolidation of financial power from merchants to central banking institutions. Comparisons contrast theological destiny with scientific determinism regarding societal control.",
    "confidence": "high"
  },
  {
    "filename": "Shadow work.md",
    "relative_path": "Dream/Shadow work.md",
    "category": "3 RESOURCES/Happiness",
    "summary": "Jungian concepts of the persona, shadow, and anima guide identity integration exercises. Techniques address emotional suppression, vulnerability, and toxic shame reduction.",
    "confidence": "high"
  },
  {
    "filename": "Studying Abroad.md",
    "relative_path": "Dream/Studying Abroad.md",
    "category": "3 RESOURCES/How To",
    "summary": "Application guidelines detail scholarship opportunities including DAAD and Heinrich Böll programs. Expense calculations project tuition, housing, and insurance costs for German universities.",
    "confidence": "high"
  },
  {
    "filename": "Themes Note.md",
    "relative_path": "Dream/Themes Note.md",
    "category": "3 RESOURCES/GoodForLater",
    "summary": "A brief reference note preserves check-box visual styles and code block templates. Python syntax examples demonstrate basic output scripting functions.",
    "confidence": "high"
  },
  {
    "filename": "Violin.md",
    "relative_path": "Dream/Violin.md",
    "category": "3 RESOURCES/How To",
    "summary": "Instructional guides detail physical posture, bow alignment, and tone production techniques for violinists. Practice schedules prioritize regular rest cycles and diverse exercises to reduce muscle tension.",
    "confidence": "high"
  },
  # Wait, there are 4 more files in needs_ai that we should check! Let's load the scan utf-8 again to see if we missed any filenames.
  # Let's see: in Dream scan, unorganized count is 28. Let's make sure we have all of them.
  # File list in SCAN matching skipped:
  # '12-Weeks Year Framework.md', '22 lessons in 22 years.md', '48 Laws of Power.md', '_Focus.md', 'Career Advices.md', 'CHANGES.md', 'Cheat Code.md', 'Delusion.md', 'Flow.md', 'How to get PERFECT GRADES as a GAMER (How to Success in 2 different Domains at the same time).md', 'How to remember everything you learn.md', 'How to Study Programming Effectively.md', 'How to Study.md', 'If you're in your 20's watch this..md', 'Improve your critical inquiry skills.md', 'Learn 10x Faster Starting Tonight.md', 'Make Any Conversation More Fun and Fulfilling.md', 'Philopsophy that brought me back to life.md', 'Possitive Though.md', 'Productivity Note.md', 'PROKLEM.md', 'Question to Ask My Self.md', 'Riddle.md', 'Secret History Work.md', 'Shadow work.md', 'Studying Abroad.md', 'Themes Note.md', 'Violin.md'
  # Wait, let's verify if there are any others. Let's make sure they are categorized correctly.
  {
    "filename": "How to remember everything you learn.md",
    "relative_path": "Dream/How to remember everything you learn.md",
    "category": "3 RESOURCES/How To Study",
    "summary": "Analyses competence illusions like passive reading or visual familiarity. Recommends active recall and deep conceptual explanations to achieve real knowledge retention.",
    "confidence": "high"
  },
  {
    "filename": "How to Study Programming Effectively.md",
    "relative_path": "Dream/How to Study Programming Effectively.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "Recommends project-based learning focused on a single technical field. Emphasizes establishing solid fundamentals and utilizing referrals before entering the job market.",
    "confidence": "high"
  },
  {
    "filename": "How to Study.md",
    "relative_path": "Dream/How to Study.md",
    "category": "3 RESOURCES/How To Study",
    "summary": "Outlines cognitive load budgets requiring 25-40% of unoccupied memory for effective learning. Proposes a morning settling routine to reduce physical and emotional stress.",
    "confidence": "high"
  },
  {
    "filename": "If you're in your 20's watch this..md",
    "relative_path": "Dream/If you're in your 20's watch this..md",
    "category": "3 RESOURCES/Happiness",
    "summary": "Catalogs twenty-five development rules covering sleep, financial investments, marriage readiness, and gut health. Warns against self-pity and learned helplessness.",
    "confidence": "high"
  }
]

# Project_Skin classifications
skin_ai = [
  {
    "filename": "AI Engineering Job.md",
    "relative_path": "Project_Skin/AI Engineering Job.md",
    "category": "3 RESOURCES/Software Engineer",
    "summary": "This document outlines career requirements and skillsets for junior and fresher machine learning engineer roles. It details technical expectations and job profiles within the artificial intelligence sector.",
    "confidence": "high"
  },
  {
    "filename": "Array vs ArrayList vs List and ListIterator.md",
    "relative_path": "Project_Skin/Array vs ArrayList vs List and ListIterator.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This reference guide explains the distinctions, performance tradeoffs, and characteristics of Java collections including Array, ArrayList, List, and ListIterator. Code snippets demonstrate instantiation and usage of these data structures in Java applications.",
    "confidence": "high"
  },
  {
    "filename": "Audiophile.md",
    "relative_path": "Project_Skin/Audiophile.md",
    "category": "3 RESOURCES/Save for later",
    "summary": "This document compiles earbud rankings, prices, and purchasing options for high-fidelity in-ear monitors. It lists audio tracks and contenders such as Simgot and Kefine Delci for sound testing.",
    "confidence": "high"
  },
  {
    "filename": "Building PC.md",
    "relative_path": "Project_Skin/Building PC.md",
    "category": "3 RESOURCES/Save for later",
    "summary": "This budget planner lists computer components, costs, and hardware specifications for assembling a personal computer with an RTX 5060 Ti graphics card. It details trade-offs between central processing units and power supply selections to avoid cost inflation.",
    "confidence": "high"
  },
  {
    "filename": "Classification Bayes.md",
    "relative_path": "Project_Skin/Classification Bayes.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This educational note details the mathematical formulations and probability variables of the Naive Bayes classification algorithm. It uses conditional probability equations and feature dataset examples to explain the assumption of independence between attributes.",
    "confidence": "high"
  },
  {
    "filename": "Classification Ensemble.md",
    "relative_path": "Project_Skin/Classification Ensemble.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This study sheet summarizes ensemble learning methodologies including hard and soft voting classifiers. It describes support vector machines, image gradients, and histogram of oriented gradients used in face recognition algorithms.",
    "confidence": "high"
  },
  {
    "filename": "CrackNitendoGames.md",
    "relative_path": "Project_Skin/CrackNitendoGames.md",
    "category": "3 RESOURCES/How to",
    "summary": "This guide outlines the download and installation steps for the Ryujinx Nintendo Switch emulator. It provides instructions for importing product keys and installing system firmware to run games.",
    "confidence": "high"
  },
  {
    "filename": "Dev anime Story.md",
    "relative_path": "Project_Skin/Dev anime Story.md",
    "category": "3 RESOURCES/Happiness",
    "summary": "This humorous narrative describes the daily workspace experiences and personal pursuits of a backend Java developer. It portrays interactions with human resources personnel and quality assurance colleagues in a corporate setting.",
    "confidence": "high"
  },
  {
    "filename": "DM.md",
    "relative_path": "Project_Skin/DM.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "This blank markdown document does not contain any text content or structural elements. It serves as an empty placeholder file in the active repository.",
    "confidence": "high"
  },
  {
    "filename": "Docker MSSQL.md",
    "relative_path": "Project_Skin/Docker MSSQL.md",
    "category": "3 RESOURCES/DataBase",
    "summary": "This reference guide provides configuration commands and templates for deploying Microsoft SQL Server inside Docker containers. It includes Java Spring Boot repository code and docker-compose database service setups.",
    "confidence": "high"
  },
  {
    "filename": "Docker PostgresSQL.md",
    "relative_path": "Project_Skin/Docker PostgresSQL.md",
    "category": "3 RESOURCES/DataBase",
    "summary": "This deployment note explains how to manage PostgreSQL database servers using Docker containers and the Windows Services utility. It details commands for checking container status and addresses connection timeout resolutions.",
    "confidence": "high"
  },
  {
    "filename": "Dynamic Memory Allocation.md",
    "relative_path": "Project_Skin/Dynamic Memory Allocation.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "This blank markdown document does not contain any text content or structural elements. It serves as an empty placeholder file in the active repository.",
    "confidence": "high"
  },
  {
    "filename": "English Club.md",
    "relative_path": "Project_Skin/English Club.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "This placeholder document is intended for tracking language learning sessions or English club activities. It currently contains no descriptive text or schedules.",
    "confidence": "high"
  },
  {
    "filename": "enum class.md",
    "relative_path": "Project_Skin/enum class.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This programming reference defines the concept of Java enumerations used to represent groups of constant variables. It provides code examples demonstrating enum declaration and usage in software applications.",
    "confidence": "high"
  },
  {
    "filename": "Flutter.md",
    "relative_path": "Project_Skin/Flutter.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This technical guide outlines the setup and initialization steps for Flutter mobile and web applications. It details configurations for the Android SDK manager, emulator execution, and standard UI widgets.",
    "confidence": "high"
  },
  {
    "filename": "Full Stack Java.md",
    "relative_path": "Project_Skin/Full Stack Java.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This reference document outlines the steps for creating a full-stack web application using the Java Spring Boot framework. It provides sample code for model classes, including attributes, constructors, and encapsulation methods.",
    "confidence": "high"
  },
  {
    "filename": "German History.md",
    "relative_path": "Project_Skin/German History.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This historical note describes the socio-economic impact of the Treaty of Versailles on the German population after World War I. It also examines post-war educational practices and cultural mechanisms for coping with historical events.",
    "confidence": "high"
  },
  {
    "filename": "German Learning Core.md",
    "relative_path": "Project_Skin/German Learning Core.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "This study guide outlines scientific strategies and core methodologies for acquiring German language proficiency from levels A1 to C2. It highlights skills in reading, listening, and speaking while emphasizing vocabulary acquisition over word-by-word memorization.",
    "confidence": "high"
  },
  {
    "filename": "German Song.md",
    "relative_path": "Project_Skin/German Song.md",
    "category": "3 RESOURCES/Save for later",
    "summary": "This document records the German lyrics and English translations of an anime-themed pop song by artist Selphius. It provides literal translations for language practice and appreciation.",
    "confidence": "high"
  },
  {
    "filename": "Germanic Language.md",
    "relative_path": "Project_Skin/Germanic Language.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "This linguistic note analyzes common structural characteristics of Germanic languages, highlighting English definite nouns and word order constraints. It specifically explains the V2 verb placement rule in sentence constructions.",
    "confidence": "high"
  },
  {
    "filename": "House of Hypertrophy.md",
    "relative_path": "Project_Skin/House of Hypertrophy.md",
    "category": "3 RESOURCES/Productivity & Improvement",
    "summary": "This athletic guide outlines training techniques and scientific studies focused on calisthenics and muscle hypertrophy. It details the execution of lengthened supersets, full-range pushups, and partial movements for optimized muscle growth.",
    "confidence": "high"
  },
  {
    "filename": "How to build a web application in Java.md",
    "relative_path": "Project_Skin/How to build a web application in Java.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This technical walkthrough details the structural architecture of a Java Web Model-View-Controller application. It provides code models using record classes, enums, and command-line runners to build REST API endpoints.",
    "confidence": "high"
  },
  {
    "filename": "How to Enable Group Policy Editor in Windows 11 Home Edition.md",
    "relative_path": "Project_Skin/How to Enable Group Policy Editor in Windows 11 Home Edition.md",
    "category": "3 RESOURCES/How to",
    "summary": "This system administration guide explains how to activate the Group Policy Editor utility on Windows 11 Home Edition. It provides a batch script utilizing deployment image servicing commands to install missing policy packages.",
    "confidence": "high"
  },
  {
    "filename": "IELST LISTENING.md",
    "relative_path": "Project_Skin/IELST LISTENING.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "This blank markdown document does not contain any text content or structural elements. It serves as an empty placeholder file in the active repository.",
    "confidence": "high"
  },
  {
    "filename": "IELST Reading Note.md",
    "relative_path": "Project_Skin/IELST Reading Note.md",
    "category": "3 RESOURCES/Question Mark",
    "summary": "This brief document is a placeholder designed for recording academic reading notes and vocabulary. It currently contains no substantive educational materials or study plans.",
    "confidence": "high"
  },
  {
    "filename": "IELST Writing Task Guide.md",
    "relative_path": "Project_Skin/IELST Writing Task Guide.md",
    "category": "3 RESOURCES/How to",
    "summary": "This guide contains scoring criteria, structures, and stylistic rules for the writing portion of the IELTS exam. Specific guidelines outline body paragraph composition, bar graph descriptions, and linking phrases.",
    "confidence": "high"
  },
  {
    "filename": "Learn Languages FAST.md",
    "relative_path": "Project_Skin/Learn Languages FAST.md",
    "category": "3 RESOURCES/How to",
    "summary": "This document details mnemonic methodologies, accent training routines, and military language acquisition structures. Textual segments analyze code-switching exercises and spy immersion techniques.",
    "confidence": "high"
  },
  {
    "filename": "Learn ReactNative.md",
    "relative_path": "Project_Skin/Learn ReactNative.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This empty file serves as a dedicated placeholder for React Native application development and code snippet documentation. No programming data is currently active.",
    "confidence": "high"
  },
  {
    "filename": "Learning Thourgh Videos.md",
    "relative_path": "Project_Skin/Learning Thourgh Videos.md",
    "category": "3 RESOURCES/How to",
    "summary": "This notebook lists German vocabulary translations, focusing on nouns, adjectives, and prepositions from street interview videos. Example entries analyze terms for sleep quality, cycling infrastructure, and traffic safety.",
    "confidence": "high"
  },
  {
    "filename": "LOL.md",
    "relative_path": "Project_Skin/LOL.md",
    "category": "3 RESOURCES/Save for later",
    "summary": "This guide details combat strategies, lane behaviors, and match scheduling tactics for League of Legends gameplay. It provides decision frameworks for gold farming and champion positioning.",
    "confidence": "high"
  },
  {
    "filename": "Luật Dân Sự và Luật Tố Tụng Dân Sự.md",
    "relative_path": "Project_Skin/Luật Dân Sự và Luật Tố Tụng Dân Sự.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This empty file acts as a structural placeholder for legal notes regarding civil code systems and civil procedure regulations. No statutory references or legal annotations are currently written.",
    "confidence": "high"
  },
  {
    "filename": "Pasted image 20260329085207.png.md",
    "relative_path": "Project_Skin/Pasted image 20260329085207.png.md",
    "category": "4 ARCHIVES",
    "summary": "This file serves as a blank wrapper for a pasted image attachment within the vault. The document contains no descriptive annotations or text blocks.",
    "confidence": "high"
  },
  {
    "filename": "Personal Portfolio.md",
    "relative_path": "Project_Skin/Personal Portfolio.md",
    "category": "1 PROJECTS",
    "summary": "This template compiles framework options, layout guides, and coding prompts for building a portfolio website using Gatsby and Netlify. Specific inspirations detail minimalist footers and terminal visual themes.",
    "confidence": "high"
  },
  {
    "filename": "Pháp Luật.md",
    "relative_path": "Project_Skin/Pháp Luật.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This study guide outlines system hierarchies, constitutional laws, and legal liability definitions within the Vietnamese legal framework. Specific sections differentiate administrative violations and subjective culpability.",
    "confidence": "high"
  },
  {
    "filename": "Python Command.md",
    "relative_path": "Project_Skin/Python Command.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This sheet lists basic Python code blocks and an item class syntax for testing variable datatypes. It provides a simple syntax reference template.",
    "confidence": "high"
  },
  {
    "filename": "Python OOP.md",
    "relative_path": "Project_Skin/Python OOP.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This guide explains classes, constructors, methods, and instantiation procedures in Python Object-Oriented Programming. Sample scripts illustrate member attributes, memory addresses, and return functions.",
    "confidence": "high"
  },
  {
    "filename": "Quản Lý Hành Chính Nhà Nước.md",
    "relative_path": "Project_Skin/Quản Lý Hành Chính Nhà Nước.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This file is a placeholder designated for study notes on administrative state management systems. The document contains no active text or outlines.",
    "confidence": "high"
  },
  {
    "filename": "React.md",
    "relative_path": "Project_Skin/React.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This document functions as an empty repository for React library code blocks and component structures. No program scripts are currently registered.",
    "confidence": "high"
  },
  {
    "filename": "Requirement to understand this sentence.md",
    "relative_path": "Project_Skin/Requirement to understand this sentence.md",
    "category": "3 RESOURCES/How to",
    "summary": "This grammar resource breaks down German case systems, word orders, and verb conjugations through a sample breakfast sentence. It details preposition contractions, adverbs, and pronoun structures.",
    "confidence": "high"
  },
  {
    "filename": "SD HW2.md",
    "relative_path": "Project_Skin/SD HW2.md",
    "category": "3 RESOURCES/Software Engineer",
    "summary": "This assignment analyzes user story guidelines and wireframe specifications within Software Requirements Specifications (SRS). It evaluates use case models and system development methodologies.",
    "confidence": "high"
  },
  {
    "filename": "Software Deployment Project.md",
    "relative_path": "Project_Skin/Software Deployment Project.md",
    "category": "3 RESOURCES/Software Engineer",
    "summary": "This development sheet provides a user story template and acceptance criteria for a forgot-password screen. It details sequential interface steps and verification flows.",
    "confidence": "high"
  },
  {
    "filename": "Stress-Free Productivity.md",
    "relative_path": "Project_Skin/Stress-Free Productivity.md",
    "category": "3 RESOURCES/How to",
    "summary": "This book review details psychological frameworks for balancing habit efficiency, creative growth, and subjective well-being. It critiques rigid daily routines and analyzes cognitive performance mechanics.",
    "confidence": "high"
  },
  {
    "filename": "Todo.md",
    "relative_path": "Project_Skin/Todo.md",
    "category": "2 ACTIONS",
    "summary": "This personal organizer tracks task priorities, fitness goals, and learning curricula across machine learning and communications. It catalogs educational bookmarks and behavioral habits.",
    "confidence": "high"
  },
  {
    "filename": "Transaction with Authentication - JAVA.md",
    "relative_path": "Project_Skin/Transaction with Authentication - JAVA.md",
    "category": "3 RESOURCES/Programming",
    "summary": "This technical specification outlines Java authentication steps and database transactions for user balance deductions. A text flow diagram illustrates validation checkpoints and abort sequences.",
    "confidence": "high"
  },
  {
    "filename": "Tòng Hợp LS Đảng.md",
    "relative_path": "Project_Skin/Tòng Hợp LS Đảng.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This comprehensive compilation registers historical milestones, party conferences, and strategic guidelines of the Vietnamese Communist Party. It catalogs revolutionary timelines, military actions, and leadership changes.",
    "confidence": "high"
  },
  {
    "filename": "UI with Coding Agent.md",
    "relative_path": "Project_Skin/UI with Coding Agent.md",
    "category": "3 RESOURCES/Save for later",
    "summary": "This catalog outlines prompts and design aesthetics for landing pages generated via automated coding tools. It lists parameters for Swiss minimalism, glassmorphism, and Neobrutalism.",
    "confidence": "high"
  },
  {
    "filename": "Untitled.md",
    "relative_path": "Project_Skin/Untitled.md",
    "category": "4 ARCHIVES",
    "summary": "This file is a blank document containing no system text, tags, or headers. It acts as an uninitialized placeholder.",
    "confidence": "high"
  },
  {
    "filename": "Venture Capital.md",
    "relative_path": "Project_Skin/Venture Capital.md",
    "category": "3 RESOURCES/Save for later",
    "summary": "This file serves as a placeholder for notes on funding strategies, investment rounds, and portfolio valuations. No financial content is currently recorded.",
    "confidence": "high"
  },
  {
    "filename": "VIetnam General Law Revision.md",
    "relative_path": "Project_Skin/VIetnam General Law Revision.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This revision guide outlines constitutional laws, state agencies, and parliamentary structures in Vietnam. It analyzes court jurisdictions, election rules, and administrative roles.",
    "confidence": "high"
  },
  {
    "filename": "Vietnam party history.md",
    "relative_path": "Project_Skin/Vietnam party history.md",
    "category": "3 RESOURCES/History & Politic",
    "summary": "This document archives diagrams, leadership notes, and chapter summaries regarding the political history of the Vietnamese revolutionary party. Specific topics outline party leaders and historical timelines.",
    "confidence": "high"
  }
]

def load_scan(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    start = content.find('{')
    return json.loads(content[start:])

def main():
    # 1. Merge Dream scan + classifications
    dream_scan = load_scan('Dream_scan_utf8.json')
    dream_scan['ai_classified'] = dream_ai
    with open('Dream_merged_classifications.json', 'w', encoding='utf-8') as f:
        json.dump(dream_scan, f, indent=2, ensure_ascii=False)
        
    # 2. Merge Project_Skin scan + classifications
    skin_scan = load_scan('Project_Skin_scan_utf8.json')
    skin_scan['ai_classified'] = skin_ai
    with open('Project_Skin_merged_classifications.json', 'w', encoding='utf-8') as f:
        json.dump(skin_scan, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
