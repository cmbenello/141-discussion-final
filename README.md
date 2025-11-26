

# 141 Discussion final prep

IMPORTANT DISCLAIMER
--------------------
I do not know what will be on your exam or midterm. This project was assembled quickly, and some problems may feel oddly phrased or slightly unusual. However, all solutions have been fully tested and verified. Use this as a structured practice environment, but continue to study from lecture, worksheets, discussion, and your own notes. If you find any unclear wording, inconsistent difficulty, or potential test errors, please email me so I can correct them for everyone.


This should be p similar to the midterm one BUT I have made some changes becuase I think some stuff wasn't working before so please just read over this before you start

Purpose of This Repository
--------------------------
This repository provides a complete, automated practice system designed to help you prepare for Python fundamentals at the level expected in CMSC 141. It includes:

- expressions and arithmetic
- conditionals and loops
- lists and tuples
- strings and dictionaries
- recursion on lists
- tree and trie algorithms
- scoping, copying, and mutability
- conceptual “guess the output” scenarios

Every problem has:
- an associated test in the tests/ directory
- a reference implementation in the solutions/ directory
- metadata (category, tags, difficulty) to help you focus your practice

Difficulty Scaling Note
-----------------------
Students mentioned that earlier versions of this project included problems that were too easy or did not match exam style. Based on that feedback:

- this version contains fewer total problems,
- there are no trivial warm-up questions,
- difficulty level 3 corresponds roughly to exam difficulty,
- difficulty level 4 is above exam difficulty and is intended for mastery.

If you can comfortably solve level‑4 problems, the midterm should feel manageable.

Repository Layout
-----------------
```
.
├── problems/               # All student‑implementable problem stubs
├── solutions/              # Reference implementations
├── tests/                  # Pytest suites for every problem
├── engine/                 # Assessment and practice engine
├── run_assessment.py       # Generates full or topic‑based diagnostics
├── run_practice.py         # Interactive random‑practice mode
├── run_problem.py          # Run a single problem’s tests
└── README.md
```

The engine/ directory handles problem discovery, registry building, single‑problem evaluation, assessment report generation, and interactive sessions.

How to Begin
------------

1. Run an assessment to get a baseline overview of strengths and weaknesses:

```
export USE_SOLUTIONS=0
python run_assessment.py
```

A JSON report will be saved in data/assessments/.

2. Work through the conceptual problems early. The files in problems/strings_dicts and the semantic‑trap questions in problems/extra_qs contain valuable exercises on scoping, copying, mutation, and flow of evaluation.

3. Practice topic by topic. Use pytest directly for targeted study:

```
pytest tests/test_lists_tuples.py
pytest tests/test_strings_dicts.py
pytest tests/test_recursion_lists.py
pytest tests/test_trees_tries.py
```

To test a single function:

```
pytest -q -k "lt_14_windowed_sublists"
```

Using Reference Solutions
-------------------------
To test your own implementations:

```
export USE_SOLUTIONS=0
pytest -v
```

To test using the reference solutions (to verify tests or expected behavior):

```
export USE_SOLUTIONS=1
pytest -v
```

Interactive Practice Mode
-------------------------
Launch an interactive problem session with:

```
python run_practice.py
```

Options:
- --topic basics        (restrict to a single topic)
- --min-difficulty 3    (filter by difficulty)
- --one-shot            (run exactly one random problem)

Assessment Mode
----------------
Generate a full diagnostic across all topics:

```
export USE_SOLUTIONS=1
python run_assessment.py
```

Or restrict scope:

```
python run_assessment.py --topics basics,strings_dicts --num-per-topic 2 --seed 141
```

A summary and JSON report will appear in data/assessments/.

Suggested Study Strategy
------------------------
1. Run the diagnostic.
2. Focus on difficulty‑3 problems in categories where you scored poorly.
3. Move on to difficulty‑4 problems when comfortable.
4. Re‑run tests until everything passes.
5. Compare your approaches with the reference solutions.

Transparency Note
-----------------
Some problems were written quickly and may feel unusual. Their purpose is to target conceptual weak points, not to serve as perfect exam replicas. Despite this, all solutions and tests are correct and validated. If anything appears unclear or inconsistent, reach out so it can be improved.

Contact
-------
If you have questions, find errors, want clarification on a problem, or notice inconsistencies, please email me. I want this to be as helpful and accurate as possible.

Final Message
-------------
Good luck. If you work through these problems systematically and focus on the more challenging items, you will be well‑prepared for the exam. You are absolutely capable of doing well.

— ㅊ 다녀감