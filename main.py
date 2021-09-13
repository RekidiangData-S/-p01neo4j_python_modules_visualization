"""docker run \
>     --name testneo4j \
>     -p7474:7474 -p7687:7687 \
>     -d \
>     -v $HOME/neo4j/data:/data \
>     -v $HOME/neo4j/logs:/logs \
>     -v $HOME/neo4j/import:/var/lib/neo4j/import \
>     -v $HOME/neo4j/plugins:/plugins \
>     --env NEO4J_AUTH=neo4j/test \
>     neo4j:latest

"""
from utilities import *
from neo4gdb import *

if __name__ == '__main__':
    packages = get_pip_list()

    # Creating Nodes
    for pkg in packages:
        if 'zope' not in pkg:
            print('Creating Node for {}'.format(pkg))
            r = create_node(pkg)

    print('Creating Relationships. Please wait...')
    for pkg in packages:
        if 'zope' not in pkg:
            print('Processing...{}'.format(pkg))
            dependants = get_package_detail(pkg)
            for dep in dependants:
                if dep is not None and dep != '':
                    print('Creating relationship between {} and {}'.format(pkg, dep))
                    # Create Relationship
                    create_relationship(pkg, dep)
