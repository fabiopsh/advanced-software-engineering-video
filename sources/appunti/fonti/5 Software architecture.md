# 5 Software architecture.pdf

31 pagine


## Pagina 1 — 1 immagini/figure: guardare il PNG

Software architecture
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 1 immagini/figure: guardare il PNG

Software architecture
To create good products we need to pay attention to its overall 
organization 
Software architecture affects performance, usability, security, 
reliability, maintainability, …


## Pagina 3 — 1 immagini/figure: guardare il PNG

Component
Element implementing a coherent set of features
Collection of services that may be used by other components


## Pagina 4 — 6 immagini/figure: guardare il PNG

Architectural design issues


## Pagina 5 — 1 immagini/figure: guardare il PNG

Non-functional quality attributes


## Pagina 6 — 1 immagini/figure: guardare il PNG

Non-functional quality attributes
(Important for final product - not for prototype)


## Pagina 7 — 1 immagini/figure: guardare il PNG

Warning
Optimizing one non-functional attribute affects others
security
performance
usability
availability
time–to-market
simplicity


## Pagina 8 — 1 immagini/figure: guardare il PNG

Non-functional quality attributes
System decomposition


## Pagina 9 — 1 immagini/figure: guardare il PNG

Services, components, modules
Service       = coherent unit of functionality
Component = software unit offering one or more services
Module       = set of components


## Pagina 10 — 1 immagini/figure: guardare il PNG

Warning
Simplicity is essential 
(Agile manifesto)
As the number of components increases, the number of 
relationships tends to increase at a faster rate


## Pagina 11 — 1 immagini/figure: guardare il PNG

Control complexity


## Pagina 12 — 1 immagini/figure: guardare il PNG

Layered architectures
• Each layer is an area of concern 
and is considered separately from 
other layers
• Within each layer, the 
components are independent and 
do not overlap in functionality 
• The architectural model is a high-
level model that does not include 
implementation information 
(Concerns may not be always 
100% separated in practice)


## Pagina 13 — 2 immagini/figure: guardare il PNG

Cross-cutting concerns
• Systemic concerns affecting whole 
system
• Every layer must take them into account 
• Cross-cutting concerns add interactions 
between the layers


## Pagina 14 — 1 immagini/figure: guardare il PNG

Generic layers for web-based app
Software architect customises this by deciding whether she needs less/more layers


## Pagina 15

Warning
System decomposition must be done (partly) in conjunction with 
choosing technologies for your system 
e.g. choice of using relational database affects components at higher layers 
e.g. choice of supporting interfaces on mobile devices calls for using corresponding UI 
development toolkits


## Pagina 16 — 1 immagini/figure: guardare il PNG

Non-functional quality attributes
System decomposition
Distribution architecture


## Pagina 17

Distribution architecture
Define servers and allocation of components to servers


## Pagina 18 — 1 immagini/figure: guardare il PNG

Client-server architecture
Suited to applications in which clients access a shared database 
and business logic operations on those data
Several servers (e.g. Web servers, db servers), load balanced


## Pagina 19 — 1 immagini/figure: guardare il PNG

Client-server architecture
Model-View-Controller pattern 
• Architectural pattern for client-
server interaction
• Model decoupled from its 
presentation
• Each view registers with model 
so that if model changes all 
views can be updated


## Pagina 20 — 2 immagini/figure: guardare il PNG

MVC tutorial
https://www.youtube.com/watch?v=p6TIUgZHAT4


## Pagina 21 — 2 immagini/figure: guardare il PNG

Client-server architecture
Client-server communication usually with HTTP and XML/JSON
Multi-tier client-server architecture
Service-oriented architecture


## Pagina 22

Choosing distribution architecture
Data type and data updates
If you are mostly using structured data that may be updated by different system features, it 
is usually best to have a single shared database that provides locking and transaction 
management.  If data is distributed across services, you need a way to keep it consistent and 
this adds overhead to your system.
Change frequency
If you anticipate that system components will be regularly changed or replaced, then isolating 
these components as separate services simplifies those changes.
The system execution platform
If you plan to run your system on the cloud with users accessing it over the Internet, it is 
usually best to implement it as a service-oriented architecture because scaling the system is 
simpler. 
If your product is a business system that runs on local servers, a multi-tier architecture may 
be more appropriate.


## Pagina 23 — 1 immagini/figure: guardare il PNG

Non-functional quality attributes
System decomposition
Distribution architecture
Technology issues


## Pagina 24 — 1 immagini/figure: guardare il PNG

Technologies choices
Affect and constrain overall system architecture
Difficult/expensive to change them during development


## Pagina 25

Database
Relational databases
• e.g. MySQL 
• data is organised into 
structured tables
• particularly suitable when 
• you need transaction 
management and
• data structures are predictable 
and simple
NoSQL databases
• e.g. MongoDB 
• data has a more flexible, 
user-defined organization
• more flexible and efficient 
for data analysis
• data can be organized 
hierarchically, efficient 
concurrent processing of 
‘big data’ possible


## Pagina 26 — 2 immagini/figure: guardare il PNG

Why NoSQL databases
https://www.youtube.com/watch?v=0X43QfCfyk0


## Pagina 27

Delivery platform
• Delivery can be as a web-based or a mobile product 
• Mobile issues
•
Intermittent connectivity 
•
Processor power
•
Power management  
•
Reduced screen size and on-screen keyboard 
•
Different decomposition architectures for the web-based and mobile 
versions (e.g. to ensure that performance is maintained) 
 
→ Decide early whether to focus on mobile or desktop version of product


## Pagina 28 — 1 immagini/figure: guardare il PNG

Server
• To run on customer servers or to run on the cloud? 
• For consumer products: SOA+cloud
• For business products, there may be
• Concerns on cloud security issues
• Less need to cope with spikes in demand
• If you develop for the cloud, next decision is to choose provider
• Not easy to move product across cloud providers
vendor lock-in


## Pagina 29

Development technology
• Development technologies (e.g. mobile development toolkit, 
web application framework) influence the architecture of your 
product 
• e.g. many web development frameworks assume use of model-view-controller 
architectural pattern
• The development technology that you use may indirectly 
influence the architecture of your product
• e.g. if your team is used to relational databases then …


## Pagina 30 — 2 immagini/figure: guardare il PNG

Non-functional quality attributes
System decomposition
Distribution architecture
Technology issues


## Pagina 31 — 1 immagini/figure: guardare il PNG

Reference
Chapter 4 – Software architecture
