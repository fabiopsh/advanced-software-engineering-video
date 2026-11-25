# 10 Testing.pdf

34 pagine


## Pagina 1 — 1 immagini/figure: guardare il PNG

Testing
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 1 immagini/figure: guardare il PNG

Introduction


## Pagina 3 — 1 immagini/figure: guardare il PNG

[0,2:08]
«This
was
caused
by
an
internal
variable
related
to
the
horizontal
velocity
of
the
launcher
exceeding
a
limit
which
existed in the software of this computer.»
https://www.youtube.com/watch?v=PK_yguLapgA


## Pagina 4

Testing
1) Execute your program using data that simulate user inputs
2) Observe program’s behaviour
Behaviour is 
what your 
expected?
yes
no
Test
succeeded
Test
failed


## Pagina 5

Types of testing
Functional testing
Test functionality of overall system to discover bugs
User testing
Test that product is useful to and usable by end users
Alpha testing: “Do you really want these features?”
Beta testing: Early version of product distributed to users to check product usability and effective interoperability
Performance and load testing
Test that system responds quickly to service requests
Test that system can handle different loads and scales gracefully as the load increases
Security testing
Find vulnerabilities that attackers may exploit


## Pagina 6 — 1 immagini/figure: guardare il PNG

Warning (1/2)


## Pagina 7 — 2 immagini/figure: guardare il PNG

≠
Warning (2/2)
software testing ≠ software verification


## Pagina 8 — 1 immagini/figure: guardare il PNG

Introduction
Functional testing


## Pagina 9 — 1 immagini/figure: guardare il PNG

Functional testing
Large set of program tests so that all code is executed at least once
Testing should start on the day you start writing code
Develop/test cycle simplified by automated tests
Functional testing is a staged activity


## Pagina 10

Unit testing
Test program units (e.g. function, method)  in isolation
Unit testing principle
If a program unit behaves as expected for a set of inputs that have some shared 
characteristics, it will behave in the same way for a larger set whose members share 
these characteristics.
 
Example
If your program behaves correctly on the input set {1, 5, 17, 45, 99}, you may 
conclude that it will also process all other integers in the range 1 to 99 correctly


## Pagina 11

Unit testing: Equivalence partitions
Identify “equivalence partitions”: sets of inputs that will be 
treated the same in your code 
Test your program using several inputs from each equivalence 
partition
Programmers make mistakes at boundaries: Identify partition 
boundaries and choose inputs at these boundaries


## Pagina 12 — 2 immagini/figure: guardare il PNG

Unit testing: Guidelines


## Pagina 13

Feature testing
A product feature implements some useful user functionality
Features must be tested to show that functionality 
(1) is implemented as expected and 
(2) meets the real needs of users
Feature normally implemented by multiple interacting program units
Two types of tests
(1) Interaction tests 
Testing interactions between units (developed by different developers)
Can also reveal bugs in program units that were not exposed by unit testing
(2) Usefulness tests 
Testing that feature implements what users are likely to want
Product manager should be involved in designing usefulness tests


## Pagina 14 — 2 immagini/figure: guardare il PNG

From user stories to feature tests


## Pagina 15

System testing
Testing the system as a whole
• To discover unexpected/unwanted interactions between the features 
• To discover if system features work together effectively to support what 
users really want to do
• To make sure system operates as expected in the different environments 
where it will be used
• To test responsiveness, throughput, security, and other quality attributes 
Tip: Use scenarios/user stories to identify users’ end-to-end pathways


## Pagina 16

Release testing
Testing a system that is intended for release to customers
• Release testing tests the system in its real operational environment (rather than 
in a test environment)
• The aim of is to decide if the system is good enough to release, not to detect 
bugs in the system
Needed since preparing a system for release involves packaging the system for 
deployment, installing used software and libraries, configure parameters – and 
mistakes can be made in that process
If you deploy on the cloud, an automated continuous release process can be used


## Pagina 17 — 1 immagini/figure: guardare il PNG

Introduction
Functional testing
Test automation


## Pagina 18 — 1 immagini/figure: guardare il PNG

Test automation
Automated testing widely used in product development companies
Testing frameworks available for all widely used programming languages
Executable tests check that software return expected result for input data


## Pagina 19 — 1 immagini/figure: guardare il PNG

Test automation
Good practice: Structure automated tests in three parts
1.
Arrange - Set up the system to run the test (define test parameters, mock objects if needed)
2.
Action - Call the unit that is being tested with the test parameters
3.
Assert – Assert what should hold if test executed successfully.


## Pagina 20

Test automation
Test code can include bugs!
Good practice to reduce the chances of test errors:
1. Make tests as simple as possible
2. Review all tests along with the code that they test


## Pagina 21 — 1 immagini/figure: guardare il PNG

Test automation
Unit tests are the easiest to automate
Good unit tests reduce (do not eliminate) need of feature tests
GUI-based testing expensive to automate, API-based testing preferrable 
Need multiple assertions to check that feature executed as expected
System testing involves testing system as a surrogate user
Perform sequences of user actions
Manual system testing boring and error prone
Testing tools record series of actions and automatically replay them
70%
20%
10%


## Pagina 22 — 1 immagini/figure: guardare il PNG

Introduction
Functional testing
Test automation
Test-driven development


## Pagina 23 — 1 immagini/figure: guardare il PNG

Test-driven development
“First write executable test, then write the code” [XP]
Write mini-unit tests


## Pagina 24 — 1 immagini/figure: guardare il PNG

Test-driven development
Pros
• Systematic approach: tests 
clearly linked to code sections, 
no untested sections
• Tests help understanding 
program code
• Simplified, incremental 
debugging 
• (Arguably) simpler code
Cons
• Difficult to apply TDD to system 
testing
• TDD discourages radical 
program changes
• TDD leads you to focus on the 
tests rather than on the problem 
you are trying to solve
• TDD leads you to think too much 
about implementation details 
rather than on overall program 
structure


## Pagina 25 — 1 immagini/figure: guardare il PNG

Introduction
Functional testing
Test automation
Test-driven development
Security testing


## Pagina 26

Security testing
Objectives:
• Find vulnerabilities that an attacker may exploit 
• Provide convincing evidence that system is sufficiently secure
Finding vulnerabilities harder than finding bugs
• You must test for something that software should NOT do (potentially infinite 
number of tests)
• Normal functional tests may not reveal vulnerabilities 
• The software stack (OS, libraries, DBs, …)  on which your product depends may 
contain vulnerabilities


## Pagina 27

Security testing
Comprehensive security testing requires 
specialist knowledge (e.g. involve external 
specialists for penetration testing, 
expensive)
Adopt a risk-based approach
• identify main security risks to your 
product 
• develop tests to demonstrate that the 
product protects itself from these risks
Possible to automate some of these tests, 
others inevitably require manual checking 
of behaviour/files
Examples of security risks
• Unauthorized attacker gains access to a 
system using authorized credentials
• Authorized individual accesses resources 
that are forbidden to that person
• Authentication system fails to detect 
unauthorized attacker
• Attacker gains access to database using 
SQL poisoning attack
• Improper management of HTTP sessions
• HTTP session cookies are revealed to an 
attacker
• Confidential data are unencrypted
• Encryption keys are leaked to potential 
attackers


## Pagina 28

Security testing
Mindset: when testing security, you need to think 
like an attacker rather than a normal end-user
• deliberately try to do the wrong thing 
• repeat actions several times
-> labs on security


## Pagina 29 — 1 immagini/figure: guardare il PNG

Introduction
Functional testing
Test automation
Test-driven development
Security testing
Code reviews


## Pagina 30

Limitations of testing
1. You test code against your understanding of what that code 
should do. If you have misunderstood the purpose of the 
code, then this will be reflected in both the code and the tests.
2. Testing may not provide coverage of all the code you have 
written. (TDD shifts the problem to code incompleteness).
3. Testing does not really tell you anything about other attributes 
of a program (e.g. readability, structure, evolvability).


## Pagina 31 — 1 immagini/figure: guardare il PNG

Code reviews
Code reviews complement testing


## Pagina 32

Code reviews
Often a single code reviewer is used (part of same DevOps team, or not)
Reviewer can also comment on readability and understandability of code
Review session should focus on 200-400 lines of code
Checklist often used, e.g.
Are meaningful variables and function names used? (General)
Have all data errors been considered and tests developed for these? (General)
Are all exceptions explicitly handled? (General)
Are default function parameters used? (Python)
Are types used consistently? (Python) 
Is the indentation level correct? (Python)
Reviews can be triggered by commits on shared repositories
Several code review tools available, often used together with messaging systems 
like Slack


## Pagina 33 — 1 immagini/figure: guardare il PNG

Code reviews (example)
Chapters are team members working within a special area (e.g., front office developers, back office 
developers, database admins, testers). 
A guild is a community of members across the organization with shared interests (e.g., web technology, test 
automation),  who want to share knowledge, tools code and practices. 
Chapters (sometimes guilds) do code reviews for squads. Two «+1» required to merge.


## Pagina 34 — 1 immagini/figure: guardare il PNG

Reference
Chapter 9 – Testing
