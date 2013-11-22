#!/bin/bash
#
# Run our web service
#

# working direct to set the path to our modules (not 
# the most efficient but it works)
export YELP_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}/"/)" && cd .. && pwd )"

echo -e "\n** starting service from $YELP_HOME **\n"

# configuration
export PYTHONPATH=${YELP_HOME}/yelp:${PYTHONPATH}

# run
python ${YELP_HOME}/mysite/manage.py runserver
