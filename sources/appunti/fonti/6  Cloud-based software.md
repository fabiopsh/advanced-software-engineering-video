# 6  Cloud-based software.pdf

46 pagine


## Pagina 1 — 1 immagini/figure: guardare il PNG

Cloud-based software
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2

Cloud computing
• Powerful computer hardware + high-speed networking have led 
to the development of cloud computing
• Virtualised resources (e.g. compute, storage, platform) 
accessible on demand
• Main advantages
• Scalability 
(maintain performance as load increases)
• Elasticity 
(adapt server configuration to changing demands)
• Resilience
(maintain service in the event of server failures)
• Cost 
(CapEx reduction, pay-per-use)


## Pagina 3 — 1 immagini/figure: guardare il PNG

Virtualization and containers


## Pagina 4 — 2 immagini/figure: guardare il PNG

From VMs to containers
• Server virtualization
• Many virtual machines (each with its OS) 
running on same physical server
• (“Type 1” hypervisor loaded directly on HW)
Server hardware
Server hardware
Container manager
Hypervisor
Key idea of containers: Exploit OS 
kernel’s capability of allowing multiple 
isolated user-space instances
+ lighter (require less resources, from Gb to Mb)
+ faster to start (from mins to secs)
- share same OS


## Pagina 5 — 1 immagini/figure: guardare il PNG

What is Docker?
Docker is a platform that allows us
to run applications in an isolated environment
Docker allows us to develop and run portable applications
by exploiting containers


## Pagina 6

How old are containers?
• For decades, UNIX chroot command provided a simple form of filesystem isolation
• 1998 – FreeBSD jail utility extended chroot sandboxing to processes
• 2005 – Google started developing CGroups for Linux kernel and began moving its 
infrastructure to containers
• 2008 – Linux Containers (LXC) provided a complete containerization solution
2013 - Docker added the missing pieces - portable images and friendly UI – to the containerization puzzle, and 
containers entered the mainstream
The Docker platform consisted of:
• Docker Engine (for creating and running containers)
• Docker Hub  (for distributing containers)


## Pagina 7 — 1 immagini/figure: guardare il PNG

Docker
• Docker exploits container-based virtualization to 
run multiple isolated guest instances on the 
(same) OS
• Software components are packaged into images, 
which are exploited as read-only templates to 
create and run containers
• External volumes can be mounted to ensure data 
persistence


## Pagina 8 — 5 immagini/figure: guardare il PNG

“Build, ship, and run any app, anywhere”


## Pagina 9 — 2 immagini/figure: guardare il PNG

Docker images
• (read-only) templates used to create containers
• stored in a (private or public) Docker registry
- registry structured in repositories
- each repository contains a set of images, for different
versions of a software
- images identified by pairs repository:tag
- Docker Hub 
• images structured into (read-only) layers
• each layer is in turn an image, lowest layer called base image
• running container can write in new top layer, changes can be committed into new image
Debian
Java
Dropwizard
Container


## Pagina 10 — 7 immagini/figure: guardare il PNG

Docker commands
image
container
registry
push
pull
run
commit
build
Dockerfile


## Pagina 11 — 1 immagini/figure: guardare il PNG

Learn Docker in 12 min
https://www.youtube.com/watch?v=YFl2mCHdv24
[1:57 -12:00]


## Pagina 12 — 3 immagini/figure: guardare il PNG

Demo
install Docker
simple php “hello world” app
index.php
Dockerfile
find php image from Docker Hub
>docker build –t hello-world .
>docker run –p 80:80 hello-world
use a volume to share folder between host and container
use one process per container


## Pagina 13 — 2 immagini/figure: guardare il PNG

How can we manage applications consisting 
of multiple (micro)services with Docker?


## Pagina 14 — 6 immagini/figure: guardare il PNG

product/api.py
product/Dockerfile
docker-compose.yml
//product service
>docker-compose up
//service composition
>docker build …
>docker run …


## Pagina 15 — 6 immagini/figure: guardare il PNG

docker-compose.yml
>docker-compose up
//service composition
website/index.php
//website
//compose creates virtual network, we can 
//directly use service name (product-service)
write Dockerfile …


## Pagina 16 — 3 immagini/figure: guardare il PNG

Docker Compose in 12 min
https://www.youtube.com/watch?v=Qw9zlE3t8Ko


## Pagina 17 — 1 immagini/figure: guardare il PNG

Virtualization and containers
Everything as a service


## Pagina 18 — 6 immagini/figure: guardare il PNG

Pizza as a Service


## Pagina 19 — 1 immagini/figure: guardare il PNG

*aaS
•
IaaS provides (virtualized) servers, storage, networking
•
IaaS provider manages all infrastructure
•
Client responsible for all other aspects of the deployment (e.g., OS, app)
•
Example: EC2, S3
•
SaaS provides software on-demand for use, accessible via thin clients or APIs
•
SaaS provider manages infrastructure + OS + app
•
Client responsible for nothing
•
Example: salesforce.com
•
PaaS provides whole platform as a service (VMs,  OS, services, SDKs,…)
•
PaaS provider manages infrastructure + OS + enabling SW 
•
Client responsible for installing and managing app
•
Examples:  Heroku, Azure, GAE
+ FaaS …


## Pagina 20 — 1 immagini/figure: guardare il PNG

Virtualization and containers
Everything as a service
SaaS


## Pagina 21

SaaS
Software products were initially installed on customers’ 
computers
• Customers had to configure software 
• Customers had to deal with software updates
• Software product company had to maintain different product versions
SaaS
• Product delivered as a service
• Customers do not have to install software
• They pay a subscription and access product from remote


## Pagina 22

Benefits of SaaS for product providers
Cash flow
Regular cash flow: Customers pay periodic subscription or pay-per-usage
Update management
You control product updates, customers receive update at same time
No need of simulateneously maintaining several versions
Reduced costs
Continuous deployment
You can deploy new software versions as soon as changes have been made and tested
Payment flexibility
Different payment options can attract wider range of customers 
e.g. small companies or individuals can avoid paying large upfront software costs
Try before you buy
You can make early free/low-cost product available and get customer feedback
Data collection 
You can easily collect data on product usage and customers


## Pagina 23

Pros & cons for customers
• Mobile, laptop, and desktop access
• No upfront costs for software or servers
• Immediate software updates
• Reduced software management costs
• Privacy regulation conformance
e.g. EU countries have strict laws on storage of personal info
• Security concerns
Customers may not want to pass data control to external provider
• Network constraints 
Can limit response time when much data transfer
• Data exchange
Can be difficult if cloud does not provide suitable API
• Loss of control over updates
• Service lock-in


## Pagina 24

Design issues for SaaS
Local vs. remote processing
Some features can be executed locally 
+ reduced network traffic 
+ increased response speed
-  increased power consumption for battery-powered devices
Authentication
Product own authentication system vs. 
 
Federated authentication vs.
 
      Individual Google/LinkedIn/… credentials
Information leakage
Security risks with multiple users from multiple organizations
Multi-tenant vs. multi-instance database management
Single repository vs. separate copies of system and database


## Pagina 25 — 1 immagini/figure: guardare il PNG

Virtualization and containers
Everything as a service
SaaS
Multi-tenant and multi-instance systems


## Pagina 26

Multi-tenant vs. Multi-instance 
systems


## Pagina 27 — 2 immagini/figure: guardare il PNG

Multi-tenant systems
• Single database schema shared by all 
system’s users
• Items in database tagged with tenant 
identifier to provide “logical isolation”


## Pagina 28 — 1 immagini/figure: guardare il PNG

Multi-tenant systems
Mid-size and large businesses 
rarely want to use generic multi-tenant software
often prefer a customized version adapted to their own requirements


## Pagina 29 — 1 immagini/figure: guardare il PNG

Multi-tenant systems: UI configurability
UI configurability can be implemented 
by employing user profiles 
• Users asked to select their organization 
or provide their business email address
• Product uses profile information to 
create personalized version of interface
• e.g. generic company name and logo replace 
with company’s ones
• e.g. some features of menus disabled


## Pagina 30 — 1 immagini/figure: guardare il PNG

Multi-tenant systems: DB schema adaptation
Corporate users may wish to extend or adapt DB schema
to meet their specific business needs
Solution I: Add a number of extra 
fields to each table and allow 
customers to use these fields as they 
wish
• Issues:
• Difficult to know how many extra 
columns to include (too few will be 
insufficient, too many will lead to 
wasted space)
• Different customers are likely to need 
different types of columns


## Pagina 31 — 1 immagini/figure: guardare il PNG

Multi-tenant systems: DB schema adaptation
Corporate users may wish to extend or adapt DB schema
to meet their specific business needs
Solution II: Add a field to each 
table that identifies a separate 
“extension table” and allow 
customers to create these extension 
tables to reflect their needs.
e.g. The extension fields for tenant T516/ Item 
100 are ‘Location’, ‘Weight’ and ‘Fragile’, with 
values ‘A17/S6’, ‘4’, and ‘False’
e.g. The extension fields for T632/Item 100 are 
‘Delivered’ and ‘Place’, and their values are 
‘2017/1/15’ and ‘Dublin’
Issue: added complexity


## Pagina 32

Multi-tenant systems: Security issues
Security is the major concern of corporate customers with multi-tenant databases
• As information from all customers is stored in the same database, a software bug or an 
attack could lead to the data of some or all customers being exposed to others
Multilevel access control 
• access to data must be controlled at both the organizational level and the 
individual level
• organizational level access control to ensure that any database operations act on only that 
organization’s data
• individual users accessing the data should also have their own access permissions 
Encryption of data 
• To ensure corporate users that their data cannot be viewed by people from other 
companies if some kind of system failure occurs
• Encrypted data can be decrypted only when accessed with the appropriate key
• Encryption/decryption are computationally intensive operations → usually only 
sensitive data are encrypted


## Pagina 33

Multi-tenant vs. Multi-instance 
systems


## Pagina 34

Multi-instance systems
Each customer has its own system that is adapted to its needs, 
including its own database and security controls
• conceptually simpler than multi-tenant systems
• avoids security concerns such as inter-organization data leakage


## Pagina 35

Multi-instance systems
Two types of multi-instance systems:
• VM-based
• software instance and database for each customer run in its own VM 
• all users from same customer may access the shared system database
• Container-based
• each user has an isolated version of software and database running in a 
set of containers
• most suited to products in which users mostly work independently, with 
little data sharing (e.g. for individual users)
It is also possible to run containers on a virtual machine
a business could have its own VM-based system and run containers on top of this for individual users


## Pagina 36 — 1 immagini/figure: guardare il PNG

Pros and cons of multi-instance databases


## Pagina 37 — 1 immagini/figure: guardare il PNG

Virtualization and containers
Everything as a service
SaaS
Multi-tenant and multi-instance systems
Cloud software architecture


## Pagina 38 — 1 immagini/figure: guardare il PNG

Architectural decisions


## Pagina 39 — 1 immagini/figure: guardare il PNG

DB organization
There are three possible ways 
of providing a customer 
database in a cloud-based 
system:
1.
As a multi-tenant system, shared by 
all customers for your product. This 
may be hosted in the cloud using 
large, powerful servers.
2.
As a multi-instance system, with 
each customer database running on 
its own virtual machine.
3.
As a multi-instance system, with 
each database running in its own 
container. The customer database 
may be distributed over several 
containers.


## Pagina 40

DB organization
Different types of customers have different expectations about 
software products
Examples:
• Consumers or small businesses do not expect branding and personalization, local 
authentication system, or varying individual permissions → You can use a multi-tenant 
database with a single schema
• Large companies are more likely to want a database adapted to their needs → Possible to 
some extent with a multi-tenant system, easier with a multi-instance database
• For products in which database has to consistent at all times (e.g. finance) → You need a 
transaction-based system: either a multi-tenant database or a database per customer 
running on a virtual machine (with all users from each customer sharing the VM-based 
database)


## Pagina 41

Scalability
• Scalability = ability to adapt automatically to load changes 
• Achieved by
• By adding new virtual servers (scaling out)
• Or by increasing the power of a system server (scaling up) 
in response to increasing load
• Scaling out typical of cloud-based systems
• Product must be organized so that individual software 
components can be replicated and run in parallel
• Load-balancing mechanisms direct requests to different 
instances of the components (e.g. with PaaS)


## Pagina 42 — 1 immagini/figure: guardare il PNG

Resilience
Resilience = ability to continue to deliver critical services in the 
event of system failure or malicious system use 
“Hot standby” 
• Replicas of software and data maintained in 
different locations
• Database updates are mirrored
• System monitor continuously checks system 
status
Cheaper alternative: “cool stanby”
• data restored from backup
• system unavailable till data restore is complete


## Pagina 43

Software structure
+ independent services that can be replicated, 
distributed, and migrated
+ particularly suitable for cloud-based software 
with services deployed in containers
Monolith   vs.   Fine-grain, stateless services
Monolithic approach often employed to build prototype 
When different parts have to be updated at different times and 
when only some parts have to scale → microservices


## Pagina 44 — 1 immagini/figure: guardare il PNG

Cloud platform
Both technical and business issues
e.g. EU countries have strict requirements on data 
protection and on where data are stored → need cloud 
provider providing guarantees on storage locations


## Pagina 45 — 1 immagini/figure: guardare il PNG

Cloud platform
Both technical and business issues
Make an “exit plan” to mitigate vendor lock-in
Trade-off between direct and indirect costs 
(e.g. cloud management)
May need to interoperate with other 
software used by your customers
Some companies prefer to deal with 
trusted providers
“Guaranteed” QoS?


## Pagina 46 — 1 immagini/figure: guardare il PNG

Reference
Chapter 5 – Cloud-based software
