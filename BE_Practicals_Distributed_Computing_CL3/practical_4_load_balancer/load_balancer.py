import time

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def distribute_request(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

class Server:
    def __init__(self, name):
        self.name = name

    def process_request(self):
        print(f"Server {self.name}: Processing request...")
        # Simulate processing time
        time.sleep(1)
        print(f"Server {self.name}: Request processed.")

# Create servers
server1 = Server("Server A")
server2 = Server("Server B")
server3 = Server("Server C")

# Create load balancer
load_balancer = LoadBalancer([server1, server2, server3])

# Simulate requests coming from clients
requests = range(10) 
for request in requests:
    server = load_balancer.distribute_request()
    server.process_request()
