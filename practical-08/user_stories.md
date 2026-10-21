# Practical 8: User Stories Backlog & Acceptance Criteria

## SRS Requirement Reference
> "A registered library member can borrow up to a maximum of 3 physical books at any given time for an allowable lending period of 14 days per book. If a borrowed book is not returned within 14 days, the system marks the book as overdue, levies an automated daily overdue fine of $1.00 per late day, and automatically suspends the member's borrowing and renewal privileges until all overdue books are checked in and outstanding fines are cleared. A member can view their active borrowings, search catalog availability, and request a 7-day renewal for an active loan provided the book has not been reserved by another patron and no outstanding penalties exist on the member's account. Library Staff (Librarians) have authorization to process check-ins and check-outs, manually override account suspensions under administrative discretion, issue fee waivers, and view delinquent account audit reports."

---

## Generated User Stories

### Story US-01: Borrow Book within Quota Limit
- **Role**: Registered Library Member
- **User Story**:  
  **As a** registered library member with good standing,  
  **I want** to borrow up to 3 books for 14 days,  
  **So that** I can access reading materials without exceeding my allowed borrowing limit.
- **Acceptance Criteria (Given-When-Then)**:
  - **Scenario 1 (Successful checkout within quota)**:
    - **Given** a registered member has 1 active borrowed book and no unpaid fines or overdue books,
    - **When** the member requests to borrow 1 available book from the catalog,
    - **Then** the system approves the loan, sets the due date to exactly 14 calendar days from today, and updates the member's active loan count to 2.
  - **Scenario 2 (Borrowing limit reached)**:
    - **Given** a registered member already has 3 active borrowed books,
    - **When** the member attempts to borrow an additional book,
    - **Then** the system denies the checkout and displays an error message stating: "Borrowing quota exceeded. You may only borrow up to 3 books at a time."

---

### Story US-02: Overdue Fine Calculation and Account Suspension
- **Role**: System / Automated Scheduler
- **User Story**:  
  **As a** library management system,  
  **I want** to automatically calculate a $1.00 daily fine and suspend account privileges for overdue books,  
  **So that** patrons return books promptly and inventory remains available for the community.
- **Acceptance Criteria (Given-When-Then)**:
  - **Scenario 1 (Book becomes overdue)**:
    - **Given** a borrowed book has passed its 14-day due date without being returned,
    - **When** the automated daily circulation batch job runs at midnight,
    - **Then** the system marks the loan status as 'Overdue', applies a fine of $1.00 per elapsed day past the due date, and updates the member account status to 'Suspended'.
  - **Scenario 2 (Suspended member attempts loan or renewal)**:
    - **Given** a member account has a status of 'Suspended' due to an overdue book or outstanding fine,
    - **When** the member attempts to borrow a new book or renew an existing loan,
    - **Then** the system blocks the transaction and prompts the user: "Borrowing privileges suspended due to overdue books or outstanding fines."

---

### Story US-03: Loan Renewal
- **Role**: Registered Library Member
- **User Story**:  
  **As a** registered library member,  
  **I want** to renew an active borrowed book for an additional 7 days,  
  **So that** I have more time to finish reading without incurring overdue penalties.
- **Acceptance Criteria (Given-When-Then)**:
  - **Scenario 1 (Eligible renewal without reservations)**:
    - **Given** a member has an active borrowed book that is not overdue, the member has no unpaid fines, and no other patron has reserved the title,
    - **When** the member submits a renewal request for that book,
    - **Then** the loan due date is extended by 7 days from the current due date and a confirmation is displayed.
  - **Scenario 2 (Renewal blocked due to reservation hold)**:
    - **Given** another library member has placed a reservation hold on the borrowed book,
    - **When** the current borrower requests a renewal,
    - **Then** the system denies the renewal and presents the message: "Cannot renew: this item has an active reservation hold for another member."

---

### Story US-04: Outstanding Fine Settlement
- **Role**: Registered Library Member
- **User Story**:  
  **As a** library member with an accumulated fine,  
  **I want** to pay my outstanding overdue fines online or at the circulation desk,  
  **So that** my account suspension is lifted and my borrowing privileges are restored.
- **Acceptance Criteria (Given-When-Then)**:
  - **Scenario 1 (Full payment and account reinstatement)**:
    - **Given** a member has an account suspension solely due to a $5.00 unpaid fine after returning overdue books,
    - **When** the member pays the full balance of $5.00 via payment gateway or librarian desk,
    - **Then** the system records the payment transaction receipt, clears the outstanding balance to $0.00, and immediately changes the account status from 'Suspended' to 'Active'.
  - **Scenario 2 (Partial payment keeps suspension)**:
    - **Given** a member owes $10.00 in accumulated fines,
    - **When** the member submits a partial payment of $4.00,
    - **Then** the remaining balance is updated to $6.00 and the account status remains 'Suspended' until all fines are settled.

---

### Story US-05: Librarian Administrative Suspension Override & Fee Waiver
- **Role**: Authorized Librarian / Staff
- **User Story**:  
  **As a** library staff member (Librarian),  
  **I want** to manually override an account suspension and issue fee waivers under administrative discretion,  
  **So that** legitimate disputes, documented medical emergencies, or library errors can be resolved.
- **Acceptance Criteria (Given-When-Then)**:
  - **Scenario 1 (Discretionary fee waiver and reinstatement)**:
    - **Given** an authenticated librarian accesses a suspended member's profile displaying an overdue fine of $3.00,
    - **When** the librarian enters an authorized override reason (e.g., "Library transit delay") and submits a fee waiver,
    - **Then** the system waives the fee, logs the librarian's ID and timestamp in the audit trail, and restores the member's borrowing status to 'Active'.
  - **Scenario 2 (Audit logging verification)**:
    - **Given** an override action is performed,
    - **When** the circulation supervisor views the delinquent account audit report,
    - **Then** the audit log contains the exact date, librarian identifier, overridden fine amount, and mandatory reason string.

---

## INVEST Evaluation Matrix

| Story ID | Independent | Negotiable | Valuable | Estimable | Small | Testable | Verdict & Remediation |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **US-01** (Borrow Limit) | Yes | Yes | Yes | Yes (2 SP) | Yes | Yes | **Passes**. Focused purely on borrow transaction and quota validation. |
| **US-02** (Overdue & Suspension) | Yes | Yes | Yes | Yes (3 SP) | Yes | Yes | **Passes**. Decoupled from fine payment and renewal. |
| **US-03** (Book Renewal) | Yes | Yes | Yes | Yes (2 SP) | Yes | Yes | **Passes**. Relies on reservation status but independently testable. |
| **US-04** (Fine Settlement) | Yes | Yes | Yes | Yes (3 SP) | Yes | Yes | **Passes**. Covers reinstatement lifecycle. |
| **US-05** (Librarian Override) | Yes | Yes | Yes | Yes (3 SP) | Yes | Yes | **Passes**. Administrative capability with strict audit logging. |

---

## MoSCoW Prioritization

| Priority | Story ID | Story Title | Business & Technical Rationale |
| :--- | :--- | :--- | :--- |
| **Must Have (M)** | **US-01** | Borrow Book within Quota Limit | Core library business capability. Without checking out books and enforcing the 3-book limit, the circulation system cannot function. |
| **Must Have (M)** | **US-02** | Overdue Fine Calculation & Suspension | Critical policy enforcement mechanism to prevent inventory depletion and loss of physical books. |
| **Should Have (S)**| **US-04** | Outstanding Fine Settlement | Essential to allow suspended users to recover their active borrowing status once fines accrue. |
| **Should Have (S)**| **US-03** | Loan Renewal | Significant patron experience feature. Prevents unnecessary check-ins when no one is waiting, but can be deferred past MVP. |
| **Could Have (C)** | **US-05** | Librarian Suspension Override & Fee Waiver | High business value for customer service and error handling, but not blocker for Day-1 launch of self-service lending. |
| **Won't Have (W)** | *(Future)* | Automated SMS Reminders & Lost Book Replacement Billing | Out of scope for current sprint iteration. |
