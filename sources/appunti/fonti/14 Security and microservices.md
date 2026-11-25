# 14 Security and microservices.pdf

27 pagine


## Pagina 1

Antonio Brogi
Department of Computer Science
University of Pisa
Security and microservices


## Pagina 2 — 1 immagini/figure: guardare il PNG

Challenges of securing microservices


## Pagina 3

The broader the attack surface, the higher the risk
Monolith
• inter-component communications within single process
Microservices
•
inter-service communication via remote calls
•
(potentially) large number of entry points
→ attack surface broadens
•
security of app = strength of weakest point


## Pagina 4

Distributed security screening affects performance
Monolith
• security screening done once, request dispatched to corresponding 
component
Microservices
• Each microservice has to carry out independent security screening
•
may need to connect to a remote security token service 
•
repeated, distributed security checks affect performance
• Solutions
•
Work around: trust-the-network 
 
(and skip security checks at each microservice)
•
Industry trend: zero-trust networking principles 
 
→ overall performance must be taken into consideration


## Pagina 5 — 2 immagini/figure: guardare il PNG

Bootstrapping trust among microservices needs automation
Service-to-service communication must take place on protected channels
If you use certificates:
-
Each microservice must be provisioned with a certificate (and corresponding private key) 
to authenticate itself to another microservice during service-to-service interactions
-
Recipient microservice must know how to validate the certificate of calling microservice
-
Need a way to bootstrap trust between microservices
-
(Need also to revoke and rotate certificates)
→To manage large-scale deployments of hundreds of microservices, 
automation is needed


## Pagina 6

Tracing requests spanning multiple microservices is challenging
A log is the recording of an event of a service
Logs can be aggregated to produce metrics that reflect system state (e.g. 
average invalid access requests per hour) and that may trigger alerts
Traces help you track a request from the point where it enters the system to 
the point where it leaves the system
Unlike in monolithic applications, a request to a microservices deployment
may span multiple microservices 
→ correlating requests among microservices is challenging
Tools
-
e.g. Prometheus and Grafana to monitor incoming requests 
-
e.g. Jaeger and Zipkin for distributed tracing


## Pagina 7

Containers complicate credentials/policies handling
Containers are immutable servers, they don’t change state after spin up
great to simplify deployment and to achieve horizontal-scalability
But for each service we need to maintain a dynamic list of allowed clients and 
a dynamic set of access-control policies
e.g. get updated policies from some policy admin endpoint (with a push or pull model)
Each service must also maintain its own credentials, which need to be rotated
periodically
e.g. keep credentials in container filesystem and inject them at boot time


## Pagina 8

Distribution makes sharing user context harder
User context has to be passed explicitly from one microservice to another
Challenge: Build trust between microservices so that receiving microservice 
accepts user context passed from calling microservice
Popular solution
 
JSON Web Token (JWT) to share user context among microservices
 Idea: messages carrying user attributes in a cryptographically safe way


## Pagina 9

Security responsibilities distributed among different teams
Polyglot architecture: Different squads can use different technology stacks 
Different teams can use different security best practices, and different tools 
for static and dynamic security testing
Security responsibilities distributed across different teams
Organizations often adopt hybrid approach, with centralized security team 
and security experts in the teams


## Pagina 10 — 1 immagini/figure: guardare il PNG

Summary
Challenges of securing microservices
•
The broader the attack surface, the higher the risk
•
Distributed security screening affects performance
•
Bootstrapping trust among microservices needs automation
•
Tracing requests spanning multiple microservices is challenging
•
Containers complicate credentials/policies handling
•
Distribution makes sharing user context harder
•
Security responsibilities distributed among different teams
P. Siriwardena, N. Dias. Microservices security in action. 2020.


## Pagina 11 — 1 immagini/figure: guardare il PNG

Challenges of securing microservices
Smells and refactoring for microservices security


## Pagina 12

Multivocal review of white and grey literature 
Review of white and grey literature (58 references) to answer two research 
questions
#1 Which are the most recognised smells indicating possible security violations in 
microservice-based applications?
#2 How to refactor a microservice-based application to mitigate the effect of a security 
smell?
Result: Taxonomy with 
 
10 refactoring associated with 
 
 
10 smells potentially affecting 
 
 
 
3 security properties


## Pagina 13

Properties
Taken by ISO/IEC 25010 software quality standard
Confidentiality
degree to which a product or system ensures that data are accessible 
only to those authorized to have access
Integrity 
degree to which a system, product, or component prevents unauthorized 
modification of computer programs or data
Authenticity 
degree to which the identity of a subject or resource can be proved to be 
the one claimed


## Pagina 14

Microservice-based application does not enact access control in some microservices
→ Potential “confused deputy problem” with attacker getting data it shouldn’t be able to get
→ Potential violation of confidentiality of data (and business functions)
Client permissions need to be verified at request time
Client identity should be verified without introducing extra latency and contention with 
frequent calls to a centralized service
Most suggested refactoring: employ OAuth 2.0
- token-based security framework for delegated access control 
- resource owner can grant client access to a resource on its behalf
- access granted for limited time and with limited scope
Insufficient access control
Use Oauth 2.0
Confidentiality


## Pagina 15

Some microservices are directly accessible by external clients 
→ Each such microservice must check authentication and authorization for each request
→ Increased exposure of credentials → Increased likelihood of confidentiality violations
→ Higher cost of application maintenance
Most cited refactoring: Add API gateway
•
microservices not directly accessible by external clients
•
API gateway can enforce authentication, authorization, throttling, message content validation
•
microservices can stay behind a firewall
Publicly accessible microservices
Add API gateway
Confidentiality


## Pagina 16

Microservices are granted unnecessary access levels, permissions, or functionalities that are not 
needed to deliver their business functions
e.g. service can read/write data in db or messages in queue even if db or queue not needed by the service to 
deliver its business function
Resources are unnecessarily exposed
 
→ Increased attack surface against confidentiality and integrity properties
Most cited refactoring: Follow Least privilege principle
Unnecessary privileges
to microservices
Follow the least
privilege principle
Confidentiality
Integrity
Least Privilege Principle: Allow running code only the permissions 
needed to complete the required tasks and no more.


## Pagina 17

Use of “home-made” crypto code can cause confidentiality, integrity and authenticity issues
Can get even worse than no encryption (false sense of security)
Solution
- Exploit encryption libraries heavily tested by the community and regularly reviewed/patched
- Avoid experimental encryption algorithms (not yet known vulnerabilities) 
«Home-made» 
crypto code
Use established
encription techniques
Confidentiality
Integrity
Authenticity


## Pagina 18

Microservice-based application accidentally exposes sensitive data
 
e.g. data was stored without any encryption or employed protection has vulnerabilities/flaws
→ intruders can access/modify data, including credentials
 
→ confidentiality, integrity and authenticity can be violated 
All sensitive data should stay always encrypted, and decrypted only when needed
-
most DBMSs support automatic encryption
-
OSs support disk-level encryption 
-
application-level encryption is another option
-
cached data should be encrypted too
Encryption is resource consuming → identify critical data and encrypt only “as needed”
Non-encrypted
data exposure
Encypt all sensitive
data at rest
Confidentiality
Integrity
Authenticity


## Pagina 19

Hardcoded secrets (e.g. API keys, client secrets, credentials) contained
- in microservice source code
- in application deployment scripts (e.g. environment variables passing secrets in a Docker Compose spec)
Never store secrets in environment variables
 
 → they could be accidentally exposed (e.g. exception handlers may send info to logging platform)
 
 
→ confidentiality and integrity of secrets may get violated
Solution: Encrypt secrets
Best practices:
- Do not store credentials alongside applications or in source code repositories
- Do not employ environment variables to pass secrets
Hardcoded secrets
Encrypt secrets at rest
Confidentiality
Integrity
Authenticity


## Pagina 20

Microservices interacting without enacting a secure communication channel
 
→ data is exposed to man-in-the-middle, eavesdropping, and tampering attacks
→ potential confidentiality, integrity and authenticity issues (intruders can access alter data in transit)
Solutions
- Use mutual Transport Layer Security: widely accepted solution, encrypting data in transit and 
ensuring its integrity and confidentiality
- Mutual TLS also allows a microservice to legitimately identify the microservice it is talking to (mutual 
authentication)
Non-secured
service-to-service 
communications
Use mutual TLS
Confidentiality
Integrity
Authenticity


## Pagina 21

Unauthenticated requests (external or microservice-to-microservice) 
Crucial that microservices can authenticate one another (especially when user context is passed)
If traffic not authenticated then microservices are exposed to security attacks like tampering with data, 
denial of service, or elevation of privileges
Refactorings
- Use Mutual TLS
- Use OpenID Connect
-- uses JWT containing authenticated user info
-- microservices verify user identity with authorization server
Unauthenticated
traffic
Use mutual TLS
Authenticity
Use OpenId Connect


## Pagina 22

Application provides multiple access points to handle user authentication
→ Each access point constitutes a potential attack vector for intruder to authenticate as end user
→ Higher cost of application maintenance
Use a Single Sign-On approach
 
- single entry point to handle user authentication and to enforce security for all user requests
 
- facilitates log storage and auditing 
Single sign-on can be achieved by
- adding API gateway (if not there), and 
- employing OpenID Connect (to share user contexts)
Mutiple user 
authentication
Add API gateway
Authenticity
Use OpenId Connect
Use single sign-on


## Pagina 23

Authorization can be enforced at the edge of the application (API gateway) and/or by each microservice 
of the application.
If application only handles authorization at the edge
 
→ “central” authorization point becomes bottleneck → reduced performance and efficiency
Possibility of (another form of) “confused deputy problem“: microservices trust the gateway based on 
its mere identity -> potential violation of authenticity
Solution: enacting a decentralized authorization approach
- transmit an access token (e.g. JWT) together with each request to a microservice
- access to microservice is granted to caller only if a known and correct token is passed
Centralised
authorization
Use decentralised
authorization
Authenticity


## Pagina 24 — 1 immagini/figure: guardare il PNG

Summary
smells
refactorings
properties
F. Ponce, J. Soldani, H. Astudillo, A. Brogi. Smells and Refactorings for Microservices Security: A Multivocal Literature Review. 
The Journal of Systems and Software. 2022.
55%
43%
43%
34%
33%


## Pagina 25 — 1 immagini/figure: guardare il PNG

Challenges of securing microservices
Smells and refactoring for microservices security
How to eliminate security smells?


## Pagina 26 — 3 immagini/figure: guardare il PNG

How to eliminate security smells?
1. Detect security smells
2. Triage security smells
taking into account
▪
service relevance
▪
smell impact on quality attributes
as well as
▪
needed effort to refactor
▪
possible need to interact with other teams
3. Choose and implement a refactoring
Need of supporting tools!


## Pagina 27 — 2 immagini/figure: guardare il PNG

Challenges of securing microservices
Smells and refactoring for microservices security
How to eliminate security smells?
