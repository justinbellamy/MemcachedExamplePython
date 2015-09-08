import pylibmc
memcached = pylibmc.Client(['127.0.0.1'], binary=True, behaviors={"tcp_nodelay": True})

#Using mapping interface
memcached["First"] = "First Value"
print memcached["First"]
del memcached["First"]


#Using classic style
if memcached.add("Second", "Second Value"):
    print memcached.get("Second")

if memcached.prepend("Second", "This is the... "):
    print memcached.get("Second")

if memcached.append("Second", "!"):
    print memcached.get("Second")

if memcached.replace("Second", "Second Value Replaced"):
    print memcached.get("Second")

if memcached.add("Second", "A Different Value"):
    print memcached.get("Second")
else:
    print "Couldn't add to key:Second, a value already exists."
memcached.delete("Second")

#Using increments and decrements
if memcached.set("3", "10"):
    print memcached.get("3")
    memcached.incr("3")
    print memcached.get("3")
    memcached.decr("3")
    print memcached.get("3")

#Print a "deleted" key. Should return the constant None
memcached.delete("3")
print memcached.get("3")

#Attempt to replace a key that doesn't exist & handle the error gracefully
try:
    memcached.replace("Fourth", "Fourth Value")
except pylibmc.Error as e:
    print "Can't replace something that doesn't exist! - " + str(e)

#Clear everything
memcached.flush_all()