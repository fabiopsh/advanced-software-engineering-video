# 9 Splitting the monolith.pdf

34 pagine


## Pagina 1

Splitting the monolith
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 4 immagini/figure: guardare il PNG

Microservices (recap)
In order to
(1) shorten lead time for new features and updates, and
(2) scale, effectively
develop applications as sets of small scale, stateless services:
each running in its own container
communicating with lightweight mechanisms
built around business capabilities
decentralizing data management
independently deployable
horizontally scalable
fault resilient
+ employ a DevOps approach


## Pagina 3 — 3 immagini/figure: guardare il PNG

The monolith grows over time
new functionalities and lines of 
code continuously added
 cohesion all sorts of unrelated 
code kept together
 loose coupling small change can 
impact rest of monolith, need to 
redeploy the big beast


## Pagina 4 — 1 immagini/figure: guardare il PNG

Split the monolith when 
it becomes a problem


## Pagina 5 — 1 immagini/figure: guardare il PNG

"Seam"-driven splitting


## Pagina 6 — 1 immagini/figure: guardare il PNG

Find the «seams»
line where two pieces of fabric are sewn together in a garment
portion of code that can be treated in isolation and worked on 
without impacting the rest of the codebase


## Pagina 7

Find the seams
Identify seams that can become service boundaries
- e.g., exploiting the notion of «bounded context» 
-
some info does not need to communicated outside, some can be shared with other contexts
-
cell analogy: membranes define what is in and out and determine what can pass 
-e.g., also exploiting namespace concepts of programming languages
-
Java’s packages


## Pagina 8 — 5 immagini/figure: guardare il PNG

Example
Online music retailer MusicCorp’ monolith covers four contexts
Catalog - Everything to do with metadata about the items offered for sale
Finance - Reporting for accounts, payments, refunds, etc.
Warehouse - Dispatching & returning of customer orders, managing inventory levels, etc.
Recommendation - Patent-pending, revolutionary recommendation system


## Pagina 9 — 3 immagini/figure: guardare il PNG

Organize code around the seams
Create packages representing these contexts, 
and then move existing code into them
Incremental refactoring and testing
Code left over may identify new bounded context
Use code to analyze dependencies between packages
- Packages representing bounded contexts in organization should interact like real organization groups
-
e.g., Warehouse package should not depend on Finance package if no such dependency in real organization 
- Tools like Structure 101 graphically show inter-package dependencies
Do the above incrementally, really


## Pagina 10 — 2 immagini/figure: guardare il PNG

Where to start breaking?


## Pagina 11 — 4 immagini/figure: guardare il PNG

Where to start breaking?
Start from where we can get the most benefit
Typical drivers
Pace of Change 
e.g., load of changes in inventory management coming, split out Warehouse seam first
Team Structure 
e.g., delivery team split across two geographical regions
Security
e.g., all sensitive information handled by Finance code, additional protection there
Technology
e.g., team working on Recommendation system experimenting new algorithms in Clojure
Tangled dependencies
Pull out the seam that is least depended on, if possible
e.g., looking at dependency graph


## Pagina 12 — 1 immagini/figure: guardare il PNG

Databases
The mother of all tangled dependenices
database
Need to find seams in our databases so that we can split them out cleanly
Databases often used to integrate multiple services


## Pagina 13 — 3 immagini/figure: guardare il PNG

Databases
Understand which parts of code read from and write to 
the database
e.g., use tools like Hybernate
Detect database-level constraints 
e.g., foreign-key relationship across tables used by different 
parts of code
e.g., use tools like SchemaSpy
Some tables may be used from different bounded 
contexts, too
Let’s see some examples of database refactoring …


## Pagina 14 — 1 immagini/figure: guardare il PNG

"Seam"-driven splitting
Database refactoring


## Pagina 15 — 1 immagini/figure: guardare il PNG

Databases example: Breaking foreign key relationships
Catalog code uses Line items table to store info on an album
Finance code uses Ledger table to track financial info
To generate monthly reports like 
“We sold 600 copies of Tones and I’s Dance monkey and made 2,000 USD”
Finance code accesses Line items table, and a foreign-key relationship from 
Ledger table to Line items table exists
How to stop Finance code accessing the Line items table?
[Ledger = book of financial accounts]


## Pagina 16 — 4 immagini/figure: guardare il PNG

Databases example: Breaking foreign key relationships
Solution: Expose data via API in the Catalog package
overhead introduced (yes)
foreign key relationship lost 
- constraints will have to be managed in the services rather at the database level
- may* need to implement consistency check across services, or to trigger actions to clean up 
related data
*choice often not based on technology, e.g., how to handle an order that refers to a catalog ID of an item that has 
been removed from the catalog?


## Pagina 17 — 2 immagini/figure: guardare il PNG

Databases example: Shared static data
Solutions
(1) Duplicate table for each package
- potential consistency challenge
(2) Treat this shared static data as code (e.g., configuration file)
- consistency issues remain (though perhaps easier to update config files than db tables)
(3) Push static data into a separate service
- overkill?


## Pagina 18 — 5 immagini/figure: guardare il PNG

Databases example: Shared mutable data
Domain concept – Customer - implicitly modeled in 
the database
Solution: Create new Customer service and make 
Finance and Warehouse invoking its API
Finance code tracks customers’ payments and refunds
Warehouse code updates orders dispatched and received
Both Finance and Warehouse access Customer record table


## Pagina 19 — 4 immagini/figure: guardare il PNG

Databases example: Shared tables
Solution: Store the two concepts separately, split table in two
Catalog needs to store name and price of record we sell
Warehouse needs to keep electronic record of inventory
Two concepts stored in same Item table


## Pagina 20 — 1 immagini/figure: guardare il PNG

What to split first: schemas or services?
Splitting schemas (potentially) increases number of database calls, may 
break transactional integrity [see later]
Splitting schemas but keeping application code together makes reverting 
changes easier


## Pagina 21 — 1 immagini/figure: guardare il PNG

"Seam"-driven splitting
Database refactoring
Transactions


## Pagina 22 — 4 immagini/figure: guardare il PNG

Transactions
All-or-nothing transactions are useful, multiple tables updated «at once», 
always stay in consistent states
Example- When creating a new order:
Order table updated 
Picking table updated (for dispatching item)
Single transaction in 
a monolithic schema
Transactional safety lost with two separate schemas  
What if insert order record succeeds but insert picking 
record fails?


## Pagina 23 — 2 immagini/figure: guardare il PNG

Transactions: Solutions (1)
Abort entire operation with compensating transaction(s)
e.g., if insert order record succeeds but insert picking record fails, then 
- start compensating transaction to undo the committed transaction in the order table
- report failure via UI
Issues
Where the logic to handle compensating transactions? 
- Customer service, Warehouse service, elsewhere?
What if compensating transaction fails? (retry)
What if we need to enforce consistency of 5 (rather than 2) ops?


## Pagina 24 — 4 immagini/figure: guardare il PNG

Transactions: Solutions (2)
Employ distributed transactions
Transaction manager orchestrates the various transactions being done
Two-phase commit
- Voting phase: each participant tells manager whether its local transaction can go ahead
- If transaction manager gets a yes vote from all participants, it tells them all to go ahead and 
perform their commits – otherwise it sends a rollback to all parties
Vulnerabilities
If transaction manager goes down, pending transactions never complete
If one participant fails to respond during voting, everything blocks
What if a commit fails after voting?


## Pagina 25 — 2 immagini/figure: guardare il PNG

Transactions: Solutions (3)
eventual consistency
Try again later


## Pagina 26 — 1 immagini/figure: guardare il PNG

"Seam"-driven splitting
Database refactoring
Transactions
Reporting


## Pagina 27 — 3 immagini/figure: guardare il PNG

The Reporting Database
Reporting typically needs to group together data from across multiple parts 
of organization in order to generate useful output, e.g.,
combine data from general ledger with descriptions of sold items from catalog
combine purchase histories and customer profiles to get behaviour of customers
In monoliths, reports often run on read replica of primary database (for 
performance reasons)
What to do if database has been split?


## Pagina 28 — 2 immagini/figure: guardare il PNG

Reporting on multiple systems: Solutions (1)
Data retrieval via service calls
reporting system pulls data from source systems via API calls
does not scale well with large volumes of data
exposed APIs may not be designed for reporting (e.g., no way to retrieve all customers)
- inefficient, may generate load for target service


## Pagina 29 — 2 immagini/figure: guardare il PNG

Reporting on multiple systems: Solutions (2)
Data Pumps
data pushed to the reporting system
data pump maps service db to reporting schema
coupling worth to pay to make reporting easier
- data pump should be built & managed by the team managing the service
- data pump version controlled together with service
can be piggybacked by backup operations (Netflix “backup data pumps”)


## Pagina 30 — 3 immagini/figure: guardare il PNG

Reporting on multiple systems: Solutions (3)
Event Data Pumps
microservices can emit events based on the state change of entities that they manage
- e.g., Customer service may emit event when a customer is created/updated/deleted
write event subscriber that pumps data into reporting database
- no coupling with db of source microservice
- just binding to events emitted by service (meant to be exposed)
- event-based flow of data to reporting system faster than periodically scheduled data pump
- event data pump needs not to be managed by team managing the service
- drawback: all required information must be broadcasted as events, may not scale well for large 
volumes of data


## Pagina 31 — 1 immagini/figure: guardare il PNG

"Seam"-driven splitting
Database refactoring
Transactions
Reporting
Concluding remarks


## Pagina 32

Concluding remarks
Splitting a monolith can be painstaking but
• Planning small, incremental changes makes it easier to understand impact 
of each change and how to mitigate costs of (unavoidable) mistakes
Growing a service till it needs to be split is completely OK but
• we should understand when it needs to be split – and split it – before the 
split becomes too expensive


## Pagina 33

Reference
Sam Newman. Building microservices. O’Reilly. 2021. 
(Chapter 5)


## Pagina 34 — 2 immagini/figure: guardare il PNG

Next lab(s) …
