import Pyro4

@Pyro4.expose
class StringConcatination:
    def concateStrings(self, string1, string2):
        return string1 + string2
    
daemon = Pyro4.Daemon()

# Set remote server object
server = StringConcatination()
uri = daemon.register(server)

ns = Pyro4.locateNS()
print(f"Server URI: {uri}")
ns.register("string.concatenator", uri)

# Start the server
print("Server is running...")
daemon.requestLoop()