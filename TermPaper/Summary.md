On the Locality of Java 8 streams in Real- Time Big Data Applications
----

Big data frameworks do not consider computer server architectures. The access times of data may differ depending on the core on which the access is requested. The performance is degraded when the data access is requested throughout a group of servers. 
Java is the primary programming language to be used to develop the big data applications. Java 8 is the new version in which streams are used for data access to simplify parallel programming. This paper introduces that there are no built-in parallel stream sources which will operate on big datasets. This paper details recent work from the JUNIPER project, an EU framework 7 project, which is used for big data applications. The results shows that when reading data from disk, the thread affinity degrades the performance of java streams.
In JUNIPER project, the thread pool for parallel processing will consist of RTSJ real time threads. Java’s built-in streams have some drawbacks. One of which is that the in-memory sources store all their data in heap memory. This heap is not sufficient to access the big datasets. Another drawback is that file-based sources produce sequential streams. To overcome these drawbacks we used idea of store collection which reads data from a file on demand. 
The java 8 stream model uses the Java fork-join framework to obtain parallel execution. This framework allows the users to specify tasks that can be divided and executed in parallel systems. The performance improvements in big data applications are most likely to come from optimizing the locality of main memory accesses in computer architecture.
The first set of experiments establishes the memory access times for local and remote servers separately. Second set measured the execution times of memory access. In the third set, the long integers are read from disk. The results shows that the memory access from a remote server is slower than the local source. We can conclude that stored collections are a better source than java arrays to improve the performance of the system. 


Modeling Apache Hive based applications in Big Data architectures
---
Big Data applications is a power-ful tool which suppors designers and administrators in achieving disambiguation of their computing resources.Thse architectures are complex,rapid and adaptive so,that it can fit to the needs.This Big Data area is a recent application coming in to field,resulting from the technological advancement and emerging requirements used to process low cost and low quality data.

Big data is used in application feild to exploit very large and unstructured databases.Existed work related to support huge distributed computations on data organized in tabular data strctures to store number of rows and columns so that it can balance workload by distributing the data in that tables.

Computing is performed in two phases as map phase and reduce phase map is to run the desired task and reduce is to collect and process output.Thedrowbacks are this model introducing abstract primitives, such as high level query languages which is a big relief to the devolepers but it is making designes life complicate when taking decisions based on performance evaluation as it additionally complicates the architecture.

In order to overcome these complicaions the author described a mul-tiformalismapproach.Which pro-vides an in-depth description of the simthesysformalism,simthesysBigData. SIMTHESysBigData has been devel-oped to describe at low application level the architecture of a Big Data system based on Apache Hadoop and simple map-reduce pipelines. The formalism offers the elements as share,adddata,actionarc,dataArc.The approach hides the complexity of the system behind a structural,foundational description of the architecture and a logicaldescription of the query operation, keeping the rep-resentation close to metaphors that are familiar for domain experts of the Big Data field.









HPC in BIG DATA Age
---
An Evaluation Report for Java-Based Data- Intensive Applications Implemented with Hadoop and OpenMPI


The data complexity increased a lot in past few years both in public and enterprise domains posting new challenges in High Performance Computing (HPC) .The author explained about the techniques utilized in both cloud and HPC domains such as parallelization and also evaluates the HPC cluster.

The author describes about: management of growing data volume, dealing with dynamic and streaming data, coming from different sources, analysis complexity of the data processing algorithms, complexity of data structures, and availability of hard time constraints to the duration of data processing.

It also describes us about the parallelization Techniques, Hadoop drawbacks and how we overcome them from the previous stage.

We can also figure out the future work on evaluating elaborated parallelization technique in big data domain for complex applications. 

Programming Your Network at Run-time for Big Data Applications
-----
The author explored an integrated network control architecture to program the network at run-time for big data applications using optical circuits with a Software Defined Networking (SDN) controller. Here we use Hadoop as an example and we discuss the integrated network control architecture, job scheduling topology and routing configuration for Hadoop jobs. We particularly study the run-time network configuration for big data applications to jointly optimize applications performance
And network utilization

Our analysis suggests that such an integrated control has great potential to improve application performance with relatively small configuration overhead.

We focus on the run-time network reconfiguration for big data applications and the dynamic interaction between application components and the SDN controller in data centers. We study the programmability on every layer of network from physical topology to routing and flow level traffic engineering



A Bloat-Aware Design for Big Data Applications
----

The author in this paper described about the study bloat using two big data applications :
Hive: A large scale data warehouse software which will be built on hadoop and 
Giraph: An apache open source graph analutics initiated by yahoo.

The data objects in the system has to be bounded all the time they have no chance to grow proportionally with the data size, to overcome this we implement a design paradigm recommend to merge small objects and access the objects which are merged 

We can figure out two fundemental problems , one space related that is the large space occupied by object header and referances will lead to low packing factor of the memory , and the other is time related that is large amounts of objects and referenaces leads to poor GC performance.









