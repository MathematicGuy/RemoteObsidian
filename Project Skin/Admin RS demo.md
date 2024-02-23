**Core Administration**

- **UC001: Manage Users**
    - **Trigger:** Admin accesses the user management area.
    - **Description:** Admins can create, edit, delete, and view details of all user accounts (candidates, reviewers, and other admins).
    - **Normal Flow:**
        1. Admin selects "Manage Users".
        2. System displays a list of existing users with search/filter options.
        3. Admin can click to view details, edit permissions, or change account status (active/inactive).
- **UC002: Manage Exams**
    - **Trigger:** Admin accesses the exam creation area.
    - **Description:** Admins can create, edit, delete, and manage the availability of exams.
    - **Normal Flow**
        1. Admin selects "Create Exam"
        2. Admin inputs exam title, description, instructions, test cases, time limits, and scoring parameters (including ChatGPT's influence).
        3. System saves the exam. Admin can set it to "Active" to allow candidates to take it.

**System Configuration**

- **UC003: Configure ChatGPT Integration**
    - **Trigger:** Admin accesses the ChatGPT configuration settings.
    - **Description:** Admins can set API keys, parameters that control how ChatGPT analyzes code, and how heavily its output weighs in scoring.
- **UC004: System Settings**
    - **Trigger:** Admin accesses general system settings.
    - **Description:** Admins control site-wide settings such as branding (logo, colors), email notifications, security options, etc.

**Reporting and Analytics**

- **UC005: View Exam Results**
    - **Trigger:** Admin selects "Exam Reports".
    - **Description:** Admins view aggregate scores on exams, identify trends (common errors), and potentially problematic questions.
- **UC006: User Activity Tracking**
    - **Trigger:** Admin selects "User Activity".
    - **Description:** Admins can monitor logins, submissions, and actions taken by users to track engagement and identify potential issues (e.g., cheating attempts).

**Additional Possibilities (Depending on your project's scope)**

- **Manage Reviewers:** If you have a dedicated pool of reviewers, admins might recruit, assign them to specific exams, and track their performance.
- **Content Moderation:** Admins may need tools to review flagged submissions or user reports.
- **Advanced Technical Settings:** If applicable, manage server configuration, database settings, etc.

**Important Notes:**

- **Security:** Admin accounts should have the highest level of security and access logging within the system.
- **UI Considerations:** The admin dashboard needs to be clear and well-organized to manage these diverse tasks effectively.
- **Prioritize:** Start with the core use cases critical to run the exam system, then add advanced features as needed.