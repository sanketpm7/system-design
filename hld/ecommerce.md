**Recommendation:**

Kafka: Kafka is commonly used as a distributed streaming platform for ingesting and processing real-time data streams. It serves as a buffer between the data producers and consumers, providing scalability and fault tolerance. Kafka is a crucial component for real-time data processing scenarios, and its inclusion in the architecture seems appropriate.

Spark Streaming cluster: Spark Streaming is used for processing real-time data streams, making it suitable for scenarios where low-latency processing is required. However, if your use case primarily involves batch processing or if the data ingestion rate is relatively low, you might not need Spark Streaming and could use batch processing with Apache Spark instead.

Hadoop cluster: Hadoop clusters, particularly HDFS, are commonly used for distributed storage and batch processing of large datasets. If your recommendation service primarily relies on real-time data processing or if you're not dealing with massive amounts of data that require HDFS for storage, a Hadoop cluster might be unnecessary.

Spark Job: The Spark job is responsible for training recommendation models using data stored in Hadoop. If your recommendation service relies solely on pre-trained models or if the data processing and model training can be done in real-time without the need for batch processing, a separate Spark job might not be necessary.

Recommendation Service: The recommendation service serves personalized recommendations to users based on their preferences and behavior. This component is essential for delivering the final recommendations to end-users and would likely be required in most recommendation systems.



Seller Adds the items
-> Items get pushed to Kafka
-> Once the Warehouse receives the items, they're updated in Warehouse DB
-> Once Warehouse DB is updated, it triggers an event --> `update InventoryDB`
-> Inventory DB gets updates

Checkout service:
-> The proceeds to buy the items, they items get locked for 3 mins
-> 