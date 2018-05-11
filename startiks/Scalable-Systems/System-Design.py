Twitter:

1) User account management
2) Tweet Generation
  a) Retweet
  b) Limitations, etc
3) Follow/unfollow
4) Feed dashboard
    a) Pinning Posts
5) Endorsements and Notifications
6) Search and Analytics
    a.Recommendations


Thought Process:
Divide the set of requirements into services:

Each service is a set of three tiers
-Application server tier
-In-memory/cache server tier
-Source of truth/persistence tier

Each tier is a distributed system
    -distributed K-V store or similar

Multiple Services for Twitter :

1) User account management:
    K: User id, V: All properties of an user (
    CRUD API's
Why Distributed:
  Storage: Number of records and size of each record (400M * 1KB) -400G
  computer Based : Latency:  Low:Throughput

How Distributed:
 - Horizontal sharding on has on range of key ( horizontal partitioning )
 -

NOSQL: Not only SQL and I will use other ways to access .

2) Social Graph:
    In-memory: Needed
    Source of truth: Needed

    Data Model and API's:
    K:<user id> , V: List of Followers:Sorted  by edge weight
    K:<user_id> : V: List of Followees: Sorted by edge weight
    K-V style workload

    Why distributed:
       Storage: Number of records:Number os users * Number of followers
       Compute: Latency: Low : Throughput: Does not seem high unless read is concerned .
    How Distributed:
        Horizontal:

if 's: Given an id, return the top followees:
        Given an id, return the set of followers.

    API's: Given an id, return

    Videos:
    Latency:
    Throughput:


3)Tweet Generation Service:
    - App-Server:  In-memory : needed: Source of truth: Needed
    Data Model and API's:
    K-V:<userid/tweet-id> V:payload if it's master tweet:' path to media:timestamps:number of re-tweets:
    CRUD API's
why distriburted:
    Storage:6k/sec
    Compute:Latency:Low,
            Througput: 6k/sec writes + 300k/sec
    How distributed:
        Horizontal hash on user id
4)



4)Feed Service ( Timeline ):
Tiers: Appserver : In-memory ,
Yes:Source of TRuth

Data model and API's
K-V:
K:userid
V: Paginated List of tweets sorted by tie sorted by followee relevance
API:Get/user/?sort=timestamp&count=100 & start = 0

why Distributed:
 No of records: No of active users:Size of record:Set of materialized twets + a larger set of non-materialized tweets

Throughput: 300k/sec
Latency:super low

How Distributed:
 Horizontal
 when 1 system has to talk to another system , throw Publisher subscriber-
Scalable transport from one service to another

100%push: Problem : Network Fanout: write Latency is huge:
Pro:Consistent and ready feed cache

100%pull:Write Latency is low: Feed service will load on demand

Hybrid: Selective push + publication in a pub-sub service:

why Distributed:
  Number of records:Number of users * Number of following

5) Notification Service:



6) Endorsements

Streaming Analytics:

Imagine a data center that has 100s of machines, each of which exposes 1000s of statistics (CPU utilization, memory utilization,etc)
per second. Design a distributed system that collects and aggregates these to produce the following dashboards:

1) Given a machine id and a window size, plot min,max avg of all statistics over that window:

2) Given a statistic id and a window size , plot min,max,avg of that stat for all hosts in that window

3) Given a machine id and a time range, plot min, max,avg of all statistics over the time range

4)Given a statistic id and a time range, plot min,max,avg of all hosts over the time range


Data aggregation service:

    First start with a single server approach :

    K:Value: K:<machine/stat/timestamp>:V:stat value
    API:  Create(K,V)
        GET (machine id, 8 hrs) - > < returns min, max, avg for each minute >480 values per stat id
        GET (stat id, 8 hrs)

Host|Stat|Timestamp|min|max|avg|count

Bucketize based on Timestamp and a circular buffer
[0] -> [x*y ]
[1]->
[2]->

Why Distributed:

1) 500,000 recods/sec
500,000 /min* 480 min *32 bytes

2)-Time Bucket
Table [1min]
...

Table[480min]
When distributed maintain 2 tables ( host-based /stat-id):To avoid scatter-gather .
[hash(host-id)] [Timestamp]
[hash(stat-id)] [Timestamp]

pub/sub - class(Functional Rqmnts):

GET/event-key/offset,batch
-
1) Millions of clients can publish at the same time
2) Each event can be consumed by millions of consumers
3) Events/messages should be purged after 7 days
4) Once pub is acknowledged , message should be seen by consumer atleast once
5) Consumers can look into message list by
 offset:

Services:

producer
Consumer
Registration

ProducerService Tiers:
AppServer
