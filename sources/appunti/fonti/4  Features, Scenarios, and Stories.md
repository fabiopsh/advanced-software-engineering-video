# 4  Features, Scenarios, and Stories.pdf

36 pagine


## Pagina 1 — 1 immagini/figure: guardare il PNG

Features, scenarios, and 
stories
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 2 immagini/figure: guardare il PNG

Introduction
Factors driving the design of software products
• Inspiration
• Business/consumer needs not met by existing products
• Dissatisfaction with existing products
• Technical changes making new product types possible


## Pagina 3 — 5 immagini/figure: guardare il PNG

Requirements documentation
Ma´anaatik kat´ann
(We don’t understand your language)
¿Donde estamos?
(Where are we?)


## Pagina 4

Introduction
Product-based software engineering needs less requirements 
documentation that project-based software engineering
• Requirements not set by customers
• Requirements change
Identify product features (= fragments of functionality) instead
• Need to understand potential users
• Interviews/surveys
• Informal user analysis/consultations
• Warning: e.g. business managers buy product, employees (may not 
want to) use it


## Pagina 5 — 1 immagini/figure: guardare il PNG

Introduction
User 
representations 
(personas) 
and 
natural 
language 
descriptions (scenarios and stories) help identifying product 
features


## Pagina 6 — 1 immagini/figure: guardare il PNG

Personas


## Pagina 7

Personas
Who are the target users for our product?
• Need to understand potential users to design features useful for them
• Background, skills and experience of potential users are important
Personas are (imagined) types of product users
• e.g. for a dentist agenda: dentist, receptionist, patient
• Generally we need a few (1-2, max 5) personas to identify key product 
features


## Pagina 8 — 5 immagini/figure: guardare il PNG

Aspects of persona descriptions


## Pagina 9 — 3 immagini/figure: guardare il PNG

Using photos in persona descriptions?
It is sometimes helpful to use an appropriate stock photograph 
to represent the person in the persona. Some studies suggest 
that this helps project teams use personas more effectively.
Using photos is misleading. Personas shouldn’t be about how people look, but what they do. (Steve Cable)
Detailed personas encouraged the team to assume that demographic information drove motivations. (Sara Wachter-Boettcher)
Persona profiles with a smiling photo result in an increase in 
willingness to use the personas. (Joni Salminen et al.)
Gender has a mediating influence on perceived attributes 
of males and females. (Francine M. Deutsch)


## Pagina 10 — 1 immagini/figure: guardare il PNG

Example of persona
→Doesn’t have technical background
→Wants product supporting administration
Personalization
Job-related
Education
Relevance


## Pagina 11 — 2 immagini/figure: guardare il PNG

Personas allow developers 
to “step into the users’shoes”
When studying the users is not 
possible (e.g. for some new products) 
we can develop proto-personas


## Pagina 12 — 1 immagini/figure: guardare il PNG

Personas
Scenarios


## Pagina 13

Scenarios
To discover product features, we can define scenarios of user 
interactions with the product
Scenario = narrative describing a situation in which a user is 
using our product’s features to do something she wants to do


## Pagina 14 — 2 immagini/figure: guardare il PNG

Scenarios


## Pagina 15

Scenarios
Narrative, high-level scenarios facilitate communication and 
stimulate design creativity
Scenarios are not specifications, though (they lack detail and 
may be incomplete)


## Pagina 16

Writing scenarios
Several scenarios (e.g. 3-4) for each persona, covering main 
responsabilities of persona
Written from user’s perspective
Each team member should (individually) create some scenarios, 
and then discuss them with rest of team and with users (if 
possible)


## Pagina 17 — 1 immagini/figure: guardare il PNG

Personas
Scenarios
User stories


## Pagina 18 — 1 immagini/figure: guardare il PNG

User stories
Scenarios = high-level stories of product use
User stories = finer-grained narratives
As a           <role> 
I want to  <do something> 
So that     <reason/values>


## Pagina 19 — 2 immagini/figure: guardare il PNG

Agile user stories
ProNetLicensing.co
Player


## Pagina 20 — 1 immagini/figure: guardare il PNG

1.
Our highest priority is to satisfy the customer through early and continuous delivery of 
valuable software.
7. Working software is the primary measure of progress.
10. Simplicity--the art of maximizing the amount of work not done--is essential.
• organize and chunk work into units that represent value to the customer
▪
distinguish more valuable from less important
▪
visualize units of work, through simple stories
-
template: As a (who) + I want to (what) + So I can (why)
▪
stories written from the user’s viewpoint
▪
good quality stories make rest of development process more efficient
▪
good user stories create business value for the users
• build software from the users perspective


## Pagina 21 — 3 immagini/figure: guardare il PNG

Splitting user stories
ProNetLicensing.co
Player


## Pagina 22 — 1 immagini/figure: guardare il PNG

• Think about application the way the user thinks about it
• Developers tend to see the application as a stack
• User thinks of an application in terms of valuable «slices of functionality»
• Build software incrementally, as slices of functionality
• A good story should take 1-2 days of work
• Split long stories into several shorter stories, which can be prioritized
• Example of how to split stories
3.
Deliver working software frequently, from a couple of weeks to a couple of months, 
with a preference to the shorter timescale.
10. Simplicity--the art of maximizing the amount of work not done--is essential.


## Pagina 23 — 1 immagini/figure: guardare il PNG

User stories for planning
• Scrum product backlog is often a set of user stories
• Long stories (epics) to be broken into simpler stories
• Stories are associated with priorities (and possibly
also with an estimate of effort needed to implement
the story) and sorted according to priority
(«requirements triage»)


## Pagina 24 — 1 immagini/figure: guardare il PNG

Stories and scenarios
It is possible to express all the functionalities described in a 
scenario as user stories
… so why bothering with scenarios?
Scenarios
+ read more naturally
+ make it easier to understand stories
+ provide more context


## Pagina 25 — 1 immagini/figure: guardare il PNG

Stories and scenarios
On the other hand, we can “jump” directly from Personas to 
Stories (and skip Scenarios)


## Pagina 26 — 1 immagini/figure: guardare il PNG

Example: Tic Tac Toe
Rules
• A grid of 3x3 squares
• Two players (X and O)
• Players take turns putting their marks in empty squares
• First player to get 3 of her marks in a row/column/diagonal wins
• When all 9 squares are full, the game is over


## Pagina 27

Persona: Player
Pierfrancesco, age 9, is an elementary school student in 
Pisa. He lives with his parents and an older sister. 
Together, he enjoys going to the beach, playing video 
games (if his parents allow it), and playing football. 
Often, the entire family visits the grandparents who live 
in Firenze. On the long train ride to Firenze, he likes to 
play board games with his father and sometimes his 
sister. Once he grows up, he wants to become a police 
officer or firefighter.
He grew up with computers and smartphones and knows 
how to use them, but he obviously is not interested into 
diving deeper into the technology. In the end, for him, 
using technology is about having fun, not learning. Board 
games are great fun for him, but it would be even cooler 
if those games were usable on his phone or PC.
(Generated by last year class)


## Pagina 28

User stories
As a
Player
I want to
have a timer
So that
the game is even shorter
As a
Player
I want to
select my next valid move
So that
I can play the game
As a
Player
I want to
select my symbol
So that
I can customise my games
As a
Player
I want to
play against the computer
So that
I can (learn how to) play alone
As a
Player
I want to
know when I win/fail/tie
So that
I can celebrate, be sad, or play again
As a
Player
I want to
ask for a rematch
So that
I can eventually win
As a
Player
I want to
surrender
So that
I can stop suffering from losing
As a
Player
I want to
See an update board
So that
I can decide on my next move
As a
Player
I want to
See whose turn it is
So that
I know if I should play a move
As a
Player
I want to
See the winning combo
So that
I can better see it
As a
Player
I want to
Start a new game
So that
I can play with others on same device
(Generated by last year class)


## Pagina 29 — 1 immagini/figure: guardare il PNG

Personas
Scenarios
User stories
Feature identification


## Pagina 30

Feature identification
Aim: Getting a list of features that define our product
Properties 
• Independence - A feature should not depend on how other system 
features are implemented and should not be affected by the order of 
activation of other features.
• Coherence - Features should be linked to a single item of functionality. 
They should not do more than one thing, and they should never have 
side effects.
• Relevance - System features should reflect the way users normally 
carry out a task. They should not offer obscure functionality that is 
rarely required.


## Pagina 31 — 1 immagini/figure: guardare il PNG

Knowledge sources for feature design
You can use user scenarios and user stories to inform the team of 
what users want and how they might use the software features.
You may have experience of 
existing products or decide to 
research what these products 
do as part of your development 
process. Sometimes your 
features have to replicate 
existing features in these 
products because they provide 
fundamental functionality that 
is always required.
This is knowledge of the domain or work area (e.g., finance, event booking) that your 
product aims to support. By understanding the domain, you can think of new 
innovative ways of helping users do what they want to do.
New products often emerge to 
take advantage of technological 
developments since their 
competitors were launched. If you 
understand the latest technology, 
you can design features to make 
use of it.


## Pagina 32 — 1 immagini/figure: guardare il PNG

Factors in feature set design


## Pagina 33 — 1 immagini/figure: guardare il PNG

Feature creep
Number of product features grows as new potential users are 
envisaged
• Marketing executives want to meet all users’ demands
• Marketing pressure to include competitors’features
• Desire to support both experienced and inexperienced users


## Pagina 34 — 1 immagini/figure: guardare il PNG

Avoiding feature creep


## Pagina 35 — 1 immagini/figure: guardare il PNG

Feature derivation
Product development team must meet to discuss scenarios and 
stories to extract the list of product feature descriptions
Start prototyping to demonstrate (first novel and critical) features


## Pagina 36 — 1 immagini/figure: guardare il PNG

Reference
Chapter 3 – Features, Scenarios, and Stories
