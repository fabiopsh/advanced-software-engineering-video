# 8 Architectural smells and refactorings for microservices.pdf

37 pagine


## Pagina 1

Architectural smells and 
refactoring for microservices
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 4 immagini/figure: guardare il PNG

Microservices
develop applications as sets of small scale, stateless services:
each running in its own container
communicating with lightweight mechanisms
built around business capabilities
decentralizing data management
independently deployable
horizontally scalable
fault resilient
+ employ a DevOps approach


## Pagina 3 — 1 immagini/figure: guardare il PNG

Ok, got it
Now, does my app respect the "microservices principles"?
And, if not, how can I refactor it?


## Pagina 4 — 1 immagini/figure: guardare il PNG

Principles, smells and refactorings


## Pagina 5 — 1 immagini/figure: guardare il PNG

How can architectural smells affecting 
design principles of microservices be 
detected, and then resolved via 
refactoring?


## Pagina 6 — 1 immagini/figure: guardare il PNG

“An architectural smell is a commonly used 
architectural decision that negatively impacts 
system lifecycle qualities.”


## Pagina 7

A multivocal review
Review of white and grey literature (41 references) aimed at
identifying 
• the most recognised architectural smells for microservices, and 
• the architectural refactorings to resolve them
principle
smell
smell
refactoring
refactoring
refactoring


## Pagina 8 — 1 immagini/figure: guardare il PNG

Design principles
Independent deployability
The microservices forming an application should be independently deployable
Horizontal scalability
The microservices forming an application should be horizontally scalable
Isolation of failures
Failures should be isolated
Decentralization
Decentralisation should occur in all aspects of microservice-based applications, 
from data management to governance
→possibility of adding/removing replicas of single microservices


## Pagina 9 — 1 immagini/figure: guardare il PNG

architectural 
smells
principles


## Pagina 10 — 2 immagini/figure: guardare il PNG

independent deployability
multiple services 
in one container
package each service in
a separate container


## Pagina 11 — 1 immagini/figure: guardare il PNG

invocation to specific
instance
horizontal scalability
endpoint-based
service interaction
add service discovery
add message router
add message broker
55%
31% (e.g. load balancer)
14% (e.g. message queue)


## Pagina 12 — 1 immagini/figure: guardare il PNG

App clients invoke directly app services 
(similar to endpoint-based service interaction smell)
(Adding API gateway can be useful also for authentication, throttling, …)
horizontal scalability
no API gateway
add API gateway


## Pagina 13 — 2 immagini/figure: guardare il PNG

add message broker
isolation of failures
wobbly service interaction
add circuit breaker
The interaction of m1 with m2 is wobbly
when a failure of m2 can trigger a failure of m1
use timeouts
add bulkhead
16%
42%
22%
20%


## Pagina 14 — 2 immagini/figure: guardare il PNG

Multiple services access same DB
decentralisation
shared persistence
split database
add data manager
merge services
50%
41%
9%
Why “evil”?
•
Different services managed by different teams, teams must work independently
•
Services must be developed, deployed and scaled independently


## Pagina 15

s1
s2
db
shared persistence
s1
s2
db'
db"
split database
- db splitted
- small changes to s1,s2
- not always possible/easy to implement
- eventual data consistency for replicated data
add data manger
- dm added
- very small changes to s1,s2
- added communication overhead
s1
s2
db
dm
s1+2
db
merge services
- s1 and s2 merged into single service
- not always easy/reasonable to implement


## Pagina 16 — 2 immagini/figure: guardare il PNG

decentralisation
single-layer teams
split teams by service


## Pagina 17

horizontal scalability
no API gateway
endpoint-based
service interaction
add API gateway
add service discovery
add message router
add message broker
isolation of failures
wobbly service interaction
add circuit breaker
use timeouts
decentralisation
shared persistence
split database
add data manager
merge services
independent deployability
multiple services 
in one container
package each service in
a separate container
add bulkhead
ESB misuse
rightsize ESB
single-layer teams
split teams by service


## Pagina 18 — 1 immagini/figure: guardare il PNG

Principles, smells and refactorings
MicroFreshener


## Pagina 19 — 1 immagini/figure: guardare il PNG

MicroFreshener
A tool for
• editing app specifications
• automatically identifying architectural smells
• applying architectural refactorings to resolve the identified smells


## Pagina 20

horizontal scalability
no API gateway
endpoint-based
service interaction
add API gateway
add service discovery
add message router
add message broker
isolation of failures
wobbly service interaction
add circuit breaker
use timeouts
decentralisation
shared persistence
split database
add data manager
merge services
add bulkhead
Excerpted taxononomy


## Pagina 21 — 5 immagini/figure: guardare il PNG

Modelling application architecture
Graphical representation
service
data store
message broker
message router
edge
d
Example
c
circuit breaker
t
timeout
dynamic discovery


## Pagina 22 — 2 immagini/figure: guardare il PNG

endpoint-based service interaction


## Pagina 23 — 2 immagini/figure: guardare il PNG

wobbly service interaction


## Pagina 24 — 2 immagini/figure: guardare il PNG

shared persistence


## Pagina 25 — 4 immagini/figure: guardare il PNG

MicroFreshener
• (freely) usable to analyse & refactor microservice-based apps
• industrial case study
• controlled experiment 
100% vs. 49% smells identified
83% vs. 1% participants resolved all smells
•
4 no API gateway smells 
•
1 shared persistence smell
•
2 API gateways added
•
1 data manager added


## Pagina 26 — 1 immagini/figure: guardare il PNG

Principles, smells and refactorings
MicroFreshener
Remarks


## Pagina 27 — 3 immagini/figure: guardare il PNG

«Let it be» refactoring supported


## Pagina 28

Architecture level ≠Implementation level
Concrete implementation of refactoring left to application manager 
(much like in design patterns)
Applying a refactoring in MicroFreshener does not change the 
implementation of the application


## Pagina 29 — 4 immagini/figure: guardare il PNG

Example
d  c t
d  c t
s1
s1
add timeouts in s1
//implementation level


## Pagina 30 — 5 immagini/figure: guardare il PNG

Example (cont.)
d  c t
d  c  t
or
s1
s1
add new component
modify s1
//implementation level


## Pagina 31 — 6 immagini/figure: guardare il PNG

Scalability: team-based views


## Pagina 32 — 2 immagini/figure: guardare il PNG

Example
d  c t
d  c  t
vs.
s1
s1
s1
s1
s2
s2
s2
s2


## Pagina 33 — 2 immagini/figure: guardare il PNG

Container orchestration does change application behaviour


## Pagina 34 — 3 immagini/figure: guardare il PNG

MicroFreshener
app
e.g. setting ingress node in Kubernetes 
adds API gateway to application
manifest
manifest
e.g. adding a sidecar container 
to introduce a circuit breaker
e.g. setting networking policies 
to introduce bulkheads


## Pagina 35 — 1 immagini/figure: guardare il PNG

Principles, smells and refactorings
MicroFreshener
Remarks
A toolchain for microservices


## Pagina 36 — 8 immagini/figure: guardare il PNG

TosKeriser
MicroFreshener
TosKose
app
MicroMiner
automated completion of app spec by 
discovering and including the needed
Docker-based runtime environments
automated deployment on top of 
existing container orchestrators
MicroTOM
static analysis of K8s 
manifest + dynamic
mining of running app
static analysis of K8s manifest
and Kiali graph


## Pagina 37 — 1 immagini/figure: guardare il PNG

Reference
•
J. Soldani, G. Muntoni, D. Neri, A. Brogi. The μTOSCA toolchain: Mining, analyzing, and refactoring microservice-based
architectures. Software: Practice and Experience, 51(7):1591–1621, 2. 2021.
•
A. Brogi, D. Neri, L. Rinaldi, J. Soldani. Orchestrating incomplete TOSCA applications with Docker. Science of Computer
Programming, 166:194–213. 2018.
•
M. Bogo, J. Soldani, D. Neri, A. Brogi. Component-aware Orchestration of Cloud-based Enterprise Applications, from
TOSCA to Docker and Kubernetes. Software: Practice and Experience, 50:1793–1821. 2020
•
Jacopo Soldani, Javad Khalili, and Antonio Brogi. Offline Mining of Microservice-Based Architectures. SN Computer
Science, 4, 2023.
https://github.com/di-unipi-socc/
D. Neri, J. Soldani, O. Zimmermann, A. Brogi. Design principles, architectural smells
and refactorings for microservices: A multivocal review. SICS Software-Intensive
Cyber-Physical Systems, 35:3–15. 2020.
(Other references)
