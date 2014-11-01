ASSIGNMENT 3
-----------------------------


![Alt text](http://i.imgur.com/F1mnnYy.png "Optional title")


Q. How do you add nodes to your Hadoop cluster? 


The best way to install and setup a multi node cluster is to start installing two individual single node Hadoop clusters and merge them together with minimal configuration changes in which one Ubuntu box will become the designated master and the other box’s will become a slave, we can add n number of slaves as per our future request.

The best way to install and setup a multi node cluster is to start installing two individual single node Hadoop clusters and merge them together with minimal configuration changes in which one Ubuntu box will become the designated master and the other boxâ€™s will become a slave, we can add n number of slaves as per our future request.





![Alt text](http://i1.wp.com/bigdatahandler.com/wp-content/uploads/2013/10/m1.png "Optional title")




Networking plays an important role here, before merging both single node servers into a multi node cluster we need to make sure that both the node pings each other .Now we need to select the master node and slave node,  we need to add them in ‘/etc/hosts’ file on each machine by entering 

Networking plays an important role here, before merging both single node servers into a multi node cluster we need to make sure that both the node pings each other .Now we need to select the master node and slave node,  we need to add them in â€˜/etc/hostsâ€™ file on each machine by entering 


sudo vi /etc/hosts

We need to add the slaves with unnique names and restart the system

Sudo shutdown -r now

Go to the master system and edit the host file by typing the below commands

SQo vi /etc/hosts

Copying ssh key to the slave

ssh-copy-id -i ~/.ssh/id_rsa.pub

Q Can everyone in class add the remaining members of the class to their cluster?

Yes we can add the remaining members of the class to their cluster by using multiple node cluster process.

Q Can everyone simultaneously run their own Hadoop cluster, AND be a slave (worker) in another Hadoop cluster?

Yes , this can be done but we cannot figure the the jobs and we also cant track the defects if we run hadoop cluster simultaneously .


We cannot RUn hadoop in server with small ram size beaccuse it need more space beacuse it handles big data , and we might need 4gb ram to install  hadoop cluster



