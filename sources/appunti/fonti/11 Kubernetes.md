# 11 Kubernetes.pdf

35 pagine


## Pagina 1

Kubernetes
Antonio Brogi
Department of Computer Science
University of Pisa


## Pagina 2 — 1 immagini/figure: guardare il PNG




## Pagina 3 — 1 immagini/figure: guardare il PNG

Containers
Containers provide a lightweight mechanism for isolating an 
application's environment
Container images can be executed reliably on any machine, 
providing us portability from development to deployment
Multiple workloads can be placed on the same physical 
machine, achieving  higher resource (memory and CPU) 
utilization


## Pagina 4 — 3 immagini/figure: guardare il PNG

Automated deployment vs. container orchestration
https://www.youtube.com/watch?v=u_iAXzy3xBA&t=1067s [17:47-20:55]


## Pagina 5 — 1 immagini/figure: guardare il PNG

Questions
What happens if your container dies? 
What happens if the machine running your container fails? 
What if you have multiple containers that need the communicate
one another? How do you enable networking between containers? 
If your production environment consists of multiple machines, how 
do you decide which machine to use to run your container?


## Pagina 6 — 1 immagini/figure: guardare il PNG

Container orchestration
The director of an orchestra holds the vision for a musical performance
and
communicates
with
the
musicians
to
coordinate
their
individual
instrumental contributions to achieve this overall vision
The
architect
of
a
system
simply
composes
the
music
(defines
the
containers to be run) and then hands over control to the orchestra director
(container orchestration platform) to achieve that vision


## Pagina 7

Kubernetes: A container orchestration platform
K8s manages the entire lifecycle of individual containers, spinning up and 
shutting down resources as needed
if a container shuts down unexpectedly, K8s reacts by launching another container in its place
K8s provides a mechanism for applications to communicate with each other 
even as underlying individual containers are created and destroyed
Given a set of container workloads to run and a set of machines on a cluster, 
the container orchestrator examines each container and determines the 
optimal machine to schedule that workload 
J. Jordan. An introduction to Kubernetes.


## Pagina 8 — 1 immagini/figure: guardare il PNG




## Pagina 9 — 2 immagini/figure: guardare il PNG

K8s in 5 minutes 
https://www.youtube.com/watch?v=PH-2FfFD2PU


## Pagina 10 — 1 immagini/figure: guardare il PNG

“Desired state management” 
deployment yaml file
Pods, images, replicas
K8s cluster services, API
Worker (container host), Kubelet process
What if we loose a worker?


## Pagina 11 — 1 immagini/figure: guardare il PNG




## Pagina 12

K8s design principles: Declarativeness
We simply define the desired state of our system 
K8s
•
will detect when the actual state of the system doesn't meet our expectations and 
•
it will intervene to fix the problem, making our system self-healing
Desired state defined by a collection of objects
•
each object has a specification in which you provide the desired state and 
a status which reflects the current state of the object
•
K8s constantly polls each object to ensure that its status is equal to the specification
•
if an object is unresponsive, K8s will spin up a new version to replace it
•
if a object's status has drifted from the specification, K8s will issue the necessary commands 
to drive that object back to its desired state


## Pagina 13 — 1 immagini/figure: guardare il PNG

K8s design principles: Distribution
K8s provides a unified interface for interacting with a cluster of machines 
We don't have to worry about communicating with each machine individually


## Pagina 14 — 1 immagini/figure: guardare il PNG

K8s design principles: Decoupling
Containers should be developed with a single concern in mind 
→microservice-based architecture
K8s naturally supports the idea of decoupled services which can be scaled 
and updated independently


## Pagina 15

K8s design principles: Immutable infrastructure
To get the most from containers and container orchestration, we should be 
deploying immutable infrastructure
e.g. log in to a container on a machine to update a library make changes →build a new container 
image, deploy the new version, and terminate the older version
During the life-cycle of a project (development - testing - production) we
should use the same container image (and only modify configurations 
external to the container image, e.g. by mounting a config file)
Containers are designed to be ephemeral, ready to be replaced by another 
container instance at any time 
Maintaining immutable infrastructure makes it easier roll back applications to 
previous state (eg. if an error occurs) - we can simply update our 
configuration to use an older container image


## Pagina 16 — 1 immagini/figure: guardare il PNG




## Pagina 17 — 1 immagini/figure: guardare il PNG

K8s objects
K8s objects can be defined in manifests (YAML or JSON files)


## Pagina 18 — 1 immagini/figure: guardare il PNG

K8s objects: Pod
A Pod consists of
• one or more (tightly related) containers
• a shared networking layer
• shared filesystem volumes


## Pagina 19 — 1 immagini/figure: guardare il PNG

K8s objects: Deployment
A Deployment object includes a collection of Pods defined by a template and 
a replica count (number n of how many copies of the template we want to 
run)
The cluster will always try to have n Pods available
e.g. if we define a deployment with a replica count of 10 and 3 of those Pods crash, 3 
more Pods will be scheduled to run on a different machine in the cluster


## Pagina 20 — 1 immagini/figure: guardare il PNG

K8s objects: Deployment
Example: Deployment object to run 10 instances of a container which serves 
an ML model over a REST interface


## Pagina 21 — 1 immagini/figure: guardare il PNG

K8s objects: Service
Each Pod is assigned a unique IP address that we can use to communicate 
with it
Q: How to communicate with Pods if the set of Pods running as part of the Deployment 
can change at any time?
K8s Service provides a stable endpoint to direct traffic to the desired Pods 
even as the exact underlying Pods change due to updates/scaling/failures
Services know which Pods they should send traffic to based on labels (key-
value pairs) which we define in the Pod metadata


## Pagina 22 — 1 immagini/figure: guardare il PNG

K8s objects: Service
Example: Service wrapped around the previous Deployment example


## Pagina 23 — 1 immagini/figure: guardare il PNG

K8s objects: Ingress
Service allows us to expose applications behind a stable endpoint - only 
available to internal cluster traffic
To to expose our application to traffic external to our cluster, we need to 
define an Ingress object
We can select which Services to make publicly available


## Pagina 24 — 1 immagini/figure: guardare il PNG

K8s objects: Ingress
Example


## Pagina 25

K8s objects
Many more:
• Job
• Volume
• Secret
• Namespace
• ConfigMap
• HorizontalPodAutoscaler
• StatefulSet
• …


## Pagina 26 — 1 immagini/figure: guardare il PNG




## Pagina 27

K8s control plane
Two types of machines in a cluster:
•
master node - (often single) machine that contains most of the control plane 
components 
•
worker node - machine that runs the application workloads


## Pagina 28 — 1 immagini/figure: guardare il PNG

K8s control plane (master node)
User provides new/updated object specification to API server of master 
node 
•
API server validates update requests and acts as unified interface for questions about 
cluster's current state
•
State of cluster* is stored in a distributed key-value store etcd, a distributed key-
value store
(*cluster configuration, object specifications, object statuses, nodes on the cluster, object-node assignments etc.)


## Pagina 29 — 1 immagini/figure: guardare il PNG

K8s control plane (master node)
The scheduler determines where objects should be run
The scheduler 
• asks the API server which objects haven't been assigned to a machine
• determines which machines those objects should be assigned to 
• replies back to the API server to reflect this assignment


## Pagina 30 — 1 immagini/figure: guardare il PNG

K8s control plane (master node)
The controller-manager monitors cluster state through the API server
If actual state differs from desired state, the controller-manager will make 
changes via the API server to drive the cluster towards the desired state


## Pagina 31 — 1 immagini/figure: guardare il PNG

K8s control plane (worker node)
kubelet
• acts as a node's "agent" which communicates with 
the API server to see which container workloads 
have been assigned to the node
• responsible for spinning up pods to run these 
assigned workloads
• when a node first joins the cluster, kubelet
announces the node's existence to the API server so 
the scheduler can assign pods to it


## Pagina 32 — 1 immagini/figure: guardare il PNG

K8s control plane (worker node)
kube-proxy enables containers to communicate with each other across the various nodes on 
the cluster


## Pagina 33 — 1 immagini/figure: guardare il PNG




## Pagina 34

Concluding remarks
When should you NOT use K8s?
• If you can run your workload on a single machine
• If your compute needs are light
• If you don't need high availability and can tolerate downtime
• If you don't envision making a lot of changes to your deployed services
• If you have a monolith and don't plan to break it into microservices


## Pagina 35 — 6 immagini/figure: guardare il PNG

K8s vs. Docker Swarm
Docker Swarm
Kubernetes

Simpler to install

Softer learning curve

Features auto-scaling

Higher fault tolerance 

Huge community

Backed by Cloud Native Computing 
Foundation (CNCF)
Preferred in environments where 
simplicity and fast development is 
favored
Preferred for environments where 
medium to large clusters are running 
complex applications
