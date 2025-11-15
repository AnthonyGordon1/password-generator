# Secure Password Generator

A simple, configurable Python utility for generating strong random passwords using cryptographically secure methods.  
This script is designed with security best practices in mind, ensuring safe character sets and customizable policies.

---

## Features
- Uses Python’s `secrets` module for **cryptographic randomness** (safer than `random`).
- Configurable password length (default: 15 characters).
- Customizable punctuation set (default: `!@#$%^&*`).
- Ensures high entropy and avoids unsafe punctuation that may cause parsing issues.
- Lightweight and easy to integrate into other projects or labs.

---

## Installation
Clone the repository or copy the script into your project:

```bash
git clone https://github.com/AnthonyGordon1/password-generator.git
cd password-generator
