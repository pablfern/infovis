source env/bin/activate

export DATABASE_URL="postgres://postgres:1@localhost/censo2010"
export STATIC_URL="/static/"
export DEBUG="True"
export ROOT=`pwd`
export MANAGE="python $ROOT/manage.py"

alias m=$MANAGE
