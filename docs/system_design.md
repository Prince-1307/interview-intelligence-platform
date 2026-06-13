# Interview Intelligence Platform

## User Flow

Home Page
↓
Upload Resume
↓
Paste Job Description
    ↓
Generate Questions
    ↓
Answer Questions
    ↓
AI Evaluation
    ↓
Feedback Report
    ↓
Dashboard

---

## Database Design

### Candidates

- id
- name
- email
- created_at

### Interview Sessions

- id
- candidate_id
- job_title
- created_at
- overall_score

### Questions

- id
- session_id
- question
- question_type

### Answers

- id
- question_id
- candidate_answer
- score
- feedback

---

## Feature Roadmap

### Phase 1
- Flask Setup
- Landing Page

### Phase 2
- Resume Upload

### Phase 3
- Resume Parsing

### Phase 4
- Job Description Input

### Phase 5
- Question Generation

### Phase 6
- Answer Evaluation

### Phase 7
- Feedback Engine

### Phase 8
- Dashboard