name: ❓ Question
description: Ask a question about usage, setup, or behavior
title: "[Question]: "
labels:
  - "type: question"

body:
  - type: textarea
    id: question
    attributes:
      label: ❓ Your Question
      description: Ask your question clearly and concisely.
      placeholder: |
        What are you trying to understand?
        What have you already tried?
    validations:
      required: true

  - type: textarea
    id: context
    attributes:
      label: 📚 Context
      description: Provide relevant context (code snippets, commands, configs).
      placeholder: |
        Paste relevant code, logs, or configuration here.
    validations:
      required: false

  - type: dropdown
    id: topic
    attributes:
      label: 🧭 Topic
      description: What is your question related to?
      options:
        - Installation
        - Configuration
        - Usage
        - CI / GitHub Actions
        - Documentation
        - Other
    validations:
      required: true

  - type: checkboxes
    id: checklist
    attributes:
      label: ✅ Checklist
      description: Please confirm the following before submitting.
      options:
        - label: I have read the README
          required: true
        - label: I have checked existing issues
          required: true