# Experiment 8: AI-Based Conversion of Requirements into User Stories

## Aim
To convert a given Software Requirement Specification (SRS) excerpt into user stories and acceptance criteria using an AI tool (GitHub Copilot / Windsurf / Ollama / Claude), and to evaluate their completeness and quality using the INVEST framework and MoSCoW prioritization.

## Course Outcome(s) Mapped
- **CO4**: Apply modern software engineering tools, AI assistants, and automated documentation generators to streamline software maintenance, specification, and testing workflows.

## Tools / Software Required
- **AI Tool**: GitHub Copilot Chat / Windsurf / Claude / Ollama (free, offline alternative).
- **Documentation Platform**: Markdown editor / VS Code.

---

## Pre-Lab Theory
In Agile software development frameworks (Scrum, Kanban, XP), requirements are articulated not as exhaustive waterfall documents, but as **User Stories**. 
1. **User Story Format**:
   $$\text{"As a [role], I want [feature], so that [benefit]"}$$
   - **Role**: Identifies the user persona performing the action.
   - **Feature**: Describes the capability or behavior desired.
   - **Benefit**: Captures the underlying business value or user motivation.
2. **Acceptance Criteria (Given-When-Then / Gherkin format)**:
   - **Given**: The pre-condition or starting context.
   - **When**: The action or event triggered by the user or system.
   - **Then**: The observable outcome, state transformation, or system reaction.
3. **The INVEST Quality Checklist** (Bill Wake):
   - **I - Independent**: Stories should not depend tightly on other stories to be developed and tested.
   - **N - Negotiable**: Stories capture intent, leaving architectural implementation details open to team discussion.
   - **V - Valuable**: Delivers demonstrable value to an end user or stakeholder.
   - **E - Estimable**: Sufficiently clear that developers can gauge technical effort/story points.
   - **S - Small**: Scoped small enough to be completed within a single sprint iteration.
   - **T - Testable**: Unambiguous criteria enabling automated or manual QA pass/fail verification.
4. **MoSCoW Prioritization Technique**:
   - **Must Have (M)**: Vital requirements without which the product cannot operate.
   - **Should Have (S)**: High-priority features that are important but not strictly day-1 blockers.
   - **Could Have (C)**: Desirable enhancements implemented if time and budget permit.
   - **Won't Have (W)**: Features explicitly agreed to be deferred to future releases.

---

## Input SRS Requirement Excerpt
```text
"A registered library member can borrow up to a maximum of 3 physical books at any given time for an allowable lending period of 14 days per book. If a borrowed book is not returned within 14 days, the system marks the book as overdue, levies an automated daily overdue fine of $1.00 per late day, and automatically suspends the member's borrowing and renewal privileges until all overdue books are checked in and outstanding fines are cleared. A member can view their active borrowings, search catalog availability, and request a 7-day renewal for an active loan provided the book has not been reserved by another patron and no outstanding penalties exist on the member's account. Library Staff (Librarians) have authorization to process check-ins and check-outs, manually override account suspensions under administrative discretion, issue fee waivers, and view delinquent account audit reports."
```

---

## Sample Prompt(s) for AI Tool

### Primary Prompt:
> **"Convert this requirement description into 5 user stories with acceptance criteria in Given-When-Then format, evaluate them against the INVEST checklist, and prioritize using MoSCoW: [paste SRS text]"**

### Follow-up Refinement Prompt:
> **"Review story US-02 and US-04 to ensure independence and provide explicit boundary condition scenarios (e.g., partial payment, reservation holds)."**

---

## Sample Output (Step Executed + Result Shown)

### Step 1: User Stories Generated
1. **US-01 (Book Checkout & Quota)**:
   - *Story*: As a registered library member, I want to borrow up to 3 physical books for 14 days, so that I can access study materials within borrowing limits.
2. **US-02 (Overdue Detection & Account Suspension)**:
   - *Story*: As a library management system, I want to automatically accrue daily fines of $1.00 and suspend delinquent accounts, so that borrowers return books on time.
3. **US-03 (Self-Service Book Renewal)**:
   - *Story*: As a registered library member, I want to renew my active loan for 7 additional days, so that I have more time to read when no other patrons have reserved the book.
4. **US-04 (Fine Settlement & Account Reinstatement)**:
   - *Story*: As a suspended library member, I want to pay my accrued overdue fines, so that my borrowing privileges are restored immediately.
5. **US-05 (Staff Administrative Override & Audit)**:
   - *Story*: As an authorized librarian, I want to override account suspensions and issue fee waivers with an audit note, so that special patron situations can be resolved fairly.

### Step 2: Given-When-Then Acceptance Criteria Verification
```gherkin
Feature: Book Borrowing and Overdue Management

  Scenario: Member borrows book within allowable quota
    Given a registered member has 1 active borrowed book and zero unpaid fines
    When the member requests to borrow 1 available book
    Then the system records the loan with a due date 14 days from today
    And increments the member's active loan count to 2

  Scenario: Member attempts to exceed 3-book limit
    Given a registered member currently holds 3 active borrowed books
    When the member requests to checkout another book
    Then the checkout is rejected with message "Borrowing quota exceeded"

  Scenario: Automated overdue fine calculation at midnight
    Given an unreturned book loan has exceeded 14 calendar days
    When the daily circulation batch job executes
    Then a fine of $1.00 is added to the member account for each overdue day
    And the member account status is set to "Suspended"

  Scenario: Attempting renewal when a reservation hold exists
    Given a member holds an active loan that has a reservation hold by another patron
    When the member submits a renewal request
    Then the renewal is denied with message "Cannot renew: item reserved by another patron"

  Scenario: Account reinstatement upon full fine settlement
    Given a member is suspended with $5.00 in outstanding fines and all books returned
    When the member completes a payment of $5.00
    Then the outstanding balance becomes $0.00
    And the account status transitions to "Active"
```

### Step 3: INVEST Review Matrix
- All 5 stories scored **Pass** across all 6 criteria:
  - **Independent**: Each story handles a distinct lifecycle phase (Checkout, Penalty, Renewal, Settlement, Staff Override).
  - **Negotiable**: Allows flexibility in UI design, payment gateways, and batch job scheduling.
  - **Valuable**: Directly links to student/patron satisfaction or library asset protection.
  - **Estimable**: Clear domain rules allow 2-3 story point estimation per story.
  - **Small**: Scoped narrowly enough to implement in 1 sprint iteration.
  - **Testable**: Given-When-Then scenarios provide deterministic test assertions.

### Step 4: MoSCoW Prioritization
- **Must Have**: US-01 (Borrowing within quota), US-02 (Overdue tracking & suspension).
- **Should Have**: US-04 (Fine payment & reinstatement), US-03 (7-day renewal).
- **Could Have**: US-05 (Librarian manual override & audit).
- **Won't Have**: Automated SMS notices, replacement cost billing (deferred to v2).

---

## Expected Output / Deliverable
A sprint backlog consisting of 5 user stories formulated with role, capability, and business value, complete with Gherkin Given-When-Then scenarios, INVEST quality evaluation, and MoSCoW prioritization.

## Result
Thus the experiment was executed successfully using AI-assisted tools to transform an unstructured requirements specification excerpt into Agile user stories with testable acceptance criteria, verified against the INVEST framework.

---

## Viva-Voce Questions & Detailed Answers

### 1. What is the standard format of a user story?
**Answer:**  
The standard format of a user story is:
$$\text{"As a [type of user / role], I want [action / feature / goal], so that [benefit / business value]."}$$
- **Role**: Identifies who benefits from the capability (e.g., student, admin, buyer).
- **Action**: What the user wants to accomplish in terms of software behavior.
- **Benefit**: Why the feature is needed and the quantifiable or experiential value it provides.

### 2. What does the INVEST acronym stand for in Agile user stories?
**Answer:**  
The INVEST framework (formulated by Bill Wake) defines six characteristics of a quality user story:
- **I - Independent**: Minimizes dependencies on other stories so work can be prioritized, planned, and delivered in any order.
- **N - Negotiable**: It is an invitation to conversation between developers and product owners, not a rigid contract.
- **V - Valuable**: Must provide tangible value to customers, users, or the business.
- **E - Estimable**: The scope must be understood well enough for developers to accurately estimate time or story points.
- **S - Small**: Sized to fit comfortably within a single sprint iteration (typically 1 to 3 story points).
- **T - Testable**: Contains clear acceptance criteria so QA or automated tests can verify whether it passes or fails.

### 3. What is the Given-When-Then format used for?
**Answer:**  
The Given-When-Then format originates from **Behavior-Driven Development (BDD)** (used in tools like Cucumber and Behave) to specify acceptance criteria:
- **Given**: Establishes the initial context, state of the world, or prerequisites (e.g., *Given a user is logged in with valid credentials*).
- **When**: Describes the specific action, event, or trigger (e.g., *When the user clicks the 'Logout' button*).
- **Then**: Specifies the observable outcome, side effect, or assertion (e.g., *Then the session token is invalidated and the user is redirected to the home page*).  
It bridges the communication gap between business analysts, developers, and QA engineers, serving as the blueprint for automated acceptance testing.

### 4. Why might an AI-generated user story need to be reviewed by a business analyst?
**Answer:**  
While AI tools excel at structuring syntactic stories from text, an experienced Business Analyst (BA) must review them because:
1. **Hallucinations & Speculation**: AI models may invent assumptions not present in the original SRS (e.g., assuming credit card payment or 30-day grace periods).
2. **Hidden Business Rules & Edge Cases**: AI may miss subtle regulatory, security, or legal requirements (e.g., GDPR data retention, localized tax laws, or institutional policies).
3. **Ambiguity Resolution**: Natural language requirements often contain conflicting statements that require stakeholder interviews and human negotiation to clarify.
4. **Scope Creep & Feasibility**: AI may generate stories that look plausible but are architecturally impractical, misaligned with current release milestones, or violate non-functional constraints (performance, licensing, compliance).
