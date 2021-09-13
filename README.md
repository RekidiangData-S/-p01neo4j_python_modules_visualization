# Neo4j Python Modules Visualzation

A simple tool written in python that visualize the installed python modules on your mechine in neo4j. The code is part of the blog poist [Visualizing Python modules and dependencies with Neo4j](http://blog.adnansiddiqi.me/visualizing-python-modules-and-dependencies-with-neo4j/)


## How to execute

Start Docker and execute the command :
> docker pull neo4j 

to pull the Neo4j docker image.

> docker run \
    --name testneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/test \
    neo4j:latest
    
    
    AUTH :
    * **username** : neo4j
    * **password** : test