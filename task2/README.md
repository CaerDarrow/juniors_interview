<h1 align="center">
  Animals
</h1>
<hr>

<p align="center">
  <a href="#test-assignment">Test assignment</a> •
  <a href="#tech-stack">Tech stack</a> •
  <a href="#how-to-run-tests">How to run tests</a>
</p>

## Test assignment
[test assignment](task2.md)

## Tech stack
- [Python 3.11](https://www.python.org/downloads/)


## How to run tests

1. Prepare venv (use poetry)
   - setup poetry
     ```bash
      poetry config virtualenvs.in-project true &&
      poetry shell
     ```
   - install deps
     ```bash
      poetry install
     ```

   
2. Move to working dir
   ```bash
   cd test2
   ```

3. Run script
   ```bash
   python solution.py
   ```

4. Run tests (pytest)
   ```bash
   pytest -rA -p no:warnings
   ```

<br>
<br>
<p align="center">
  <a href="https://github.com/mrKazzila">GitHub</a> •
  <a href="https://mrkazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>