For every additional element, why you are adding it
1 extra server& a load balancer, REPLICA for MYSQL

2 servers: to provide redundance and high availability, in the event that one server is down, the other takes over.
loadbalancer: for distributing traffic equally and also prevent overloading so that every server can be in action
MySQL Master/Replica: To ensure there is Data Consistency between the servers

What distribution algorithm your load balancer is configured with and how it works
Random distribution algorithm: It randomly distributes load across the servers available.

Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
Active-Passive Configuration setup

difference between the two
In Active-Active all instances handle request concurrently, while in active-passive the active instance handles the request, as the passive instance is on standby

How a database Primary-Replica (Master-Slave) cluster works
MySQL Master Replica cluster: To ensure data syncronization between the two servers
The master is where data writes occur while REPLICA node syncronizes with the master and can only handle read requests

What is the difference between the Primary node and the Replica node in regard to the application
The primary handles writes operation while Replica node handles read operation

Likely Issues
Where are SPOF
Potential SPOF exist in the load balancer. If load balancer fails traffic distribution is distracted
-To solve this problem a redundant load balancer can be added

Security issues (no firewall, no HTTPS)
There is No firewall or HTTPS
Add firewall to filter and secure incoming traffic.
Enable HTTPS for encrypting data in transit.

No monitoring
No monitoring capability hence challenges to detect and address issues
Monitoring is important for system health and performance

https://imgur.com/mpsBnZ
