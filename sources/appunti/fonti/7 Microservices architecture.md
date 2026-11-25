# 7 Microservices architecture.pdf

44 pagine


## Pagina 1 — 1 immagini/figure: guardare il PNG

Microservices architecture
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 1 immagini/figure: guardare il PNG

Introduction


## Pagina 3

Introduction
How to decompose a system into components?
• Components can be developed in parallel by different teams
• Components can be reused, replaced, distributed across multiple computers 
• Components must be easily replicated, run in parallel, and migrated to exploit cloud-
based scalability, reliability, and elasticity
→ use stateless services that maintain persistent information 
    in local db


## Pagina 4

Introduction (cont.)
Software service
• Software component that can be accessed over the Internet
• Given an input, a service produces a corresponding output, without 
side effects
• Service is accessed through its published interface, all implementation 
details are hidden 
• Services do not maintain any internal state
• State information is either stored in a database or maintained by the service requestor
• State information can be included in service request, updated state info in service result
• Services can be dynamically reallocated from one virtual server to another → scalability


## Pagina 5

Introduction (cont.)
Service-oriented architecture (SOA, late 1990s)
• Independent, stand-alone services, with public interfaces, implemented with 
different technologies
Web Services (early 2000s)
• XML, SOAP, WSDL … plus dozens (!) of other standards
• Web services exchanging large and complex XML data → message management 
overhead
Modern service-oriented systems
• simpler, light weight service interaction protocols 
• simpler interfaces, more efficient format for encoding message data
• lower overheads, faster execution


## Pagina 6

Introduction (cont.)
Amazon’s rethinking of what a service should be 
• a service should be related to a single business function
• services should be completely independent, with their own database
• service should manage their own user interface
• it should be possible to replace/replicate a service without changing other services
→ microservices = 
    small-scale stateless services that have a single responsibility


## Pagina 7 — 1 immagini/figure: guardare il PNG

Example
System using an authentication module providing:
• user registration
• authentication using UID/password
• two-factor authentication 
• user information management
• password reset
To identify the microservices that might be 
used for the authentication system
• break coarse-grain features into more detailed functions
• look at the data used and identify a microservice for each 
logical data item to be managed
• minimize amount of replicated data management


## Pagina 8 — 1 immagini/figure: guardare il PNG

Introduction
Microservices


## Pagina 9 — 1 immagini/figure: guardare il PNG

Microservices
Microservices 
• small-scale services that can be combined to create applications
• independent (service interface not affected by changes to other services)
• possible to modify and re-deploy service without changing/stopping other services


## Pagina 10 — 2 immagini/figure: guardare il PNG

Microservices
Coupling measures number of inter-component relationships
Low coupling  → independent services, independent updates
Cohesion measures number of intra-component relationships 
High cohesion → less inter-service communication overhead
“Single responsibility principle”
• Each service should do one thing only and it should do it well
How big should a microservice be?  “Rule of twos”
• Service can be developed, tested, and deployed by a team in two weeks
• Team can be fed with two large pizzas (8-10 people)


## Pagina 11 — 3 immagini/figure: guardare il PNG

Why so many people for a microservice?
• To implement service functionality
• To develop code that makes service completely independent 
• processing incoming and outgoing messages
• manage failures (service/interaction failures)
• manage data consistency when data are used by other services
• maintain service own interface
• Test service and service interactions
• Support service after deployment


## Pagina 12 — 1 immagini/figure: guardare il PNG

Introduction
Microservices
Microservices architecture


## Pagina 13 — 4 immagini/figure: guardare il PNG

Motivations
(1) Shorten lead time for new features and updates

accelerate rebuild and redeployment
(2) Scale, effectively
Each microservice can be deployed in a separate container 
→quick stop/restart without affecting other services
→service replicas can be quickly deployed


## Pagina 14 — 1 immagini/figure: guardare il PNG

Examples
(1) Shorten lead time for new features and updates
(2) Scale, effectively
Uber
2014: single Python monolith
2053: 5,000+ microservices 
Spotify


## Pagina 15 — 2 immagini/figure: guardare il PNG

Example
Photo-printing system 
for mobile devices
Separate services for each area of functionality
API gateway 
•
insulates user app from the system’s microservices
•
single point of contact 
•
translates app service requests into calls to microservices


## Pagina 16 — 2 immagini/figure: guardare il PNG

?


## Pagina 17 — 1 immagini/figure: guardare il PNG

Architectural design decisions
Development teams for each service are autonomous
How to decompose system into a set of microservices?
-
Not too many (low cohesion -> communication overhead)
-
Not too few (high coupling -> less independency for updates/deployment/..)
Difficult
Some tips
1. Balance fine-grain functionality and system performance
2. Follow the “common closure principle” 
 (elements likely to be changed at the same time should stay in same service)
3. Associate services with business capabilities 
4. Services should have access only to the data they need  
 (+ data propagation mechanisms)
Starting points (tips)
-
Start by looking at the data services have to manage
-
Start with a monolith, and decompose it later


## Pagina 18 — 2 immagini/figure: guardare il PNG

Service communications
Synchronous vs. asynchronous service interaction
+ easier to write and undestand
+ looser coupling, more efficient 
-  more difficult to write and understand


## Pagina 19 — 2 immagini/figure: guardare il PNG

Service communications
Direct vs. indirect service communication
Messages addressed to service name 
Messages sent to message broker, which 
 
finds address of requested service
 
can handle message translation
Example of message broker: RabbitMQ
Messages directly sent to service address
+ Simpler
+ Faster 
- Requester must know recipient’s URI
+ Can support synchronous & asynchr. interactions
+ Easier to modify/replace services
- More complex
- Slower


## Pagina 20 — 1 immagini/figure: guardare il PNG

Data distribution and sharing
Each microservice should manage its own data
To deal with data dependencies:
1.
Data sharing should be as little as possible
2.
Most sharing should be read-only, with few services responsible for data updates
3.
Include a mechanism to keep db copies used by replicated services consistent


## Pagina 21

Data distribution and sharing
Shared database architectures employ ACID transactions to serialize updates and 
avoid inconsistency
In distributed systems we must trade-off data consistency and performance
→ 
Microservices systems must be designed to tolerate some degree of data 
inconsistency
Two types of inconsistency have to be managed:
1.
Dependent data inconsistency 
Actions/failures of one service can cause data managed by another service to become 
inconsistent
2.  Replica inconsistency 
Several replicas of the same service may be executing concurrently
Each with its own db copy, each updates its own db copy
→ Need to make these dbs “eventually consistent”


## Pagina 22 — 2 immagini/figure: guardare il PNG

CAP theorem
Brewer’s conjecture (PDOC 2000): 
It is impossible for a software service to provide Consistency, 
Availability and Partition-tolerance at the same time
where

Consistency: each service returns the «right» response to each request

Availability: each request must result in a response

Partition-tolerance: network can delay/lose arbitrarily many messages among nodes
¬ (C ∧ A ∧ P)
≡ 
 
 
[P=true in distributed systems]
     ¬ (C ∧ A)
≡ 
 
 
[De Morgan]
     ¬ C ∨ ¬ A
≡ 
 
 
[De Morgan]
     A ➞ ¬ C
≡ 
 
 
[De Morgan]
     C ➞ ¬ A


## Pagina 23

A   ➞   ¬ C
write(d,v1)
ok
update(d,v1)
ok
read(d)
d=v1
S1
S2
C
C’
write(d,v1)
ok
write(d,v2)
ok
update(d,v1)
ok
update(d,v2)
read(d)
d=v1
S1
S2
C
C’
X
≡
(for S2)


## Pagina 24 — 1 immagini/figure: guardare il PNG

CAP theorem
Practical implications:
Solution 1 (A ∧ P): Guarantee availability, and provide best-effort consistency
Most used in microservices, if strong consistency is not a must
Possibly trading off, e.g. tolerate one hour out of date but not one day out of date
Solution 2 (C ∧ P): Guarantee strong consistency, and provide best-effort 
availability


## Pagina 25 — 3 immagini/figure: guardare il PNG

The Saga pattern
Example
Implement each business transaction that spans multiple services as a saga
A saga is a sequence of local transactions
Each local transaction updates a database and triggers next local transaction(s) in the saga 
If a local transaction fails then the saga executes a series of compensating transactions
Two ways of coordinating sagas:
Choreography - each local transaction publishes event that triggers next local transaction(s)
Orchestration - an orchestrator tells participants which local transactions to execute
Compensating transactions:
•
Backward model - undo changes made by previously executed local transactions
•
Forward model – “retry later”


## Pagina 26 — 1 immagini/figure: guardare il PNG

Netflix approach
To replicate data in n nodes:
• «write to the ones you can get to, then fix it up afterwards»
• use quorum: e.g. (n/2 + 1) of the replicas must respond


## Pagina 27 — 4 immagini/figure: guardare il PNG

Service coordination
Orchestration
vs.
Choreography


## Pagina 28 — 1 immagini/figure: guardare il PNG

Service coordination
Publish&subscribe mechanisms
+ no explicit controller
-  harder debugging
-  harder recovery
Tip: start with orchestration, switch to choreography only if product inflexible/hard to update
Explicit controller orchestrating


## Pagina 29 — 1 immagini/figure: guardare il PNG

Failure management
Something will go wrong, unavoidably
→ Services must be designed to cope with failures
Example
A service offers a functionality F by invoking two other services, 
each available 99% of time and independent one another.
F will probably be NOT available for around ___ each day
3 seconds
30 seconds
3 minutes
30 minutes
X


## Pagina 30 — 1 immagini/figure: guardare il PNG

Failure management


## Pagina 31 — 1 immagini/figure: guardare il PNG

A service client invokes a remote service via a circuit breaker object that 
functions in a similar fashion to an electrical circuit breaker. 
When the number of consecutive failures crosses a threshold, the circuit breaker 
trips, and for the duration of a timeout period all attempts to invoke the remote 
service will fail immediately. 
After the timeout expires the circuit breaker allows a limited number of test 
requests to pass through. If those requests succeed the circuit breaker resumes 
normal operation. Otherwise, the timeout period begins again.
Failure management
Example: Circuit breaker


## Pagina 32 — 3 immagini/figure: guardare il PNG

Application should tolerate failures
Failure management
I’m Good


## Pagina 33 — 1 immagini/figure: guardare il PNG

Chaos Monkey randomly terminates VM instances and 
containers that run inside your production environment
Test (bravely)
Failure management


## Pagina 34 — 1 immagini/figure: guardare il PNG

Introduction
Microservices
Microservices architecture
Service deployment


## Pagina 35

DevOps approach
Same team responsible for service 
development, deployment and managements
Dev
Ops
DevOps


## Pagina 36 — 1 immagini/figure: guardare il PNG

Continuous Deployment pipeline


## Pagina 37 — 1 immagini/figure: guardare il PNG

Monitoring
Testing cannot prevent 100% of unanticipated problems
→
Need to monitor the deployed services


## Pagina 38 — 1 immagini/figure: guardare il PNG

Monitoring
If a service fails, you can roll back to previous version
When you introduce a new version of a service, you maintain the old version but 
change the “current version link” to point at the new service.
If monitor detects a problem with new version of “Cameras 002” service, it switches 
the “current version link” back to version 001 of the Cameras service.
Example


## Pagina 39 — 1 immagini/figure: guardare il PNG

Introduction
Microservices
Microservices architecture
Service deployment
Concluding remarks


## Pagina 40

Concluding remarks
• Many pros of microservices, including
• shorter lead time
• effective scaling
• Cons
• communication overhead
• complexity
• “wrong cuts”
• “avoiding data duplication as much as possible while keeping microservices in isolation
is one of the biggest challenges”
• “A poor team will always create a poor system”


## Pagina 41 — 1 immagini/figure: guardare il PNG

Concluding remarks


## Pagina 42 — 1 immagini/figure: guardare il PNG

Concluding remarks
Don't even consider microservices unless you have a 
system that's too complex to manage as a monolith
[M. Fowler]


## Pagina 43 — 13 immagini/figure: guardare il PNG

…
Can I play with 
microservices?
e.g. 
Uber:    208  million users (June 2026)
Netflix: 325+ million users (December 2025)
Spotify: 777  million users (June 2026)


## Pagina 44 — 1 immagini/figure: guardare il PNG

Reference
Chapter 6 – Microservices Architecture
