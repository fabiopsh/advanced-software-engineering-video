# 12 DevOps.pdf

51 pagine


## Pagina 1 — 1 immagini/figure: guardare il PNG

DevOps
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 1 immagini/figure: guardare il PNG

DevOps?


## Pagina 3 — 2 immagini/figure: guardare il PNG

https://www.youtube.com/watch?v=_I94-tJlovg


## Pagina 4 — 3 immagini/figure: guardare il PNG

-slow response to business needs
-weeks to deploy into production env
-new code needs to be massaged to fit into production env
-deployments need to be scheduled
New mindset, new tools
• Source control (e.g. GitHub)
• Build & test code continuously (e.g. Jenkins, Travis)
• Configuration management (e.g. Puppet, Chef, SaltStack, Ansible)
• App performance monitoring (e.g. NewRelic, Pingdom Server Monitor)
Integrate dev&ops teams to improve collaboration 
and productivity
+automate code testing, workflows, infrastructure
+continuosly measuring app performance
+development env = production env
+more frequent releases
+faster response to business needs


## Pagina 5 — 1 immagini/figure: guardare il PNG

Development | Deployment | Support
Separate teams responsible for 
software development, release, and 
support 
• development team passes “final” version of software 
to release team
• release team builds release version, tests it, 
prepares releases documentation, and releases 
software to customers
• support team provides customer support
Development team (or separate 
maintenance team) responsible for 
implementing software changes


## Pagina 6

Development | Deployment | Support
Issues
• Communication delays between teams
• Separate teams use different tools, have different skills, often don’t 
understand the other’s problems
• Days needed to fix urgent bugs or security vulnerabilities


## Pagina 7 — 3 immagini/figure: guardare il PNG




## Pagina 8 — 1 immagini/figure: guardare il PNG

DevOps approach
Three factors enabling a change:
1.
Agile software engineering reduced software development time → traditional 
release process became a bottleneck 
2.
Amazon re-engineered its software into (micro)services, assigning both service 
development and service support to same team
3.
SaaS release of software became possible on public/private clouds
DevOps (Development + Operations) integrates 
development + deployment + support 
in a single team


## Pagina 9

DevOps principles
Everyone is responsible for everything
All team members have joint responsibility for developing, delivering, 
and supporting the software
Everything that can be automated should be automated
All/most activities involved in testing, deployment, and support should 
be automated
Measure first, change later
DevOps should be driven by measuring collected data about the system 
and its operation


## Pagina 10

DevOps benefits
Faster deployment
Dramatic reduction of human communication delays → faster deployment 
to production
Reduced risk
Small functionality increment in each release → less chance of feature 
interactions and system failures/outages
Faster repair
No need to discover which team is responsible for fixing problem and to 
wait for them to fix it
More productive teams
DevOps teams more productive than teams involved in separate activities


## Pagina 11

DevOps culture
Creating a DevOps team means bringing together a number of 
different skill sets, including
• software engineering
• UX design
• security engineering
• infrastructure engineering
• customer interaction
Successful DevOps team
• culture of mutual respect and sharing
• developers should support the software services that they have 
developed


## Pagina 12 — 1 immagini/figure: guardare il PNG

DevOps?
Code management


## Pagina 13 — 2 immagini/figure: guardare il PNG

Code management
Objective
• Manage the evolving codebase: store and retrieve 
versions of components and entire systems
• Let developers work in parallel without interfering, 
and integrate their work
Main features
• Code transfer to/from the developer’s file store
• Version storage and retrieval (files are never 
overwritten)
• Branching and merging for concurrent work
• Version information and change history
• Project support: all files of a project can be checked 
out together
Why it matters
• Basis for DevOps automation (CI/CD, infrastructure 
as code) and for measurement
(10.1 of textbook)


## Pagina 14 — 1 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation


## Pagina 15

“Everything that can be should be automated” 
Continuous integration 
Each time a developer commits a change to the project’s master branch, an 
executable version of the system is built and tested.
Continuous delivery 
Executable software is tested in a simulated product’s operating environment. 
Continuous deployment 
New release of system made available to users every time a change is made to the 
master branch of the software.
Infrastructure as code
Machine-readable models of infrastructure (network, servers, routers, etc.) on which 
the product executes are used by configuration management tools to build the 
software’s execution platform. The software to be installed, such as compilers and 
libraries and a DBMS, are included in the infrastructure model.


## Pagina 16 — 1 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation
Continuous integration


## Pagina 17

Continuous Integration
System integration (system building) is more than compiling:
• install db software and set up db with appropriate schema
• load test data into db
• compile the files that make up the product
• link compiled code with libraries and other components used
• check that external services used are operational
• move configuration files to correct locations (and delete old ones)
• run system tests to check that integration has been successful
If a system is infrequently integrated, problems can be difficult 
to isolate, and fixing them slows down system development → 
continuous integration should be used


## Pagina 18 — 1 immagini/figure: guardare il PNG

Continuous Integration
An integrated version of the system is created and tested every 
time a change is pushed to the system’s shared code repository
On completion of the push operation, repository sends message 
to integration server to build a new version of the product


## Pagina 19 — 2 immagini/figure: guardare il PNG

Don’t “break the build”


## Pagina 20 — 2 immagini/figure: guardare il PNG

Don’t “break the build”
Adopt an “integrate twice” approach to system integration
1- integrate and test on your own computer 
2- push code to project repository to trigger integration server


## Pagina 21

Advantage of Continuous Integration
It is faster to find and fix bugs in the system
If you make a small change and some system test fails, the problem almost certainly 
lies in the new code that you pushed 
A working system is always available to the whole team
It can be used to test ideas and to demo system to management and customers
“Quality culture” in development team
No team members wants the stigma of breaking the build
Everybody checks her work carefully before pushing it to project repo


## Pagina 22 — 2 immagini/figure: guardare il PNG

Incremental build process
Code integration tools only repeat actions if dependent files have 
been changed
Example
• At first integration, all source code files and executable test files 
are compiled
• Subsequently, object code files are created only for modified 
tests and for modified source code files
Example (modification timestamps)
• date(compiled code) > date(source code) → do nothing
• date(compiled code) < date(source code) → recompile
• date(compiled code) < date(class definition) → recompile


## Pagina 23

Tools
System building tools
Unix make (oldest)
Ant, Maven (Java)
Rake (Ruby)
…
Continuous integration tools 
Jenkins (open-source)
Travis, Bamboo 
GitHub actions
…


## Pagina 24 — 1 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation
Continuous integration
Continuous delivery and deployment


## Pagina 25

Continuous delivery
Continuous Integration creates an executable version of a software 
system by building system and running tests on your computer or 
project integration server
Real production environment will differ from development 
environment
• production server may have different filesystem organization, access 
permissions, installed applications
• new bugs may show up
Continuous delivery ensures that changed system is ready for delivery 
to customers
• feature tests in production environment to make sure that environment does 
not cause system failures
• load tests to check how software behaves as number of users increases
Containers are the simplest way to create a replica of a production 
environment


## Pagina 26 — 1 immagini/figure: guardare il PNG

Continuous delivery and deployment
To deliver
• after initial integration testing, 
configure staged test environment 
(replica of production environment)
• run system acceptance tests 
(functionality, load, performance)
To deploy
• software and data are transferred to 
production servers
• new service requests stopped, older 
version processes outstanding 
transactions
• switch to new system version and 
restart processing


## Pagina 27

Benefits of continuous deployment
Reduced costs
Fully automated deployment pipeline
Faster problem solving
If a problem occurs, it will probably affect only a small part of the 
system and the source of that problem will be obvious
Faster customer feedback
You can deploy new features when they are ready for customer use
Users’ feedback can be used to to identify improvements 
A/B testing
If you have many customers and several servers
• deploy new software version only on some servers 
• use load balancer to divert some customers to the new version
• measure and assess how new features are used
(Continuous deployment only practical for cloud-based systems)


## Pagina 28

Why not deploying every single change?
Business reasons not to deploy every software change to 
customers:
1. You have incomplete features that could be deployed, do not want to 
disclose this to competitors until implementation is complete
2. Customers may be irritated by continually changing software, especially 
if this affects UI 
3. You may wish to synchronize your releases with known business cycles
e.g. start of academic year for education market


## Pagina 29

Tools
CI tools such as Jenkins and Travis may also be used to support 
continuous delivery and deployment. 
These tools can integrate with infrastructure configuration 
management tools such as Chef and Puppet and Ansible to 
implement software deployment. 
For cloud-based software, it is often simpler to use containers in 
conjunction with CI tools rather than use infrastructure 
configuration management software.


## Pagina 30 — 1 immagini/figure: guardare il PNG

CI&CD: Jenkins
https://www.youtube.com/watch?v=k_fVlU1FwP4


## Pagina 31 — 1 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation
Continuous integration
Continuous delivery and deployment
Infrastructure as Code


## Pagina 32

Motivation
Manually maintaining a computing infrastructure with tens or 
hundreds of servers is expensive and error-prone
• many different physical/virtual servers that have different 
configurations and run different software packages
• when new versions of software become available, some servers may 
have to be updated, others may not because of dependencies with 
older versions of software
• difficult to manually keep track of software installed on each server 
(e.g. emergency changes are not always documented)


## Pagina 33 — 1 immagini/figure: guardare il PNG

IaC
• Automate the process of updating software 
on servers, by using a machine readable 
model of the infrastructure
• Configuration Management (CM) tools, like 
Puppet and Chef and Ansible, can 
automatically install software and services 
on servers according to the infrastructure 
definition
• When changes have to be made, 
infrastructure model is updated and CM 
tool makes the changes to all servers


## Pagina 34

Advantages of IaC
Visibility
Infrastructure defined as stand-alone model that can be 
read/understood/reviewed by whole DevOps team.
Reproducibility 
Installation tasks will always be performed in the same sequence, same 
environment will be always created. You do not have to rely on people 
remembering the order that they need to do things.
Reliability
Automation avoids simple mistakes made by system administrators when 
making same changes to several servers. 
Recovery
Infrastructure model can be versioned and stored in a code management 
system. If infrastructure changes cause problems, you can easily revert 
to older version and reinstall the environment that you know works.


## Pagina 35 — 1 immagini/figure: guardare il PNG

IaC: Puppet
https://www.youtube.com/watch?v=QFcqvBk1gNA


## Pagina 36 — 2 immagini/figure: guardare il PNG

Puppet: case study
• New York Stock Exchange (NYSE)
• World’s largest stock exchange by market capitalization
• NYSE part of Intercontinental Exchange (ICE)
• Challenge 
• Needed to scale up workloads and infrastructure efficiently and cost-effectively
• Provisioning was too slow and held up developers’ work
• ICE was mostly satisfied with open source Puppet, but relied on some 
workarounds
• Solution
• Expand Puppet Enterprise (PE) use from NYSE to other ICE systems
• Results
• 75% of ICE’s 20,000 servers managed by Puppet Enterprise
• Increase from 300 servers per admin to 700 servers per admin
• Provisioning dev environments reduced from 1-2 days to 21 minutes
• No workarounds needed: Puppet Enterprise “just works”
•
“We don’t troubleshoot systems anymore. If a server is flaky or slow, we just rebuild it. 
Whatever machine gets pulled out and replaced at night, we’re confident it will be identical 
to the others in the farm, and will perform as expected, because there’s no manual touch.”


## Pagina 37 — 2 immagini/figure: guardare il PNG

Chef
https://www.youtube.com/watch?v=_pUdL4w9E7k


## Pagina 38

Containers
Containers are a very effective way to deploy cloud-based 
products
• Simple to provide identical execution environments
• for each type of server you use, you define the environment you need and build an 
image for execution
• when you update your software, you create new image that includes the modified 
software
• You can employ a container management system, such as Kubernetes, 
for scaling/resiliency …


## Pagina 39 — 1 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation
Continuous integration
Continuous delivery and deployment
Infrastructure as Code
DevOps measurement


## Pagina 40

DevOps measurement
You should try to continuously improve your DevOps process to 
achieve faster deployment of better quality software 
→
Need to measure and analyse product and process data 
• Process measurements 
to collect & analyze data on development/testing/deployment processes
• Service measurements 
to collect & analyze data on software’s performance/reliability/acceptability to customers
• Usage measurements 
to collect & analyze data on how customers use your product
(help you identify issues and problems with the software itself)
• Business success measurements 
to collect & analyze data on how your product contributes to overall business success
(hard to isolate contribution of DevOps to business success - that may be due e.g. to DevOps 
introduction or to better managers)


## Pagina 41

DevOps measurement
Measuring software and its development is a complex process 
• need to identify suitable metrics that give you useful insights 
• need to find reliable ways of collecting and analyzing metrics data
• some measures (e.g. customer satisfaction) must be inferred from other 
metrics (e.g. number of returning customers) 
Software measurement should be automated as far as possible
• instrument your software to collect data about itself 
• use monitoring system to collect data about software’s performance and 
availability
Process measurement is not simple
• different people record information differently
• e.g. to record lead time for implementing a change
• Is the “lead time” the overall elapsed time or the time spent by developers?
• How to take into account higher priority changes whose implementation slowed down 
other changes?


## Pagina 42 — 2 immagini/figure: guardare il PNG

DevOps measurement
Example: Measuring the achievement of the goal of shipping 
cloud-based code frequently without causing customer outages
Metrics
Weekly presentation of results 
of analyses of collected data 
and trends


## Pagina 43

DevOps measurement
To collect data
• you may use continuous integration tools like Jenkins to collect data 
on deployments, successful tests, etc.
• you may use monitoring services featured by cloud providers like 
Amazon’s Cloudwatch to collect data on availability and performance
• you may collect customer-supplied data from issue management 
systems
• you may add instrumentation to your product to gather data on its 
performance and how it is used by customers
• use log files, where log entries are timestamped events reflecting customer actions and/or 
software responses
• log as many events as possible
• use available log analysis tools to extract useful information about on how your software is 
used


## Pagina 44 — 1 immagini/figure: guardare il PNG

APM: New Relic AI
https://www.youtube.com/watch?v=7vBhF4Ph_LA


## Pagina 45 — 2 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation
Continuous integration
Continuous delivery and deployment
Infrastructure as Code
DevOps measurement
Spotify engineering culture


## Pagina 46 — 1 immagini/figure: guardare il PNG

Spotify engineering culture
https://www.youtube.com/watch?v=v6gQuVCHJ1Q


## Pagina 47 — 12 immagini/figure: guardare il PNG

47
[Part I]
•
Agile principles

Loosely coupled, tightly aligned squads

Cros- pollination

Internal open-source model for code

Frequent releases, enabled by decoupling
•
Focus on people: motivation, community, trust
• Fail fast → learn fast → improve fast

Spotify is a fail-friendly environment

Fail walls, post-mortems, retrospectives

Failure recovery (rather than failure avoidance)

Limited blast radius via decoupled architecture
and gradual rollout
• Product development approach

Lean startup principles (think|build|ship|tweak )

Impact > Velocity

Innovation > Predictability

Value delivery > Plan fullfillment
• 10% hack time
• Experiment-friendly culture
• Waste-repellent culture

«if it works, keep it, otherwise dump
it»

Minimize need of big projects

Minimal bureaucracy to avoid chaos

Improvement boards, Toyota 
improvement «kata»
• «Health culture heals broken
process»

Culture-focused roles (agile coaches)

Boot camps

Story telling


## Pagina 48 — 1 immagini/figure: guardare il PNG

Q: «squads»?
A: Agile team organization …
A squad has a dedicated Product Owner who feeds user stories to build. Squads have all the skills and tools 
needed to design, develop, test and release to production, being an autonomous, self-organising team, 
experts in their product area. 
Chapters are team members working within a special area (e.g., front office developers, back office 
developers, database admins, testers). Chapter members exchange ideas to promote innovation and 
‘cross pollination’ across teams. 
A tribe is a collection of squads within the same business area (e.g., mobile). The squads within a tribe sit in 
the same area. Spotify implements shared lounges to create inter-squad interaction, and regular informal 
team events and get together where squads share what they are working on. Tribe Leader is responsible 
for providing the right environment for all the squads.
A guild is a community of members across the organization with shared interests (e.g., web technology, test 
automation),  who want to share knowledge, tools code and practices.


## Pagina 49 — 1 immagini/figure: guardare il PNG

Q: How is code reviewing performed at Spotify?
A: Chapters (sometimes guilds) do code reviews for squads. 
Two «+1» required to merge.


## Pagina 50 — 2 immagini/figure: guardare il PNG

DevOps?
Code management
DevOps automation
Continuous integration
Continuous delivery and deployment
Infrastructure as code
DevOps measurement
Spotify engineering culture


## Pagina 51 — 1 immagini/figure: guardare il PNG

Reference
Chapter 10 – DevOps and Code Management
